#tris
import pygame, time

#TODO migliora leggibilità del codice, aggiungi eventuali commenti e metti argomenti a funzioni

#stampa griglia
def disegnaGriglia():
    schermo.fill(bg)
    for x in range(1,3):
        #linee orrizonatali
        pygame.draw.line(schermo, coloreGriglia, (0, x * 100), (larghezzaSchermo, x * 100), SpessoreGriglia)
        #linee verticali
        pygame.draw.line(schermo, coloreGriglia, (x * 100,0), (x * 100, altezzaSchermo), SpessoreGriglia)
        
def disegnaCaselle(board, coloreX, coloreO, spessore):
    x_pos = 0
    for colonna in board:
        y_pos = 0
        for cella in colonna:
            if cella == 1:
                pygame.draw.line(schermo, coloreX, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), spessore)
                pygame.draw.line(schermo, coloreX, (x_pos * 100 + 15, y_pos * 100 + 85), (x_pos * 100 + 85, y_pos * 100 + 15), spessore)

            elif cella == -1:
                pygame.draw.circle(schermo, coloreO, (x_pos * 100 + 50, y_pos * 100 + 50), 38, spessore)
            y_pos += 1
        x_pos += 1

def controllaVincitore(board):
    vin = 0 #vincitore
    gmvr = False #Game Over

    y_pos = 0
    for colonna in board: 
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

#colori
bianco = (246, 255, 222)
nero = (50, 50, 50)
bg = (28, 170, 200)
coloreGriglia = (23, 145, 135)

vincitore = 0
gameOver = False


#cursore
clickSfx = pygame.mixer.Sound("assets/audio/kenney_interface-sounds/Audio/click_001.ogg")
clickSfx.set_volume(0.3)
puntatore = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Default/pointer_c_shaded.png")

#immagini
X = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Double/cross_large.png")
O = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Double/progress_empty.png")

pygame.mouse.set_visible(False)
#inizializzazione finestra
schermo = pygame.display.set_mode(size=(larghezzaSchermo, altezzaSchermo))
pygame.display.set_caption("Tris")


#loop di gioco
run = True
while run:
    #stampa la griglia
    disegnaGriglia()
    disegnaCaselle(gameBoard, nero, bianco, SpessoreGriglia)

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
               #cliccato = True
        #elif evento.type == pygame.MOUSEBUTTONUP and cliccato == True:
            #if evento.button == 1:
               #cliccato = False
            pos = pygame.mouse.get_pos()
            cellaX = pos[0]
            cellaY = pos[1]
            if gameBoard[cellaX // 100][cellaY // 100] == 0:
                gameBoard[cellaX // 100][cellaY // 100] = player
                player *= -1 #salva un pò di tempo invece di essere player 1 & 2 sono player 1 & -1
                vincitore, gameOver = controllaVincitore(gameBoard)
                if gameOver == True:
                    print(f"Il vincitore è il giocatore {vincitore}!")

        
    pygame.display.update()
pygame.quit()


