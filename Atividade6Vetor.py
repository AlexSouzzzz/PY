#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date

conta1 = []
data1 = []
conta2 = []
data2 = []
conta3 = []
data3 = []
conta4 = []
data4 = []
conta5 = []
data5 = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

while True:
    
    depositar = int(input("Qual conta deseja depositar?  1, 2, 3, 4 ou 5?"))
    
    if depositar == 1:
        
        conta1.append(float(input("Quanto quer depositar?  :")))
        data1.append(date.today())
        total1 = sum(conta1)
        
        print("Foram depositados R${} na conta no dia {}, a conta tem um valor total de R${}".format(conta1[count1],data1[count1],total1))
        count1 += 1
        
    elif depositar == 2:
              
        conta2.append(float(input("Quanto quer depositar?  :")))
        data2.append(date.today())
        total2 = sum(conta2)
        
        print("Foram depositados R${} na conta no dia {}, a conta tem um valor total de R${}".format(conta2[count2],data2[count2],total2))
        count2 += 1
        
    elif depositar == 3:
              
        conta3.append(float(input("Quanto quer depositar?  :")))
        data3.append(date.today())
        total3 = sum(conta3)
              
        print("O valor de R${} foi depositado na conta no dia {}, a conta tem um valor total de R${}".format(conta3[count3],data3[count3],total3))        
        count3 += 1
        
    elif depositar == 4:
              
        conta4.append(float(input("Quanto quer depositar?  :")))
        data4.append(date.today())
        total4 = sum(conta4)
        
        print("Foram depositados R${} na conta no dia {}, a conta tem um valor total de R${}".format(conta4[count4],data4[count4],total4))       
        count4 += 1
        
    elif depositar == 5:
              
        conta5.append(float(input("Quanto quer depositar?  :")))
        data5.append(date.today())
        total5 = sum(conta5)
        
        print("Foram depositados R${} na conta no dia {}, a conta tem um valor total de R${}".format(conta5[count5],data5[count5],total5))        
        count5 += 1
        
    else: break


# In[ ]:




