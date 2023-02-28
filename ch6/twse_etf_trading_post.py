import requests

if __name__ == "__main__":
    URL = "https://www.twse.com.tw/zh/exchangeReport/MI_INDEX"
    form_data = {
        "response": "json",
        "type": "0099P",
        "date": "20221220"
    }
    resp = requests.post(URL, data=form_data)
    data = resp.json()
    print(data)
