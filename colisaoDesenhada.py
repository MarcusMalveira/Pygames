import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("desenho com mouse")

# JOGADOR
x = 400
y = 300
z = 0

velocidade_z = 0
gravidade = 0.2
forca_pulo = 6

tamanho = 10
velocidade = 2

# PAREDES
pontos = []
obstaculos = []
espessura = 5

rodando = True
clock = pygame.time.Clock()

while rodando:

    # -------------------
    # EVENTOS
    # -------------------

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # -------------------
    # MOUSE
    # -------------------

    botoes_mouse = pygame.mouse.get_pressed()

    if botoes_mouse[0]:

        posicao = pygame.mouse.get_pos()

        if len(pontos) > 0:

            ponto_anterior = pontos[-1]

            dx = posicao[0] - ponto_anterior[0]
            dy = posicao[1] - ponto_anterior[1]

            distancia = max(abs(dx), abs(dy))

            if distancia > 0:

                for i in range(distancia + 1):

                    x_linha = ponto_anterior[0] + dx * i / distancia
                    y_linha = ponto_anterior[1] + dy * i / distancia

                    obstaculo = pygame.Rect(
                        int(x_linha) - espessura // 2,
                        int(y_linha) - espessura // 2,
                        espessura,
                        espessura
                    )

                    obstaculos.append(obstaculo)

        pontos.append(posicao)

    # -------------------
    # TECLADO
    # -------------------

    teclas = pygame.key.get_pressed()

    # -------------------
    # MOVIMENTO HORIZONTAL
    # -------------------

    if teclas[pygame.K_a]:
        x -= velocidade

    if teclas[pygame.K_d]:
        x += velocidade

    jogador = pygame.Rect(x, y, tamanho, tamanho)

    if z <= 2:

        for obstaculo in obstaculos:

            if jogador.colliderect(obstaculo):

                if teclas[pygame.K_d]:
                    jogador.right = obstaculo.left
                    x = jogador.x

                if teclas[pygame.K_a]:
                    jogador.left = obstaculo.right
                    x = jogador.x

    # -------------------
    # MOVIMENTO VERTICAL
    # -------------------

    if teclas[pygame.K_w]:
        y -= velocidade

    if teclas[pygame.K_s]:
        y += velocidade

    jogador = pygame.Rect(x, y, tamanho, tamanho)

    if z <= 2:

        for obstaculo in obstaculos:

            if jogador.colliderect(obstaculo):

                if teclas[pygame.K_s]:
                    jogador.bottom = obstaculo.top
                    y = jogador.y

                if teclas[pygame.K_w]:
                    jogador.top = obstaculo.bottom
                    y = jogador.y

    # -------------------
    # PULO
    # -------------------

    if teclas[pygame.K_SPACE] and z == 0:
        velocidade_z = forca_pulo

    if z > 0 or velocidade_z != 0:

        z += velocidade_z
        velocidade_z -= gravidade

        if z <= 0:
            z = 0
            velocidade_z = 0

    # -------------------
    # LIMITES DA TELA
    # -------------------

    if x < 0:
        x = 0

    if x > largura - tamanho:
        x = largura - tamanho

    if y < 0:
        y = 0

    if y > altura - tamanho:
        y = altura - tamanho

    # -------------------
    # DESENHO
    # -------------------

    tela.fill((255, 255, 255))

    # paredes
    for i in range(1, len(pontos)):

        pygame.draw.line(
            tela,
            (0, 255, 0),
            pontos[i - 1],
            pontos[i],
            espessura
        )

    # sombra
    pygame.draw.ellipse(
        tela,
        (80, 80, 80),
        (x, y + tamanho, tamanho, 4)
    )

    # jogador
    pygame.draw.rect(
        tela,
        (255, 0, 0),
        (x, y - z, tamanho, tamanho)
    )

    pygame.display.update()
    clock.tick(60)

pygame.quit()