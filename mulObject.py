#!/usr/bin/env python
#encoding:UTF-8
import numpy as np
import random
from fun.funUserDefine import *
from operation.cross.cross_fun import cross
from operation.change.change_fun import change
from operation.choice.choice_fun import choice

#评价函数，输出当前种群的非支配个体
from operation.choice.estimate import create_estimate

#200个个体, 30个变量， 变量数值范围0到2**14
#交叉概率0.6， 编译概率0.1
xN=200
yN=30
alfa=0.9
belta=0.1

random.seed(0)
np.random.seed(0)

#测试population
#population=np.random.randint(0,1000, xN*yN).reshape(xN, yN)*1.0
population=np.random.rand(xN, yN)
functionObject=ZDT1(population)

old_population=population.copy()
cross(population, alfa)
change(population, belta)
new_population=population.copy()
temp_population=np.vstack((old_population, new_population))

###运行200次
for i in xrange(200):
    #输出当前种群的非支配个体数
    print len( create_estimate(new_population, functionObject) )
 
    old_population=new_population
    next_set=choice(temp_population, functionObject)
    new_population=temp_population[list(next_set), ]

    cross(new_population, alfa)
    change(new_population, belta)
    temp_population=np.vstack((old_population, new_population))

###判断 new_population 支配集 效果 
print create_estimate(new_population, functionObject)

   

