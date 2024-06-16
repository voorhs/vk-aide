from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import urllib.parse
import json
from .get_name_by_silent_token import exhange_silent_token

app = FastAPI()

@app.get('/')
def get_home_page():
    return HTMLResponse(content=open('static/index.html').read())


@app.get('/vkid_button.js')
def get_index_js():
    return FileResponse(path='static/vkid_button.js')

@app.get('/auth_success')
def auth_success(payload: str, state: str):
    decoded_payload = urllib.parse.unquote(payload)
    payload_dict = json.loads(decoded_payload)
    response = exhange_silent_token(silent_token=payload_dict["token"], uuid=payload_dict['uuid'])
    response = response['response']['success'][0]
    name = f"{response['first_name']} {response['last_name']}"
    return {"name": name}
