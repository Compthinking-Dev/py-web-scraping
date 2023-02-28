import json

if __name__ == "__main__":
    with open("gossiping.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # ensure_ascii=False: 檔案內容可顯示非英文字元
    # indent=2: 格式內容縮排兩個空格
    # sort_keys=True: 排序 keys
    with open("gossiping2.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
