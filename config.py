import pandas as pd
from scipy.special import comb
from itertools import combinations, product
from collections import defaultdict as ddict

Mode = 'Online' #这个先不要改，后面计划增加供货模式和离线模式

blacklist = {
    'Global' : ' 五金店 钢结构房 平房 学校 小型公寓', #在这里填写你没有或者完全不想用的建筑，空格分隔，优先级最高
    'Online' : '小型公寓 水厂 花园洋房 复兴公馆 加油站 人民石油'
}

whitelist = {
    'Global' : '', #在这里填写一定要上的建筑，空格分隔
    'Train'  : '商贸中心 复兴公馆 小型公寓 花园洋房'
}

'''
     在这里填写你的建筑的星级
'''
BuildStars = {
    5 : '电厂 小型公寓 居民楼 木屋 五金店 木材厂 食品厂 菜市场 造纸厂 钢结构房 平房 学校 便利店 服装店 水厂',
    4 : '纺织厂 图书城 零件厂',
    3 : '民食斋 钢铁厂 人才公寓 中式小楼 加油站 花园洋房',
    2 : '空中别墅 商贸中心 复兴公馆 媒体之声 企鹅机械',
    1 : '人民石油'
}

'''
    在这里填写你的 政策/照片/任务 加成
'''
Policy = {
    'Global':  6,
    'Online':  2,
    'Offline': 0,
    'Residence': 3,
    'Business': 9,
    'Industrial': 12,
    'JiaGuoZhiGuang': 1.8#国庆也填在这
}

Photos = {
    'Global':  1.8,
    'Online':  1.6,
    'Offline': 1.6,
    'Residence': 3,
    'Business': 3,
    'Industrial': 2.7
}

Tasks_d  = {#如果是100%则填写1
            '纺织厂': 1,
            '钢铁厂': 1,
            '木材厂': 2,
            'Global':  0,
            'Online':  0,
            'Offline': 0,
            'Residence': 0,
            'Business': 0,
            'Industrial': 0,
        }

'''
    在这里填写你当前的建筑等级
'''

Grades =    {'中式小楼': 800,
             '五金店': 800,
             '人才公寓': 800,
             '人民石油': 800,
             '企鹅机械': 800,
             '便利店': 1023,
             '加油站': 800,
             '商贸中心': 800,
             '图书城': 800,
             '复兴公馆': 800,
             '媒体之声': 800,
             '学校': 800,
             '小型公寓': 800,
             '居民楼': 800,
             '平房': 800,
             '服装店': 800,
             '木屋': 1129,
             '木材厂': 1184,
             '民食斋': 800,
             '水厂': 800,
             '电厂': 800,
             '空中别墅': 800,
             '纺织厂': 800,
             '花园洋房': 800,
             '菜市场': 800,
             '造纸厂': 800,
             '钢结构房': 800,
             '钢铁厂': 800,
             '零件厂': 800,
             '食品厂': 800}
'''
    自动升级功能过几天上线，敬请期待
'''

TotalGold = '1 aa'

'''
    以下部分请不要随意改动
'''

Industrial  = '木材厂 食品厂 造纸厂 水厂 电厂 钢铁厂 纺织厂 零件厂 企鹅机械 人民石油'
Business = '便利店 五金店 服装店 菜市场 学校 图书城 商贸中心 加油站 民食斋 媒体之声'
Residence = '木屋 居民楼 钢结构房 平房 小型公寓 人才公寓 花园洋房 中式小楼 空中别墅 复兴公馆'

if Mode == 'Online':
    Industrial   = Industrial.split()
    Business = Business.split()
    Residence  = Residence.split()
    for build in blacklist['Global'].split() + blacklist['Online'].split():
        if build in Industrial:
            Industrial.remove(build)
        if build in Business:
            Business.remove(build)
        if build in Residence:
            Residence.remove(build)
    totalBuilds = Business + Residence + Industrial

BaseIncome = pd.read_csv('baseIncome.csv', encoding='gb2312')
Upgrade    = pd.read_csv('upgrade.csv')

searchSpace = product(combinations(Industrial,3),
                      combinations(Business,3), combinations(Residence,3))
searchSpaceSize = comb(len(Industrial),3)*comb(len(Business),3)*comb(len(Residence),3)

buildsDict = dict()

for star, builds in BuildStars.items():
    for build in builds.split():
        if build in totalBuilds:
            incomeRow = BaseIncome[(BaseIncome.buildName == build) & (BaseIncome.star == star)]
            buildsDict[build] = {
                    'category' : incomeRow.category.values[0],
                    'star' : star,
                    'rarity' : incomeRow.rarity.values[0],
                    'baseIncome' : incomeRow.baseIncome.values[0],
                    'buff' : dict()
                    }
