# class ContaCorrente():
#     def __init__(self,nconta,nometitular):
#         self.nconta=nconta
#         self.nometitular= nometitular
#         self.saldo= 0
        


#     def alterarNome(self,novonome):
#         self.nometitular=novonome

#     def deposito(self,valordeposito):
#         novosaldo=self.saldo + valordeposito
#         self.saldo=valordeposito
#         return self.saldo
#     # (f"o valor depositado foi de R$ " , valordeposito ," o novo saldo é de R$ " , self.saldo)
        
#     def saque(self, valorsaque):
#         if valorsaque > self.saldo:
#             print("valor em conta insuficiente")
#         else:
#             saldo= self.saldo - valorsaque
#             self.saldo -= valorsaque
#             print(f"o valor do saque é de R$" , valorsaque, " o novo saldo é de R$", self.saldo)
#             return self.saldo


# novaconta= ContaCorrente("0001002", 'Davi Eliote')
# novaconta.alterarNome('Eliote')
# novaconta.deposito(100)
# print(novaconta.saldo)
# novaconta.saque(20)
# print(novaconta.saldo)



# carro= {"marca":"BMW",
#         "ano": 2024,
#         "modelo": "320i"
#         }

# for carros, chaves in carro.items():
#     print(f' {carros} = {chaves}')

#     carro["ano"]= 2023

# carro.clear()
# # print(carro.popitem())
# print(carro)


arr=[1,2,3]
arr2=[4,5,6]


for item in arr2:
    arr.append(item)
print(arr)