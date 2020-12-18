# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pathlib
import pandas
import json
p = pathlib.Path.home() / 'Dropbox' / 'Riksarkivet' / '1800_ner' / '1800_dataset'


# %%
fileList = list(p.rglob('*conll.txt'))


# %%

with open('trainingSetFullNoScrambledSent.txt', 'w+') as train, open('valSet.txt', 'w+') as val:
    
    totalNoOfSentsTrain = 0
    totalNoOfSentsVal = 0
    for doc in fileList:
        with open(doc, mode='r') as f:
            
            headerAndSentList = [line.strip('# ').strip() for line in f if line.startswith('#')]
            header = {}
            
            for i in range(0, 41):
                keyValue = headerAndSentList[i].split(':')
                if len(keyValue) > 1:
                    header[keyValue[0]] = keyValue[1].strip()
            if not header['sentenceOrder'] == 'scrambled':
                noOfSents = int(header['sentences'].replace(',', ''))
                noOfTokens = int(header['words'].replace(',', ''))
                
                totalNoOfSentsTrain += int(noOfSents * 0.9)
                totalNoOfSentsVal += noOfSents - int(noOfSents * 0.9)
                
                train.write('\n' + header['title'] + '\n')
                val.write('\n' + header['title'] + '\n')
                sentIndex = 1
                for elem in headerAndSentList:
                    if elem.startswith('text') and sentIndex <= int(noOfSents * 0.9):
                        train.write(elem.split('=')[1].strip())
                        if sentIndex % 4 == 0:
                            train.write('\n')
                        sentIndex += 1
                    elif elem.startswith('text'):
                        val.write(elem.split('=')[1].strip())
                        if sentIndex % 4 == 0:
                            val.write('\n')
                        sentIndex += 1
                train.write('\n')
                val.write('\n')

    print(str(totalNoOfSentsTrain) + '\n' + '\n' + str(totalNoOfSentsVal) + '\n')
        

# %%



