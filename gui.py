import pygame
import time
from game import Game

GRID_WIDTH, GRID_HEIGHT, MARGIN = 60, 60, 0
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


WINDOW_SIZE = [480, 480]
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

grid = [[0 for x in range(8)] for y in range(8)]


def getBoardString(row, col):
	clicked = ""
	clicked += str(boardColList[col])
	clicked += str(8-row)
	return clicked


def getBoardStringBlack(row, col):
	clicked = ""
	clicked += str(boardColList[::-1][col])
	clicked += str(row+1)
	return clicked


def getBoardCoordinates(boardString):
	col = boardString[0]
	row = int(boardString[1])
	return (boardColList.index(col), 8-row)


def getBoardCoordinatesBlack(boardString):
	col = boardString[0]
	row = int(boardString[1])
	return (boardColList[::-1].index(col), row+1)


def renderPieceOnCoordinates(row, col):
	screen.blit(pygame.image.load(
		pieceImagePath[grid[row][col]]), (col*(MARGIN+GRID_WIDTH), row*(MARGIN+GRID_WIDTH)))


# This function will render entire board
def renderBoard():
	for row in range(8):
		for col in range(8):
			color = YELLOW
			if((row+col) % 2 == 1):
				color = GREEN
			pygame.draw.rect(screen, color, [
							 (MARGIN + GRID_WIDTH) * col+MARGIN, (MARGIN + GRID_HEIGHT)*row+MARGIN, GRID_WIDTH, GRID_HEIGHT])
			try:
				renderPieceOnCoordinates(row, col)
			except KeyError:
				pass


def renderBoardBlack():
	for row in range(8):
		for col in range(8):
			color = GREEN
			if((row+col) % 2 == 1):
				color = YELLOW
			pygame.draw.rect(screen, color, [
							 (MARGIN + GRID_WIDTH) * col+MARGIN, (MARGIN + GRID_HEIGHT)*row+MARGIN, GRID_WIDTH, GRID_HEIGHT])
			try:
				renderPieceOnCoordinates(row, col)
			except KeyError:
				pass


MODE = False  # True means two player mode and False means one player
PLAYER = True or MODE  # True means white and False means black

# Main loop
g = Game()
turn = PLAYER
done, checkmate = False, False
clicks = []

while not done:
	font = pygame.font.Font('OpenSans-Regular.ttf', 32)
	screen.fill(BLACK)
	
	text1 = font.render('Single player White', 0, WHITE, BLACK)
	textRect1 = text1.get_rect()
	textRect1.center = (240, 170)
	screen.blit(text1, textRect1)
	
	text2 = font.render('Single player Black', 0, WHITE, BLACK)
	textRect2 = text2.get_rect()
	textRect2.center = (240, 240)
	screen.blit(text2, textRect2)
	
	text3 = font.render('Two players', 0, WHITE, BLACK)
	textRect3 = text3.get_rect()
	textRect3.center = (240, 310)
	screen.blit(text3, textRect3)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()

			if(240-textRect1[0]/2<pos[0]<240+textRect1[0]/2 and 170-textRect1[1]/2<pos[1]<170+textRect1[1]/2):
				MODE = False
				PLAYER = True
				done = True
			elif(240-textRect2[0]/2<pos[0]<240+textRect2[0]/2 and 240-textRect2[1]/2<pos[1]<240+textRect2[1]/2):
				MODE = False
				PLAYER = False
				done = True
			elif(240-textRect3[0]/2<pos[0]<240+textRect3[0]/2 and 310-textRect3[1]/2<pos[1]<310+textRect3[1]/2):
				MODE = True
				PLAYER = True
				done = True
	clock.tick(60)
	pygame.display.flip()

done = False
while not done:
	grid = g.board.get_pretty_board() if PLAYER else g.board.get_actual_board_black()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN and turn:
			pos = pygame.mouse.get_pos()
			col = pos[0] // (GRID_WIDTH + MARGIN)
			row = pos[1] // (GRID_HEIGHT + MARGIN)
			clicks.append(getBoardString(row, col)
						  if PLAYER else getBoardStringBlack(row, col))

	if not turn:
		g.make_best_move()
		print(str(g.board))
		print(g.board.move_list)
		if not g.get_best_move():
			print("Checkmate")
			checkmate, done = True, True
		turn = True

	if len(clicks) >= 2:
		(ci, ri), (cf, rf) = g.board.get_rowcol(
			clicks[0]),  g.board.get_rowcol(clicks[1])
		if (ri == 6 and rf == 7 and g.board.board[ri][ci] == 'P') or \
				(ri == 1 and rf == 0 and g.board.board[ri][ci] == 'p'):
			promotedTo = 'q'  # Handle promotion here
			clicks.append(promotedTo)

		if g.make_move("".join(clicks)):
			print(str(g.board))
			print(g.board.move_list)
			if not g.get_best_move():
				print("Checkmate")
				checkmate, done = True, True
			turn = MODE
		clicks = []

	screen.fill(BLACK)

	renderBoard() if PLAYER else renderBoardBlack()

	clock.tick(60)
	pygame.display.flip()

if checkmate:
	font = pygame.font.Font('OpenSans-Regular.ttf', 32)
	text = font.render('Checkmate', 0, WHITE, BLACK)
	textRect = text.get_rect()
	textRect.center = (240, 240)
	screen.blit(text, textRect)
	time.sleep(0.5)
	pygame.display.flip()
	pygame.display.update()
	time.sleep(2)

pygame.quit()
