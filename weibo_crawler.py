import requests
import json
import csv
import random
import time

BASE_URL = "https://m.weibo.cn/api/container/getIndex"
QUERY = "231522type=1&q=刹车失灵"
HEADERS_LIST = [
    # 常见User-Agent，可自行扩展
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
]

def get_comments(page):
    headers = {
        "User-Agent": random.choice(HEADERS_LIST),
        "Accept": "application/json"
    }
    params = {
        "containerid": QUERY,
        "page_type": "searchall",
        "page": page
    }
    try:
        resp = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"请求失败，状态码: {resp.status_code}")
            return None
    except Exception as e:
        print(f"请求异常: {e}")
        return None

def parse_comments(json_data):
    comments = []
    if not json_data:
        return comments
    try:
        cards = json_data.get("data", {}).get("cards", [])
        for card in cards:
            if card.get("card_type") == 9:
                mblog = card.get("mblog", {})
                # 评论内容
                text = mblog.get("text", "")
                # 用户信息
                user = mblog.get("user", {})
                user_id = user.get("id", "")
                # 点赞数
                attitudes_count = mblog.get("attitudes_count", 0)
                # 发布时间
                created_at = mblog.get("created_at", "")
                # 设备来源
                source = mblog.get("source", "")
                comments.append([user_id, text, attitudes_count, created_at, source])
    except Exception as e:
        print(f"解析异常: {e}")
    return comments

def save_to_csv(data, filename):
    with open(filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["用户ID", "评论内容", "点赞数", "发布时间", "设备来源"])
        writer.writerows(data)

def main():
    all_comments = []
    for page in range(1, 101):
        print(f"正在爬取第{page}页...")
        json_data = get_comments(page)
        comments = parse_comments(json_data)
        if not comments:
            print("本页无数据，跳过。")
        else:
            all_comments.extend(comments)
        time.sleep(random.uniform(1, 3))
    save_to_csv(all_comments, "weibo_comments.csv")
    print("爬取完成，数据已保存为 weibo_comments.csv")

if __name__ == "__main__":
    main()