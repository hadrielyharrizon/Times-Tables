from .styles import c_nome, c_show, c_idade

def conversa():
    nome = input(c_show("\nOlá!") + " Qual seu nome? ").strip().title()
    idade = input(c_nome(f"\n{nome} ") + 'quantos anos voce tem? ').strip()
    print(f'Ah que legal que você tem ' + c_idade(f'{idade}') + ' anos!')