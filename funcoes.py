import csv
import json
import random
import os
import subprocess

def carregar_questoes(caminho_arquivo: str) -> list[dict]:
    """
    Esta funcao recebe o caminho do arquivo CSV com o banco de questões e transforma cada questão em um dicionário e adiciona elas em uma lista.

    Args:
        caminho_arquivo(str) = Caminho do arquivo, ou, nome do arquivo se estiver na mesma pasta.
    
    Returns:
        list [dict] = Uma lista de dicionários.
    """
    questoes = []

    with open(caminho_arquivo, mode="r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            questao = {
                "pergunta" : linha["pergunta"],
                "respostas" : json.loads(linha["respostas"]),
                "resposta_certa" : linha["resposta_certa"],
                "resolucao" : linha["resolucao"],
            } 
            questoes.append(questao)

    return questoes

def sortear_questao(banco_questoes: list[dict]) -> dict | None:
    """
    Esta função sorteia uma questão do banco de questões e retorna ela como um dicionário.
    Ao mesmo tempo, retira a questão do banco para ela não se repetir.

    Args:
        banco_questoes (list[dict]) = Lista de dicionários com as questões.
    
    Returns:
        questao_atual (dict) = Questão sorteada do banco de questões, em formato de dicionário.
        None = Caso o banco de questões esteja vazio, retorna None.
    """
    if banco_questoes:
        random.shuffle(banco_questoes)
        questao_atual = banco_questoes.pop()
        return questao_atual
    else:
        return None

def formatar_questao(questao_atual: dict) -> str:
    """"
    Esta função recebe a variável questão_atual como um dicionário e formata ela como uma única string, para facilitar a exibição.
    
    Args:
        questao_atual (dict) = Dicionário contendo pergunta e respostas, bem como resposta certa e resolução.
    
    Returns:
        str = Texto formatado com a pergunta e alternativas identificadas por letras.
    """
    letras = ["A", "B", "C", "D"]
    linhas = [questao_atual["pergunta"], ""]

    for i, opcao in enumerate(questao_atual["respostas"]):
        linhas.append(f" {letras[i]}. {opcao}")

    return "\n".join(linhas)

def verificar_resposta(questao_atual: dict, escolha: str) -> bool:
    """
    Esta função verifica se a resposta inserida pelo usuário é a correta.
    
    Args:
        questao_atual (dict) = Dicionário contendo pergunta e respostas, bem como resposta certa e resolução.
        escolha (str) = Escolha de resposta inserida pelo usuário.

    Returns:
        bool = True se acertou, False se digitou a opção inválida.

    """
    mapa_letras = {"A": 0, "B": 1, "C": 2, "D": 3} 
    indice = mapa_letras.get(escolha.strip().upper())

    if indice is None or indice >= len(questao_atual["respostas"]):
        return False

    return questao_atual["respostas"][indice] == questao_atual["resposta_certa"]

def formatar_resolucao(questao_atual: dict) -> str:
    """
    Esta função recebe o dicionário da questão e retorna a resposta correta juntamente com a resolução matemática, formatada em uma única string.
    
    Args:
        questao_atual (dict) = Dicionário contendo pergunta e respostas, bem como resposta certa e resolução.
    
    Returns:
        str = Texto formatado com gabarito e o passo a passo da resolução.

    """
    texto_resolucao = (
        f"Resposta Correta: {questao_atual["resposta_certa"]}\n\n"
        f"Resolução:\n{questao_atual["resolucao"]}"
    )

    return texto_resolucao

def mostrar_instrucao() -> str:
    """
    Esta função retorna o texto completo com as regras e instruções do jogo para ser exibido na interface.

    Returns:
        str = Texto formatado com o objetivo, progressão das fases e regras do jogo.
    """
    instrucoes = (
        "OBJETIVO:\n"
        "Resolva os desafios de Análise Combinatória para destrancar as 5 salas e"
        " escapar.\n"
        "Para vencer o jogo, você precisa acumular 12 acertos no total.\n\n"
        "PROGRESSÃO DAS FASES:\n"
        "• Fase 1 (Fácil): 1 acerto\n"
        "• Fase 2 (Básico): 2 acertos\n"
        "• Fase 3 (Intermediário): 2 acertos\n"
        "• Fase 4 (Avançado): 3 acertos\n"
        "• Fase 5 (Difícil): 4 acertos\n\n"
        "REGRAS:\n"
        "• Acertou? Você avança na sala atual até liberar a próxima fase.\n"
        "• Errou? Você mantém seus acertos atuais, mas recebe uma nova questão"
        " do mesmo nível.\n"
        "• As questões não se repetem enquanto houver desafios inéditos.\n"
        "• Fique atento à suas vidas, você começa com 5: se esgotarem, é"
        " Fim de Jogo!"
    )
    return instrucoes

def limpar_terminal() -> None:
    """
    Esta função limpa a tela do terminal de acordo com o sistema operacional utilizado.

    Returns:
        None
    """
    # 'nt' identifica o Windows (usa 'cls'); outros sistemas (Linux/Mac) usam 'clear'
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)


