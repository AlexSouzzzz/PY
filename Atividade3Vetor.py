#!/usr/bin/env python
# coding: utf-8

# In[1]:


i = 0
lista=[]

for a in range(0,10):
    
    idade = int(input("Qual a sua idade?  :"))
    if idade >= 18:
        
        lista.append(idade)

print(" {} Pessoas são maiores de idade".format(len(lista)))


#  
