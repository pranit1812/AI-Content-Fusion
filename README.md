## Content Fusion Web App

## Detailed Project Report
**Author:** Pranit Sehgal  
**Institution:** Arizona State University (ASU)  
**ASU ID:** 1225456193  
**Email:** [pranitsehgal@gmail.com](mailto:pranitsehgal@gmail.com)

### 1. Project Aim
The primary goal of the Content Fusion Web App is to provide a solution for content creators, particularly social media influencers, who often struggle with idea generation after producing a significant number of posts or videos. The app aims to stimulate creativity by fusing two distinct ideas submitted by the user to generate new, unique content suggestions. This supports creators in maintaining engagement with their audience by continually offering fresh and innovative content.

### 2. Concept and Idea
The core concept of the Content Fusion Web App revolves around leveraging artificial intelligence to assist in content ideation. Users input two separate ideas, and through the integration of AI, specifically a language model, the app generates a synthesis of these ideas into several new content proposals. Users can then select their preferred idea and further use the app to generate visual and video content, enhancing the conceptualization and planning process of content creation.

### 3. Workflow and Architecture
The workflow of the app involves several stages:
- **Idea Input:** Users enter two distinct ideas.
- **Idea Fusion:** Using OpenAI's ChatGPT API, the app fuses the ideas to generate new content suggestions.
- **Idea Selection:** Users select their favorite idea from the generated options.
- **Image Prompt Generation:** For the selected idea, the app, again using ChatGPT, generates image prompts that capture the essence of the idea.
- **Image Generation:** These prompts are fed into DALL-E to create relevant images.
- **Video Compilation:** Using the images, a slideshow video is created with captions derived from the selected idea, providing a visual explanation of the concept.

This workflow utilizes the concept of prompt chaining, where the output of one AI-generated task is used as the input for the next, ensuring a coherent and contextually relevant generation process across different media formats (text, image, video).

### 4. Technology and AI Agents
Several AI technologies and agents are utilized in this project:
- **ChatGPT (OpenAI):** Used for generating fused content ideas and image prompts. This language model acts as a core component, driving the creative content ideation and the generation of descriptive prompts for images.
- **DALL-E (OpenAI):** Utilized for generating images based on the prompts provided by ChatGPT. This model helps in visually representing the ideas, which are essential for the video content.
- **MoviePy:** A Python library for video editing, used to create slideshow videos from the generated images, adding textual descriptions as captions to enhance understanding.

### 5. Challenges and Solutions
- **Resource Limitation:** Initial attempts to use local AI models like Stable Diffusion were hindered by hardware limitations. This was resolved by switching to cloud-based solutions (DALL-E), which provided the necessary computing power.
- **Software Compatibility Issues:** Issues with software dependencies and performance inefficiencies (e.g., long processing times on Hugging Face models) led to a pivot towards more reliable and compatible APIs provided by OpenAI.

### 6. Future Work
- **Integration of Local LLMs:** To reduce operational costs, there is an ongoing effort to integrate local versions of language models, such as LLaMA, which can potentially offer similar capabilities without incurring API costs.
- **Content Dataset Utilization:** Enriching the AI's understanding and output by training it on a large dataset of existing content ideas, enabling the generation of more targeted and innovative ideas.
- **Platform Expansion:** Expanding the app's capability to suggest not only visual content but also other forms of media such as blog posts, podcasts, etc.

### 7. Acknowledgments
Special thanks to Professor Binil Starly for his guidance and support throughout the project, providing valuable insights into the integration and practical application of AI technologies in creative industries.
> “Don’t let AI handicap you, use it as a tool” – Prof. Binil

### 8. Screenshots
(Screenshots of the application in action, demonstrating the workflow and outputs.)

