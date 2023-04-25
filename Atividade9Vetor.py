#!/usr/bin/env python
# coding: utf-8

# In[4]:



idade = []
count = 0

while True:
    
    n = int(input("Insira a idade: "))
    if n < 1:
        break
    else: 
        sexo = str(input("Qual seu sexo? \n m para masculino \n f para Feminino "))
        cabelo = str(input("Qual a sua cor de cabelo? "))
        olho = str(input("Qual a cor dos seus olhos? "))
    
        idade.append(n)
        
        if sexo == "f" and n > 17 and n < 36 and cabelo == "loiro" and olho == "verde":
            count = count + 1
    
print("A maior idade entre os habitantes é {} e existem {} do sexo feminino com cabelos loiros e olhos verdes com idade entre 18 e 35".format(max(idade), count))

