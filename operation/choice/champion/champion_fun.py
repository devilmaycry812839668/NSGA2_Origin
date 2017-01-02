#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from mycmp import *

### 锦标赛 方式选择
### 选择个体编号
"""
        individual_layer_value
        {个体号码:[个体所属层号， 个体两边的距离总值]}
"""
def champion_choice(population, individual_layer_value):
    ###参数6, 选出数为总个体的 一半 
    choice_num=6
    #个体号索引
    indicate_set=set(range(population.shape[0]))
    ###构建 字典     索引:[层号， 距离, 索引]
    layer_value_tuple_3={}
    for k, v in individual_layer_value.items():
        layer_value_tuple_3[k]=(v[0], v[1], k)

    ###layer_value_tuple_3
    next_remain=[]
    ###选择次数为 总个体数的一半
    for i in xrange(int(population.shape[0]/2)):
        temp_list=[]
        choice_set=set(random.sample(indicate_set, choice_num))
        for k in choice_set:
            temp_list.append(layer_value_tuple_3[k])

        temp_list.sort(cmp=mycmp)

        next_remain.append(temp_list[0][2])
    return next_remain

