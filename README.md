# 程序说明

通过python脚本调用[UniExtract](https://github.com/Bioruebe/UniExtract2)来实现安装包文件的解压，并根据不同的文件类型，将对应文件分类到不同的文件夹。在config.py中需要明确uniextract2的位置，才能正常执行。

## 环境部署

python - 3.7

```bash
pip install -r requirements.txt
```

## 使用方式

```bash
python main.py --file_path FILE_PATH --extract_path EXTRACT_PATH --task_id TASK_ID --folder TRUE/FALSE
```

参数说明

|参数|描述|
|:---:|:---:|
|file_path|安装包文件路径|
|extract_path|解压目标路径，默认为安装文件包同目录|
|task_id|分析系统中对应的任务ID,默认为-1|
|folder|安装包路径为一个文件夹|


eg:
在非分析系统中解压一个软件到指定路径
```bash
python main.py \
--file_path "C:\\temp\\temp.exe" \
--extract_paht "C:\\temp\\extract" \
```

eg:
在非分析系统中解压一个软件同级目录
```python
python main.py \
--file_path "C:\\temp\\temp.exe"
```

eg:
在非分析系统中选择一个由安装包构成的文件夹
```python
python main.py \
--file_path "C:\\temp"
--folder true 
```
