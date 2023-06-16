import csv
import json

import pandas as pd

def read():
    # 读取CSV文件
    csvData = pd.read_csv('22.csv', header = 0,encoding="gbk")  

    # 读取CSV文件包含的列名并转换为list
    columns = csvData.columns.tolist()

    # 创建空字典
    outPut = {}

    # 将CSV文件转为字典
    for col in columns:
        
        outPut[col] = str(csvData.loc[0, col]) # 这里一定要将数据类型转成字符串，否则会报错

    # 将字典转为json格式
    jsonData = json.dumps(outPut) # 注意此处是dumps，不是dump

    # 保存json文件
    with open(r'testData.json', 'w') as jsonFile:
        jsonFile.write(jsonData)

def readCsv(): 
    # with open('22.csv', 'rb') as file:
    #     # 创建csv读取对象
    #     reader = csv.reader(file)
    #     # 遍历每一行数据
    #     for row in reader:
    #         print(row)
    # # 打开文件，指定读取模式

    jsonfile = open('./data/pediatric.json','w')
    with open('./data/pediatric.csv', 'r',encoding="gb18030") as file:
        # 创建csv读取对象
        reader = csv.reader(file)
        # 跳过表头
        fieldNmaes = next(reader)
        reader = csv.DictReader(file, fieldNmaes)

        for row in reader:
            text = '%(title)s\n%(ask)s\n%(answer)s'%{
                "title":row.get('title'),
                "ask":row.get('ask'),
                "answer" :row.get('answer')
            }
            jsonObject = {"text":text}
            print(jsonObject)
            json.dump(jsonObject, jsonfile, ensure_ascii=False)
            jsonfile.write("\n")

if __name__ == "__main__":
    readCsv()