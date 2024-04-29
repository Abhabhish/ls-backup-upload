
import json
from label_studio_sdk import Client

LABEL_STUDIO_URL = 'http://13.200.132.100:8080/'
API_KEY = '1ad455ebad23562dd63cc0fd91c56877e9f14c8d'

ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
project = ls.get_project(id=36)

# print(project)
tasks = project.get_tasks()
# # print(tasks)
for task in tasks:
    f_name  = task['data']['ocr'].split('-')[-1]
    task_id = task['id']
    with open('main.txt','a') as f:
        f.write(f'{f_name},{task_id}\n')
    

