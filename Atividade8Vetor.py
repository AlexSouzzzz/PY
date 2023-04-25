#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cand1 = []
cand2 = []
cand3 = []
cand4 = []
branco = []
nulo = []

while True:
    
    voto = int(input("Em quem você deseja votar?\n 1 para Candidato 1\n 2 para Candidato 2\n 3 para Candidato 3\n 4 para Candidato 4\n 5 para NULO \n 6 para BRANCO"))
    
    if voto == 1:
        cand1.append(voto)
        
    elif voto == 2:
        cand2.append(voto)
        
    elif voto == 3:
        cand3.append(voto)
        
    elif voto == 4:
        cand4.append(voto)
        
    elif voto == 5:
        nulo.append(voto)
        
    elif voto == 6:
        branco.append(voto)
        
    elif voto == 0:
        break
        
print("O candidato 1 recebeu {} votos, o candidato 2 recebeu {} votos, o candidato 3 recebeu {} votos, o candidato 4 recebeu {} votos, votos nulos foram {} e brancos foram {}".format(len(candidato1),len(candidato2),len(candidato3),len(candidato4),len(nulo),len(branco)))


# In[ ]:




