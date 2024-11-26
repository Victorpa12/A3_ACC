# Dentro do loop principal, onde verificamos se o jogador fechou uma célula:
if ccell:
    index = ccell.index
    if not ccell.winner:
        pygame.draw.circle(win, RED, (ccell.rect.centerx, ccell.rect.centery), 2)

    # Esta variável acumulará os pontos ganhos neste turno
    points_this_turn = 0

    # Verifica e define os lados como "fechados" ao fazer o movimento
    if up and not ccell.sides[0]:
        ccell.sides[0] = True
        if index - ROWS >= 0:            
            cells[index-ROWS].sides[2] = True
        next_turn = True

    if right and not ccell.sides[1]:
        ccell.sides[1] = True
        if (index + 1) % COLS > 0:
            cells[index+1].sides[3] = True
        next_turn = True

    if bottom and not ccell.sides[2]:
        ccell.sides[2] = True
        if index + ROWS < len(cells):            
            cells[index+ROWS].sides[0] = True
        next_turn = True

    if left and not ccell.sides[3]:
        ccell.sides[3] = True
        if (index % COLS) > 0:
            cells[index-1].sides[1] = True
        next_turn = True

    # Após fechar os lados, verifique se a célula foi fechada e conte os pontos
    for cell in cells:
        points = cell.checkwin(player)
        points_this_turn += points  # Acumula os pontos para este turno

    # Atualiza a pontuação do jogador
    fillcount += points_this_turn
    if player == 'X':
        p1_score += points_this_turn
    else:
        p2_score += points_this_turn

    # Checa o final do jogo
    if fillcount == ROWS * COLS:
        print(p1_score, p2_score)
        gameover = True

    # Alterna o turno caso o jogador não tenha fechado nenhum quadrado
    if points_this_turn == 0:
        turn = (turn + 1) % len(players)
        player = players[turn]