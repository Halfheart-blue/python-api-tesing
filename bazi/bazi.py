#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  钉钉或微信pythontesting 技术支持qq群：630011153 144081101
# CreateDate: 2019-2-21

# -*- coding:utf-8 -*-

import  sxtwl
import argparse
import collections
import pprint
from bidict import bidict


Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
ten_deities = {
    '甲':bidict({'甲':'比肩', "乙":'劫财', "丙":'食神', "丁":'伤官', "戊":'偏财',
        "己":'正财', "庚":'偏官', "辛":'正官', "壬":'偏印', "癸":'印', "子":'沐浴', 
        "丑":'冠带', "寅":'建', "卯":'帝旺', "辰":'衰', "巳":'病', "午":'死',
        "未":'墓', "申":'绝', "酉":'胎', "戌":'养', "亥":'长生'}),
    '乙':bidict({'甲':'劫财', "乙":'比肩', "丙":'伤官', "丁":'食神', "戊":'正财',
        "己":'偏财', "庚":'正官', "辛":'偏官', "壬":'印',"癸":'偏印', "子":'病', 
        "丑":'衰', "寅":'帝旺', "卯":'建', "辰":'冠带', "巳":'沐浴', "午":'长生',
        "未":'养', "申":'胎', "酉":'绝', "戌":'墓', "亥":'死'}),  
    '丙':bidict({'丙':'比肩', "丁":'劫财', "戊":'食神', "己":'伤官', "庚":'偏财',
        "辛":'正财', "壬":'偏官', "癸":'正官', "甲":'偏印', "乙":'印',"子":'胎', 
        "丑":'养', "寅":'长生', "卯":'沐浴', "辰":'冠带', "巳":'建', "午":'帝旺',
        "未":'衰', "申":'病', "酉":'死', "戌":'墓', "亥":'绝'}),
    '丁':bidict({'丙':'劫财', "丁":'比肩', "戊":'伤官', "己":'食神', "庚":'正财',
        "辛":'偏财', "壬":'正官', "癸":'偏官', "甲":'印',"乙":'偏印', "子":'绝', 
        "丑":'墓', "寅":'死', "卯":'病', "辰":'衰', "巳":'帝旺', "午":'建',
        "未":'冠带', "申":'沐浴', "酉":'长生', "戌":'养', "亥":'胎'}),  
    '戊':bidict({'戊':'比肩', "己":'劫财', "庚":'食神', "辛":'伤官', "壬":'偏财',
        "癸":'正财', "甲":'偏官', "乙":'正官', "丙":'偏印', "丁":'印',"子":'胎', 
        "丑":'养', "寅":'长生', "卯":'沐浴', "辰":'冠带', "巳":'建', "午":'帝旺',
        "未":'衰', "申":'病', "酉":'死', "戌":'墓', "亥":'绝'}),
    '己':bidict({'戊':'劫财', "己":'比肩', "庚":'伤官', "辛":'食神', "壬":'正财',
        "癸":'偏财', "甲":'正官', "乙":'偏官', "丙":'印',"丁":'偏印',"子":'绝', 
        "丑":'墓', "寅":'死', "卯":'病', "辰":'衰', "巳":'帝旺', "午":'建',
        "未":'冠带', "申":'沐浴', "酉":'长生', "戌":'养', "亥":'胎'}),     
    '庚':bidict({'庚':'比肩', "辛":'劫财', "壬":'食神', "癸":'伤官', "甲":'偏财',
        "乙":'正财', "丙":'偏官', "丁":'正官', "戊":'偏印', "己":'印',"子":'死', 
        "丑":'墓', "寅":'绝', "卯":'胎', "辰":'养', "巳":'长生', "午":'沐浴',
        "未":'冠带', "申":'建', "酉":'帝旺', "戌":'衰', "亥":'病'}),
    '辛':bidict({'庚':'劫财', "辛":'比肩', "壬":'伤官', "癸":'食神', "甲":'正财',
        "乙":'偏财', "丙":'正官', "丁":'偏官', "戊":'印', "己":'偏印', "子":'长生', 
        "丑":'养', "寅":'胎', "卯":'绝', "辰":'墓', "巳":'死', "午":'病',
        "未":'衰', "申":'帝旺', "酉":'建', "戌":'冠带', "亥":'沐浴'}),  
    '壬':bidict({'壬':'比肩', "癸":'劫财', "甲":'食神', "乙":'伤官', "丙":'偏财',
        "丁":'正财', "戊":'偏官', "己":'正官', "庚":'偏印', "辛":'印',"子":'帝旺', 
        "丑":'衰', "寅":'病', "卯":'死', "辰":'墓', "巳":'绝', "午":'胎',
        "未":'养', "申":'长生', "酉":'沐浴', "戌":'冠带', "亥":'建'}),
    '癸':bidict({'壬':'劫财', "癸":'比肩', "甲":'伤官', "乙":'食神', "丙":'正财',
        "丁":'偏财', "戊":'正官', "己":'偏官', "庚":'印',"辛":'偏印', "子":'建', 
        "丑":'冠带', "寅":'沐浴', "卯":'长生', "辰":'养', "巳":'胎', "午":'绝',
        "未":'墓', "申":'死', "酉":'病', "戌":'衰', "亥":'帝旺'}),          
    
}
gan5 = {"甲":"木", "乙":"木", "丙":"火", "丁":"火", "戊":"土", "己":"土", 
    "庚":"金", "辛":"金", "壬":"水", "癸":"水"}
