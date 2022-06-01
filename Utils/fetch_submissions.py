import requests
from datetime import datetime
import json

PROBLEMS_URL = "https://leetcode.com/api/problems/algorithms/"
SUBMISSIONS_URL = "https://leetcode.com/api/submissions/?offset={}&limit={}"

with open("secrets.json", "r") as secrets:
    f = json.load(secrets)
    FILE_PATH = f["FILE_PATH"]
    FILE_PATH2 = f["FILE_PATH2"]
    LEETCODE_SESSION = f["LEETCODE_SESSION"]
    csrf_token = f["csrftoken"]

cookies = {
    "csrftoken": csrf_token,
    "NEW_PROBLEMLIST_PAGE": "1",
    "LEETCODE_SESSION": LEETCODE_SESSION,
}


def build_dict(
    timestamp: int,
    title: str,
    title_slug: str,
    status: str,
    lang: str,
    runtime: str,
    memory: str,
    code: str,
) -> dict:
    return {
        "timestamp": datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S"),
        "title": title,
        "title_slug": title_slug,
        "status": status,
        "lang": lang,
        "runtime": runtime,
        "memory": memory,
        "code": code,
    }


def get_submissions():
    current = 0
    response_json: dict = {"has_next": True}

    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    # while ("detail" not in response_json and "has_next" in response_json and response_json["has_next"]):
    response_json = requests.get(
        SUBMISSIONS_URL.format(current, 20), cookies=cookies
    ).json()

    if "submissions_dump" in response_json:
        for sub in response_json["submissions_dump"]:
            submission = build_dict(
                sub["timestamp"],
                sub["title"],
                sub["title_slug"],
                sub["status_display"],
                sub["lang"],
                sub["runtime"],
                sub["memory"],
                sub["code"],
            )

            if sub["status_display"] == "Accepted" and submission not in data:
                data.append(submission)

        # current += 20
        # time.sleep(1)

    # if "detail" in response_json:
    #     print("CURRENT:", current)
    #     print(response_json["detail"])

    data.sort(key=lambda x: x['timestamp'], reverse=True)

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

get_submissions()