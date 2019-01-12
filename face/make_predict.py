#-*-coding:utf-8-*-#
"""
@Author: ypp
@Filetype:python source code
@Tool: Vim & Gcc
"""
import os
import sys
inputfile = sys.argv[1]
with open(inputfile,'r') as f:
    lines = f.readlines()
    for line in lines:
        predict = line.split()[-1]
        true = line[:line.rfind('.')].split('_')[-1]
        
        new_line = 'ture {} {}'.format(true,predict)
        print(new_line)
