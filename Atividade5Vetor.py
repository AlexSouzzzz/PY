#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pessoas = []
total = []

while True:
    
    pessoas.append(str(input("Insira o nome: ")))
    pessoas.append(int(input("Insira a idade: ")))
    pessoas.append(float(input("Insira a altura: ")))
    
    total.append(pessoas[:])
    pessoas.clear()
    total.sort()
    
    continuar = (str(input("Quer Adicionar outra pessoa? sim/não ")))
    
    if continuar == "não":
        break
        
print(total)


# In[ ]:




