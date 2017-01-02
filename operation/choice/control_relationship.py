#!/usr/bin/env python
#encoding:UTF-8

###支配集建立
###建立 {个体号码：[支配其的个数， 被其支配的个体列表]}
"""
        individual_indicate 个体的索引号码 列表 [0, 1, 2, ...]
        objValueList 个体索引号，目标函数1和2的 三元列表
        obj_1_dict 个体索引号，目标函数1的 字典
"""
def control_relationship(objValueList, individual_indicate, obj_1_dict, obj_2_dict):
    """
    建立 个体索引号:[[支配其的个体索引号列表]:[被其支配的个体索引号列表]]
    """
    obj_1_sorted=sorted(objValueList, key=lambda x:x[1], reverse=True)
    obj_2_sorted=sorted(objValueList, key=lambda x:x[2], reverse=True)

    """
    根据目标函数的多少来设定 支配字典的个数
    """
    control_1_dict={}.fromkeys(individual_indicate)
    control_2_dict={}.fromkeys(individual_indicate)

    #目标函数1的排序结果，做支配集判断
    for i in individual_indicate:
        ###大于， 小于， 等于
        control_1_dict[i]=[[], [], []]
        for j in obj_1_sorted:
            if i!=j[0]:
                if j[1]>obj_1_dict[i]:
                    control_1_dict[i][0].append(j[0])
                elif j[1]<obj_1_dict[i]:
                    control_1_dict[i][1].append(j[0])
                else:
                    control_1_dict[i][2].append(j[0])

    #目标函数2的排序结果，做支配集判断
    for i in individual_indicate:
        control_2_dict[i]=[[], [], []]
        for j in obj_2_sorted:
            if i!=j[0]:
                if j[2]>obj_2_dict[i]:
                    control_2_dict[i][0].append(j[0])
                elif j[2]<obj_2_dict[i]:
                    control_2_dict[i][1].append(j[0])
                else:
                    control_2_dict[i][2].append(j[0])

    #结合目标一，二的支配情况，做出最终的支配集合    
    control_dict={}.fromkeys(individual_indicate)
    for i in individual_indicate:
        control_dict[i]=[None, None]
        control_dict[i][0]=set.intersection(set(control_1_dict[i][0]), set(control_2_dict[i][0]))
        control_dict[i][1]=set.intersection(set(control_1_dict[i][1]), set(control_2_dict[i][1]))
        ###判断弱支配关系
        control_dict[i][0]=set.union(control_dict[i][0], set.intersection(set(control_1_dict[i][0]), set(control_2_dict[i][2])), set.intersection(set(control_1_dict[i][2]), set(control_2_dict[i][0])))
        control_dict[i][1]=set.union(control_dict[i][1], set.intersection(set(control_1_dict[i][1]), set(control_2_dict[i][2])), set.intersection(set(control_1_dict[i][2]), set(control_2_dict[i][1])))
        
    #control_dict 为最终的支配解集
    for i in control_dict:
        control_dict[i][0]=len(control_dict[i][0])
    return control_dict


