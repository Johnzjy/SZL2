# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:15:48 2018

@author: 310128142
"""

import sys, os, string, time
import os,os.path
import re
import tqdm

input_dir="./";
#input_dir="../dumpBak/";
output_dir="./";
def unzip_SZL2(_path,_file):
    rar_path=_path+_file
    un_file_name,num=os.path.splitext(rar_path)
    if len(num) == 4:
        un_path,format_name=os.path.splitext(un_file_name)
        if format_name == ".7z":
            un_path = '"{}"'.format(un_path)
            _cwd=os.getcwd()
            os.chdir('C:\Program Files (x86)\MyDrivers\DriverGenius')# 7z.exe path
            cmd = '7z.exe x "{}" -o{} -aos -r'.format(rar_path,un_path);
            os.system(cmd)
            os.chdir(_cwd)
        else:
            print "%s is not 7-zip file"%rar_path
    else:
        continue


if __name__ == '__main__':
    path="E:\\python\\github warehouse\\new data\\SZL2\\1101\\"
    filename="am_hq_index.7z.001"
    z=unzip_SZL2(path,filename)