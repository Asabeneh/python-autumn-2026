'''
.txt
.pdf
.xls
.csv
.tsv
.json
tson
'''

""" f = open('sample.txt', 'r')
lines = f.read().splitlines()
for index, line in enumerate(lines):
    words = line.split()
    if 'make' in words:
        print(f'The work make was found in line {index + 1}')
        print(f'Line - {index + 1}', line)
f.close() """

with open('sample.txt','r') as f:
    lines = f.read().splitlines()
    for index, line in enumerate(lines):
        words = line.split()
        if 'make' in words:
            print(f'The work make was found in line {index + 1}')
            print(f'Line - {index + 1}', line)
