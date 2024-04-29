import json

invoices = json.load(open('main.json',encoding='utf-8'))


invoices_dict = {}
for invoice in invoices:
    f_name = invoice['data']['ocr'].split('-')[-1]
    invoices_dict[f_name] = invoice




import json
from label_studio_sdk import Client

LABEL_STUDIO_URL = 'http://13.200.132.100:8080/'
API_KEY = '1ad455ebad23562dd63cc0fd91c56877e9f14c8d'

ls = Client(url=LABEL_STUDIO_URL, api_key=API_KEY)
project = ls.get_project(id=32)


tasks = project.get_tasks()
# print(tasks)
for task in tasks:
    f_name  = task['data']['ocr'].split('-')[-1]
    task['annotations'] = invoices_dict[f_name]['annotations']
    for annotation in task['annotations']:
        annotation['completed_by']=1
    # task['annotations']['completed_by']=1
    

print(tasks)

with open('out.json','w',encoding='utf-8') as f:
    json.dump(tasks,f)


