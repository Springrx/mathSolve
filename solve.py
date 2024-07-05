import json
dirtyData=[]
# 打开并读取JSON文件
with open('a.json', 'r', encoding='utf-8') as file:
    dirtyData = json.load(file)
dirtyData = dirtyData['example']
clearData = []
def remove_fields(data, fields_to_remove):
    
    # 移除字典中的指定字段
    # :param data: 原始字典
    # :param fields_to_remove: 要移除的字段列表
    # :return: 移除字段后的字典
    
    for field in fields_to_remove:
        if field in data:
            del data[field]
    return data
# 要删除的字段
fields_to_remove = ["year", "category", "score",'index']
for json_data in dirtyData:
    # 移除指定字段
    modified_data = remove_fields(json_data, fields_to_remove)
    clearData.append(modified_data)

with open('clearData.json', 'w', encoding='utf-8') as file:
    json.dump(clearData, file, ensure_ascii=False, indent=4)

print("数据已成功写入 'clearData.json'")
