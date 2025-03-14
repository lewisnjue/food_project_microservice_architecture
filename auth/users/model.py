from sqlmodel import SQLModel, Field


class Users(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    email: str = Field(index=True,nullable=False,unique=True)
    password:str = Field(nullable=False)






