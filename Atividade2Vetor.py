#!/usr/bin/env python
# coding: utf-8

# In[1]:


qnt = int(input("Quantos produtos você quer registrar? "))
n = 1
total = 0

for a in range(0,qnt):
    valor = float(input("Informe o valor dos produtos {} ".format(n)))
    total += valor
    
    n += 1

print("O valor total do produto é {} R$".format(total))


# In[ ]:




