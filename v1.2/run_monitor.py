from getResellList import get_rest_list
from config.config import min_price_cny
from creater import create


def run_mon(sort=0):
    while True:
        res_data = get_rest_list(sort=sort)
        for item in res_data:
            priceCny = int(float(item.get("priceCny")))
            gName = item.get("gName")
            albumName = item.get("albumName")
            albumId = item.get("albumId")
            gId = item.get("gId")
            gNum = item.get("gNum")
            print("名称：%s，简称：%s，albumId：%s，gId：%s，gNum：%s，当前价格：%s，抢购价格：%s，是否匹配：%s" % (
                albumName,
                gName,
                albumId,
                gId,
                gNum,
                priceCny,
                min_price_cny,
                min_price_cny >= priceCny))
            if min_price_cny >= priceCny:
                res = create(price=priceCny, album_id=albumId, g_num=gNum, g_id=gId)
                print("订单信息：%s" % res)


if __name__ == "__main__":
    test = run_mon(sort=1)
    print(test)
