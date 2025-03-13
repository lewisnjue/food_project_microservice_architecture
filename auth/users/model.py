from sqlmodel import SQLModel, Field,create_engine




class Users(SQLModel,table=True):
    id: int | None = Field(default=None,primary_key=True)
    email: str = Field(index=True,nullable=False)
    password:str = Field()




"""
change this ones in no time just for testing , change to deployment ones 
"""
database_name = 'default.db'


database_url = f"sqlite:///{database_name}"



engine = create_engine(database_url,echo=True)


SQLModel.metadata.create_all(engine)
