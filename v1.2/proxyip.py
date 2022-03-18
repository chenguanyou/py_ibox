from config.config import success


def proxy_ip():
    # 星速云 xingsudaili.com
    api = "http://user.xingsudaili.com:25434/jeecg-boot/extractIp/s?uid=1500836734514565122&orderNumber=" \
          "CN2022030723274814&number=1&wt=json&randomFlag=true&detailFlag=true&useTime=60&region="
    req = success.get(url=api)
    req_json = {'https': 'https://%s' % str(req.json().get("result")[0]).split(',')[0]}
    print("本次代理ip：%s" % req_json)
    return req_json


if __name__ == "__main__":
    a = proxy_ip()
    print(a)
