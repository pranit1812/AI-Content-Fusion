

from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip, concatenate_videoclips
import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import os


OPENAI_API_KEY = "add your key"
openai.api_key = OPENAI_API_KEY

def generate_content_ideas(idea1, idea2):
    prompt = f"Generate 3 innovative content ideas combining: '{idea1}' and '{idea2}.Make sure they have a title and 2-3 sentences'."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative content creator assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.6
        )
        content = response['choices'][0]['message']['content']
        ideas = [idea.strip() for idea in content.split("\n\n") if idea.strip()]
        return ideas if len(ideas) >= 3 else ["Insufficient content."] * (3 - len(ideas))
    except Exception as e:
        st.error(f"Failed to generate ideas: {str(e)}")
        return ["Error occurred in generating ideas."]

def generate_image_prompts(idea):
    
    prompt = f"Create three short and unique prompts for generating images that visually represent the theme and essence of this idea: '{idea}'."
    try: 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        content = response['choices'][0]['message']['content']
        image_prompts = [prompt.strip() for prompt in content.split("\n") if prompt.strip()]
        return image_prompts if len(image_prompts) >= 3 else ["Insufficient prompts."] * (3 - len(image_prompts))
    except Exception as e:
        st.error(f"Failed to generate image prompts: {str(e)}")
        return []

def generate_images(image_prompts):
    images = []
    for prompt in image_prompts:
        try:
            response = openai.Image.create(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            image_url = response['data'][0]['url']
            image_response = requests.get(image_url)
            img = Image.open(BytesIO(image_response.content))
            images.append(img)
        except Exception as e:
            st.error(f"Failed to generate image: {str(e)}")
            return []
    return images




def generate_slideshow(idea, images):
    video_path = "output_slideshow.mp4"
    
    
    title_end = idea.find('"', idea.find('"') + 1) + 1
    title = idea[:title_end].strip()
    sentences = idea[title_end:].strip().split('. ')
    subtitles = sentences[:2]  # Ensure only two subtitles are taken
    
    
    descriptions = [title] + subtitles + [''] * (3 - len(subtitles) - 1)
    
    clips = []
    for idx, (image, desc) in enumerate(zip(images, descriptions)):
        text_clip = TextClip(desc, fontsize=35, color='black', method='caption', size=(image.width, None), align='center', stroke_width=1).set_duration(3).set_position(('center', 'bottom'))
        image_clip = ImageSequenceClip([np.array(image)], fps=1).set_duration(3)
        combined_clip = CompositeVideoClip([image_clip, text_clip.set_position(("bottom"))], size=image.size)
        clips.append(combined_clip)
    
    video = concatenate_videoclips(clips, method='compose')
    video.write_videofile(video_path, fps=24, codec='libx264')
    return video_path



def app():
    st.title('Creative Content Idea Generator')
    with st.form("idea_form"):
        idea1 = st.text_input("Enter First Idea", key="idea1")
        idea2 = st.text_input("Enter Second Idea", key="idea2")
        submit_button = st.form_submit_button("Generate Ideas")
        
    if submit_button and idea1 and idea2:
        ideas = generate_content_ideas(idea1, idea2)
        st.session_state.ideas = ideas
    
    if 'ideas' in st.session_state and st.session_state.ideas:
        st.write("Generated Ideas:")
        for idx, idea in enumerate(st.session_state.ideas, start=1):
            with st.container():
                st.markdown(f"### Idea {idx}")
                st.markdown(f"> {idea}")
                if st.button(f"Create an explanatory Video for Idea {idx}", key=f"button{idx}"):
                    image_prompts = generate_image_prompts(idea)
                    if image_prompts:
                        images = generate_images(image_prompts)
                        if images:
                            video_path = generate_slideshow(idea, images)
                            if video_path:
                                st.video(video_path)
                            else:
                                st.error("Failed to generate slideshow. Please try again.")
                        else:
                            st.error("Failed to generate images. Please try again.")
                    else:
                        st.error("Failed to generate image prompts. Please try again.")

if __name__ == "__main__":
    app()

