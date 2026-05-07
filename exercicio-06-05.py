produtos = ["maçã", "banana", "pera", "melancia", ]
precos = [40.00,  80.00, 15.00, 20.00,  30.00,]

print(produtos)
print(produtos[0])
print(produtos[-1])
print(len(produtos))

# para exibir:
print(f"o produto { produtos[0]} custa R${precos[0]},")

# para remover o ultimo produto também:
produtos.remove(produtos[-1])
precos.remove(precos[-1])

# para somar o preco de todos os produtos:
total = sum(precos)
print(f"o total deu R${total}")

# logica condicional if\ else para desconto:
if total  < 100:
    exit()
else:
    desconto = 0.95
    c = total * desconto
    print(f" o tatal agora com desconto e de R${total}.")    

                          