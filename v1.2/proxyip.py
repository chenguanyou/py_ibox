from config.config import success, proxy_ip_api


def proxy_ip():
    # 星速云 xingsudaili.com
    api = proxy_ip_api
    req = success.get(url=api)
    req_json = {'https': 'https://%s' % str(req.json().get("result")[0]).split(',')[0]}
    print("本次代理ip：%s" % req_json)
    return req_json


if __name__ == "__main__":
    a = proxy_ip()
    print(a)
