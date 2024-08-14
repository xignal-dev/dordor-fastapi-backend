import os, sys
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router

app = FastAPI()

# origins에는 protocal, domain, port만 등록한다.
origins = [
    "http://localhost:3000", "http://223.130.139.104:8080", "http://175.45.204.196:8080"
    # "http://192.168.0.13:3000", # url을 등록해도 되고
    # "*" # private 영역에서 사용한다면 *로 모든 접근을 허용할 수 있다.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # cookie 포함 여부를 설정한다. 기본은 False
    allow_methods=["*"],    # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다.
    allow_headers=["*"],	# 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(api_router)

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}