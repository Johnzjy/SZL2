# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:04:34 2019

@author: 
"""

import os
import os.path
import re
import string
import sys
import time



output_dir="./";
PATH_7z_EXE= 'C:\Program Files (x86)\MyDrivers\DriverGenius' 

SZL2_mode_dict={
                "snap":"_snap_level_spot", #证券行情快照档位表  SecuritySnapshotLevel
                "trade":"_hq_trade_spot", #逐笔成交表 Trade
                }


def unzip_7z(_path,_file):
    """
    unzip the 7-zip to the current path

    Parameters
    ----------
    _path:zip file path
    _file:zip file name

    Returns
    -------

    """

    rar_path=_path+_file
    print (rar_path)
    un_file_name,num=os.path.splitext(rar_path)# 解压包后是.00x多个解压包 ，提取压缩文件名
    if len(num) == 4:
        un_path,format_name=os.path.splitext(un_file_name)
        if format_name == ".7z":
            un_path = '"{}"'.format(un_path)
            _cwd=os.getcwd()

    
            os.chdir(PATH_7z_EXE)# 7z.exe path 
            cmd = '7z.exe x "{}" -o{} -aos -r'.format(rar_path,un_path); #解压到当前文件夹下
            os.system(cmd)
            os.chdir(_cwd)
        else:
            print ("%s is not 7-zip file"%rar_path)

def unzip_SZL2(module_SZL2,input_dir=None):
    """
    choose different modele to unzip to the path

    Parameters
    ----------
    module_SZL2 ： 模式名多为SZL2_mode_dict 的key 值
    Returns
    -------

    """
    
    if module_SZL2 not in SZL2_mode_dict.keys():
        raise ValueError ("the SZL2 module input error!")
    else:
        print (os.getcwd())
    if input_dir is None:
        input_dir="./"
    for root, dirnames, filenames in os.walk(input_dir):#文件遍历所有文件夹
        for filename in filenames:
            
            if not filename.endswith(SZL2_mode_dict[module_SZL2]+".7z.001"):
                continue
            path=os.getcwd()+root[1:]+"\\"
            print(path)
            unzip_7z(path,filename)

def clean_snap(code_list,input_dir=None):#清理snap
    if input_dir is None:
        input_dir="./"

    for root, dirnames, filenames in os.walk(input_dir):
        for filename in filenames[:2]:
            #print filename.endswith(suffix)
            if not filename.endswith(SZL2_mode_dict['snap']+".txt"):
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

def load_SZL2(code_list,input_dir):
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
if __name__ == '__main__':
    clean_snap("000001")