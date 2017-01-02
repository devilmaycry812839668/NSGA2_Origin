#!/usr/bin/env python
#encoding:UTF-8
from control_relationship import control_relationship

def create_estimate(population, functionObject):
    ###为函数对象赋值新的种群个体
    functionObject.population=population
    #选择算子
    obj_1_result=functionObject.objFun_1().tolist()
    obj_2_result=functionObject.objFun_2().tolist()

    #个体索引号
    individual_indicate=range(population.shape[0])
    #建立个体索引号，目标函数1和2的 三元列表
    objValueList=zip(individual_indicate, obj_1_result, obj_2_result)

    """
    考虑是否简化
    """
    #建立个体索引号，目标函数1的 二元列表转换为字典
    obj_1_dict=dict(zip(individual_indicate, obj_1_result))
    #建立个体索引号，目标函数2的 二元列表转换为字典
    obj_2_dict=dict(zip(individual_indicate, obj_2_result))

    """
        individual_indicate 个体的索引号码 列表 [0, 1, 2, ...]
        objValueList 个体索引号，目标函数1和2的 三元列表
        obj_1_dict 个体索引号，目标函数1的 字典
    """
    ###建立 {个体号码：[支配其的个数， 被其支配的个体列表]}
    ###建立支配集合，并返回为： control_dict
    control_dict=control_relationship(objValueList, individual_indicate, obj_1_dict, obj_2_dict)

    ### 支配层列表 
    layer_0=[]
    for k, v in control_dict.items():
        if v[0]==0:
            layer_0.append(objValueList[k])

    return layer_0

