import json
oldDataFile='old.json'
newDataFile='new.json'
mergedDataFile='merged.json'
oldData=[]
newData=[]
with open(oldDataFile, 'r', encoding='utf-8') as file:
    data = json.load(file)
    oldData = data["data"]
with open(newDataFile, 'r', encoding='utf-8') as file:
    data = json.load(file)
   
    newData = data
newIndex=oldData[len(oldData)-1]["id"]+1
for json_data in newData:
    json_data['id']=newIndex
    newIndex+=1
    oldData.append(json_data)
with open(mergedDataFile, 'w', encoding='utf-8') as file:
    json.dump(oldData, file, ensure_ascii=False, indent=4)
print("数据已成功写入"+mergedDataFile)

