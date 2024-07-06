import json
import os
from process_fill_in_blank import process_fill_in_blank
from process_single_choice import process_single_choice

class RawData:
    def __init__(self, filePath, fileType):
        self.processedData=[]
        self.filePath = filePath
        self.fileType = fileType

    def processRawData(self,startIndex):
        endIndex = 0
        with open(self.filePath, 'r', encoding='utf-8') as file:
            data = json.load(file)       
        if self.fileType == 'fill_in_blank':
            transformed_data = process_fill_in_blank(data,startIndex)
            endIndex = transformed_data[len(transformed_data)-1]['id']
            self.processedData = transformed_data            
        if self.fileType == 'single_choice':
            transformed_data = process_single_choice(data,startIndex)
            endIndex = transformed_data[len(transformed_data)-1]['id']
            self.processedData = transformed_data           
        return endIndex

    def getProcessedData(self):
        return self.processedData

processed_data = []
startIndex=0
# Get the list of files in the /rawData directory
file_list = os.listdir('rawData')

# Iterate over each file
for file_name in file_list:
    # Check if the file name starts with 'fill_in_blank'
    file_type=''
    if file_name.startswith('fill_in_blank'):
        # Create a new instance of RawData
        file_name = 'rawData/' + file_name
        file_type = 'fill_in_blank'
    if file_name.startswith('single_choice'):
        # Create a new instance of RawData
        file_name = 'rawData/' + file_name
        file_type = 'single_choice'
    raw_data = RawData(file_name, file_type)        
    # Process the raw data
    endIndex=raw_data.processRawData(startIndex)  
    startIndex=endIndex+1     
    # Get the processed data
    processed_data.append(raw_data.getProcessedData())
with open('processedData.json', 'w', encoding='utf-8') as file:
    json.dump(processed_data, file, ensure_ascii=False, indent=4)