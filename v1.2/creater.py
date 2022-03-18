import json
import time
import webbrowser

import applescript
import pygame

from config.config import success, header, video_type, pay_nft_cache, video_volume


def create(price, album_id, g_num, g_id, types=0):
    if g_id in pay_nft_cache:
        return {"msg": "订单请不要多次提交", "data": {}}
    api = "https://api-app.ibox.art/nft-mall-web/v1/nft/order/create"
    data = {
        "payChannel": 22,  # 付款渠道
        "price": price,  # 价格
        "albumId": album_id,  # albumId 商品标识
        "type": types,  # 0是购买藏品，1是购买盲盒
        "gNum": g_num,  # 商品的gnum
        "gId": g_id  # 商品的gid
    }
    req = success.post(url=api, headers=header(is_login=True), data=json.dumps(data))
    pay_nft_cache.append(g_id)
    try:
        req_json = req.json()
        if req_json.get("message"):
            web_pay_url = req_json.get("data").get("orderStr")
            webbrowser.open(web_pay_url, new=0, autoraise=True)
            if video_type:
                applescript.run('set volume output volume %s' % video_volume)  # 设置音量为100
                pygame.mixer.init()
                pygame.mixer.music.load('./ok.mp3')
                # 播放音乐2分钟后停止
                pygame.mixer.music.play()
                time.sleep(120)
                pygame.mixer.music.stop()
        return {"msg": "购买成功了。", "data": req_json}
    except:
        return {"msg": "购买失败了，可能被别人抢跑了。", "data": req.text}


if __name__ == '__main__':
    a = create(price=50, album_id=100000393, g_num=44738, g_id=100648345)
    print(a)
