import funcoes
import time


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
                arquivos = ["fase1_facil.csv", "fase2_basico.csv", "fase3_intermediario.csv", "fase4_avancado.csv", "fase5_dificil.csv"]
                acertos_necessarios = [1, 2, 2, 3, 4]
                acertos = 0
                fase = 0
                vidas = 5
                banco_questoes = funcoes.carregar_questoes(arquivos[fase])
                while True:
                    if acertos < acertos_necessarios[fase]:
                        print("="*20, f"FASE {fase+1}", "="*20)
                        print(f" Você tem {vidas} vida(s) restante(s).")
                        questao_atual = funcoes.sortear_questao(banco_questoes)
                        print(funcoes.formatar_questao(questao_atual))
                        escolha = input(" Insira sua resposta: ").upper()
                        if funcoes.verificar_resposta(questao_atual, escolha):
                            print(" Parabéns, vc acertou.")
                            acertos += 1
                            input("\n Pressione a tecla 'enter' para continuar:  ")
                            funcoes.limpar_terminal()
                        else:
                            print(" Que pena, vc errou.")
                            vidas -= 1
                            if vidas < 1:
                                print(" Que pena, vc gastou todas suas vidas, reinicie e tente novamente.")
                                input("\n Pressione a tecla 'enter' para regressar ao menu: ")
                                funcoes.limpar_terminal()
                                break
                            print(funcoes.formatar_resolucao(questao_atual))
                            input("\n Pressione a tecla 'enter' para continuar:  ")
                            funcoes.limpar_terminal()
                    else:
                        if fase == 4:
                            print(" Parabéns, vc chegou ao final do jogo!!")
                            input("\n Pressione a tecla 'enter' para regressar ao menu: ")
                            funcoes.limpar_terminal()
                            break
                        else:
                            print(" Parabéns, você acertou a quantidade necessária e passou de fase.")
                            acertos = 0
                            fase += 1
                            banco_questoes = funcoes.carregar_questoes(arquivos[fase])
                            input("\n Pressione a tecla 'enter' para continuar:  ")
                            funcoes.limpar_terminal()


                
            case "2":
                print(" Você escolheu sair...")
                break 
            case "3":
                print()
                print(funcoes.mostrar_instrucao())
                input("\n Pressione a tecla 'enter' para continuar:  ")
                funcoes.limpar_terminal()

            case _:
                print(" Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()