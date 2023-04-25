#!/usr/bin/env python
# coding: utf-8

# In[1]:


filial1 = []
filial2 = []
filial3 = []
filial4 = []

while True:
    
    n1 = float(input("Qual da faturamento da primeira filial?  :")) 
    
    if n1 > 0:
        filial1.append(n1)
        media1 = sum(filial1)/len(filial1)

    n2 = float(input("Qual da faturamento da segunda filial?  :"))
    
    if n2 > 0:
        filial2.append(n2)
        media2 = sum(filial2)/len(filial2)
        
    n3 = float(input("Qual da faturamento da terceira filial?  :"))
    
    if n3 > 0:
        filial3.append(n3)
        media3 = sum(filial3)/len(filial3)
        
    n4 = float(input("Qual da faturamento da quarta filial?  :"))
    
    if n4 > 0:
        filial4.append(n4)
        media4 = sum(filial4)/len(filial4)

    vender = str(input("Deseja fazer mais alguma venda? sim/não"))

    if vender == "não":
        break


# In[4]:


print("A primeira filial vendeu um total de R${} com uma média de R${}, já a segunda vendeu R${} com uma média de R${}. A terceira vendeu um total de R${} e uma média de R${}, a quarta vendeu R${} de total e R${} de média."
      .format(sum(filial1),media1,sum(filial2),media2,sum(filial3),media3,sum(filial4),media4))


# In[ ]:




