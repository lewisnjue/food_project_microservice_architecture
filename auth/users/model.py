from sqlmodel import SQLModel, Field
import uuid

class Users(SQLModel,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True)
    email: str = Field(index=True,nullable=False,unique=True)
    password:str = Field(nullable=False)






