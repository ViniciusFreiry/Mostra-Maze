# Mostra-Maze

## Descrição

Este projeto implementa a geração e exibição de um labirinto aleatório utilizando o algoritmo **Aldous-Broder** para a criação do labirinto e o algoritmo **A\* (A estrela)** para a resolução. O labirinto gerado é mostrado em uma interface gráfica criada com **Pygame**. O código visualiza o labirinto, marca o caminho da solução caso exista e permite a interação com o algoritmo de geração.

### Objetivo

O código tem como objetivo gerar um labirinto usando o algoritmo de **Aldous-Broder**, que é um algoritmo de **caminho aleatório**. O labirinto gerado pode ser resolvido (se houver solução) utilizando o algoritmo **A\***.

## Estrutura do Código

O código é composto por várias classes e funções que realizam as tarefas de geração e visualização do labirinto:

### Classes

1. **ArestasFechadas**
   - Representa as arestas (superior, inferior, esquerda, direita) que podem ser fechadas em uma célula do labirinto.

2. **Celula**
   - Representa cada célula no labirinto.
   - Contém informações sobre o estado da célula (se foi visitada, se está aberta, etc.) e as cores usadas para desenhá-la.
   - Possui métodos para desenhar a célula na tela.

3. **AldousBroder**
   - Implementa o algoritmo **Aldous-Broder** para a geração do labirinto.
   - Contém métodos para gerar o labirinto e resetar o estado das células.

4. **Malha**
   - Representa a matriz de células que compõem o labirinto.
   - Contém métodos para gerar e desenhar o labirinto.

### Funções

- **resolve_labirinto**: Resolve o labirinto gerado utilizando o algoritmo **A\***, marcando as células no caminho da solução.
- **main**: Inicializa o Pygame, define a interface gráfica e executa o loop principal, desenhando o labirinto e exibindo a solução, caso exista.

## Como Usar

### Pré-requisitos

- Python 3.x
- Pygame (Instalar com `pip install pygame`)

### Execução

Para executar o código, basta rodar o arquivo `maze001.py`:

```bash
python maze001.py
