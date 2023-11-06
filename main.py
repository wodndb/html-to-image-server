from typing import Union
from fastapi import FastAPI
from html2image import Html2Image

hti = Html2Image(size=(500, 200))
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    html = """<h1> An interesting title </h1> This page will be red"""
    css = "body {background: red;}"

    hti.screenshot(html_str=html, css_str=css, save_as='red_page.png')
    return {"item_id": item_id, "q": q} 