# -*- coding:UTF-8 -*-
"""
DATE:
    2019/2/18
"""
from sklearn import tree
import pandas as pd
from sklearn.externals.six import StringIO
from sklearn.preprocessing import LabelEncoder

if __name__ == '__main__':
    with open('lenses.txt', 'r') as fr:
        lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lenses_target = []
    for each in lenses:
        lenses_target.append(each[-1])
    lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']  # 特征标签
    lenses_list = []  # 保存lenses数据的临时列表
    lenses_dict = {}

    for each_label in lensesLabels:
        for each in lenses:
            lenses_list.append(each[lensesLabels.index(each_label)])
        lenses_dict[each_label] = lenses_list
        lenses_list = []
    print(lenses_dict)                                                     #打印字典信息
    lenses_pd = pd.DataFrame(lenses_dict)                                    #生成pandas.DataFrame
    print(lenses_pd)
    # 打印pandas.DataFrame
    le = LabelEncoder()  # 创建LabelEncoder()对象，用于序列化
    for col in lenses_pd.columns:  # 为每一列序列化
        lenses_pd[col] = le.fit_transform(lenses_pd[col])
    print(lenses_pd)

    clf = tree.DecisionTreeClassifier(max_depth=4)  # 创建DecisionTreeClassifier()类
    clf = clf.fit(lenses_pd.values.tolist(), lenses_target)  # 使用数据，构建决策树
    dot_data = StringIO()
    tree.export_graphviz(clf, out_file=dot_data,  # 绘制决策树
                         feature_names=lenses_pd.keys(),
                         class_names=clf.classes_,
                         filled=True, rounded=True,
                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_pdf("tree.pdf")
    print(clf.predict([[1,1,1,0]]))                    #预测