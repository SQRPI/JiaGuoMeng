# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:50:13 2019
@author: sqr_p
"""

import numpy as np
from tqdm import tqdm
from queue import PriorityQueue as PQ
from config import buildsDict, Grades, TotalGold, Upgrade, searchSpace,\
                   searchSpaceSize, UnitDict

# last_result=(('人才公寓', '木屋', '居民楼'), ('五金店', '菜市场', '便利店'), ('食品厂', '电厂', '木材厂'))


class NamedPQ(object):
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
        return

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority


def calculateComb(buildings):
#    Golds = TotalGold
    buildtuple = buildings[0] + buildings[1] + buildings[2]
    NowGrade = [Grades[build] for build in buildtuple]
#    Rarities = [buildsDict[build]['rarity'] for build in buildtuple]
    comboBuff = dict()
    for build in buildtuple:
        comboBuff[build] = 1
    for build in buildtuple:
        for buffedBuild, buffMultiple in buildsDict[build]['buff'].items():
            if buffedBuild in buildtuple:
                comboBuff[buffedBuild] += buffMultiple
            elif buffedBuild == 'Industrial':
                comboBuff[buildtuple[0]] += buffMultiple
                comboBuff[buildtuple[1]] += buffMultiple
                comboBuff[buildtuple[2]] += buffMultiple
            elif buffedBuild == 'Business':
                comboBuff[buildtuple[3]] += buffMultiple
                comboBuff[buildtuple[4]] += buffMultiple
                comboBuff[buildtuple[5]] += buffMultiple
            elif buffedBuild == 'Residence':
                comboBuff[buildtuple[6]] += buffMultiple
                comboBuff[buildtuple[7]] += buffMultiple
                comboBuff[buildtuple[8]] += buffMultiple

#    upgradePQ = PQ()
#    for i, build in enumerate(buildtuple):
#        upgradePQ.put(NamedPQ(Upgrade['Ratio'+Rarities[i]].iloc[NowGrade[i]-1],
#                              i))
#    while Golds > 0:
#        build = upgradePQ.get().name
#        Golds -= Upgrade[Rarities[i]].iloc[NowGrade[i]+1]
#        NowGrade[i] += 1 # upgrade build
#        upgradePQ.put(NamedPQ(Upgrade['Ratio'+Rarities[i]].iloc[NowGrade[i]-1],
#                              i))

    multiples = [buildsDict[build]['baseIncome'] * comboBuff[build] * \
                 Upgrade.incomePerSec.iloc[NowGrade[i]-1]\
                 for i, build in enumerate(buildtuple)]
    TotalIncome = sum(multiples)
    return (TotalIncome, (NowGrade, multiples))

results = PQ()

Max = 0
for buildings in tqdm(searchSpace,total=searchSpaceSize,
                      bar_format='{percentage:3.0f}%,{elapsed}<{remaining}|{bar}|{n_fmt}/{total_fmt},{rate_fmt}{postfix}'):
    TotalIncome, Stat = calculateComb(buildings)
    results.put(NamedPQ(-TotalIncome, (buildings, Stat)))

def showLetterNum(num):
    index = list(UnitDict.keys())[int(np.log10(num))//3]
    return str(np.round(num/UnitDict[index], 2)) + index

Best = results.get()
print('最优策略：', Best.name[0])
print('总秒伤：', showLetterNum(-Best.priority))

print('各建筑等级：', [(Best.name[0][i//3][i%3], x) for i, x in enumerate(Best.name[1][0])])
print('各建筑秒伤：', [(Best.name[0][i//3][i%3], showLetterNum(x)) for i, x in enumerate(Best.name[1][1])])

