import requests
import random

if __name__ == '__main__':
    # 代理伺服器查詢: https://free-proxy-list.net/
    proxy_ips = ['36.228.213.186:80', '106.104.134.209:8382']
    ip = random.choice(proxy_ips)
    print(f"Using {ip}")
    resp = requests.get("http://httpbin.org/get", proxies={'http': 'http://' + ip}).json()
    print(resp)
