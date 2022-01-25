import pygame
import sys

pygame.init()
# Constants for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 600
HEIGHT = 600
PAD = 10


class Board:
    """The class that contains information about the state of the board and creates the grid"""
    moves = 0

    def __init__(self, grid, width, pad, screen, color):
        self.grid_size = grid
        self.width = width
        self.increment = int(width / grid)
        self.screen = screen
        self.color = color
        self.pad = pad
        self.grid = [["#" for i in range(grid)] for j in range(grid)]
        self.win = 3 if grid == 3 else 4

    def draw(self):
        for i in range(self.grid_size - 1):
            pygame.draw.line(self.screen, self.color, (self.pad + (i+1)*self.increment, self.pad),
                             (self.pad + (i+1)*self.increment, self.pad + self.width))
            pygame.draw.line(self.screen, self.color, (self.pad, self.pad + (i+1)*self.increment),
                             (self.pad + self.width, self.pad + (i+1)*self.increment))

    def draw_o(self, x, y):
        pygame.draw.circle(self.screen, (0, 0, 255), (int(self.pad + x*self.increment + 0.5*self.increment),
                           int(self.pad + y*self.increment + 0.5*self.increment)), int(self.increment*0.5 - self.pad), 3)

    def draw_x(self, x, y):
        print(self.pad + x*self.increment, self.pad + y*self.increment)
        pygame.draw.line(self.screen, (255, 0, 0), (self.pad + x*self.increment + 5, self.pad + y*self.increment + 5),
                         (self.pad + x*self.increment + self.increment - 5,
                          self.pad + y*self.increment + self.increment - 5), 3)
        pygame.draw.line(self.screen, (255, 0, 0), (x*self.increment + self.increment + self.pad - 5,
                                                    self.pad + y*self.increment + 5),
                         (x*self.increment + self.pad + 5, y*self.increment + self.increment + self.pad - 5), 3)

    def check_winning(self, turn):
        if turn == 0:
            player = "x"
        else:
            player = "o"

        # check horizontal - vertical

        for i in range(self.grid_size):
            h_counter = 0
            v_counter = 0
            d1_counter = 0
            d2_counter = 0
            for j in range(self.grid_size):
                if self.grid[i][j] == player:
                    v_counter += 1
                if self.grid[j][i] == player:
                    h_counter += 1

            if h_counter == self.grid_size or v_counter == self.grid_size:
                return True

            if self.grid[i][i] == player:
                d1_counter += 1
            if self.grid[-i][-i] == player:
                d2_counter += 1

            if d1_counter == self.win or d2_counter == self.win:
                return True
        return False

    def insert(self, x, y, player):
        self.grid[x][y] = player
        if player == "x":
            self.draw_x(x, y)
        else:
            self.draw_o(x, y)

        Board.moves += 1

    def print(self):
        for i in range(self.grid_size):
            print(self.grid[i])
            print()
        print()

    def check_empty(self, i, j):
        if self.grid[i][j] == "#":
            return True
        else:
            return False


def main():
    # Checking for correct system arguments when executing the program.
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py 3 (or 4,5)")
    else:
        grid_size = int(sys.argv[1])
        if grid_size not in (3, 4, 5):
            sys.exit("Choose between 3x3 or 4x4, 5x5 grid")

    # Initialize the pygame window and board
    screen = pygame.display.set_mode((WIDTH + 2 * PAD, HEIGHT + 2 * PAD))
    screen.fill(WHITE)
    pygame.display.set_caption("Tic tac toe")
    board = Board(grid_size, WIDTH, PAD, screen, BLACK)
    board.draw()

    game_over = False
    trigger = "Closed"
    increment = WIDTH/grid_size
    turn = 0

    while not game_over:

        # Event Loop for the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Checking mouse clicking position
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = int(event.pos[0]//increment)
                y = int(event.pos[1]//increment)

                if board.check_empty(x, y):
                    if turn == 0:
                        board.insert(x, y, 'x')
                        if board.check_winning(turn):
                            game_over = True
                            trigger = "Player X won the game"
                        turn += 1
                        board.print()
                    else:
                        board.insert(x, y, 'o')
                        if board.check_winning(turn):
                            game_over = True
                            trigger = "Player O won the game"
                        turn -= 1

                    board.print()

        # if board is filled and noone has won the game ends in a draw.
        if board.moves == board.grid_size**2:
            game_over = True
            trigger = "Its a draw."

        pygame.display.flip()

    sys.exit(trigger)


if __name__ == "__main__":
    main()
