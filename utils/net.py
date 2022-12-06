import math
import requests
import json
from config import url
from utils.log import log


global log_flag
log_flag = True

def sent_info(task_id, percent, extract_path, status):
    global log_flag
    if task_id == -1:
        if log_flag:
            log.info(f'TaksId: -1, Don\'t send network requests')
            log_flag = False
        return
    data = {
        'taskId': task_id,
        'unpackDirName': str(extract_path),
        'status': status,
        'percent': int(percent*100)
    }
    try:
        requests.post(url, json.dumps(data), headers=(
            {"content-type": "application/json"}))
    except Exception:
        log.error(f"Send data:{data} to server:{url} failed")