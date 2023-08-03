from enum import Enum
from typing import Union
from fastapi import FastAPI

# what is pydantic
from pydantic import BaseModel

# execute to create Instans
app = FastAPI()

class Item(BaseModel):
    # has required attribute name that should be a str
    name: str
    # has required attribute price that should be a int
    price: int
    # default value is null object = None
    # what is diffirent between null and None?
    # it means is_offer is optional value 
    # nullの意味合いでレスポンスを返した時にフロントではnullではなくundefinedが渡ってくるため、認識齟齬の問題がある
    is_offer: Union[bool, None] = None



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    # check to the type of item_id
    # pathパラメーターがintで渡ってくるのが謎、必ずstrだと思っていたのに
    # conversionしてるのかも
    # print({'item_id': type(item_id)})
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    # checks to the contents of the object
    # print(vars(item))
    return {"item_name": item.name, 'item_id': item_id, 'price': item.price}

class SoccerPlayerName(str,Enum):
    Messi = "Messi"
    Ronaldo = "Ronaldo"

class Player(BaseModel):
    name: str
    country: str

# is演算子の方が処理が早いらしい
@app.get("/players/{player_name}") 
def get_Player(player_name: SoccerPlayerName)-> Player:
    if player_name is SoccerPlayerName.Messi:
        return { "name": "Lionel Andrés Messi", "country": "Argentina" }
    if player_name == SoccerPlayerName.Ronaldo:
        return { "name": "Cristiano Ronaldo","country": "Portugal" }
    
    return { "name": "none","country": "none" }

fake_item_db = [{"item_name":"Foo"},{"item_name":"Fizz"},{"item_name":"Bazz"}]

@app.get("/items")
def read_items(skip: int = 0 , limit: int = 10):
    return fake_item_db[skip: skip + 10]