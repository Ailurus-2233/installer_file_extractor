import requests
import json
from config import url

def sent_info(task_id, percent, extract_path, status):
    data = {
        'taskId': task_id,
        'unpackDirName': str(extract_path),
        'status': status,
        'percent': int(percent*100)
    }
    print(f"[log]: post {data}")
    try:
        requests.post(url, json.dumps(data), headers=(
            {"content-type": "application/json"}))
    except:
        print(f'[error]: {url} 连接异常')