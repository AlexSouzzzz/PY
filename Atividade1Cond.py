#!/usr/bin/env python
# coding: utf-8

# In[1]:


prod1=float(input('Digite o preco do produto 1:'))
prod2=float(input('Digite o preco do produto 2:'))
prod3=float(input('Digite o preco do produto 3:'))
prod4=float(input('Digite o preco do produto 4:'))

totalFaturamento=prod1+prod2+prod3+prod4




if totalFaturamento < 50000:
    print("Sua fatura foi de: R$", totalFaturamento, "você não recebeu nada de comissão")
elif totalFaturamento < 100000:
    print ("Sua fatura foi de: R$", totalFaturamento+totalFaturamento*2/100,"e você recebeu de comissão 2% ","\n e sua comissão total em dinheiro foi: R$", totalFaturamento*2/100 )
else:
    print ("Sua fatura foi de: R$",totalFaturamento+totalFaturamento*3.5/100,"e você recebeu de comissão 3,5% ","\n e sua comissão total em dinheiro foi: R$", totalFaturamento*3.5/100)


# In[ ]:




