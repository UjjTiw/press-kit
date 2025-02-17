from fastapi import FastAPI
from schemas import CompanyInfo, PressKitTopic
from agents import chain  # Assuming 'chain' is your LangChain instance

app = FastAPI(docs_url='/docs')

@app.post('/invoke')
def presskit(company_info: CompanyInfo, press_kit: PressKitTopic):
    # Convert input data to dictionary format for the chain
    input_data = {
        "company_name": company_info.company_name,
        "product_service": company_info.flagship_product,
        "achievements": company_info.achievements,
        "brand_attributes": company_info.brand_attributes,
        "press_topic": press_kit.press_topic,
        "target_media": press_kit.target_media,
        "tone": press_kit.tone,
        "agent_scratchpad": "Do searches for the latest yeas always!!!"
    }

    # Invoke the chain with the formatted input data
    response = chain.invoke(input_data)

    return {
        "message": "Press kit generated successfully.",
        "press_kit": response
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
