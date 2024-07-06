import re

# 要删除的字段
fields_to_remove = ["year", "category", "score",'index']
def replace_question(text):
    if text.startswith('问题是：'):
        return
    # 使用正则表达式匹配从字符串开始到第一个 ')' 或 '）' 之前的所有字符，并将它们替换为 "问题是："
    # '^.*?[)）]' 匹配从开始到第一个 ')' 或 '）' 的所有字符（包括 ')' 或 '）'），'?' 使匹配尽可能少的字符    
    return re.sub(r'^\d+\.\s*|^.*?[)）]', '问题是: ', text)
    
def remove_fields(data, fields_to_remove):   
    # 移除字典中的指定字段
    # :param data: 原始字典
    # :param fields_to_remove: 要移除的字段列表
    # :return: 移除字段后的字典   
    for field in fields_to_remove:
        if field in data:
            del data[field]            
    return data
def replace_answer(modified_data):
    correct_answer_letter = modified_data["answer"][0]
    # 使用正则表达式匹配所有选项，并创建一个字典存储它们
    options = re.findall(r'([A-D])\.\s*\$(.*?)\$\n', modified_data["question"])
    options_dict = {letter: content for letter, content in options}

    # 根据提供的答案字母查找对应的选项内容
    correct_option_content = options_dict.get(correct_answer_letter)
    modified_data["answer"]={correct_answer_letter:f"${correct_option_content}$"}
    return modified_data
def process_single_choice(data,startIndex):
    index=startIndex
    clearData=[]
    for json_data in data['example']:
        # 移除指定字段
        modified_data = remove_fields(json_data, fields_to_remove)
        modified_data['id']=index
        modified_data["question"]=replace_question(modified_data["question"])
        modified_data=replace_answer(modified_data)
        index+=1
        clearData.append(modified_data)
    return clearData


