import random

def show_timestable(num):
    print(f'\nA Tabuada do {num}:')
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')

def practice_timestable(num):
    print(f'\nModo Treino: A Tabuada do {num}')
    score = 0
    for _ in range(5):
        multiplier = random.randint(1, 10)
        correct_answer = num * multiplier

        while True:
            try:
                user_answer = int(input(f'{num} x {multiplier} = '))
                break
            except ValueError:
                print('Insira um número válido.')

        if user_answer == correct_answer:
            print('✅ Resposta correta!')
            score += 1
        else:
            print(f'❌ Resposta errada! A resposta correta é {correct_answer}')
    print(f'Você acertou {score} de 5.\n')

def main():
    print('----- Tabuada Interativa -----')

    while True:
        # Escolha do número
        while True:
            try:
                number = int(input('\nEscolha um número para estudar a tabuada (0 para sair): '))
                break
            except ValueError:
                print('Insira um número válido.')

        if number == 0:
            print('Programa Encerrado! 👋')
            break

        # Escolha do modo
        while True:
            try:
                mode = int(input('Escolha o modo: 1 - Aprender, 2 - Treinar: '))
                if mode in [1, 2]:
                    break
                else:
                    print('Modo inválido. Insira 1 ou 2.')
            except ValueError:
                print('Por favor, insira um número válido')

        # Executa a opção escolhida
        if mode == 1:
            show_timestable(number)
        else:
            practice_timestable(number)

if __name__ == '__main__':
    main()
