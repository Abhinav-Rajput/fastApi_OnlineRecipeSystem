import uvicorn
from fastapi import FastAPI

from uuid import UUID


app = FastAPI(
    title="Online Recipe System API",
    description="""This prototype aims to store various recipes on any menu to be viewed and 
rated by visitors. It even classifies the recipes according to the place 
of origin and menu type. Users may search for their desired recipe for 
reference, rating, and feedback purposes. It has a feature that allows 
users to attach keywords to each recipe for search purposes. 
The microservice application is an initial architecture for a robust 
online recipe platform.""",
    docs_url="/",
)

def create_login(id:UUID, username: str, password:str, type: UserType):
    account = {"id": id, "username": username, "password": password, "type": type}
    return account

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
