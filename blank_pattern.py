import json
file_path='blank.json'
data=[]
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    data = data['data']
for blank in data:
    blank["question"]=blank["question"]+'\n答案是：\n\n'
with open('blank.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
print("数据已成功写入 'blank.json'")
