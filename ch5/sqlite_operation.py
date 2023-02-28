import sqlite3
import json


def execute(fname, sql_cmd):
    with sqlite3.connect(fname) as conn:
        c = conn.cursor()
        c.execute(sql_cmd)
        conn.commit()


def select(fname, sql_cmd):
    with sqlite3.connect(fname) as conn:
        c = conn.cursor()
        c.execute(sql_cmd)
        rows = c.fetchall()
    return rows


if __name__ == "__main__":
    db = "db.sqlite"
    table = "gossiping"

    print(f"建立資料庫 {db} 及資料表 {table}")
    cmd = f"CREATE TABLE {table} (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, href TEXT, push_count INTEGER, author TEXT)"
    execute(db, cmd)

    print("插入測試資料")
    data = {
        "title": "測試文章標題",
        "href": "/bbs/Gossiping/X.9999999999.X.999.html",
        "push_count": 0,
        "author": "testAuthor"
    }
    keys = list(data.keys())
    cmd = f"INSERT INTO {table} ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}) VALUES ('{data[keys[0]]}', '{data[keys[1]]}', '{data[keys[2]]}', '{data[keys[3]]}')"
    execute(db, cmd)

    print("更新資料")
    cmd = f"UPDATE {table} SET title='更新測試文章標題' where id=1"
    execute(db, cmd)

    print("插入多筆資料")
    with open(f"{table}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            keys = list(item.keys())
            cmd = f"INSERT INTO {table} ({keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}) VALUES ('{item[keys[0]]}', '{item[keys[1]]}', '{item[keys[2]]}', '{item[keys[3]]}')"
            execute(db, cmd)

    print("選擇資料: 作者名稱含有 5566")
    cmd = f"SELECT * FROM {table} WHERE author LIKE '%5566%'"
    for row in select(db, cmd):
        print(row)
