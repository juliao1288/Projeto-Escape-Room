import csv
import json
import random

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

