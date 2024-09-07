#tris
import pygame, time

#stampa griglia
def disegnaGriglia(piano, colore, larghezzaPiano, altezzaPiano, spessore, coloreBg):
    schermo.fill(coloreBg)
    for x in range(1,3):
        #linee orrizonatali
        pygame.draw.line(piano, colore, (0, x * 100), (larghezzaPiano, x * 100), spessore)
        #linee verticali
        pygame.draw.line(piano, colore, (x * 100,0), (x * 100, altezzaPiano), spessore)
        
def disegnaCaselle(board, coloreX, coloreO, spessore, piano):
    x_pos = 0
    for colonna in board:
        y_pos = 0
        for cella in colonna:
            if cella == 1:
                pygame.draw.line(piano, coloreX, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), spessore)
                pygame.draw.line(piano, coloreX, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), spessore)

            elif cella == -1:
                pygame.draw.circle(piano, coloreO, (x_pos * 100 + 50, y_pos * 100 + 50), 38, spessore)
            y_pos += 1
        x_pos += 1

def controllaVincitore(board):
    vin = 0 #vincitore
    gmvr = False #Game Over
    
    y_pos = 0
    somma = 0 
    for colonna in board:
        for cella in colonna:
            #controlla parità
            if cella != 0:
                somma += 1
                if somma == 9:
                    gmvr = True

        #controlla colonne
        if sum(colonna) == 3:
            vin = 1
            gmvr = True
        elif sum(colonna) == -3:
            vin = 2
            gmvr = True
        #controlla righe
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == 3:
            vin = 1
            gmvr = True
        elif board[0][y_pos] + board[1][y_pos] + board[2][y_pos] == -3:
            vin = 2
            gmvr = True
        y_pos += 1
    
    #controlla croci
    if board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == 3:
        vin = 1
        gmvr = True
    elif board[0][0] + board[1][1] + board[2][2] == 3 or board[2][0] + board[1][1] + board[0][2] == -3:
        vin = 1
        gmvr = True

    return vin, gmvr


def disegnaVincitore(giocaAncora, testo, fontText, immgColore, rettangoloColore, piano, larghezza, altezza, rettangolo):
    immVittoria = fontText.render(testo, True, immgColore)
    pygame.draw.rect(piano, rettangoloColore, (larghezza // 2 - 100, altezza // 2 - 60, 200, 50), border_radius = 10)
    piano.blit(immVittoria, (larghezza // 2 - 90, altezza // 2 - 45))
    
    pygame.draw.rect(piano, rettangoloColore, rettangolo, border_radius = 10)
    piano.blit(giocaAncora, (larghezza // 2 - 35, altezza // 2 + 10))


#main
pygame.init()

player = 1
larghezzaSchermo = 300
altezzaSchermo = 300

SpessoreGriglia = 8

cliccato = False
pos = []
gameBoard = [[0,0,0],
             [0,0,0],
             [0,0,0]]
vincitore = 0
gameOver = False

#colori
beige = (246, 255, 222)
nero = (50, 50, 50)
blu = (92, 106, 128)
bianco = (255, 255, 255)
verde = (0, 143, 57)
coloreBackground = (28, 170, 200)
coloreGriglia = (21, 130, 153)

#font
font = pygame.font.SysFont(None, 25)

#rettngolo
rettGiocaAncora =  pygame.Rect(larghezzaSchermo // 2 - 38, altezzaSchermo // 2 + 2, 75, 75)

#audio
volume = 0.3
clickSfx = pygame.mixer.Sound("assets/audio/kenney_interface-sounds/Audio/click_001.ogg")
switchSfx = pygame.mixer.Sound("assets/audio/kenney_interface-sounds/Audio/switch_002.ogg")

clickSfx.set_volume(volume)
switchSfx.set_volume(volume)

#immagine finestra
icona = pygame.image.load("assets/icona/icon.png")

#immagini
icona = pygame.image.load("assets/icona/icon.png")
immGiocaAncora = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Double/rotate_cw.png")
puntatore = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Default/pointer_c_shaded.png")



#inizializzazione finestra
schermo = pygame.display.set_mode(size=(larghezzaSchermo, altezzaSchermo))
pygame.display.set_caption("Tris")
pygame.display.set_icon(icona)
pygame.mouse.set_visible(False)


#loop di gioco
run = True
while run:

  
    #stampa la griglia
    disegnaGriglia(schermo, coloreGriglia, larghezzaSchermo, altezzaSchermo, SpessoreGriglia, coloreBackground) 
    disegnaCaselle(gameBoard, nero, beige, SpessoreGriglia, schermo)

    if gameOver == True:
        if vincitore == 0:
            testoGameOver = "Pari, nessuno ha vinto"
        else:
            testoGameOver = f"il giocatore {vincitore} ha vinto!"

        disegnaVincitore(immGiocaAncora, testoGameOver, font, bianco, blu, schermo, larghezzaSchermo, altezzaSchermo, rettGiocaAncora) 
        
        if evento.type == pygame.MOUSEBUTTONDOWN and cliccato == False:
            cliccato = True
        elif evento.type == pygame.MOUSEBUTTONUP and cliccato == True:
            cliccato = False
            pos = pygame.mouse.get_pos()
            if rettGiocaAncora.collidepoint(pos):
                gameBoard = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
                vincitore = 0
                gameOver = False
                switchSfx.play()
                


    #mouse
    pos = pygame.mouse.get_pos()
    schermo.blit(puntatore, pos)
    for evento in pygame.event.get():
        #chiude il gioco se l'utente chiude la finestra
        if evento.type == pygame.QUIT:
            run = False
        #chiude il gioco se l'utente preme esc
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                run = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and gameOver == False:
            clickSfx.play()
            pos = pygame.mouse.get_pos()
            cellaX = pos[0]
            cellaY = pos[1]
            if gameBoard[cellaX // 100][cellaY // 100] == 0:
                gameBoard[cellaX // 100][cellaY // 100] = player
                player *= -1 #salva un pò di tempo invece di essere player 1 & 2 sono player 1 & -1
                vincitore, gameOver = controllaVincitore(gameBoard)
        
    pygame.display.update()
pygame.quit()


