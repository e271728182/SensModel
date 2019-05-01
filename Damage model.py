
# coding: utf-8

# In[315]:


import random as rd
import numpy as np
import pandas as pd
from copy import deepcopy
from random import random



class Human():
    def __init__(self,basal_M,basal_sd,exp_m,exp_sd,basal_homo,exp_homo,shape_death):

        self.time=0
        self.done=False
        self.nbCat
        #fitting parameters
        self.basalRate_M=basal_M
        self.basalRate_Sd=basal_sd
        self.exp_M=exp_m
        self.exp_Sd=exp_sd
        self.basal_Homo=basal_homo
        self.exp_Homo=exp_homo
        self.shape_death=shape_death
        self.totalDamage=0
        #internal variables:
        #feedback rate for all mechanism
        self.pb=self.pbDist()
        self.pe=self.peDist()
        self.categoryList=[]
        self.maxCatDamage=max([cat.cumulDamage in self.categoryList])
    
    def rPd(self,damage):
        return 2**-(self.shape_death*(1-damage))

    def spd(self,damage):
        return (self.rpd(damage)-self.rpd(0))/(1-self.rpd(0))

    def isDeadC(self):
        if self.maxCatDamage>np.random.uniform(0,1):
            return True
        else:
            return False
    def pbDist(self):
        return np.random.lognormal(self.basalRate_M,self.BasalRate_SD)

    def peDist(seff):
        return np.random.lognormal(self.exp_M,self.exp_SD)
    def calculateTotalDamage(self):

        return sum([cumul for cat.cumulDamageC in self.categoryList])
    def createCategory(self,nbCat

        for i in range(nbCat+1):
            _newCat=Category()
            self.categoryList.append(_newCat)

    def createMechanism(self,nbMec):
        for category in self.categoryList:
            for i in range(nbMec+1):
                #create a mechanism
                mec=Mechanism()
                #assign it a basal rate and & feedback rate
                mec.basalRate=self.basal_Homo*self.pb+(1-self.basal_Homo)*self.pbDist()
                mec.exp=self.exp_Homo*self.pe +(1-self.exp_Homo)*self.peDist()
                #stuff it into the mechanism list of the category
                category.mechanismList.append(mec)

    def updateTotalDamage(self):
        return sum([cat.cumulDamageC() for cat in self.categoryList])

    def updateMecDamage(self):
        for cat in self.categoryList:
            for mec in cat.mechanismList:
                mec.damageIncrement=mec.damageIncrementC(self.totalDamage)
                mec.cumulDamage=mec.cumulDamageC()

class Category(self):
    def __init__(self):
        self.mechanismList=[]
        self.cumulDamage=0
    def cumulDamageC(self):
    self.cumulDamage=self.cumulDamage+sum([mec.damageIncrementC in self.mechanismList])
    return self.cumulDamage


class Mechanism():
    def __init__(self):
        self.basalRate=0
        self.exp=0
        self.damageIncrement=0
        self.cumulDamage=0
    def damageIncrementC(self,personDamage):

        self.damageIncrement=self.damageIncrement+self.basalRate+self.exp*personDamage
        self.cumulDamage=self.cumulDamage+self.cumulDamage+self.damageIncrement
        return self.cumulDamage
    #def cumulDamageC(self):
    #    return self.cumulDamage+self.damageIncrement


#     def step(self):
#
#         for categories in self.sens.__dict__.values():
#
#             categories.initialDamage.value=categories.initialDamage.value*(1+categories.growth.value)+categories.damage.value
#
#
#             if categories.initialDamage.value>categories.treshold.value or self.time>115:
#
#                 return True
#                 break
#             else:
#                 return False
# #
#     def simulate(self,nbsim):
#         _results=np.zeros(100)
#         for i in range(0,nbsim):
#             for categories in self.sens.__dict__.values():
#
#                 categories.refresh()
#
#             self.time=0
#             self.done=False
#
#             while self.done!=True and self.time<100:
#                 self.done=self.step()
#                 if self.done!=True:
#                     _results[self.time]=_results[self.time]+1
#                 self.time=self.time+1
#         return _results/nbsim
#
#     def derivatives(self,delta,simulN,costFunction,goal):
#
#         for categories in self.sens.__dict__.values():
#             for damage in categories.__dict__.values():
#
#                 damage.mu=damage.mu+delta
#                     #run simulation with adjusted value
#                 dx=np.sum(np.square(self.simulate(simulN)-goal))
#                     #calculate derivative
#                 damage.dMu=(dx-costFunction)
#                         #print(damage.dMu)
#                 damage.mu=damage.mu-delta
#
#                 damage.sigma=damage.sigma+delta
#                         #run simulation with adjusted value
#                 dx=np.sum(np.square(self.simulate(simulN)-goal))
#                         #calculate derivative
#                 damage.dSigma=(dx-costFunction)
#                         #set value back to original
#                 damage.sigma=damage.sigma-delta
#
#     def gradient(self,learningRate):
#
#         for categories in self.sens.__dict__.values():
#             for damages in categories.__dict__.values():
#
#                 try:
#                     if damage.dMu<=0:
#                         dtoUse=max(-0.25,damage.dMu*learningRate)
#                     else:
#                         dtoUse= min(0.25,damage.dMu*learningRate)
#
#                     damage.mu=max(damage.mu-dtoUse,0)
#                     if damage.dMu<=0:
#
#                         dtoUse=max(-0.25,damage.dSigma*learningRate)
#                     else:
#                         dtoUse=min(0.25,damage.dSigma*learningRate)
#
#                     damage.sigma=max(damage.sigma-dtoUse,0)
#                 except:
#                     pass
#
#
# # In[282]:
#
#
#
# x=pd.read_csv('C:\dev to W drive\SS.csv')
# x=x.drop(x.index[[0,18]])
# x.head(-5)
#
#
# # In[283]:
#
#
# goal=x.loc[0:101,['Survivors']].as_matrix()
#
# print(goal.shape)
# goal=np.squeeze(goal)
# print(goal.shape)
#
#
# # In[284]:
#
# sCurve=np.zeros(len(goal))
# print(sCurve.shape)
#
#
# # In[316]:
#
#
# delta=0.0000000000000000001
# simulN=2000
# learningRate=0.5
# test=Human()
#
# #test.sens.treshold.mu=tm+0.25
# #test.sens.treshold.sigma=ts
# #test.sens.growth.mu=gm
# #test.sens.growth.sigma=gs
# #test.sens.initialDamage.mu=inm
# #test.sens.initialDamage.sigma=ins
# #test.sens.damage.mu=dm
# #test.sens.damage.sigma=ds
# for i in range(10):
#
#     sCurve=test.simulate(simulN)
#     costFunction=np.sum(np.square(sCurve-goal))
#     print('costfunction ',costFunction)
#    #print('treshold',test.sens.treshold.mu)
#     test.derivatives(delta,simulN,costFunction,goal)
#     test.gradient(learningRate)
#
#
# # In[305]:
#
#
# print(sCurve)
#
#
# # In[23]:
#
#
# print(test.sens.growth.value)
#
#
# # In[300]:
#
#
# tm=test.sens.treshold.mu
# ts=test.sens.treshold.sigma
# gm=test.sens.growth.mu
# gs=test.sens.growth.sigma
# inm=test.sens.initialDamage.mu
# ins=test.sens.initialDamage.sigma
# dm=test.sens.damage.mu
# ds=test.sens.damage.sigma
#
#
# # In[298]:
#
#
# print(test.sens.initialDamage.mu)
# print(test.sens.treshold.mu)
# print(test.sens.growth.mu)
# print(test.sens.damage.mu)
#
#
# # In[299]:
#
#
# print(test.sens.initialDamage.dMu)
# print(test.sens.treshold.dMu)
# print(test.sens.growth.dMu)
# print(test.sens.damage.dMu)
