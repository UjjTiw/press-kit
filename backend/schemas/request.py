from pydantic import BaseModel

class CompanyInfo(BaseModel):
    company_name: str
    flagship_product: str
    achievements: str
    brand_attributes: str

class PressKitTopic(BaseModel):
    press_topic: str
    target_media: str
    tone: str