gan_health = {
    "金":'''
    秋天较走运
    申月、酉月、猴年和鸡年运气较好
    下午三点至下午七点是吉时
    西方是吉方
    住朝西的房子较吉利
    睡房在房子的西方较好
    睡房的西方有窗字较顺利
    金属床有利健康
    办公桌朝西有助工作效率
    吉祥颜色是白色
    室内装璜用白色系统
    穿衣用白色系列
    开白色车子较平安易发财
    勿伤心，注意呼吸系统、肺、肠, 筋
    武术、击搏、兵器运动、健身房运动也很好
    和金有关的工作较容易''',
    "木":'''
    春天或清风徐来的天气较走运
    卯月、寅月、兔年和虎年运气较好
    上午三点至上午七点是吉时
    东方是吉方
    住朝东的房子较吉利
    睡房在房子的东方较好
    睡房的东方有窗字较顺利
    木床有利健康
    办公桌朝东有助工作效率
    吉祥颜色是绿色
    室内装璜用绿色系统
    穿衣用绿色系列
    开绿色车子较平安易发财
    多喝点酸性饮料，忌生气，注意神精系统、肝、胆、头肩、肝胆
    多打高尔夫球、公园散步、徒步树林等户外运动
    和木有关的工作较容易。''',
    "水":'''
    身体需要注意: 胫足、膀胱肾(比如结石) 多喝水
    冬天或冷天气较走运
    亥月、子月、猪年和鼠年运气较好
    晚上九点至上午一点是吉时
    北方较冷是吉方
    住朝北的房子较吉利
    睡房在房子的北方较好
    睡房的北方有窗字较顺利
    金属床或水床有利健康
    办公桌朝北有助工作效率
    吉祥颜色是黑色
    室内装璜用黑色系统
    穿衣用黑色系列，带珠宝也不错
    开黑色车子较平安易发财
    多喝水，注意肾脏系统
    多做游泳、潜水、滑雪、钓鱼、溜冰等户外运动
    和水有关的工作较容易。''',    
    "火":'''
    夏天或热天气较走运
    午月、巳月、马年和蛇年运气较好
    上午九点至下午一点是吉时
    南方较热是吉方
    住朝南的房子较吉利
    睡房在房子的南方较好
    睡房的南方有窗字较顺利
    木床有利健康
    办公桌朝南有助工作效率
    吉祥颜色是红色
    室内装璜用红色系统
    穿衣用红色系列
    开红色车子较平安易发财
    要常笑，注意心脏系统、血液循环、眼睛、额齿
    多做打篮球、网球、排球、骑单车等户外运动
    和火有关的工作较容易''',
    "土":'''
    春、夏、秋、冬四季交接之时段较走运
    丑、辰、未、戌月和牛、龙、羊、狗年运气较好
    上午二点、八点左右和下午二点、八点左右都是吉时
    起居环境和气候不要太乾或太湿
    睡房在房子的中间较好
    办公桌靠房子的中间，有助工作效率
    吉祥颜色是棕黄色
    室内装璜用棕黄色系统
    穿衣用棕黄色系列，带古玉很不错
    开棕黄色车子较平安易发财
    勿常担心事情，太多虑 
    吃些甜点，注意消化系统、脾、肌肉
    多做园艺、露营、走路等户外运动。下棋、宗教场所都好
    和土有关的工作较容易''',      
}
Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
zhi5 = {"子":{"壬":56,"癸":184}, 
    "丑":{"辛":40,"癸":56, "己":144}, 
    "寅":{"戊":40,"丙":40, "甲":160},
    "卯":{"甲":56, "乙":184}, 
    "辰":{"癸":40,"乙":56, "戊":144}, 
    "巳":{"庚":40,"戊":56, "丙":144}, 
    "午":{"丙":56, "丁":184},
    "未":{"甲":40,"丁":56, "己":144}, 
    "申":{"戊":40,"壬":40, "庚":160},
    "酉":{ "庚":56, "辛":184}, 
    "戌":{"丙":40,"辛":56, "戊":144}, 
    "亥":{"戊":40,"甲":40, "壬":160}}

