import json

def upload_post(post):
    print(f"Uploading: {post.get('title', 'No title')}")  # post は辞書（dict）であるべき

def main():
    with open("dist/posts.json", "r", encoding="utf-8") as file:
        posts = json.load(file)  # ここで JSON を読み込む

    if not isinstance(posts, list):  # posts がリストでなければリストにする
        posts = [posts]

    for post in posts:
        upload_post(post)

if __name__ == "__main__":
    main()
