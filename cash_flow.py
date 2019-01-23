# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:19:55 2019

@author: 310128142
"""
import pandas as pd
import os
import Config_File
import tqdm


path="am_snap_level_spot_1008.man"

timeframe="%Y%m%d%H%M%S%f"# 时间格式

def SNL2_Man_to_df(file_path):
    """
    将.man file转换成 dataframe 格式

    Parameters
    ----------
    file_path: 文件路径

    Returns
    -------

    """
    col=Config_File.SNL2_columns
    df=pd.DataFrame(columns=col)
    with open(file_path,"r") as f: #read file 
        snap_lines=f.readlines()
        
    for item,line in tqdm.tqdm (enumerate(snap_lines[100:120]),desc='Extract datas',unit='datas'):

        data_list=line[:].split('\t')
        data_list[-1]=data_list[-1].split()[0]
        df.loc[item]=data_list
    
    df=df.apply(pd.to_numeric,errors='ignore') #转换成数字 忽略该列错误
        
    return df

def SNL2_Day_Data(date):
    """
    将该文件目录下的snap level 上下午合并成一个dataframe
    TODO: 文件搜寻
    Parameters
    ----------
    date: 该日期 格式（1010--“yydd”）

    Returns
    -------

    """
    am_file_name="am_snap_level_spot_%s.man"%date
    pm_file_name="pm_snap_level_spot_%s.man"%date
    if not os.path.exists(am_file_name):
        raise IOError ("The <%s> file is not exist"%am_file_name)
    if not os.path.exists(pm_file_name):
        raise IOError ("The <%s> file is not exist"%pm_file_name)
    print("loading %s"%am_file_name)
    am_data=SNL2_Man_to_df(am_file_name)
    print("loading %s"%pm_file_name)
    pm_data=SNL2_Man_to_df(pm_file_name)
    result=am_data.append(pm_data)
    result=result.reset_index()
    return result

def streaming_tick_data(data_frame):#逐步查分大单
    """
    逐步查分大单，目前默认100000以上的单子

    Parameters
    ----------
    data_frame: input dataframe

    Returns
    -------

    """
    data_frame["ORD_List_S1"]=split_tick(data_frame,'ORDERQTY_S1')
    data_frame["ORD_List_B1"]=split_tick(data_frame,'ORDERQTY_B1')
    data_frame["ORD_S1_BIG"]=data_frame["ORD_List_S1"].apply(lambda x:sorting_tick(x,100000000000,100000))#从100000000000 到 100000
    data_frame["ORD_B1_BIG"]=data_frame["ORD_List_B1"].apply(lambda x:sorting_tick(x,100000000000,100000))
    data_frame["Reduce_B1"],data_frame["Increase_B1"]=change_tick(data_frame.ORD_List_B1)
    return data_frame
    
    


def split_tick(df,column_name):#将ORDERQTY 查分成list
    """
    ORD_List_S1
    ORD_List_B1
    

    Parameters
    ----------
    df: 
    column_name: 

    Returns
    -------

    """plit_list=list()
    for tick in tqdm.tqdm(df.iterrows()):
        temp=tick[1][column_name]
        if len(str(temp)):
            if type(temp)==int:
                order_s1=[str(temp)]
            else:
          
                order_s1=temp.split('|',)
        else:
            order_s1=[]
       
        split_list.append(order_s1)
    return split_list

def sorting_tick(tick_ls,max_level,min_level):
    """
    将买卖LIST中按照大小sorting

    Parameters
    ----------
    tick_ls: 标签“ ORD_List_S1；ORD_List_B1”
    max_level: 最大值
    min_level: 最小值

    Returns
    -------

    """
    sum_tk=0

    if len(tick_ls):
    
        for i in tick_ls:
            
          
            i = int(i)
   
            if i <max_level and i >=min_level:
                sum_tk +=i
            else:
                pass
    return sum_tk
    
def change_tick(tick_array):#每次计三秒内变化
    reduce_list = list()
    increase_list=list()
    for i in range(len(tick_array)):
        if i is 0:
            reduce_list.append([])
            increase_list.append([])
        else:
            k=i-1
            reduce,increase=[],[]
            last=tick_array.iloc[k]
            last=list(map(int,last))
            now=tick_array.iloc[i]
            now=list(map(int,now))
            #print(last,now)
            for num in last:
                


                if now is None :
                    reduce.append(num)
                elif num not in now:
                    reduce.append(num)
               

                else:
                    now.remove(num)
                    

            increase=now

            reduce_list.append(reduce)
            increase_list.append(increase)
        
    return reduce_list,increase_list
            

    
    
    
    
x=SNL2_Day_Data(1009)
y=streaming_tick_data(x)

print(y)