# mathSolve
processedData中是处理好的数据
rawData中是数据来源
data必须在example字段中
文件放在rawData文件夹中：填空题以fill_in_blank开头，单选以single_choice开头
## 数量统计
填空题总数166道
单选题总数480道
合计646道
## todo
填空题需要改成'\n答案是\n\n'的样式
需要将jsonl格式的数据整合进去

## data pattern
1、选择题：以问题是: 开头，在需要进行选择的地方有(     )
{"id": 0, "question": "问题是: question（       ）\nA:4\nB:2\nC:1\nD:0", "answer": {"B": "2"}}
2、填空题：以\n\n答案是\n\n结尾，在需要填空的地方有空格或(     )
{"id": 3, "question": "question（       ）。 A. 10\n B. 18\n C. 20\n\n答案是：\n\n", "answer": ["C"]}

