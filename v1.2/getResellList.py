from config.config import success, header, proxy_ip_type
from proxyip import proxy_ip


def get_rest_list(sort: int):
    '''
    :param sort: 0最新，1最低价格
    :return:
    '''
    api = "https://api-app.ibox.art/nft-mall-web/v1.2/nft/product/getResellList?origin=0&page=1&pageSize=20&sort=%s&type=0" % sort
    while True:
        try:
            if proxy_ip_type:
                http_args = {"url": api, "headers": header(is_login=False), "proxies": proxy_ip()}
            else:
                http_args = {"url": api, "headers": header(is_login=False)}
            req = success.get(**http_args)
            req_json = req.json()
            datas = sorted(req_json.get("data").get("list"), key=lambda key: float(key.__getitem__('priceCny')),
                   reverse=False)
            datas = [
                {"gName": item.get("gName"),
                 "albumName": item.get("albumName"),
                 "albumId": item.get("albumId"),
                 "gId": item.get("gId"),
                 "priceCny": item.get("priceCny"),
                 "gNum": item.get("gNum")
                 } for item in datas[0:6]]
            return datas
        except:
            print("信息源获取失败，重试中。")
            continue


if __name__ == "__main__":
    test = get_rest_list(sort=0)
    print(test)
