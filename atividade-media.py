import math

nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
nota3 = float(input("digite a segunda nota "))

media = (nota1 + nota2 + nota3) / 3
media = round(media, 2 )
#aqui outra forma arrednodar;
#media = round(media, 1)

print = ("a media foi de:", media)


if media >= 0 and media <= 5.5:
    print ("reprovado, nota:",media)

elif media > 5.5 and media <= 6.5:
    print("em recuperacao", media)

elif media > 6.5 and media <= 10:
    print("aprovado:",media) 

else:
    print("numero nao condiz com uma nota de 0 a 10") 


