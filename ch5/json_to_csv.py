import pandas as pd
import json


if __name__ == "__main__":
    # 單純的 list of dictionaries, 可使用 pandas read_json()
    df = pd.read_json("gossiping.json", encoding="utf-8")
    df.to_csv("gossiping.csv", index=False, encoding="utf-8")

    # 若資料有多個 keys, 使用 .DataFrame() 指定要轉換的 list of dictionaries
    with open("channel_videos.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data["videos"])
    df.to_csv("channel_videos.csv", index=False, encoding="utf-8")

    # .DataFrame() 可以處理 key to list of values, 也可以處理 list of dictoinaries
    my_dict = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    }
    df = pd.DataFrame(my_dict)
    df.to_csv("my_data_from_dict.csv", index=False)

    my_list = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35}
    ]
    df = pd.DataFrame(my_list)
    df.to_csv("my_data_from_list.csv", index=False)
