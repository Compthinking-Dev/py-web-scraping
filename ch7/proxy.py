import requests
import random

if __name__ == '__main__':
    # 代理伺服器查詢: https://free-proxy-list.net/
    proxy_ips = ['40.76.245.70:8080', '206.81.31.215:80']
    ip = random.choice(proxy_ips)
    print(f"Using {ip}")
    resp = requests.get("http://httpbin.org/ip", proxies={'http': 'http://' + ip}).json()
    print(resp)
