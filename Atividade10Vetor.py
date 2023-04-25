#!/usr/bin/env python
# coding: utf-8

# In[5]:


acidentes = []
totalAcidente = []

while True:
    acidentes.append(int(input("Qual o código da cidade? ")))
    acidentes.append(str(input("Qual o estado? ")))
    acidentes.append(int(input("Números de veículos de passeio em 2021: ")))
    acidentes.append(int(input("Quantidade de acidentes de trânsito com vítimas: ")))
    
    totalAcidente.append(acidentes[:])
    acidentes.clear()

    continuar = str(input("Quer continuar inserindo dados? s/n"))
    
    if continuar == "n":
        break
        
print("Cidade|Estado|Passeios|Acidentes \n {}".format(totalAcidente))


# In[ ]:





# In[ ]:




