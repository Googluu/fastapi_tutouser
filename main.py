from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    gpt_3_5_turbo = "gpt-3.5-turbo"
    gpt_4 = "gpt-4"
    gpt_4_32k = "gpt-4-32k"

app= FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.get("/model/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.gpt_3_5_turbo:
#         print(f'value {model_name}')
#         return {"model": model_name}
#     elif model_name.value == "gpt-4":
#         print(f'value {model_name.value}')
#         return {"model": model_name}
    
#     return {"model": model_name}

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path": file_path}