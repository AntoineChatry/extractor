import re
import shutil
import os

for line in open("file.txt", "r+", encoding='UTF-8'):
    fo = open("destfile.txt", "a+", encoding="UTF-8")
    for match in re.findall(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', line):
        fo.write(line)
