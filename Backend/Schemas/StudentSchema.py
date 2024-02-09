from pydantic import BaseModel, Field


class UserAddBase(BaseModel):
    user_name: str
    password: str
    email: str
    phone: int = Field()
    role: str
