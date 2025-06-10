import random
import time
class FIFO():
    def __init__(self, tamanho):
        self.fila = []
        self.tamanho = tamanho
        self.page_faults = 0
        self.contador_acesso = {}
    
    def adicionar(self, elemento):
        if elemento not in self.fila:
            self.page_faults += 1
            if len(self.fila) >= self.tamanho:
                self.fila.pop(0)
            self.fila.append(elemento)
    
    def rodar(self, processos):
        self.page_faults = 0
        for processo in processos:
            self.adicionar(processo)
            #print(f"Fila: {self.fila}, Page Faults: {self.page_faults}")

class LRU():
    def __init__(self, tamanho):
        self.fila = []
        self.tamanho = tamanho
        self.page_faults = 0
        self.ultimo_acesso = {}  # Dicionário para registrar o momento do último acesso
        self.contador_tempo = 0   # Contador para simular a passagem do tempo
    
    def adicionar(self, elemento):
        self.contador_tempo += 1
        
        if elemento in self.fila:
            # Atualiza o tempo do último acesso se o elemento já está na fila
            self.ultimo_acesso[elemento] = self.contador_tempo
        else:
            self.page_faults += 1
            if len(self.fila) >= self.tamanho:
                # Encontra o elemento com o último acesso mais antigo
                lru_element = min(self.fila, key=lambda x: self.ultimo_acesso[x])
                self.fila.remove(lru_element)
                del self.ultimo_acesso[lru_element]
            
            self.fila.append(elemento)
            self.ultimo_acesso[elemento] = self.contador_tempo
    
    def rodar(self, processos):
        self.page_faults = 0
        self.ultimo_acesso = {}
        self.contador_tempo = 0
        for processo in processos:
            self.adicionar(processo)
            #print(f"Fila: {self.fila}, Page Faults: {self.page_faults}")

class LFU():
    def __init__(self, tamanho):
        self.fila = []
        self.tamanho = tamanho
        self.page_faults = 0
        self.contador_acesso = {}
    
    def adicionar(self, elemento):
        if elemento not in self.fila:
            self.page_faults += 1
            if len(self.fila) >= self.tamanho:
                lfu_element = min(self.fila, key=lambda x: self.contador_acesso[x])
                self.fila.remove(lfu_element)
                del self.contador_acesso[lfu_element]
            self.fila.append(elemento)
            self.contador_acesso[elemento] = 1
        else:
            self.contador_acesso[elemento] += 1
    
    def rodar(self, processos):
        self.page_faults = 0
        self.contador_acesso = {}
        for processo in processos:
            self.adicionar(processo)
            #print(f"Fila: {self.fila}, Page Faults: {self.page_faults}")
            
tamanhoFila = 5
fifo = FIFO(tamanhoFila)
lru = LRU(tamanhoFila)
lfu = LFU(tamanhoFila)

n = 5
processos = [random.randint(0, 9) for _ in range(n)]
print(processos)

def executar(politica,processos):
    inicio = time.time()

    politica.rodar(processos)

    fim = time.time()
    tempo_total = (fim - inicio) * 1000
    #print(f"Tempo de execução: {tempo_total:.3f} ms")
    return tempo_total