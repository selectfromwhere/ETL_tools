#!/usr/bin/python
# coding: UTF-8
import subprocess
import re
import date_list as dl

f = open('bq_query.sql')
query = f.read()
f.close()

for i in range(len(dl.date_list)):
	dates = dl.date_list[i]
	queryx = query.replace('$PART_DAY', dates[0]).replace('$YDAY', dates[1]).replace('$TDAY', dates[2])
	print(queryx)
	subprocess.call(queryx)
