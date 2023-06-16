from argparse import ArgumentParser
import json
import multiprocessing
import os
from pathlib import Path
from rich.progress import Progress
import re

from bs4 import BeautifulSoup

#Meeting needs params

#1.answer item length > 100
CONTENT_LENGTH_LIMIT:int = 100

#2.answer list contain item count >=5
ANSWER_COUNT_LIMIT:int = 5

#whether print not meet need data
DUMP_LOG:bool = False

def extractContent(doc:str):
    soup = BeautifulSoup(doc, features="lxml")
    anchors1 = soup.find_all('p')
    anchors2 = soup.find_all('br')
    anchors3 = soup.find_all('div')
    for item in anchors1:
        item.append('\n')
    for item in anchors2:
        item.append('\n')
    for item in anchors3:
        item.append('\n')
    pattern = re.compile(r'<[^>]+>',re.S)
    result = pattern.sub('', soup.get_text().strip())
    ret = re.sub(r'http\S+', '', result)

    return ret

def finilize(line, doc:dict, outPath:Path):
    single_qa_Count:int = 0
    answers = doc.get('answers')
    if len(answers) == 0:
        if DUMP_LOG:print(f'answer empty \n{line}')
        return single_qa_Count
    if len(answers) < ANSWER_COUNT_LIMIT:
        if DUMP_LOG:print(f'answer count ={len(answers)}\n{line}')
        return single_qa_Count
    with open(outPath,'at') as outFile:
        for answer in answers:
            content = extractContent(answer.get('content'))
            if len(content) < CONTENT_LENGTH_LIMIT:
                if DUMP_LOG:print(f'answer len ={len(content)}\n{answer}')
                continue
            text = '%(title)s\n%(detail)s\n%(content)s'%{
                "title" : doc.get('question').get('title'),
                "detail": extractContent(doc.get('question').get('detail')),
                "content" : content
            }
            jsonObject = {"text":text, "url": answer.get('url')}
            json.dump(jsonObject, outFile, ensure_ascii=False)
            outFile.write("\n")
            single_qa_Count = single_qa_Count + 1
    return single_qa_Count

def doProcessTask(filePath:Path, output:Path): 
    question_tag = 'Zhihu Model:'
    outputFile = output / (filePath.stem + '.json')
    if os.path.exists(outputFile):
        os.remove(outputFile)
    total_qa_count:int = 0
    total_count:int = 0
    with open(filePath, 'r') as file:
        for line in file:
            linePos = line.find(question_tag)
            if linePos == -1:
                continue
            total_count +=1
            question_dict = json.loads(line[linePos + len(question_tag):])
            total_qa_count += finilize(line, question_dict, outputFile)
    print(f'{filePath} file total lines:{total_qa_count}')
    return total_qa_count, total_count

def processFileParallel(folder:str):
    fileNames = [Path(os.path.join(folder, f)) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if DUMP_LOG:print(fileNames)
    output = fileNames[0].parent / 'output'
    output.mkdir(parents=True, exist_ok=True)
    
    threads = []
    #all crawl files qa pairs count
    sum_qa_count = 0
    #ll crawl files  line count
    sum_total_count = 0
    Pool = multiprocessing.Pool(processes=5)
    with Progress() as progress:
        task_id = progress.add_task("[readFile]Working...", total=len(fileNames))
        for name in fileNames:
            proc = Pool.apply_async(doProcessTask, (name, output))
            threads.append(proc)
        for proc in threads:
            total_qa_count, total_count = proc.get()
            sum_qa_count += total_qa_count
            sum_total_count += total_count
            progress.advance(task_id)
        print(f'{str(output)} folder contain total lines:{sum_total_count} total QA-pairs:{sum_qa_count}')

def getArgs():
	parser = ArgumentParser('handle zhi hu crawl data tools')
	parser.add_argument('path',help='file folder path')
	r = parser.parse_args()
	return r

if __name__ == "__main__":
    r = getArgs()
    processFileParallel(r.path)