from flask import Flask, render_template, url_for, redirect
import pygame
import numpy as np
import random
import math


from pygame.locals import *

app = Flask(__name__)


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


    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    CYAN = (0, 255, 255)
    


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


                # # Ask for Player 2 Input
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

 pass
def SPR():
  pass
def SPRAI():
   pass
def play_connect_fourAI():
   
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    CYAN = (0, 255, 255)

    ROW_COUNT = 6
    COLUMN_COUNT = 6

    PLAYER = 0
    AI = 1

    EMPTY = 0
    PLAYER_PIECE = 1
    AI_PIECE = 2

    WINDOW_LENGTH = 4

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
     # Initialize pygame
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
    pass
def peng():
    pygame.init()
    icon = pygame.image.load("static/ping-pong.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("PING-PONG")
    
    # Define sound files
    hit_sound = pygame.mixer.Sound("static/pong.ogg")
    score_sound = pygame.mixer.Sound("static/score.ogg")

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
    

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', games=games, Games2=Games2)
@app.route('/game/<int:game_id>')
def start_game(game_id):
    if game_id == 1:
        play_connect_four()
        
    elif game_id == 2:
        play_tic_tac_toe()
       
    elif game_id == 3:
        SPR()
       
    elif game_id == 4:
        play_tic_tac_toe_AI()
    
    elif game_id == 5:
        play_connect_fourAI()
    elif game_id == 6:
        SPRAI()
    elif game_id == 8:
        pungAI()
    elif game_id == 7:
        peng()
    return render_template('end.html')

@app.route("/Info")
def Info():
    return render_template('Info.html')
if __name__=="__main__":
    app.run(debug=True)
