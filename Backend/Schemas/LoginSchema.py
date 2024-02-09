from pydantic import BaseModel, Field


class LoginBase(BaseModel):
    email: str = Field(pattern='^[a-zA-Z0-9._%+-]+@sece\.ac\.in$')
    password: str = Field(min_length=6)

