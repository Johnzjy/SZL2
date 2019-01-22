# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:52:10 2019

@author: 310128142
"""

SNL2_columns=[
              "TradeDate"   ,
              "OrigTime"    ,
              "SendTime"    ,
              "RecvTime"    ,
              "dbTime"      ,#入库时间
              "ChannelNo"   ,
              "SecurityID"  ,
              "SecurityIDSource",
              "MDStreamID"  ,#010	现货（股票，基金，债券等）集中竞价交易快照行情
              "OfferPX1"    ,
              "BidPX1"      ,
              "OfferSize1"  ,
              "BidSize1"    ,

              "OfferPX2"    ,
              "BidPX2"      ,
              "OfferSize2"  ,
              "BidSize2"    ,

              "OfferPX3"    ,
              "BidPX3"      ,
              #20lines
              "OfferSize3"  ,
              "BidSize3"    ,

              "OfferPX4"    ,
              "BidPX4"      ,
              "OfferSize4"  ,
              "BidSize4"    ,


              "OfferPX5"    ,
              "BidPX5"      ,
              "OfferSize5"  ,
              "BidSize5"    ,
              #30lines
              "OfferPX6"    ,
              "BidPX6"      ,
              "OfferSize6"  ,
              "BidSize6"    ,

              "OfferPX7"    ,
              "BidPX7"      ,
              "OfferSize7"  ,
              "BidSize7"    ,

              "OfferPX8"    ,
              "BidPX8"      ,
              #40lines
              "OfferSize8"  ,
              "BidSize8"    ,

              "OfferPX9"    ,
              "BidPX9"      ,
              "OfferSize9"  ,
              "BidSize9"    ,

              "OfferPX10"    ,
              "BidPX10"      ,
              "OfferSize10"  ,
              "BidSize10"    ,
              #50lines
              "NUMORDERS_B1" ,#买一总委托笔数
              "NOORDERS _B1" ,#买一揭示委托笔数
              "ORDERQTY_B1"  ,#买一价委托队列(  | 分隔)
              "NUMORDERS_S1	",#卖一总委托笔数
              "NOORDERS _S1" ,#卖一揭示委托笔数
              "ORDERQTY_S1"  ,#卖一价委托队列(  | 分隔)


              ]
