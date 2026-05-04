from pydantic import BaseModel
from typing import List, Optional


class PriceItem(BaseModel):
    size: Optional[str]
    price: Optional[float]
    package_type: Optional[str]
    sku: Optional[str]


class KeyValue(BaseModel):
    key: Optional[str]
    value: Optional[str]


class ProductResponse(BaseModel):
    product_name: Optional[str]
    description: Optional[str]
    product_brand: Optional[str]
    material_id: Optional[List[str]]
    product_number: Optional[str]
    product_key: Optional[str]
    price: List[PriceItem]
    alies: List[KeyValue]       
    descriptions: List[KeyValue]
    images: List[str]
    attributes: List[KeyValue]
    safty_info: List[KeyValue]    