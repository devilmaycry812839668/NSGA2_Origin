#!/usr/bin/env python
#encoding:UTF-8 
import numpy as np

def change(population, belta):
    #均匀变异
    #变异 belta  0.1

    individualSum=population.shape[0]*population.shape[1]

    locate=np.random.randint(0, individualSum, int(individualSum*belta))

    column=locate/population.shape[1]
    row=locate%population.shape[1]

    #以下代码没有考虑不同属性范围域不同的问题
    #
    #np.random.rand  默认认为所有的范围空间都是 0到1 区间
    for k in xrange(int(individualSum*belta)):
        population[column[k], row[k]]=np.random.rand()


###
###以下是测试用例
if __name__=="__main__":
    np.random.seed(0)
    xN=20
    yN=3
    belta=0.1
    population=np.random.rand(xN*yN).reshape(xN, yN)*1.0

    ###运行函数
    change(population, belta)
    print population

