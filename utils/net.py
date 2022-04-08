import requests
import json
from config import url
from utils.log import log

global flag
flag = True

def sent_info(task_id, percent, extract_path, status, test_flag):
    if test_flag:
        return
    global flag
    data = {
        'taskId': task_id,
        'unpackDirName': str(extract_path),
        'status': status,
        'percent': int(percent*100)
    }
    if int(percent * 100) % 10 == 0 and flag:
        log.info(f"Sending data:{data} to server:{url}")
        flag = False
    if int(percent * 100) % 10 != 0:
        flag = True 
    try:
        requests.post(url, json.dumps(data), headers=(
            {"content-type": "application/json"}))
    except Exception:
        log.error(f"Send data:{data} to server:{url} failed")