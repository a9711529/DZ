# coding: utf-8

import os

wordCount = 0
result = open('result.txt', "w")

for name in os.listdir('.'):
    if name.__contains__('python'):
        print(name)
        result.write('File name contains python: ' + name + '\n')

    f = open(name)
    word = f.read()
    if word.count('python'):
        result.write('File contain python: ' + name + '\n')
    wordCount += word.count('python')
    f.close()
result.write('word count: ' + str(wordCount) + '\n')
result.close()
