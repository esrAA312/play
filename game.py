from flask import Flask, render_template
import pygame
import numpy as np
import random
import math
from pygame.locals import *


# Initialize the Flask application.
app = Flask(__name__)

# Define a list of game dictionaries for the first category.
games = [

{
        'id': 1,
        'name': 'Connect Four',
        'icon': 'count.png',
    },

        {
        'id': 2 ,
        'name': 'Tic Tac Toe',
        'icon': 'tic-tac-toe.png'
    },

        {
        'id': 3,
        'name': 'scissor&paper&rock',
        'icon': 'rock-paper-scissors.png'
    },

{
        'id': 7,
        'name': 'ping-pong',
        'icon': 'ping-pong.png'
    }
]
# Define a second list of game dictionaries for the second category
Games2 = [

        {
        'id': 4 ,
        'name': 'Tic Tac Toe',
        'icon': 'tic-tac-toe.png'
    },


        {
        'id': 5,
        'name': 'Connect Four',
        'icon': 'count.png'
    },



        {
        'id': 6,
        'name': 'scissor&paper&rock',
        'icon': 'rock-paper-scissors.png'
    },
    {
        'id': 8,
        'name': 'ping-pong',
        'icon': 'ping-pong.png'
    },
]

def play_connect_four():

    # Define colors
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    CYAN = (0, 255, 255)
    

    # Define the number of rows and columns
    ROW_COUNT = 6
    COLUMN_COUNT = 6

    def create_board():
        board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
        board[row][col] = piece

    def is_valid_location(board, col):
        return board[ROW_COUNT-1][col] == 0

    def get_next_open_row(board, col):
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(board):
        print(np.flip(board, 0))

    def winning_move(board, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == 1:
                    pygame.draw.circle(screen,YELLOW , (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == 2: 
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()


    board = create_board()
    print_board(board)
    game_over = False
    turn = 0

    pygame.init()
    icon = pygame.image.load("static/count.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("CONNET 4")

    SQUARESIZE = 60

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE


    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 30)

# This loop will continue to run as long as the game is not end.
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game_over = True
               pygame.quit
               break

# a mouse motion event 
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
                else: 
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, CYAN)
                            screen.blit(label, (40,10))
                            game_over = True


                # Ask for Player 2 Input
                else:				
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, CYAN)
                            screen.blit(label, (40,10))
                            game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(2000)
    pygame.quit()
def play_tic_tac_toe():

   # Define colors
    BLACK = (0, 0, 0)
    beige_rgb = (225, 220, 130)
    YELLOW = (255, 215, 0)

    # Initialize Pygame
    pygame.init()
    icon = pygame.image.load("static/tic-tac-toe.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Tic Tac Toe")

    # Set up the screen
    WIDTH, HEIGHT = 500, 500
    ROWS, COLS = 3, 3
    SQUARE_SIZE = WIDTH // COLS
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    

    # Fonts
    FONT = pygame.font.SysFont(None, 60)

    # Create the board
    board = np.zeros((ROWS, COLS))

    def draw_board():
        screen.fill(beige_rgb)
        # Draw lines
        for i in range(1, ROWS):
            pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE),15)
        for i in range(1, COLS):
            pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT),15)
        # Draw pieces
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 1:
                    pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),
                                     (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE * 3 // 4), 15)
                    pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE * 3 // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4),
                                     (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE * 3 // 4), 15)
                elif board[row][col] == 2:
                    pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3, 15)
                    
    def check_winner():
        # Check rows
        for row in range(ROWS):
            if board[row][0] == board[row][1] == board[row][2] != 0:
                return board[row][0]
        # Check columns
        for col in range(COLS):
            if board[0][col] == board[1][col] == board[2][col] != 0:
                return board[0][col]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != 0:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return board[0][2]
        # Check if the board is full
        if not 0 in board:
            return 0
        return None

    turn = 1  # Player 1 starts
    game_over = False
    # This loop will continue to run as long as the game is not over.
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                break
            #Mouse Handling
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if turn == 1:
                    col = event.pos[0] // SQUARE_SIZE
                    row = event.pos[1] // SQUARE_SIZE
                    if board[row][col] == 0:
                        board[row][col] = 1
                        turn = 2
                else:
                    col = event.pos[0] // SQUARE_SIZE
                    row = event.pos[1] // SQUARE_SIZE
                    if board[row][col] == 0:
                        board[row][col] = 2
                        turn = 1
        if game_over:
            break
        draw_board()
        winner = check_winner()
        if winner is not None:
            if winner == 0:
                text = FONT.render("It's a draw!", True, YELLOW, BLACK)
            else:
                text = FONT.render(f"Player {winner} wins!", True, YELLOW, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(3000)
            game_over = True
        
        pygame.display.update()

    pygame.quit()
def SPR():
    pygame.init()

    # Set up the screen
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rock Paper Scissors")
    icon = pygame.image.load("static/rock-paper-scissors.png")
    pygame.display.set_icon(icon)

    # Load images
    rock_img = pygame.image.load("static/rock-user1.png")
    paper_img = pygame.image.load("static/paper-user2.png")
    scissors_img = pygame.image.load("static/scissors-user3.png")
    rock_comp_img = pygame.image.load("static/rock1.png")
    paper_comp_img = pygame.image.load("static/paper2.png")
    scissors_comp_img = pygame.image.load("static/scissors3.png")

    # Game variables
    player1_choice = None
    player2_choice = None
    winner = None

    # Function to check winner
    def check_winner(player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return None
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
            (player1_choice == 'paper' and player2_choice == 'rock') or \
            (player1_choice == 'scissors' and player2_choice == 'paper'):
            return "Player 1"
        else:
            return "Player 2"

    # Main game loop
    running = True
    while running:
        screen.fill((102, 150, 255))

    
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
               pygame.quit()
               return 0
        # keybard handling
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player1_choice = 'rock'
                elif event.key == pygame.K_2:
                    player1_choice = 'paper'
                elif event.key == pygame.K_3:
                    player1_choice = 'scissors'
                elif event.key == pygame.K_r:
                    player2_choice = 'rock'
                elif event.key == pygame.K_p:
                    player2_choice = 'paper'
                elif event.key == pygame.K_s:
                    player2_choice = 'scissors'
            
        # Blit images
        screen.blit(rock_img, (100, 300))
        screen.blit(paper_img, (300, 300))
        screen.blit(scissors_img, (500, 300))
        screen.blit(rock_comp_img, (100, 100))
        screen.blit(paper_comp_img, (300, 100))
        screen.blit(scissors_comp_img, (500, 100))

        # Check winner
        if player1_choice and player2_choice:
            winner = check_winner(player1_choice, player2_choice)
            font = pygame.font.SysFont(None, 100)
            text = font.render("Winner: {}".format(winner or "Tie!"), True, (0, 0, 0),(225, 225,225))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 50))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        # Update display
        pygame.display.flip()
        pygame.time.wait(100)
        pygame.display.update()
    # Quit Pygame
    pygame.quit()

def SPRAI():
    pygame.init()

    # Set up the screen
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rock Paper Scissors")
    icon = pygame.image.load("static/rock-paper-scissors.png")
    pygame.display.set_icon(icon)

    # Load images
    rock_img = pygame.image.load("static/rock-user.png")
    paper_img = pygame.image.load("static/paper-user.png")
    scissors_img = pygame.image.load("static/scissors-user.png")
    rock_comp_img = pygame.image.load("static/rock.png")
    paper_comp_img = pygame.image.load("static/paper.png")
    scissors_comp_img = pygame.image.load("static/scissors.png")

    # Game variables
    def ai_choose():
        return random.choice(['rock', 'paper', 'scissors'])

    player1_choice = None
    player2_choice = ai_choose()
    winner = None

    # Function to check winner
    def check_winner(player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return "Tie"
        elif (player1_choice == 'rock' and player2_choice == 'scissors') or \
             (player1_choice == 'paper' and player2_choice == 'rock') or \
             (player1_choice == 'scissors' and player2_choice == 'paper'):
            return "Player"
        else:
            return "AI"

    # Main game loop
    running = True
    while running:
        screen.fill((102, 150, 255))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return 0

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player1_choice = 'rock'
                elif event.key == pygame.K_2:
                    player1_choice = 'paper'
                elif event.key == pygame.K_3:
                    player1_choice = 'scissors'

        if not running:
            break

        # Blit images
        screen.blit(rock_img, (100, 300))
        screen.blit(paper_img, (300, 300))
        screen.blit(scissors_img, (500, 300))
        screen.blit(rock_comp_img, (100, 100))
        screen.blit(paper_comp_img, (300, 100))
        screen.blit(scissors_comp_img, (500, 100))

        # Display instructions
        tx = "Press 1 for rock, 2 for paper, 3 for scissors"
        font = pygame.font.SysFont(None, 40)
        te = font.render(tx, True, (0, 0, 0), (225, 225, 225))
        screen.blit(te, (WIDTH // 2 - te.get_width() // 2, HEIGHT // 2 - te.get_height() // 2))

        # Check winner
        if player1_choice:
            winner = check_winner(player1_choice, player2_choice)
            font = pygame.font.SysFont(None, 100)
            text = font.render("Winner: {}".format(winner), True, (0, 0, 0), (225, 225, 225))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 50))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        # Update display
        pygame.display.flip()
        pygame.time.wait(100)

    # Quit Pygame
    pygame.quit()
    

def play_connect_fourAI():
    # Define colors
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    CYAN = (0, 255, 255)
    # Define the number of rows and columns 
    ROW_COUNT = 6
    COLUMN_COUNT = 6

    PLAYER = 0
    AI = 1
    # Define constants for the board cell states.
    EMPTY = 0
    PLAYER_PIECE = 1
    AI_PIECE = 2

    WINDOW_LENGTH = 4

    def create_board():
        # Creates and returns a game board initialized with zeros.
        board = np.zeros((ROW_COUNT,COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
       # Places a piece on the game board at the specified location.
        board[row][col] = piece

    def is_valid_location(board, col):
        #Checks if a column on the game board is valid for placing a new piece.
        return board[ROW_COUNT-1][col] == 0

    def get_next_open_row(board, col):
        #Finds the next available row in a specified column for placing a piece.
        for r in range(ROW_COUNT):
            if board[r][col] == 0:
                return r

    def print_board(board):
        # Prints the game board 
        print(np.flip(board, 0))

    def winning_move(board, piece):
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True

    def evaluate_window(window, piece):
        score = 0
        opp_piece = PLAYER_PIECE
        if piece == PLAYER_PIECE:
            opp_piece = AI_PIECE

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(board, piece):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(COLUMN_COUNT-3):
                window = row_array[c:c+WINDOW_LENGTH]
                score += evaluate_window(window, piece)

        ## Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(ROW_COUNT-3):
                window = col_array[r:r+WINDOW_LENGTH]
                score += evaluate_window(window, piece)

        ## Score posiive sloped diagonal
        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
                score += evaluate_window(window, piece)

        for r in range(ROW_COUNT-3):
            for c in range(COLUMN_COUNT-3):
                window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
                score += evaluate_window(window, piece)

        return score

    def is_terminal_node(board):
        return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0
    #minimax algorithm with alpha-beta pruning to determine the best move.
    def minimax(board, depth, alpha, beta, maximizingPlayer):
        valid_locations = get_valid_locations(board)
        is_terminal = is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(board, AI_PIECE):
                    return (None, 100000000000000)
                elif winning_move(board, PLAYER_PIECE):
                    return (None, -10000000000000)
                else: # Game is over, no more valid moves
                    return (None, 0)
            else: # Depth is zero
                return (None, score_position(board, AI_PIECE))
        if maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, AI_PIECE)
                new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        else: # Minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = board.copy()
                drop_piece(b_copy, row, col, PLAYER_PIECE)
                new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def get_valid_locations(board):
        valid_locations = []
        for col in range(COLUMN_COUNT):
            if is_valid_location(board, col):
                valid_locations.append(col)
        return valid_locations

   

    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if board[r][c] == PLAYER_PIECE:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == AI_PIECE: 
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        pygame.display.update()

    board = create_board()
    print_board(board)
    game_over = False

    pygame.init()
    icon = pygame.image.load("static/count.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("CONNET 4")
    SQUARESIZE = 60

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 30)

    turn = random.randint(PLAYER, AI)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                break
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):
                            label = myfont.render("Player wins!!", 1, CYAN)
                            screen.blit(label, (40,10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        print_board(board)
                        draw_board(board)


        # # Ask for Player 2 Input
        if turn == AI and not game_over:				

            col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = myfont.render("AI wins!!", 1, CYAN)
                    screen.blit(label, (40,10))
                    game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

        if game_over:
            pygame.time.wait(2000)
    pygame.quit()
def play_tic_tac_toe_AI():
     
    pygame.init()
    icon = pygame.image.load("static/tic-tac-toe.png")
    pygame.display.set_icon(icon)
    # Set up the display
    WIDTH, HEIGHT = 500, 500
    LINE_WIDTH = 15
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = WIDTH // BOARD_COLS
    CIRCLE_RADIUS = SQUARE_SIZE // 3
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 15
    SPACE = SQUARE_SIZE // 4

    # Define colors
    BLACK = (0, 0, 0)
    beige_rgb = (225, 220, 130)
    YELLOW = (255, 215, 0)

    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill(beige_rgb)

    # Board
    board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    # Fonts
    font = pygame.font.Font(None, 74)


    # Drawing functions
    def draw_lines():
        for col in range(1, BOARD_COLS):
            pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)

    def draw_figures():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 'X':
                    pygame.draw.line(screen, BLACK, 
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                     CROSS_WIDTH)
                    pygame.draw.line(screen, BLACK, 
                                     (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), 
                                     (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                     CROSS_WIDTH)
                elif board[row][col] == 'O':
                    pygame.draw.circle(screen, BLACK, 
                                       (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 
                                       CIRCLE_RADIUS, CIRCLE_WIDTH)

    def display_message(message):
        text = font.render(message, True, YELLOW,BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)

    def check_winner(player):
        # Check rows
        for row in board:
            if all([spot == player for spot in row]):
                return True
        # Check columns
        for col in range(BOARD_COLS):
            if all([board[row][col] == player for row in range(BOARD_ROWS)]):
                return True
        # Check diagonals
        if all([board[i][i] == player for i in range(BOARD_ROWS)]) or all([board[i][BOARD_COLS - 1 - i] == player for i in range(BOARD_ROWS)]):
            return True
        return False

    def is_board_full():
        return all([spot != ' ' for row in board for spot in row])

    def minimax(board, depth, is_maximizing):
        # Implements the minimax algorithm to determine the optimal move for the current player.

        if check_winner('O'):
            return 1
        if check_winner('X'):
            return -1
        if is_board_full():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(BOARD_ROWS):
                for j in range(BOARD_COLS):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        score = minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(BOARD_ROWS):
                for j in range(BOARD_COLS):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        score = minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    def best_move():
        # finding the maximum value in a set of values
        best_score = float('-inf')
        move = None
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, 0, False)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    # Main game loop
    player = 'X'  # Human player starts
    game_over = False

    draw_lines()
# This loop will continue to run as long as the game is not over.
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = player
                    draw_figures()

                    if check_winner(player):
                        game_over = True
                        display_message(f"{player} wins!")
                        break

                    player = 'O' if player == 'X' else 'X'

            if player == 'O' and not game_over:
                move = best_move()
                if move:
                    board[move[0]][move[1]] = 'O'
                    draw_figures()

                    if check_winner('O'):
                        game_over = True
                        display_message("AI wins!")
                        break

                    player = 'X'

        if is_board_full() and not game_over:
            game_over = True
            display_message("It's a tie!")
            break

        pygame.display.update()
    pygame.quit()


def pungAI():
    # Function to reset the ball's position and speed.
    def reset_ball():
        nonlocal ball_speed_x, ball_speed_y  # Use nonlocal to modify variables outside the current scope.
    
        # Set the ball's position to the center horizontally and a random vertical position.
        ball.x = screen_width / 2 - 10
        ball.y = random.randint(10, 100)
        
        # Randomly change the ball's direction for both x and y axes.
        ball_speed_x *= random.choice([-1, 1])
        ball_speed_y *= random.choice([-1, 1])

# Function to update the score when a point is won.
    def point_won(winner):
        nonlocal cpu_points, player_points, ball_speed_x, ball_speed_y  # Use nonlocal to modify variables outside the current scope.
        
        # Check if the CPU won the point.
        if winner == "cpu":
            cpu_points += 1  # Increment CPU points.
            pygame.mixer.Sound.play(score_sound)  # Play scoring sound.

        # Check if the player won the point.
        if winner == "player":
            player_points += 1  # Increment player points.
            pygame.mixer.Sound.play(score_sound)  # Play scoring sound.


        reset_ball()

    def animate_ball():
        nonlocal ball_speed_x, ball_speed_y
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.bottom >= screen_height or ball.top <= 0:
            ball_speed_y *= -1
            pygame.mixer.Sound.play(wall_hit_sound)

        if ball.right >= screen_width:
            point_won("cpu")

        if ball.left <= 0:
            point_won("player")
        #Checks if the ball collides with the player's paddle
        if ball.colliderect(player) or ball.colliderect(cpu):
            ball_speed_x *= -1
            pygame.mixer.Sound.play(paddle_hit_sound)

    def animate_player():
        nonlocal player_speed
        player.y += player_speed
    # Ensure the player does not move above the top of the screen.
        if player.top <= 0:
            player.top = 0
     # Ensure the player does not move below the bottom of the screen.
        if player.bottom >= screen_height:
            player.bottom = screen_height
    
    def animate_cpu():
        nonlocal cpu_speed
        cpu.y += cpu_speed
        # Adjust CPU speed to follow the ball's vertical position.
        if ball.centery <= cpu.centery:
            cpu_speed = -6
        if ball.centery >= cpu.centery:
            cpu_speed = 6
        # Ensure the CPU does not move above the top of the screen.
        if cpu.top <= 0:
            cpu.top = 0
         # Ensure the CPU does not move below the bottom of the screen.
        if cpu.bottom >= screen_height:
            cpu.bottom = screen_height
    # Initialize the pygame 
    pygame.init()
    clock = pygame.time.Clock()
          # Set the dimensions for the screen.
    screen_width = 1000
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    icon = pygame.image.load("static/ping-pong.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PING-PONG")
    DARK_BLUE = (0, 0, 139)
    clock = pygame.time.Clock()

    ball = pygame.Rect(0, 0, 30, 30)
    # Position the ball at the center of the screen.
    ball.center = (screen_width / 2, screen_height / 2)

    cpu = pygame.Rect(0, 0, 20, 100)
    cpu.centery = screen_height / 2

    player = pygame.Rect(0, 0, 20, 100)
    player.midright = (screen_width, screen_height / 2)

    ball_speed_x = 6
    ball_speed_y = 6
    player_speed = 0
    cpu_speed = 6

    cpu_points, player_points = 0, 0
    max_points = 6

    # Load sounds
    pygame.mixer.init()
    score_sound = pygame.mixer.Sound("static/score.ogg")
    paddle_hit_sound = pygame.mixer.Sound("static/pong.ogg")
    wall_hit_sound = pygame.mixer.Sound("static/pong.ogg")

    score_font = pygame.font.Font(None, 100)

    # Countdown
    countdown = 5
    countdown_font = pygame.font.Font(None, 200)
    #start countdown
    while countdown > 0:
        screen.fill(DARK_BLUE)
        countdown_text = countdown_font.render(str(countdown), True, "white")
        screen.blit(countdown_text, (screen_width / 2 - 50, screen_height / 2 - 50))
        pygame.display.flip()
        pygame.time.wait(1000)
        countdown -= 1

    winner = None
# This loop will continue to run as long as the game is not end.
    while True:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            #KEYboard handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed = -6
                if event.key == pygame.K_DOWN:
                    player_speed = 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player_speed = 0
                if event.key == pygame.K_DOWN:
                    player_speed = 0

        # Check for winner
        if cpu_points >= max_points:
            winner = "AI"
        elif player_points >= max_points:
            winner = "Player"
        
        if winner:
            screen.fill(DARK_BLUE)
            winner_text = score_font.render(f'{winner} Wins!', True, "white")
            screen.blit(winner_text, (screen_width / 2 - 150, screen_height / 2 - 50))
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.quit()
            # used to exit the pengAI() function early and end the game loop 
            return winner

        # Change the positions of the game objects
        animate_ball()
        animate_player()
        animate_cpu()

        # Clear the screen
        screen.fill(DARK_BLUE)

        # Draw the score
        cpu_score_surface = score_font.render(str(cpu_points), True, "white")
        player_score_surface = score_font.render(str(player_points), True, "white")
        screen.blit(cpu_score_surface, (screen_width / 4, 20))
        screen.blit(player_score_surface, (3 * screen_width / 4, 20))

        # Draw the game objects
        pygame.draw.aaline(screen, 'white', (screen_width / 2, 0), (screen_width / 2, screen_height))
        pygame.draw.ellipse(screen, 'red', ball)
        pygame.draw.rect(screen, 'white', cpu)
        pygame.draw.rect(screen, 'white', player)

        # Update the display
        pygame.display.update()
        clock.tick(60)

def peng():
    pygame.init()
    icon = pygame.image.load("static/ping-pong.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PING-PONG")
    
    # Define sound files
    hit_sound = pygame.mixer.Sound("static/pong.ogg")
    score_sound = pygame.mixer.Sound("static/score.ogg")
    # Define SCREEN
    WIDTH, HEIGHT = 1000, 600
    DARK_BLUE = (0, 0, 139)
    FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    # Paddles
    player1 = pygame.Rect(0, 0, 20, 100)
    player1.midright = (WIDTH-10, HEIGHT/2)
    player2 = pygame.Rect(0, 0, 20, 100)
    player2.midleft = (10, HEIGHT/2)
    player1_score, player2_score = 0, 0

    # Ball
    ball = pygame.Rect(0, 0, 20, 20)
    ball.center = (WIDTH/2, HEIGHT/2)
    x_speed, y_speed = 1, 1

    def end_game(winner):
        message = FONT.render(f"{winner} wins!", True, "white")
        SCREEN.blit(message, (WIDTH/2 - message.get_width()/2, HEIGHT/2 - message.get_height()/2))
        pygame.display.update()
        pygame.time.wait(3000)
        return True  # Game over flag
    #start by countdown
    def countdown():
        countdown_font = pygame.font.Font(None, 200)
        countdown = 5
        while countdown > 0:
            SCREEN.fill(DARK_BLUE)
            countdown_text = countdown_font.render(str(countdown), True, "white")
            SCREEN.blit(countdown_text, (WIDTH / 2 - countdown_text.get_width() / 2, HEIGHT / 2 - countdown_text.get_height() / 2))
            pygame.display.flip()
            pygame.time.wait(1000)
            countdown -= 1

    # Run countdown before game starts
    countdown()

    game_over = False

    # This loop will continue to run as long as the game is not over.
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        # Keyboard Handling
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_UP]:
            if player1.top > 0:
                player1.top -= 2
        if keys_pressed[pygame.K_DOWN]:
            if player1.bottom < HEIGHT:
                player1.bottom += 2
        if keys_pressed[pygame.K_w]:
            if player2.top > 0:
                player2.top -= 2
        if keys_pressed[pygame.K_s]:
            if player2.bottom < HEIGHT:
                player2.bottom += 2

        # Detect collisions between the ball and player paddles
        if ball.y >= HEIGHT:
            y_speed = -1
            hit_sound.play()  # Play hit sound
        if ball.y <= 0:
            y_speed = 1
            hit_sound.play()  # Play hit sound
        if ball.x <= 0:
            player1_score += 1
            ball.center = (WIDTH/2, HEIGHT/2)
            x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
            score_sound.play()  # Play score sound
        if ball.x >= WIDTH:
            player2_score += 1
            ball.center = (WIDTH/2, HEIGHT/2)
            x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
            score_sound.play()  # Play score sound
        if player1.x - ball.width <= ball.x <= player1.right and ball.y in range(player1.top-ball.width, player1.bottom+ball.width):
            x_speed = -1
            hit_sound.play()  # Play hit sound
        if player2.x - ball.width <= ball.x <= player2.right and ball.y in range(player2.top-ball.width, player2.bottom+ball.width):
            x_speed = 1
            hit_sound.play()  # Play hit sound

        # Render score
        player1_score_text = FONT.render(str(player1_score), True, "white")
        player2_score_text = FONT.render(str(player2_score), True, "white")

        # Check if a player has won
        if player1_score == 10:
            game_over = end_game("Player 1")
        if player2_score == 10:
            game_over = end_game("Player 2")
            
        # Move the ball
        ball.x += x_speed * 2
        ball.y += y_speed * 2

        # Draw everything
        SCREEN.fill(DARK_BLUE)
        pygame.draw.rect(SCREEN, "white", player1)
        pygame.draw.rect(SCREEN, "white", player2)
        pygame.draw.circle(SCREEN, "RED", ball.center, 15)
        SCREEN.blit(player1_score_text, (WIDTH/2 + 50, 50))
        SCREEN.blit(player2_score_text, (WIDTH/2 - 50, 50))
        pygame.draw.line(SCREEN, 'white', (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), 2)

        pygame.display.update()
        CLOCK.tick(300)
    pygame.quit()
    
#  Flask application
@app.route("/")
@app.route("/home")
def home():
    # Renders the 'home.html' template and passes 'games' and 'Games2' as variables to the template.
    return render_template('home.html', games=games, Games2=Games2)

# Route for starting a game, accessed via "/game/<int:game_id>" where 'game_id' is a number.
@app.route('/game/<int:game_id>')
def start_game(game_id):
    # Check the game_id to determine which game to play.
    if game_id == 1:
        # Call the function to play Connect Four.
        play_connect_four()
    elif game_id == 2:
        # Call the function to play Tic Tac Toe.
        play_tic_tac_toe()
    elif game_id == 3:
        # Call the function for the SPR game.
        SPR()
    elif game_id == 4:
        # Call the function to play Tic Tac Toe with AI.
        play_tic_tac_toe_AI()
    elif game_id == 5:
        # Call the function to play Connect Four with AI.
        play_connect_fourAI()
    elif game_id == 6:
        # Call the function for SPR with AI.
        SPRAI()
    elif game_id == 7:
        # Call the function for the 'Peng' game.
        peng()
    elif game_id == 8:
        # Call the function for the 'Pung' game with AI.
        pungAI()
    # After playing the game, render the 'end.html' template to show the end screen.
    return render_template('end.html')

# Route for the info page, accessed via "/Info".
@app.route("/Info")
def Info():
    # Renders the 'Info.html' template, providing information about the games or application.
    return render_template('Index.html')

# Entry point of the application.
if __name__ == "__main__":
    # Runs the Flask application with debug mode enabled, useful for development.
    app.run(debug=True)
