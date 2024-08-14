#tris
import pygame

pygame.init()

player = 1
larghezzaSchermo = 300
altezzaSchermo = 300

SpessoreGriglia = 6

cliccato = False
pos = []
gameBoard = [[0,0,0],
             [0,0,0],
             [0,0,0]]

#cursore
clickSfx = pygame.mixer.Sound("assets/audio/kenney_interface-sounds/Audio/click_001.ogg")
clickSfx.set_volume(0.05)
puntatore = pygame.image.load("assets/cursor/kenney_cursor-pack/PNG/Outline/Default/pointer_c_shaded.png")

#immagini
X = pygame.image.load("C:/Users/ludom/Desktop/dev/python/tris/assets/cursor/kenney_cursor-pack/PNG/Outline/Double/cross_large.png")
O = pygame.image.load("C:/Users/ludom/Desktop/dev/python/tris/assets/cursor/kenney_cursor-pack/PNG/Outline/Double/progress_empty.png")

pygame.mouse.set_visible(False)
#inizializzazione finestra
schermo = pygame.display.set_mode(size=(larghezzaSchermo, altezzaSchermo))
pygame.display.set_caption("Tris")

#stampa griglia
def disegnaGriglia():
    bg = (255, 255, 200)
    coloreGriglia = (250, 200, 152)
    schermo.fill(bg)
    for x in range(1,3):
        #linee orrizonatali
        pygame.draw.line(schermo, coloreGriglia, (0, x * 100), (larghezzaSchermo, x * 100), SpessoreGriglia)
        #linee verticali
        pygame.draw.line(schermo, coloreGriglia, (x * 100,0), (x * 100, altezzaSchermo), SpessoreGriglia)
        
def disegnaCaselle(board, coloreX, coloreO):
    pass

#loop di gioco
run = True
while run:
    #stampa la griglia
    disegnaGriglia()
    puntatoreXy = pygame.mouse.get_pos()
    schermo.blit(puntatore,puntatoreXy)

    for evento in pygame.event.get():
        #chiude il gioco se l'utente chiude la finestra
        if evento.type == pygame.QUIT:
            run = False
        #chiude il gioco se l'utente scrive esc
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                run = False

        if evento.type == pygame.MOUSEBUTTONDOWN and cliccato == False:
            if evento.button == 1:
               clickSfx.play()
               cliccato = True
        if evento.type == pygame.MOUSEBUTTONUP == cliccato == True:
            if evento.button == 1:
               cliccato = False
               pos = pygame.mouse.get_pos()
               cellaX = pos[0]
               cellaY = pos[1]
               if gameBoard[cellaX // 100][cellaY // 100] == 0:
                   gameBoard[cellaX // 100][cellaY // 100] = player
                   player *= -1 #salva un pò di tempo invece di essere player 1 & 2 sono player 1 & -1
                   
                   

               
    pygame.display.update()

pygame.quit()


