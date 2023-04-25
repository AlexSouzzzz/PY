#!/usr/bin/env python
# coding: utf-8

# In[ ]:


infantil = []
juvenil = []
adolescente = []
adulto = []
senior = []

while True:
    
    idade = int(input("Qual a sua idade?  :"))
    
    if idade > 30:
        senior.append(idade)
        
    elif idade > 16:
        adulto.append(idade)
        
    elif idade > 10:
        adolescente.append(idade)
        
    elif idade > 7:
        juvenil.append(idade)
        
    elif idade > 4:
        infantil.append(idade)
        
    else:
        break

print("Existem {} pessoas na categoria infantil, {} pessoas na categoria juvenil, {} pessoas na categoria adolescente. {} pessoas na categoria adulto e {} na categoria sênior".format(len(infantil),len(juvenil),len(adolescente),len(adulto),len(senior)))

