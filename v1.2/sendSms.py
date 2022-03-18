import json
from config.config import success, header


def sendsms(phone: str):
    api = "https://api-app.ibox.art/nft-mall-web/nft/user/sendSMSCode"
    data = {"phoneNumber": phone}
    req = success.post(url=api, headers=header(is_login=False), data=json.dumps(data))
    res_json = req.json()
    if res_json.get("success"):
        return {"msg": "验证码发送成功", "data": res_json}
    return {"msg": "验证码发送失败", "data": res_json}


if __name__ == "__main__":
    a = sendsms(phone="")
    print(a)
