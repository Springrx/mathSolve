import re

# 转换函数
def process_fill_in_blank(data,startIndex):
    transformed_data = []
    idx=startIndex
    for example in data['example']:
        question_text = example['question']
        
        # 判断是否既有题号又有分数
        # if re.match(r"^\d+\.\s*（\d+\s*分）\s*", question_text):
            # 删除题号和分数部分
        #     question_cleaned = re.sub(r"^\d+\.\s*（\d+\s*分）\s*", "", question_text)
        # elif re.match(r"^\d+\.\s*\(\d+\s*分\)\s*", question_text):
            # 删除题号和分数部分
        #     question_cleaned = re.sub(r"^\d+\.\s*\(\d+\s*分\)\s*", "", question_text)
        if re.match(r'^\d+\.\s*|^.*?[)）]', question_text):
            # 删除题号和分数部分
            question_cleaned = re.sub(r'^\d+\.\s*|^.*?[)）]', "", question_text)        
        elif re.match(r"^\d+\.\s*", question_text):
            # 仅删除题号
            question_cleaned = re.sub(r"^\d+\.\s*", "", question_text)
        else:
            # 不作处理
            question_cleaned = question_text

        new_entry = {
            "id": idx,  # 使用枚举索引作为新的id
            "question": question_cleaned,
            "answer": [example['answer'].strip()]
        }
        idx+=1
        transformed_data.append(new_entry)
    return transformed_data