#!/usr/bin/env python
# coding: utf-8

# In[1]:


produto = []
valor = []
quant = []
count = 0
total = []


# In[ ]:


while True:
    
    cliente = str(input("Algum cliente esperando? s/n"))
    
    if cliente == "s":
        
        while True:
            
            produto.append(str(input("Qual é o produto? ")))
            valor.append(float(input("Qual o valor do produto? ")))
            quant.append(int(input("Quantos desse produto você quer? ")))
            
            for a in range(count,len(produto)):
                total.append(valor[count]*quant[count])
                count += 1
            
            add = str(input("Deseja adicionar mais algum item ao carrinho? s/n"))
            
            if add == "n":
                print(sum(total))
                total.clear()
                break
                
    else:
        break

