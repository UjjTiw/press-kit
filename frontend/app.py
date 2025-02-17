import gradio as gr
import requests

API_URL = "http://0.0.0.0:8000/invoke"  # Updated FastAPI endpoint

def get_prediction(company_name, flagship_product, achievements, brand_attributes, press_topic, target_media, tone):
    payload = {
        "company_info": {
            "company_name": company_name,
            "flagship_product": flagship_product,
            "achievements": achievements,
            "brand_attributes": brand_attributes
        },
        "press_kit": {
            "press_topic": press_topic,
            "target_media": target_media,
            "tone": tone
        }
    }
    
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        data = data['press_kit']
        print(data)
        evaluation = data.get("evaluation", "No evaluation provided")
        print(evaluation)
        generate_message = data.get("generate_message", "No message generated")
        print(generate_message)
        return evaluation, generate_message
    return {"error": "Error connecting to API"}

demo = gr.Interface(
    fn=get_prediction,
    inputs=[
        gr.Textbox(label="Company Name"),
        gr.Textbox(label="Flagship Product"),
        gr.Textbox(label="Achievements"),
        gr.Textbox(label="Brand Attributes"),
        gr.Textbox(label="Press Topic"),
        gr.Textbox(label="Target Media"),
        gr.Textbox(label="Tone")
    ],
    outputs=[
        gr.Textbox(label="Evaluation"),
        gr.Textbox(label="Generated Message")
    ],
    title="AI Prediction Interface",
    description="Enter company details and press kit info to get evaluation and generated message from the backend model.",
)

demo.launch()
