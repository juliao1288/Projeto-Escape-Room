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
                banco_questoes = funcoes.carregar_questoes(arquivos[fase])
                while True:
                    if acertos < acertos_necessarios[fase]:
                        print("="*20, f"FASE {fase+1}", "="*20)
                        
                        questao_atual = funcoes.sortear_questao(banco_questoes)
                        print(funcoes.formatar_questao(questao_atual))
                        escolha = input(" Insira sua resposta: ").upper()
                        if funcoes.verificar_resposta(questao_atual, escolha):
                            print(" Parabéns, vc acertou.")
                            acertos += 1
                            print(len(banco_questoes))
                            input("\n Pressione a tecla 'enter' para continuar:  ")
                            funcoes.limpar_terminal()
                        else:
                            print(" Que pena, vc errou.")
                            print(len(banco_questoes))
                            print(funcoes.formatar_resolucao(questao_atual))
                            comando = input("\n Pressione a tecla 'enter' para continuar:  ")
                            if comando.join(" "):
                                funcoes.limpar_terminal()
                    else:
                        if fase == 4:
                            print(" Parabéns, vc chegou ao final do jogo!!")
                            break
                        else:
                            print(" Parabéns, você acertou a quantidade necessária e passou de fase.")
                            acertos = 0
                            fase += 1
                            banco_questoes = funcoes.carregar_questoes(arquivos[fase])


                
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