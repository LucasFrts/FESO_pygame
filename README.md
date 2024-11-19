# BreakCode

## Descrição do Projeto

O **BreakCode** é um jogo 2D estilo puzzle, desenvolvido com o objetivo de ensinar sobre raciocínio lógico e criptografia de forma divertida. O jogador acumula pontos enquanto resolve enigmas, precisando descriptografar mensagens que envolvem associações com imagens e utilizar o raciocínio lógico para decifrar a resposta correta. 

## Especificações

- **Plataforma**: Desenvolvido em Python, utilizando a biblioteca `pygame`.
- **Modo de Jogo**: Single-player.
- **Objetivo**: Resolver enigmas descriptografando mensagens para acumular pontos.
  
## Como Funciona

1. **Imagens e Letras**: Durante o jogo, é exibida uma sequência de imagens, onde cada imagem representa um animal. O nome deste animal indica as letras possíveis para a posição correspondente na palavra enigma. Por exemplo:
   - Se a imagem for de um jacaré, as letras possíveis para aquela posição são **J**, **A**, **C**, e **R**.
   
2. **Dicas**: Uma dica aparece na parte superior da tela, indicando a palavra criptografada que o jogador deve tentar descobrir.

3. **Pontuação**: 
   - Pontos são ganhos com base em acertos e na velocidade com que o jogador resolve cada enigma.
   - A pontuação é exibida no canto superior direito da tela.

4. **Banco de Dados**: O jogo utiliza um banco de dados SQLite para armazenar os históricos do jogador, mantendo um ranking com as melhores pontuações.

5. **Tempo**: O jogo tem um cronômetro. Se o tempo chegar a zero antes que o enigma atual seja resolvido, o jogo acaba e a pontuação final é exibida.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Pygame**: Biblioteca utilizada para o desenvolvimento do jogo 2D.
- **SQLite**: Banco de dados para armazenar os históricos de pontuação do jogador.

## Requisitos

- **Python 3.x**
- **Pygame**: Pode ser instalado com o comando:
  ```bash
  pip install pygame

## Estrutura do Projeto

- **game/:** Contém a lógica principal do jogo
- **database/:** Módulo de interação com o banco de dados SQLite.
- **config/:** Configurações e dicionários de curiosidades e imagens dos animais.
- **assets/:** Imagens e outros recursos utilizados no jogo.
