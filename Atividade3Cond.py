#!/usr/bin/env python
# coding: utf-8

# In[ ]:


qntdClientes=float(input('Quantos pagantes?  :'))

qntdTotalPaga=float(input('Qual o valor total do pedido?: '))

desconto2=(qntdTotalPaga) - (qntdTotalPaga*2/100)
desconto7=(qntdTotalPaga) - (qntdTotalPaga*7.5/100)
desconto10=(qntdTotalPaga) - (qntdTotalPaga*10/100) 

if (qntdClientes <= 2):
    print("Você ganhou um desconto de 2%","\nTotal a pagar R$",desconto2,"\nCada pessoa deverá pagar: R$" , desconto2/qntdClientes )
elif (qntdClientes <=5):
    print("Você ganhou um desconto de 7,5%","\nTotal a pagar R$",desconto7,"\nCada pessoa deverá pagar: R$" , desconto7/qntdClientes)
else:
    print("Você ganhou um desconto de 10%","\nTotal a pagar R$",desconto10,"\nCada pessoa deverá pagar: R$" ,desconto10/qntdClientes)

