from times_tables import conversa, c_show

while True:
    conversa()
    reiniciar = input(c_show("\nVocê quer recomeçar? ")).strip().lower()
    if reiniciar not in ('s', 'sim'):
        print(c_show("Adeus!"))
        break