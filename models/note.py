from pydantic import BaseModel
from typing import Optional

class Note(BaseModel):
    title: str
    description: str
    important: Optional[bool] = False
