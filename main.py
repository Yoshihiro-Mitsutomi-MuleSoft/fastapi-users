import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()

dummyData = [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ]

json_list = []
for wkE in dummyData:
    ini_string = json.dumps(wkE)
    dummyDic = json.loads(ini_string)
    json_list.append(dummyDic)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def usersList():
    return dummyData

@app.get("/users/{user_id}")
async def userSingle(user_id: int):

    retStr = {"id": user_id, "email": "", "first_name": "", "last_name": "", "avatar": ""}
    dummyDic = json.loads(json.dumps(retStr))

    for x in json_list:
        if x["id"] == user_id:
            dummyDic["email"] = x["email"]
            dummyDic["first_name"] = x["first_name"]
            dummyDic["last_name"] = x["last_name"]
            dummyDic["avatar"] = x["avatar"]
            print("AAA")
            break

    return dummyDic


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
