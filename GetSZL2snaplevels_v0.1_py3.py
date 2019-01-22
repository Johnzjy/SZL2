#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import re
import string
import sys
import time


input_dir="./";
output_dir="./";
#molde='_snap_level_spot'
molde='_hq_trade_spot'

#需要根据自己的系统 7z.exe 路径更改
PATH_7z_EXE= 'C:\Program Files (x86)\MyDrivers\DriverGenius' 

def unzip_7z(_path,_file):
    """
    unzip the 7-zip to the current path

    Parameters
    ----------
    _path: file path
    _file: file name

    Returns
    -------

    """

    rar_path=_path+_file
    print (rar_path)
    un_file_name,num=os.path.splitext(rar_path)
    if len(num) == 4:
        un_path,format_name=os.path.splitext(un_file_name)
        if format_name == ".7z":
            un_path = '"{}"'.format(un_path)
            _cwd=os.getcwd()

    
            os.chdir(PATH_7z_EXE)# 7z.exe path 
            cmd = '7z.exe x "{}" -o{} -aos -r'.format(rar_path,un_path);
            os.system(cmd)
            os.chdir(_cwd)
        else:
            print ("%s is not 7-zip file"%rar_path)

def unzip_SZL2():
    """
    unzip all snap_level_spot.7z file

    Parameters
    ----------

    Returns
    -------

    """
    print (os.getcwd())
    for root, dirnames, filenames in os.walk(input_dir):
        for filename in filenames:
            #print filename.endswith(suffix)
            if not filename.endswith(molde+".7z.001"):
                continue
            path=os.getcwd()+root[1:]+"\\"
            print(path)
            unzip_7z(path,filename)

def load_SZL2(code_list):
    for root, dirnames, filenames in os.walk(input_dir):
        for filename in filenames[:2]:
            #print filename.endswith(suffix)
            if not filename.endswith(molde+".txt"):
                continue
            filenamepath = os.path.join(root, filename)
            print ("\n",filenamepath)
            infile=open(filenamepath,'r')
            Contents=[]
            for line in infile:
            
               
                try:
                    lines=line.split('\t')
                    codekey=lines[6]
                    #print codekey
                    if codekey in code_list:
                        Contents.append(line)                    
                except Exception as e:  
                    print (e)
           
            try:
                roots=root.split('\\')
                for i in roots:
                    if i.isdigit() and len(i)==4:
                      date=i
                filenames=filename.split('.txt')
                #print filenames[0],roots[-1]
                outfile='%s_%s.man' %(filenames[0],date)
                
                outfid=open(os.path.join(output_dir, outfile),'w')	
                print(Contents)
                for line in Contents:
                    try:
                        outfid.write(line)

                    except Exception as e:
                        print (e)	

                outfid.close()
            except Exception as e:  
                print (e)
def init_level2():
    """
    如果需要导入外部文件

    Parameters
    ----------

    Returns
    -------

    """
    if len(sys.argv) < 2:
        print ("python GetSHL2Snapshot.py outdir codefile")
        sys.exit(1)
        print (len(sys.argv))
    
        output_dir=sys.argv[1]
        print (output_dir)
        
        codefile=sys.argv[2]
        try:
            infile=open(codefile,'r')
        except:
            print ("wrong code list file")
            sys.exit(1)
        for line in infile:
            line=line.strip()
            codeList.append(line)
        return codeList
if __name__ == '__main__':
    #codeList=init_level2()
    codeList=["000001"]
    load_SZL2(codeList)

