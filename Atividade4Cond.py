#!/usr/bin/env python
# coding: utf-8

# In[ ]:


sexo=str(input("Qual seu sexo? \n f para Feminino \n m para Masculino"))

if sexo == "f" or "F":
    dia = str(input("Que dia é hoje?"))


if dia=="segunda":
    print("Recomendamos para você 'Romeu e Julieta'")
elif dia=="terca":
    print("Recomendamos para você 'O procurado'")
elif dia=="quarta" or "quarta-feira":
    print("Recomendamos para você 'O senhor dos anéis'")
elif dia=="quinta" or "quinta-feira":
    print("Recomendamos para você 'Como eu era antes de você'")
elif dia=="sexta" or "sexta-feira":
    print("Recomendamos para você 'Top gun'")
elif dia=="sabado":
    print("Recomendamos para você 'As cronicas de narnia'")
elif dia=="domingo":
    print("Recomendamos para você 'Eu me importo'")
    
else:
    print("Tente novamente \n O dia deve se digitado com letras minusculas e sem ç ou acentos")
    
if sexo == "m" or "M":
    dia = str(input("Que dia é hoje?:"))
if dia=="segunda":
    print("Recomendamos para você 'O código da vinci'")
elif dia=="terca":
    print("Recomendamos para você 'Velozes e furiosos'")
elif dia=="quarta" or "quarta-feira":
    print("Recomendamos para você 'American pie'")
elif dia=="quinta" or "quinta-feira":
    print("Recomendamos para você 'Não é mais um besteirol americano'")
elif dia=="sexta" or "sexta-feira":
    print("Recomendamos para você 'O homem aranha'")
elif dia=="sabado":
    print("Recomendamos para você 'Vingadores'")
elif dia=="domingo":
    print("Recomendamos para você 'Tramsformers'")
    
else:
    print("Tente novamente \n O dia deve se digitado com letras minusculas e sem ç ou acentos")


# In[ ]:




