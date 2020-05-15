FizzBuzz=Fizz=Buzz=0
#Verificação do primeiro input() se o valor é inteiro ou está no range especificado.
while True:
    try:
        valor1 = int(input("Informe o primeiro valor do intervalo, escolha entre \033[35m1\033[m e \033[34m1000\033[m: "))
        if not 1 <= valor1 <= 1000:
            raise ValueError
    except ValueError:
        print("\033[31mERRO: Valor não inteiro ou fora do intervalo permitido.\033[m")
    else:
        break
# Verificação do segundo input() se o valor é inteiro ou está no range especificado.
while True:
    try:
        valor2 = int(input(f'Informe o segundo valor do intervalo, escolha entre \033[35m{valor1}\033[m e \033[34m1000\033[m: '))
        if not valor1 <= valor2 <= 1000:
            raise ValueError
    except ValueError:
        print('\033[31mERRO: Valor não inteiro ou fora do intervalo permitido.\033[m')
    else:
        break
#Mostra o intevalo escolhido.
print('Lista:', list(range(valor1, valor2+1)))
#Laço de repetição para verificação de cada calor do intervalo.
for calc in range(valor1, valor2+1):
       if calc % 3 == 0 and calc % 5 == 0:
              print('\033[35mFizzBuzz\033[m')
              FizzBuzz += 1
       elif calc % 3 == 0:
              print('\033[34mFizz\033[m')
              Fizz += 1
       elif calc % 5 == 0:
              Buzz += 1
              print('\033[36mBuzz\033[m')
       else:
              print(calc)
print('\033[1;30m-\033[m'*20)
print(f'\033[1;30mIntervalo escolhido foi de\033[m \033[1;33m{valor1}\033[m \033[1;30ma\033[m \033[1;33m{valor2}\033[m')
print('\033[1;30m-\033[m'*20)
print('\033[1;30mResumo:\033[m')
print(f'\033[34mFizz: {Fizz}\033[m\n\033[36mBuzz: {Buzz}\033[m\n\033[35mFizzBuzz: {FizzBuzz}\033[m')
print('\033[1;30m-\033[m'*20)