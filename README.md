# 🔐 Escape Room: Análise Combinatória

Um jogo educativo e de raciocínio lógico desenvolvido em Python. O objetivo é resolver desafios de Análise Combinatória para destrancar 5 salas e conseguir escapar antes que suas vidas acabem.

## 🎮 Sobre o Jogo
Neste Escape Room, o jogador enfrenta uma série de enigmas matemáticos divididos em 5 níveis de dificuldade (do Fácil ao Difícil). Para vencer, é necessário acumular 12 respostas corretas ao longo da jornada. Se errar, você perde uma vida, mas recebe a resolução matemática passo a passo para aprender com o erro.

### Principais Funcionalidades
* **5 Fases Crescentes:** Progressão de dificuldade estruturada para testar e ensinar conceitos como Princípio Fundamental da Contagem, Permutações, Arranjos e Combinações.
* **Banco de Questões Dinâmico:** As perguntas são carregadas a partir de arquivos CSV, sendo sorteadas aleatoriamente e sem repetições durante a fase.
* **Feedback Educativo:** O jogo não mostra apenas que você errou — ele exibe a fórmula e o raciocínio detalhado por trás da resposta certa.
* **Arquitetura Modular (Clean Code):** Toda a lógica de negócio está desacoplada da exibição no terminal, deixando o código pronto para receber uma interface gráfica no futuro (como Tkinter, CustomTkinter ou Pygame).

## 📂 Estrutura do Projeto
* `main.py`: Arquivo principal que controla o fluxo da partida, o menu inicial e a transição entre as salas.
* `funcoes.py`: O núcleo lógico do jogo. Contém funções puras e tipadas (*Type Hints*) para ler arquivos, validar regras e formatar textos.
* `fase1_facil.csv` a `fase5_dificil.csv`: Base de dados local com as perguntas, alternativas (em formato JSON), gabaritos e resoluções.

## 🚀 Como Executar
1. Certifique-se de ter o Python 3.10 ou superior instalado na sua máquina.
2. Faça o clone deste repositório.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python main.py