Tasks = ddict(int)
for item, value in Tasks_d.items():
    Tasks[item] = value

for build, info in buildsDict.items():
    buildsDict[build]['baseIncome'] *=\
        (1+Policy['Global']+Policy['Online']+Policy[info['category']]+Policy['JiaGuoZhiGuang'])*\
        (1+Photos['Global']+Photos['Online']+Photos[info['category']])*\
        (1+Tasks[build]+Tasks['Global']+Tasks['Online']+Tasks[info['category']])

buffs_100 = {
                '木屋': ['木材厂'],
                '居民楼': ['便利店'],
                '钢结构房': ['钢铁厂'],
                '花园洋房': ['商贸中心'],
                '空中别墅': ['民食斋'],

                '便利店': ['居民楼'],
                '五金店': ['零件厂'],
                '服装店': ['纺织厂'],
                '菜市场': ['食品厂'],
                '学校':  ['图书城'],
                '图书城': ['学校', '造纸厂'],
                '商贸中心': ['花园洋房'],

                '木材厂': ['木屋'],
                '食品厂': ['菜市场'],
                '造纸厂': ['图书城'],
                '钢铁厂': ['钢结构房'],
                '纺织厂': ['服装店'],
                '零件厂': ['五金店'],
                '企鹅机械':['零件厂'],
                '人民石油':['加油站']
            }

buffs_50 = {'零件厂': ['企鹅机械'],
            '加油站':['人民石油']}

bufflist_258 = tuple([.2, .5, .8, 1.1, 1.4])
bufflist_246 = tuple([.2, .4, .6, .8, 1.0])
bufflist_015 = tuple([0.75*x for x in [.2, .4, .6, .8, 1.0]])
bufflist_010 = tuple([0.5*x for x in [.2, .4, .6, .8, 1.0]])
bufflist_005 = tuple([0.25*x for x in [.2, .4, .6, .8, 1.0]])
bufflist_035 = tuple([1.75*x for x in [.2, .4, .6, .8, 1.0]])

buffs_ind = {
             '媒体之声': bufflist_005,
             '钢铁厂': bufflist_015,
             '中式小楼': bufflist_246,
             '民食斋': bufflist_246,
             '空中别墅': bufflist_246,
             '电厂': bufflist_258,
             '企鹅机械': bufflist_010,
             '人才公寓': bufflist_035
             }
buffs_bus = {
             '媒体之声': bufflist_005,
             '企鹅机械': bufflist_010,
             '民食斋': bufflist_246,
             '纺织厂': bufflist_015,
             '人才公寓': bufflist_246,
             '中式小楼': bufflist_246,
             '空中别墅': bufflist_246,
             '电厂': bufflist_258
             }
buffs_res = {
             '媒体之声': bufflist_005,
             '企鹅机械':bufflist_010,
             '民食斋': bufflist_246,
             '人才公寓': bufflist_246,
             '平房': bufflist_246,
             '空中别墅': bufflist_246,
             '电厂': bufflist_258,
             '中式小楼': bufflist_035
             }

for build, info in buildsDict.items():
    if build in buffs_100:
        for buffedBuild in buffs_100[build]:
            buildsDict[build]['buff'][buffedBuild] = info['star']
    if build in buffs_50:
        for buffedBuild in buffs_50[build]:
            buildsDict[build]['buff'][buffedBuild] = info['star']*0.5

    if build in buffs_ind:
        buildsDict[build]['buff']['Industrial'] = buffs_ind[build][info['star']-1]
    if build in buffs_bus:
        buildsDict[build]['buff']['Business'] = buffs_bus[build][info['star']-1]
    if build in buffs_res:
        buildsDict[build]['buff']['Residence'] = buffs_res[build][info['star']-1]

UnitDict = {
        'G' : 1,
        'K' : 1e3,
        'M' : 1e6,
        'B' : 1e9,
        'T' : 1e12,
        'aa' : 1e15,
        'bb' : 1e18,
        'cc' : 1e21,
        'dd' : 1e24,
        'ee' : 1e27,
        'ff' : 1e30,
        'gg' : 1e33,
        'hh' : 1e36,
        'ii' : 1e39
        }
GoldNum, Unit = TotalGold.split()
try:
    TotalGold = float(GoldNum) * UnitDict[Unit]
except KeyError:
    print('单位错误,请检查金币输入')
