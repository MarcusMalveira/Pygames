import pygame;

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Meu primeiro Jogo")
x = 400
y = 300
tamanho = 3
velocidade = 0.5


rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        y -= velocidade
    if teclas[pygame.K_s]:
        y += velocidade
    if teclas[pygame.K_a]:
        x -= velocidade
    if teclas[pygame.K_d]:
        x += velocidade

    if x < 0:
        x = 0
    if x > largura - tamanho:
        x = largura - tamanho
    if y < 0:
        y = 0
    if y > altura - tamanho:
        y = altura - tamanho
        

    tela.fill((30, 30, 30))

    pygame.draw.rect(
        tela,
        (255, 255, 255),
        (x, y, tamanho, tamanho)
    )

    pygame.display.update()

pygame.quit()