import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("desenho com mouse")

pontos = []

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    

    botoes_mouse = pygame.mouse.get_pressed()

    if botoes_mouse[0]:
        posicao = pygame.mouse.get_pos()
        pontos.append(posicao)

    tela.fill((30, 30, 30))

    for i in range (1, len(pontos)):
        pygame.draw.line( tela, (255,255,255), pontos[i - 1], pontos[i], 3)
        
    pygame.display.update()

pygame.quit()