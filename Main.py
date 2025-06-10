import pygame
import sys
import time
import random
from Escalonamento import FIFO, LRU, LFU

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corrida de Algoritmos de Escalonamento")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

FONT_LARGE = pygame.font.SysFont("Arial", 36)
FONT_MEDIUM = pygame.font.SysFont("Arial", 24)
FONT_SMALL = pygame.font.SysFont("Arial", 18)

tamanhoFila = 3
n_processos = 5
processos = [random.randint(0, 9) for _ in range(n_processos)]

fifo = FIFO(tamanhoFila)
lru = LRU(tamanhoFila)
lfu = LFU(tamanhoFila)

def executar(politica, processos):
    inicio = time.time()
    politica.rodar(processos)
    fim = time.time()
    return (fim - inicio) * 1000 

tempo_fifo = executar(fifo, processos)
tempo_lru = executar(lru, processos)
tempo_lfu = executar(lfu, processos)

vencedor = ""
if tempo_fifo < tempo_lru and tempo_fifo < tempo_lfu:
    vencedor = "FIFO"
elif tempo_lru < tempo_fifo and tempo_lru < tempo_lfu:
    vencedor = "LRU"
elif tempo_lfu < tempo_fifo and tempo_lfu < tempo_lru:
    vencedor = "LFU"
else:
    vencedor = "EMPATE"

car_width, car_height = 60, 40
xFIFO, yFIFO = 50, HEIGHT // 2 - 100  
xLRU, yLRU = 50, HEIGHT // 2        
xLFU, yLFU = 50, HEIGHT // 2 + 100  

maxSpeed =  10
speedFIFO = maxSpeed/(tempo_fifo * 100)
speedLRU = maxSpeed/(tempo_lru * 100)
speedLFU = maxSpeed/(tempo_lfu * 100)

finish_line = WIDTH - 50

race_started = False
race_finished = False
winner = None

def draw_text_center(surface, font, text, color, y_offset=0):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + y_offset))
    surface.blit(text_surface, text_rect)

def draw_info():
    # Tempos de execução
    time_text1 = FONT_SMALL.render(f"FIFO: {tempo_fifo:.3f} ms", True, RED)
    time_text2 = FONT_SMALL.render(f"LRU: {tempo_lru:.3f} ms", True, GREEN)
    time_text3 = FONT_SMALL.render(f"LFU: {tempo_lfu:.3f} ms", True, BLUE)
    
    screen.blit(time_text1, (20, 20))
    screen.blit(time_text2, (20, 50))
    screen.blit(time_text3, (20, 80))
    
    # Processos
    processos_text = FONT_SMALL.render(f"Processos: {processos}", True, WHITE)
    screen.blit(processos_text, (20, HEIGHT - 30))

def draw_track():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (0, yFIFO + car_height//2), (WIDTH, yFIFO + car_height//2), 2)
    pygame.draw.line(screen, WHITE, (0, yLRU + car_height//2), (WIDTH, yLRU + car_height//2), 2)
    pygame.draw.line(screen, WHITE, (0, yLFU + car_height//2), (WIDTH, yLFU + car_height//2), 2)
    pygame.draw.line(screen, YELLOW, (finish_line, 0), (finish_line, HEIGHT), 5)

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not race_started:
                race_started = True
            if event.key == pygame.K_r and race_finished:
                # Reinicia a corrida
                race_started = False
                race_finished = False
                winner = None
                xFIFO, xLRU, xLFU = 50, 50, 50
    draw_track()
    draw_info()
    
    if not race_started:
        draw_text_center(screen, FONT_LARGE, "Pressione ESPAÇO para começar a corrida", WHITE)
    elif not race_finished:
        xFIFO += speedFIFO
        xLRU += speedLRU
        xLFU += speedLFU

        if xFIFO >= finish_line or xLRU >= finish_line or xLFU >= finish_line:
            race_finished = True
            if xFIFO >= finish_line:
                winner = "FIFO"
            elif xLRU >= finish_line:
                winner = "LRU"
            else:
                winner = "LFU"
    
    pygame.draw.rect(screen, RED, (xFIFO, yFIFO, car_width, car_height))
    pygame.draw.rect(screen, GREEN, (xLRU, yLRU, car_width, car_height))
    pygame.draw.rect(screen, BLUE, (xLFU, yLFU, car_width, car_height))
    label1 = FONT_SMALL.render("FIFO", True, WHITE)
    label2 = FONT_SMALL.render("LRU", True, WHITE)
    label3 = FONT_SMALL.render("LFU", True, WHITE)
    
    screen.blit(label1, (xFIFO + car_width//2 - 15, yFIFO - 25))
    screen.blit(label2, (xLRU + car_width//2 - 15, yLRU - 25))
    screen.blit(label3, (xLFU + car_width//2 - 15, yLFU - 25))

    if race_finished:
        draw_text_center(screen, FONT_LARGE, f"{winner} VENCEU A CORRIDA!", YELLOW)
        draw_text_center(screen, FONT_MEDIUM, "Pressione R para reiniciar", WHITE, 50)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
