frutas = ["manga", "banana", "abacaxi", "laranja", "uva"]

fruta_favorita = input("qual sua fruta favorita?  ")

if fruta_favorita not in frutas:
    print("sua fruta favorita nao esta na lista")
    exit()


# para cada posicao (indice) e fruta na lista numerada
for posicao, fruta in enumerate(frutas):
    # faca isso:
    # se a fruta dessa iteracao e igual a fruta favorita
    if fruta == fruta_favorita:
        # salva numa nova vaariavel a posiçao dessa iteracao
        posicao_fruta_favorita = posicao
        # quebra a for (faz ele parar)
        break
0
# saida do algoritimo  (print)    
print( f"minha fruta favorita esta na posicao indice {posicao_fruta_favorita}")
