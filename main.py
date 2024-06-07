from typing import Optional

from fastapi import FastAPI


app = FastAPI() # 建立一個 Fast API application

@app.get("/") # 指定 api 路徑 (get方法)
def hellow_world():
    return {"Hello": "World"}


@app.get("/date/{height}/{weight}") # 指定 api 路徑 (get方法)
def get_BMI(height: float, weight: float):
    bmi = weight / (height * height)
    return {"BMI": bmi}