# Comparacao de Algoritmos de Escalonamento: LRU, LFU e FIFO

Este repositório contém um código em Python que compara o desempenho dos algoritmos de escalonamento de páginas **LRU (Least Recently Used)**, **LFU (Least Frequently Used)** e **FIFO (First In, First Out)**. A aplicação inclui uma interface ilustrativa para visualização do comportamento de cada algoritmo ao longo do tempo.

---

## 🔍 Descrição

* **Algoritmos incluídos:** LRU, LFU e FIFO.
* **Objetivo:** Medir e comparar o desempenho dos algoritmos com base em diferentes sequências de referência.
* **Conversão IA:** O código de medição de tempo foi inicialmente desenvolvido em Java e convertido para Python com o auxílio de uma inteligência artificial. A mesma IA também foi utilizada para integrar os componentes da interface gráfica com o sistema de comparação dos algoritmos.

---

## 🖥️ Como Usar

### 1. Pré-requisitos

Certifique-se de ter o Python instalado e, em seguida, instale as bibliotecas necessárias:

```bash
pip install pygame
```

> Além do `pygame`, são utilizadas as bibliotecas `sys`, `time` e `random`, que já fazem parte da biblioteca padrão do Python.

### 2. Executando o Projeto

1. Abra o projeto na IDE **Visual Studio Code (VSCode)**.
2. Instale as bibliotecas mencionadas, se ainda não estiverem instaladas.
3. Pressione o botão **Run** no VSCode para executar o programa.

---

## 📁 Estrutura do Projeto

```
├── algoritmos/
│   ├── lru.py
│   ├── lfu.py
│   └── fifo.py
├── interface/
│   └── visualizacao.py
├── comparador.py
├── main.py
└── README.md
```

* `algoritmos/`: Implementações individuais dos algoritmos.
* `interface/`: Interface gráfica usando pygame para ilustrar o comportamento dos algoritmos.
* `comparador.py`: Lógica de comparação de desempenho entre os algoritmos.
* `main.py`: Ponto de entrada do programa.

---

## 🧠 Créditos

Este projeto foi parcialmente auxiliado por uma IA, que contribuiu na conversão de código Java para Python e na integração dos módulos de interface com os algoritmos.
