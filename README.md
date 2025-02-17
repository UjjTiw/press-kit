# AI-Powered Press Kit Generator

## Overview
This project is an AI-powered press kit generator that takes company details and press information as input and generates a structured press release, company overview, PR message, and email draft. The system is built using **FastAPI** for the backend and **Gradio** for the frontend, leveraging **LangChain** and the **Tavily Search API** for enhanced AI-generated content.

## Key Features
- Takes structured inputs related to a company's branding and press information.
- Generates a detailed press release with evaluation metrics.
- Uses **LangChain Agent** with **Tavily Search API** for enhanced responses.
- Provides an intuitive frontend using **Gradio**.

## Challenges & Solutions
One of the major challenges faced was integrating the **Tavily Search API** with LangChain to improve AI-generated responses. To overcome this:
1. Implemented a **LangChain Agent** to effectively manage tool execution.
2. Created a **custom chain** to ensure a smooth flow of retrieved information.
3. Optimized response handling to refine the final output.

## Installation & Setup
To run the project, you need **Poetry** installed on your system. Follow these steps:

1. Install dependencies:
   ```bash
   poetry install
   ```
2. Start the backend:
   ```bash
   poetry run python backend/main.py
   ```
3. Start the frontend:
   ```bash
   poetry run python frontend/app.py
   ```
4. Access the application at: [http://localhost:7680](http://localhost:7680)

## Input & Output Example

### **Input Fields**:
- **Company Name**: OpenAI
- **Flagship Product**: GPT-4
- **Achievements**: Advanced AI capabilities, improved safety features
- **Brand Attributes**: Ethical AI, innovation
- **Press Topic**: Latest AI Innovations
- **Target Media**: Tech journalists, AI researchers
- **Tone**: Professional

### **Generated Press Kit**
#### **Press Release**
> **For Immediate Release: Latest AI Innovations**
>
> **OpenAI Unveils Groundbreaking AI Innovations with GPT-4**
>
> San Francisco, CA – OpenAI, a leader in artificial intelligence research, announces the latest advancements in AI technology with the development of GPT-4...

#### **Company Overview**
> **OpenAI: Pioneering the Future of Artificial Intelligence**
>
> OpenAI was founded to ensure AGI benefits humanity. Known for its cutting-edge AI models like GPT-4, OpenAI remains at the forefront of ethical and responsible AI development...

#### **Evaluation Report**
- **Content Consistency**: 8/10
- **Writing Style & Engagement**: 7/10
- **Layout & Structure**: 9/10
- **SEO Optimization**: 6/10
- **Integration of Supplementary Data**: 8/10

### **Screenshot Attachments**
_![Screenshot 2025-02-17 at 6 43 00 AM](https://github.com/user-attachments/assets/8fe05b10-a5b1-4b22-929e-a2d4282ca952)
 generated outputs)_

## Future Improvements
- Enhance SEO keyword optimization.
- Implement a more dynamic LangChain workflow.
- Improve UI for better user experience.



