print("Seja Bem-vindo(a) a calculadora IMC")

nome = input("Para começarmos digite seu nome: ")

altura = float(input("Digite sua altura em cm: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Você está abaixo do peso")
else:
    if imc >= 25.0:
        print("Você está acima do peso")
    else:
        print("Você está no peso ideal")

print(nome,"Seu IMC é",imc)
