import requests
import random
import uuid

success = requests.session()

token = ""
proxy_ip_api = ""  # 代理ip接口
proxy_ip_type = False  # 是否开启代理ip
video_type = True  # 成功后是否播放音乐
video_volume = 80  # 成功后播放音乐的音量
pay_nft_cache = []  # 存放已经购买过的NFT，避免多次提交封号，封IP(这里不要动，系统会自动放进去)
min_price_cny = 20  # 金额小于多少进行抢
work_num = 1  # 每一次请求，线程的数量，默认为2


def header(is_login: bool):
    headers = {
        "content-type": "application/json",
        "ib-device-id": "%s" % uuid.uuid4().hex,
        "accept": "*/*",
        "ib-app-version": "1.0.7",
        "ib-platform-type": "ios",
        "ib-trans-id": "%s_iOS" % uuid.uuid4().hex,
        "accept-language": "zh-Hans-CN;q=1",
        "accept-encoding": "gzip, deflate, br",
        # "user-agent": "iBox/1.1.0 (iPhone; iOS 15.4; Scale/3.00),iBoxApp",
        "wtoken": "e%s_UQZNuFXtqqr8u5SfVJKLVYM8bObGH9W3EMWlIDgdPM80q7QYRYO03PzImE0tuQajiuk0b3h1T2veF7+Hz/B0H"
                  "AEoJlJeSt5gPYuTqq6S7dMYoLKRD81q3BgEf41psWCGJ+PCIjeaiF4HBPGmgUljN2B3w2Ee7aCtQwK2bcF1rsQ4uQJNlh"
                  "20fPRhq75jXpC1JUN2CJUHqi10c8xTxQbwajKX03jivcLa0ws6ialdRFHTRl1K+99dXY1jYatqOuqOzuz2bZnP7idHjb3Z"
                  "nj9OKaKZBXxk15/48tavyyhATKG4HJZLqiEul77gSBKObLel2fAOKAMYwXVLLlBdO39gFAVtqL+Ce/gLKOAR8RWBy+PPMQ"
                  "cW+iy1tI4TAPzr+S2Hnylk2fH38bpaI0eepMyZAGgaFYaD9PiMJL7mNAhW1ABo6QdS7WEpMJEH/kvyBfM5vq7mUa2kJnwHna"
                  "aKfy+IWY9zN7F7qNKpcfB0QU9kCqTDf6R3lPfytKsV0IfC2wZ5SbTMVMlm2G6ZPP4qnAv1+x/NVu80OBmP/ckzHrnPHsivrNC"
                  "dXQuplvD560ZoM+US&b7ee_7F9D1141D8B668D8D0596713EEF541D5CE5D427D1AAE196F30" % random.randint(0, 500)}
    if is_login:
        headers["hb-nft-token"] = token
        headers["ib-user-token"] = token

    return headers


if __name__ == '__main__':
    token = "11111"
    test = header(is_login=False)
    print(test)
