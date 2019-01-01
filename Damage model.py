
# coding: utf-8

# In[315]:


import random as rd
import numpy as np
import pandas as pd
from copy import deepcopy
from random import random
class Parameter():
    def __init__(self):
        
        self.mu=rd.uniform(0.01,0.1)
        self.sigma=rd.uniform(0.05,0.1)
        self.value=0
        self.dMu=0
        self.dSigma=0
        
        
    def assignValue(self):
        return max(rd.gauss(self.mu,self.sigma),0)

class DamageModel():
    
    def __init__(self):
        
        self.initialDamage=Parameter()               
        self.treshold=Parameter()              
        self.damage=Parameter()            
              
        self.growth=Parameter()
        
    def refresh(self):
        self.initialDamage.value=self.initialDamage.assignValue()
        self.treshold.value=self.treshold.assignValue()
        self.damage.value=self.damage.assignValue()
        self.growth.value=self.growth.assignValue()    

        
class SensModel():
    def __init__(self):
        self.cat1=DamageModel()



class Human():
    
    def __init__(self):
        self.sens=SensModel()
        self.time=0
        self.done=False 
        
    def step(self):
        
        for categories in self.sens.__dict__.values():
            
            categories.initialDamage.value=categories.initialDamage.value*(1+categories.growth.value)+categories.damage.value
        
        
            if categories.initialDamage.value>categories.treshold.value or self.time>115:

                return True
                break
            else:
                return False

    def simulate(self,nbsim):
        _results=np.zeros(100)
        for i in range(0,nbsim):
            for categories in self.sens.__dict__.values():
                
                categories.refresh()
            
            self.time=0
            self.done=False

            while self.done!=True and self.time<100:
                self.done=self.step()
                if self.done!=True:
                    _results[self.time]=_results[self.time]+1
                self.time=self.time+1
        return _results/nbsim
    
    def derivatives(self,delta,simulN,costFunction,goal):

        for categories in self.sens.__dict__.values():
            for damage in categories.__dict__.values():
              
                damage.mu=damage.mu+delta
                    #run simulation with adjusted value
                dx=np.sum(np.square(self.simulate(simulN)-goal))
                    #calculate derivative
                damage.dMu=(dx-costFunction)
                        #print(damage.dMu)
                damage.mu=damage.mu-delta

                damage.sigma=damage.sigma+delta
                        #run simulation with adjusted value
                dx=np.sum(np.square(self.simulate(simulN)-goal))
                        #calculate derivative
                damage.dSigma=(dx-costFunction)
                        #set value back to original
                damage.sigma=damage.sigma-delta

    def gradient(self,learningRate):
        
        for categories in self.sens.__dict__.values():
            for damages in categories.__dict__.values():
          
                try:
                    if damage.dMu<=0:
                        dtoUse=max(-0.25,damage.dMu*learningRate)
                    else:
                        dtoUse= min(0.25,damage.dMu*learningRate)

                    damage.mu=max(damage.mu-dtoUse,0)
                    if damage.dMu<=0:

                        dtoUse=max(-0.25,damage.dSigma*learningRate)
                    else:
                        dtoUse=min(0.25,damage.dSigma*learningRate)

                    damage.sigma=max(damage.sigma-dtoUse,0)
                except:
                    pass


# In[282]:



x=pd.read_csv('C:\dev to W drive\SS.csv')
x=x.drop(x.index[[0,18]])
x.head(-5)


# In[283]:


goal=x.loc[0:101,['Survivors']].as_matrix()

print(goal.shape)
goal=np.squeeze(goal)
print(goal.shape)


# In[284]:

sCurve=np.zeros(len(goal))
print(sCurve.shape)


# In[316]:


delta=0.0000000000000000001
simulN=2000
learningRate=0.5
test=Human()

#test.sens.treshold.mu=tm+0.25
#test.sens.treshold.sigma=ts
#test.sens.growth.mu=gm
#test.sens.growth.sigma=gs
#test.sens.initialDamage.mu=inm
#test.sens.initialDamage.sigma=ins
#test.sens.damage.mu=dm
#test.sens.damage.sigma=ds
for i in range(10):
    
    sCurve=test.simulate(simulN)        
    costFunction=np.sum(np.square(sCurve-goal))
    print('costfunction ',costFunction)
   #print('treshold',test.sens.treshold.mu)
    test.derivatives(delta,simulN,costFunction,goal)
    test.gradient(learningRate)


# In[305]:


print(sCurve)


# In[23]:


print(test.sens.growth.value)


# In[300]:


tm=test.sens.treshold.mu
ts=test.sens.treshold.sigma
gm=test.sens.growth.mu
gs=test.sens.growth.sigma
inm=test.sens.initialDamage.mu
ins=test.sens.initialDamage.sigma
dm=test.sens.damage.mu
ds=test.sens.damage.sigma


# In[298]:


print(test.sens.initialDamage.mu)
print(test.sens.treshold.mu)
print(test.sens.growth.mu)
print(test.sens.damage.mu)


# In[299]:


print(test.sens.initialDamage.dMu)
print(test.sens.treshold.dMu)
print(test.sens.growth.dMu)
print(test.sens.damage.dMu)

