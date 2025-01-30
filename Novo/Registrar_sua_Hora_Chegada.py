import os
import time
import calendar
from time import gmtime, strftime


""" Registro de Ponto """
# coding: UTF-8

os.system("cls")
admin = "programador001"

class Codigo_Terminal:

    def __Consulta_Ponto__(self):

        hora_atual = strftime("%H:%M:%S", gmtime())                 # mostrar hora atual.
        year, month = 2025, 1                                       # mostrar mês.
        print(hora_atual, calendar.month(year, month))
        print("(0) inicio de registro\n(1) fim do registro.")
        choice = input("#: ")


        if choice == "0":
            def __inicio__(user):

                global admin                                        # deixar variavel global

                hora_inicio = time.strftime("%H:%M:%S")                     # mostrar hora atual.
                if user == admin:                                           # verificar se existe a string no programa
                    salvar_registro_inicio = open("inicio.txt", "a")        # abrir um arquivo ja existente, ou criar o remetente se não existir
                    salvar_registro_inicio.write(f"{hora_inicio}\n")
                    print("(C)arquivo salvo.")

                else:
                    print(f"(X)não existem esse registro. {user}")

            __inicio__(user=input("[+]ID: "))



        elif choice == "1":
            def __fim__(user):

                global admin                                        # deixar variavel global
                hora_fim = time.strftime("%H:%M:%S")

                if user == admin:                                           # verificar se existe a string no programa
                    salvar_registro_fim = open("fim.txt", "a")              # abrir um arquivo ja existente, ou criar o remetente se não existir
                    salvar_registro_fim.write(f"{hora_fim}\n")
                    print("(C)arquivo salvo.")

                else:
                    print(f"(X)não existem esse registro. {user}")

            __fim__(user=input("[+]ID: "))

        else:
            quit()



if __name__ == "__main__":
    Codigo_Terminal.__Consulta_Ponto__(self=None)