#zhi5 = {"子":{"癸":8}, 
        #"丑":{"辛":1,"癸":2, "己":5}, 
        #"寅":{"戊":1,"丙":2, "甲":5},
        #"卯":{"乙":8}, 
        #"辰":{"癸":1,"乙":2, "戊":5}, 
        #"巳":{"庚":1,"戊":2, "丙":5}, 
        #"午":{"己":3, "丁":5},
        #"未":{"乙":1,"丁":2, "己":5}, 
        #"申":{"戊":1,"壬":2, "庚":5},
        #"酉":{"辛":8}, 
        #"戌":{"丁":1,"辛":2, "戊":5}, 
        #"亥":{"甲":3, "壬":5}}

ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
Week = ["日", "一", "二", "三", "四", "五", "六"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]

gan_hes = {
    ("甲", "己"): "中正之合 化土",
    ("乙", "庚"): "仁义之合　化金",
    ("丙", "辛"): "丙义之合　化水",
    ("丁", "壬"): "淫慝之合　化木",    
    ("戊", "癸"): "无情之合　化火",    
}

gan_chongs = {
    ("甲", "庚"): "相冲",
    ("乙", "辛"): "相冲",
    ("丙", "壬"): "相冲",
    ("丁", "癸"): "相冲",       
}

zhi_6hes = {
    ("子", "丑"): "化土",
    ("寅", "亥"): "化木",
    ("卯", "戌"): "化火",
    ("辰", "酉"): "化金",    
    ("巳", "申"): "化水",    
    ("午", "未"): "化土",        
}

zhi_3hes = {
    ("申", "子", "辰"): "化水",
    ("巳", "酉", "丑"): "化金",  
    ("寅", "午", "戌"): "化火",       
    ("亥", "卯", "未"): "化木",
}

zhi_huis = {
    ("亥", "子", "丑"): "化水",
    ("寅", "卯", "辰"): "化木",  
    ("巳", "午", "未"): "化火",       
    ("申", "酉", "戌"): "化金",
}

zhi_chongs = {
    ("子", "午"): "相冲",
    ("丑", "未"): "相冲",
    ("寅", "申"): "相冲",
    ("卯", "酉"): "相冲",
    ("辰", "戌"): "相冲",   
    ("巳", "亥"): "相冲",       
}

zhi_poes = {
    ("子", "酉"): "相破",
    ("午", "卯"): "相破",
    ("巳", "申"): "相破",
    ("寅", "亥"): "相破",
    ("辰", "丑"): "相破",   
    ("戌", "未"): "相破",       
}

zhi_poes = {
    ("子", "酉"): "相破",
    ("午", "卯"): "相破",
    ("巳", "申"): "相破",
    ("寅", "亥"): "相破",
    ("辰", "丑"): "相破",   
    ("戌", "未"): "相破",       
}

zhi_haies = {
    ("子", "未"): "相害",
    ("丑", "午"): "相害",
    ("寅", "巳"): "相害",
    ("卯", "辰"): "相害",
    ("申", "亥"): "相害",   
    ("酉", "戌"): "相害",       
}

zhi_xings = {
    ("寅", "巳"): "寅刑巳 无恩之刑",
    ("巳", "申"): "巳刑申 无恩之刑",
    ("申", "寅"): "申刑寅 无恩之刑",
    ("未", "丑"): "未刑丑 持势之刑",
    ("丑", "戌"): "丑刑戌 持势之刑",   
    ("戌", "未"): "戌刑未 持势之刑",  
    ("子", "卯"): "子刑卯　卯刑子 无礼之刑",       
}

zhi_zixings = ['辰', '午', '酉', '亥']

description = '''

'''

parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('year', action="store", help=u'year')
parser.add_argument('month', action="store", help=u'month')
parser.add_argument('day', action="store", help=u'day')
parser.add_argument('time', action="store", help=u'time')    
parser.add_argument('-b', action="store_true", default=False, help=u'直接输入八字')
parser.add_argument('-g', action="store_true", default=False, help=u'是否采用公历')
parser.add_argument('-r', action="store_true", default=False, help=u'是否为闰月，仅仅使用于农历')
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1 Rongzhong xu 2019 02 21')
options = parser.parse_args()

Gans = collections.namedtuple("Gans", "year month day time")
Zhis = collections.namedtuple("Zhis", "year month day time")

