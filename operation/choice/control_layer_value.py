#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random

def creat_layer(objValueList, individual_indicate, control_dict):
    #支配集分层
    i=0
    control_layer={}
    while control_dict!={}:
        control_layer[i]=[]
        for k, v in control_dict.items():
            if v[0]==0:
                control_layer[i].append(objValueList[k])

        ###将被支配层支配的个体 支配数减1
        for k in control_layer[i]:
            val=control_dict.pop(k[0])
            for v in val[1]:
                control_dict[v][0]=control_dict[v][0]-1
        i=i+1

    #为各支配层元素按照各自的 目标一函数， 目标二函数 排序
    #各个体选择的标准 layer, value
    individual_layer_value={}.fromkeys(individual_indicate)
    for k,v in control_layer.items():
        #k 为支配层号
        for m in v:
            individual_layer_value[m[0]]=[k, 0]

        obj_1_layer=sorted(v, key=lambda x:x[1])
        obj_2_layer=sorted(v, key=lambda x:x[2])

        ### 目标1  距离计算   
        for i in xrange(1, len(obj_1_layer)-1):
            t0=obj_1_layer[i-1]
            t1=obj_1_layer[i]
            t2=obj_1_layer[i+1]
            individual_layer_value[t1[0]][1]+=(t1[1]-t0[1])+(t2[1]-t1[1])
        #两端个体距离赋值为无穷大
        individual_layer_value[obj_1_layer[0][0]][1]+=100000000
        individual_layer_value[obj_1_layer[len(obj_1_layer)-1][0]][1]+=100000000

        ### 目标2  距离计算   
        for i in xrange(1, len(obj_2_layer)-1):
            t0=obj_2_layer[i-1]
            t1=obj_2_layer[i]
            t2=obj_2_layer[i+1]
            individual_layer_value[t1[0]][1]+=(t1[2]-t0[2])+(t2[2]-t1[2])
        #两端个体距离赋值为无穷大
        individual_layer_value[obj_2_layer[0][0]][1]+=100000000
        individual_layer_value[obj_2_layer[len(obj_2_layer)-1][0]][1]+=100000000
    return individual_layer_value


