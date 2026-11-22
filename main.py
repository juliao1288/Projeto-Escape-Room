import funcoes


def main():

    while True:

        print()
        print("="*20, "ESCAPE ROOM", "="*20)
        print(" 1 - Iniciar")
        print(" 2 - Sair")
        print(" 3 - Instruções")

        opcao = input("\n Insira sua opção: ")

        

        match opcao:
            case "1":
                funcoes.limpar_terminal()
                banco_questoes = funcoes.carregar_questoes("fase1_facil.csv")
                questao_atual = funcoes.sortear_questao(banco_questoes)

                print("="*20, "FASE 1", "="*20)
                print(funcoes.formatar_questao(questao_atual))
                escolha = input(" Insira sua resposta: ").upper()
                if funcoes.verificar_resposta(questao_atual, escolha):
                    print(" Parabéns, vc acertou.")
                    funcoes.limpar_terminal()
                else:
                    print(" Que pena, vc errou.")


                
            case "2":
                print(" Você escolheu sair...")
                break 
            case "3":
                print()
                print(funcoes.mostrar_instrucao())
                comando = input("\n Pressione a tecla 'enter' para continuar:  ")
                if comando.join(" "):
                    funcoes.limpar_terminal()

            case _:
                print(" Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()