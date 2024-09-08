#tris
import pygame, random


def disegnaMenu(piano, coloreBg, fontText, immgColore, rettangoloColore, larghezza, altezza, rettangolo1, rettangolo2):
    schermo.fill(coloreBg)
    immVsPLayer = fontText.render("Standard", True, immgColore)
    pygame.draw.rect(piano, rettangoloColore, rettangolo1, border_radius = 10)
    piano.blit(immVsPLayer, (larghezza // 2 - 40, altezza // 2 - 43))
    
    immVsComputer = fontText.render("VS Computer", True, immgColore)
    pygame.draw.rect(piano, rettangoloColore, rettangolo2, border_radius = 10)
    piano.blit(immVsComputer, (larghezza // 2 - 52, altezza // 2 + 17))


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
    elif board[0][0] + board[1][1] + board[2][2] == -3 or board[2][0] + board[1][1] + board[0][2] == -3:
        vin = 2
        gmvr = True

    return vin, gmvr


def disegnaVincitore(giocaAncora, testo, fontText, immgColore, rettangoloColore, piano, larghezza, altezza, rettangolo):
    immVittoria = fontText.render(testo, True, immgColore)
    pygame.draw.rect(piano, rettangoloColore, (larghezza // 2 - 100, altezza // 2 - 60, 200, 50), border_radius = 10)
    piano.blit(immVittoria, (larghezza // 2 - 90, altezza // 2 - 45))
    
    pygame.draw.rect(piano, rettangoloColore, rettangolo, border_radius = 10)
    piano.blit(giocaAncora, (larghezza // 2 - 35, altezza // 2 + 10))


def turnoComputer(board):
    #se l'algoritmo vede che il giocatore sta per vincere piazza la sua casella in modo da interrompere la riga altrimenti piazza casualmente

    indiceCellaRighe = 0
    IndiceColonna = 0
    piazzato = False
    for colonna in board:
        riga = [board[0][indiceCellaRighe], board[1][indiceCellaRighe], board[2][indiceCellaRighe]]
        #Controlla colonne
        if sum(colonna) == 2 and not piazzato:
            indiceCellaColonne = 0
            for cella in colonna:
                if cella == 0:
                    board[IndiceColonna][indiceCellaColonne] = -1
                    piazzato = True
                indiceCellaColonne += 1
    
        #Controlla righe
        elif sum(riga) == 2 and not piazzato:
            indiceRiga = 0
            for cella in riga:
                if cella == 0:
                    board[indiceRiga][indiceCellaRighe] = -1
                    piazzato = True             
                indiceRiga += 1
    
        indiceCellaRighe += 1
        IndiceColonna += 1

    #controlla croci
    #croce 1
    if board[0][0] + board[1][1] + board[2][2] == 2 and not piazzato:
        if board[0][0] == 0:
            board[0][0] = -1
            piazzato = True
        elif board[1][1] == 0:
            board[1][1] = -1
            piazzato = True
        elif board[2][2] == 0:
            board[2][2] = -1
            piazzato = True
    
    #croce 2
    elif board[2][0] + board[1][1] + board[0][2] == 2 and not piazzato:
        if board[2][0] == 0:
            board[2][0] = -1
            piazzato = True
        elif board[1][1] == 0:
            board[1][1] = -1
            piazzato = True
        elif board[0][2] == 0:
            board[0][2] = -1
            piazzato = True

    #se non è stato piazzato nulla, piazza casualmente

    if not piazzato:
        #controlla che la tabella non sia piena
        pieno = True
        for colonna in board:
            for cella in colonna:
                if cella == 0:
                    pieno = False  

        while not piazzato and not pieno:
            colonna = random.randint(0, 2)
            cella = random.randint(0, 2)
            if board[colonna][cella] == 0:
                board[colonna][cella] = -1
                piazzato = True


#main
pygame.init()

#Gioco
player = 1
pos = []
gameBoard = [[0,0,0],
             [0,0,0],
             [0,0,0]]
vincitore = 0
gameOver = False
modalita = 0

#colori
beige = (246, 255, 222)
nero = (50, 50, 50)
blu = (92, 106, 128)
bianco = (255, 255, 255)
verde = (0, 143, 57)
coloreBackground = (28, 170, 200)
coloreGriglia = (21, 130, 153)

#aspetto
font = pygame.font.SysFont(None, 25)
SpessoreGriglia = 8
larghezzaSchermo = 300
altezzaSchermo = 300

#rettangoli / pulsanti
rettGiocaAncora =  pygame.Rect(larghezzaSchermo // 2 - 38, altezzaSchermo // 2 + 2, 75, 75)
rettVsGiocatore = pygame.Rect(larghezzaSchermo // 2 - 100, altezzaSchermo // 2 - 60, 200, 50)
rettVsComputer = pygame.Rect(larghezzaSchermo // 2 - 100, altezzaSchermo // 2 + 2, 200, 50)

#audio
volume = 1
clickSfx = pygame.mixer.Sound("assets/audio/kenney_interface-sounds/Audio/click_001.ogg")
switchSfx = pygame.mixer.Sound("assets/audio/kenney_interface-sounds/Audio/switch_002.ogg")
winSfx = pygame.mixer.Sound("assets/audio/jingle_win_synth_00.wav")
loseSfx = pygame.mixer.Sound("assets/audio/kenney_digital-audio/Audio/spaceTrash2.ogg")

clickSfx.set_volume(volume)
switchSfx.set_volume(volume)
winSfx.set_volume(volume)
loseSfx.set_volume(volume)

riprodotto = False

#immagine finestra
icona = pygame.image.load("assets/icona/icon.png")

#immagini
icona = pygame.image.load("assets/icona/icon.png")
immGiocaAncora = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Double/rotate_cw.png")
puntatore = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Default/pointer_c_shaded.png")


#inizializzazione finestra
schermo = pygame.display.set_mode(size=(larghezzaSchermo, altezzaSchermo))
pygame.display.set_caption("Tris | menù")
pygame.display.set_icon(icona)
pygame.mouse.set_visible(False)


#loop di gioco
run = True
while run:
    if modalita == 0:
        #menu
        disegnaMenu(schermo, coloreBackground, font, bianco, blu, larghezzaSchermo, altezzaSchermo, rettVsGiocatore, rettVsComputer)
        for evento in pygame.event.get():
            #chiude il gioco se l'utente chiude la finestra
            if evento.type == pygame.QUIT:
                run = False
            #chiude il gioco se l'utente preme esc
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    run = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rettVsGiocatore.collidepoint(pos):
                    modalita = 1
                    pygame.display.set_caption("Tris | standard")
                elif rettVsComputer.collidepoint(pos):
                    pygame.display.set_caption("Tris | VS Computer")
                    modalita = 2 
                switchSfx.play()
                                   
    else:
        #stampa la griglia
        disegnaGriglia(schermo, coloreGriglia, larghezzaSchermo, altezzaSchermo, SpessoreGriglia, coloreBackground) 
        disegnaCaselle(gameBoard, nero, beige, SpessoreGriglia, schermo)  
                
        #logica  principale del gioco
        for evento in pygame.event.get():
            #chiude il gioco se l'utente chiude la finestra
            if evento.type == pygame.QUIT:
                run = False
            #chiude il gioco se l'utente preme esc
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    run = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                clickSfx.play()
                pos = pygame.mouse.get_pos()
                cellaX = pos[0]
                cellaY = pos[1]
                if gameBoard[cellaX // 100][cellaY // 100] == 0:
                    gameBoard[cellaX // 100][cellaY // 100] = player
                    if modalita == 1:
                        player *= -1 #salva un pò di tempo invece di essere player 1 & 2 sono player 1 & -1
                    elif modalita == 2:
                        turnoComputer(gameBoard)  
                vincitore, gameOver = controllaVincitore(gameBoard)

        #gameover
        if gameOver == True:

            if vincitore == 0:
                testoGameOver = "Pari, nessuno ha vinto"
                if not riprodotto:
                    loseSfx.play()
                    riprodotto = True
            else:
                testoGameOver = f"Il giocatore {vincitore} ha vinto!"
                if not riprodotto and vincitore == 2 and modalita == 2:
                    loseSfx.play()
                    riprodotto = True
                elif not riprodotto:
                    winSfx.play()
                    riprodotto = True

            disegnaVincitore(immGiocaAncora, testoGameOver, font, bianco, blu, schermo, larghezzaSchermo, altezzaSchermo, rettGiocaAncora) 
        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rettGiocaAncora.collidepoint(pos):
                    pygame.display.set_caption("Tris | menù")
                    gameBoard = [[0,0,0],
                                 [0,0,0],
                                 [0,0,0]]
                    player = 1
                    vincitore = 0
                    gameOver = False
                    modalita = 0
                    riprodotto = False
                    switchSfx.play()

    #mouse
    pos = pygame.mouse.get_pos()
    schermo.blit(puntatore, pos)
        
    pygame.display.update()
pygame.quit()


