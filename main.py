import pygame

GRID_WIDTH, GRID_HEIGHT, MARGIN = 50, 50, 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 253, 228) 
GREEN = (151, 179, 120)

boardColList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pieceImagePath = {
	'P': 'assets/wPawn.png',
	'R': 'assets/wRook.png',
	'N': 'assets/wKnight.png',
	'B': 'assets/wBishop.png',
	'Q': 'assets/wQueen.png',
	'K': 'assets/wKing.png',
	'p': 'assets/bPawn.png',
	'r': 'assets/bRook.png',
	'n': 'assets/bKnight.png',
	'b': 'assets/bBishop.png',
	'q': 'assets/bQueen.png',
	'k': 'assets/bKing.png'
}

pygame.init()

WINDOW_SIZE = [445, 445]
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

grid = [[0 for x in range(8)] for y in range(8)]

def getBoardString(row, col):
	clicked = ""
	clicked += str(boardColList[col])
	clicked += str(8-row)
	return clicked

def getBoardCoordinates(boardString):
	col = boardString[0]
	row = int(boardString[1])
	return (boardColList.index(col), 8-row)

def renderPieceOnCoordinates(row, col):
	screen.blit(pygame.image.load(pieceImagePath[grid[row][col]]), (col*(MARGIN+GRID_WIDTH), row*(MARGIN+GRID_WIDTH)))

#This function will render entire board
def renderBoard():
	for row in range(8) :
		for col in range(8):
			color = YELLOW
			if((row+col)%2 == 1):
				color = GREEN
			pygame.draw.rect(screen, color, [(MARGIN + GRID_WIDTH)* col+MARGIN, (MARGIN + GRID_HEIGHT)*row+MARGIN, GRID_WIDTH, GRID_HEIGHT])
			try:
				renderPieceOnCoordinates(row, col)
			except KeyError:
				pass
done = False

# grid[0][2] = 'k'                                 #Tasting
# grid[7][4] = 'Q'
while not done :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			col = pos[0] // (GRID_WIDTH + MARGIN)
			row = pos[1] // (GRID_HEIGHT + MARGIN)
			print(getBoardCoordinates(getBoardString(row, col)))

	screen.fill(BLACK)

	renderBoard()

	clock.tick(60)
	pygame.display.flip()
pygame.quit()
