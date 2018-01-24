#!/usr/bin/env python
# -*- coding: utf-8 -*-

# INPUT
# "October 1, 2017, Hour 0","xxxxx","xxxxx",1,0
# "October 1, 2017, Hour 0","xxxxx","xxxxx",1,0
# "October 1, 2017, Hour 0","xxxxx","",1,0
# "October 1, 2017, Hour 0","xxxxx","xxxxx",1,0
# "October 1, 2017, Hour 0","xxxxx","xxxxx",1,0

# OUTPUT
# 2017-10-01 00:00:00,xxxxx,xxxxx,1,0
# 2017-10-01 00:00:00,xxxxx,xxxxx,1,0
# 2017-10-01 00:00:00,xxxxx,,1,0
# 2017-10-01 00:00:00,xxxxx,xxxxx,1,0
# 2017-10-01 00:00:00,xxxxx,xxxxx,1,0

import csv

month = {'April':'-04','May':'-05','June':'-06',
		 'July':'-07','August':'-08','September':'-09',
		 'October':'-10','November':'-11','December':'-12',
		 'January':'-01','February':'-02','March':'-03'}

day =  {'1':'-01','2':'-02','3':'-02','4':'-02','5':'-02',
		'6':'-02','7':'-02','8':'-02','9':'-02','10':'-10',
		'11':'-11','12':'-12','13':'-13','14':'-14','15':'-15',
		'16':'-16','17':'-17','18':'-18','19':'-19','20':'-20',
		'21':'-21','22':'-22','23':'-23','24':'-24','25':'-25',
		'26':'-26','27':'-27','28':'-28','29':'-29','30':'-30','31':'-31'}

hour = {'0':' 00:00:00','1':' 01:00:00','2':' 02:00:00','3':' 03:00:00','4':' 04:00:00',
		'5':' 05:00:00','6':' 06:00:00','7':' 07:00:00','8':' 08:00:00','9':' 09:00:00',
		'10':' 10:00:00','11':' 11:00:00','12':' 12:00:00','13':' 13:00:00','14':' 14:00:00',
		'15':' 15:00:00','16':' 16:00:00','17':' 17:00:00','18':' 18:00:00','19':' 19:00:00',
		'20':' 20:00:00','21':' 21:00:00','22':' 22:00:00','23':' 23:00:00','24':' 24:00:00'}

f = open('edited.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

with open('XXXXXXXXXX.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        record = row[0].split()
        record[2] = record[2].replace(',','')
        record[0] = month[record[0]]
        record[1] = day[record[1].replace(',','')]
        record[4] = hour[record[4]]
        row[0] = record[2]+record[0]+record[1]+record[4]
        writer.writerow(row)
        print(row)
