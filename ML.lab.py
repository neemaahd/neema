#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("play.csv")


# In[3]:


data


# In[4]:


conc = np.array(data)[:,:-1] 
print(" The attributes are: ",conc)


# In[5]:


tar = np.array(data)[:,-1] 
print("The target is: ",tar) 


# In[6]:


def train(conc, tar): 
    for i, val in enumerate(tar): 
        if val == "yes": 
            specific_h = conc[i].copy() 
            break 
    for i, val in enumerate(conc): 
        if tar[i] == "yes": 
            for x in range(len(specific_h)): 
                if val[x] != specific_h[x]: 
                     specific_h[x] = '?' 
                else: 
                    pass  
        print(specific_h)


# In[7]:


print(train(conc,tar))


# In[8]:


def cand(conc, tar): 
    specific = conc[0].copy()
    
    print("\nSpecific Boundary: ", specific)
    general = [["?" for i in range(len(specific))] for i in range(len(specific))]
    print("\nGeneric Boundary: ",general)  

    
    for i, val in enumerate(conc):
        print("\nInstance", i+1 , "is ", val)

        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    specific[x] ='?'                     
                    general[x][x] ='?'
                
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(specific)): 
                if val[x]!= specific[x]:                    
                    general[x][x] = specific[x]                              
                else:                    
                    general[x][x] = '?'        
        
        print("Specific Bundary after ", i+1, "Instance is ", specific)         
        print("Generic Boundary after ", i+1, "Instance is ", general)
        print("\n")

    indices = [i for i, val in enumerate(general) if val == ['?', '?', '?', '?', '?', '?']]    
    
    for i in indices:   
        general.remove(['?', '?', '?', '?', '?', '?']) 
    
    return specific, general 
s_final, g_final = cand(conc, tar)

print("Final Specific: ", s_final, sep="\n")

print("Final General: ", g_final, sep="\n")


# In[ ]:




