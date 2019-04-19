# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/11
"""
from  sklearn import tree
# import pandas as pd

if __name__ == '__main__':
    with open('lenses.txt') as fr:
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lenses_target = []
    for each in lenses:
        lenses_target.append(each[-1])
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lenses_list=[]
    lenses_dict={}
    for each_label in lensesLabels:
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list=[]
    print(lenses_dict)                                                       #打印字典信息
    # lenses_pd = pd.DataFrame(lenses_dict)                                    #生成pandas.DataFrame
    # print(lenses_pd)
    print("%s%10s" % ("sss","aaaaaaaa"))