if options.b:
    gans = Gans(year=options.year[0], month=options.month[0], 
                day=options.day[0],  time=options.time[0])
    zhis = Gans(year=options.year[1], month=options.month[1], 
                day=options.day[1],  time=options.time[1])
else:
    
    lunar = sxtwl.Lunar();
    if options.g:
        day = lunar.getDayBySolar(
            int(options.year), int(options.month), int(options.day))
    else:
        day = lunar.getDayByLunar(
             int(options.year), int(options.month), int(options.day), options.r)
    
    gz = lunar.getShiGz(day.Lday2.tg, int(options.time))

    #　计算甲干相合    
    gans = Gans(year=Gan[day.Lyear2.tg], month=Gan[day.Lmonth2.tg], 
                day=Gan[day.Lday2.tg], time=Gan[gz.tg])
    zhis = Zhis(year=Zhi[day.Lyear2.dz], month=Zhi[day.Lmonth2.dz], 
                day=Zhi[day.Lday2.dz], time=Zhi[gz.dz])
me = gans.day

if not options.b:
    print("\n日期:")
    print("======================================")  
    print("公历:")
    print("\t{}年{}月{}日".format(day.y, day.m, day.d))
    
    Lleap = "闰" if day.Lleap else ""
    print("农历:")
    print("\t{}年{}{}月{}日".format(day.Lyear0 + 1984, Lleap, ymc[day.Lmc], rmc[day.Ldi]))

print("\n八字:   同义词：七杀|偏官 偏印|枭神 阳刃|帝旺(阳干)|冠带(阴干)")
print("="*140)    
print("{:<30s}{:<30s}{:<30s}{:<30s}".format('年【父-根】', "月【兄弟僚友-苗】", "日【自己配偶-花】", "时【子孙-实】"))
print("-"*140)
print("{:>11s}-{:<19s}{:>11s}-{:<19s}{:>11s}-{:<19s}{:>11s}-{:<19s}".format(
    gans.year, '{} [{}]'.format(gan5[gans.year], ten_deities[me][gans.year]),
    gans.month, '{} [{}]'.format(gan5[gans.month], ten_deities[me][gans.month]),
    me, '{} [{}]'.format(gan5[me], '自己'), 
    gans.time, '{} [{}]'.format(gan5[gans.time], ten_deities[me][gans.time]),
))
print("{:>11s}--{:<19s}{:>12s}--{:<19s}{:>12s}--{:<19s}{:>12s}--{:<19s}".format(
    zhis.year, ten_deities[me][zhis.year],
    zhis.month, ten_deities[me][zhis.month],
    zhis.day, ten_deities[me][zhis.day],
    zhis.time, ten_deities[me][zhis.time],
))
for item in zhis:
    out = ''
    for gan in zhi5[item]:
        out = out + "{}{}{}{} ".format(gan, gan5[gan], zhi5[item][gan],  ten_deities[me][gan])
    print("{:<25s}".format(out), end=' ')
    
print("\n\n")
print("="*140)  
pprint.pprint(dict(ten_deities[me]))
#print(ten_deities[me])

def check_subset(gans, db, desc):
    flag = True
    for item in db:
        if set(item).issubset(gans):
            if flag:
                print("\n\n{}:".format(desc))
                print("="*60)   
                flag = False
            print(item, db[item])    

check_subset(gans, gan_hes, '十干合')
check_subset(gans, gan_chongs, '十干冲')
check_subset(zhis, zhi_6hes, '地支六合')		
check_subset(zhis, zhi_3hes, '地支三合')		
check_subset(zhis, zhi_huis, '地支三会')	
check_subset(zhis, zhi_chongs, '地支相冲')	
check_subset(zhis, zhi_poes, '地支相破')	
check_subset(zhis, zhi_haies, '地支相害')	
check_subset(zhis, zhi_xings, '地支相刑')	

flag = True
for item in zhi_zixings:
    if zhis.count(item) > 1:
        if flag:
            print("\n{}:".format("地支自刑"))
            print("=========================")    
            flag = False
        print(item)    
        

# 计算五行分数 http://www.131.com.tw/word/b3_2_14.htm

scores = {"金":0, "木":0, "水":0, "火":0, "土":0}

for item in gans:  
    scores[gan5[item]] += 150
    
for item in list(zhis) + [zhis.month]:  
    for gan in zhi5[item]:
        scores[gan5[gan]] += zhi5[item][gan]

print("\n\n五行分数") 
print("="*60)  
print(scores)
short = min(scores, key=scores.get)
print("\n\n五行缺{}的建议".format(short))    
print("=========================")    
print("{}".format(gan_health[short]))







