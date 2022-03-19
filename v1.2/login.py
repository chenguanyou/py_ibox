import json
from config.config import success, header


def login(phone: str, code: str):
    api = "https://api-app.ibox.art/nft-mall-web/v1.1/nft/user/login"
    data = {"code": code, "phoneNumber": phone}
    req = success.post(url=api, headers=header(is_login=False), data=json.dumps(data))
    req_json = req.json()
    if req_json.get("success"):
        return {"msg": "登录成功", "token": req_json.get("data").get("token"), "data": req_json}
    return {"msg": "登录失败", "token": None, "data": req_json}


if __name__ == '__main__':
    test = login(phone="", code="")
    print(test)
