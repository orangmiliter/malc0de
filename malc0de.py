import re
import requests
import os
import csv
import argparse
import sys
from datetime import datetime

#time
waktu = datetime.now()
tahun = waktu.year
bulan = waktu.month
hari = waktu.day

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Input url target ", nargs='+')
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()
argspace = ' '.join(args.url)
keyword = str(argspace)


alamat = requests.get('http://malc0de.com/database/index.php?&search=ID&page=%s' % keyword).text
listParse = re.findall(r"<td>(.*?)</td>", alamat, re.I | re.M)
# print (listParse)

#hajarkeCSV
filecsv = open('malcode/malc0de-p%s-%s-%s-%s.csv' % (keyword, tahun, bulan, hari), 'w')
writecsv = csv.writer(filecsv)
writecsv.writerow(["Date", "Domain", "IP", "Autonomous System Name"])
i = 0
tempA,tempB = [],[]
for parse in listParse:
    i += 1
    if '<a href=' in parse:
        parse = re.findall(r">(.*?)</", parse, re.I | re.M)[0]
    tempA.append(parse)
    if i >= 7:
        writecsv.writerow([tempA[1], tempA[2], tempA[3], tempA[5]])
        i, tempA = 0, []
print ("malc0de-p%s-%s-%s-%s.csv" % (keyword, tahun, bulan, hari))
