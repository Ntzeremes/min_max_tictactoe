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
    def __init__(self, grid, width, pad, screen, color):
        self.grid_size = grid
        self.width = width
        self.increment = int(width/grid)
        self.screen = screen
        self.color = color
        self.pad = pad
        self.grid = ["#" for i in range(grid) for j in range(grid)]
        print(self.grid)

    def draw(self):
        for i in range(self.grid_size - 1):
            pygame.draw.line(self.screen, self.color, (self.pad + (i+1)*self.increment, self.pad),
                             (self.pad + (i+1)*self.increment, self.pad + self.width))
            pygame.draw.line(self.screen, self.color, (self.pad, self.pad + (i+1)*self.increment),
                             (self.pad + self.width, self.pad + (i+1)*self.increment))

    def check_winning(self, turn):
        if turn == 0:
            player = "x"
        else:
            player = "o"

        # check horizontal - vertical

        for i in range(self.grid_size):
            h_counter = 0
            v_counter = 0
            for j in range(self.grid_size):
                if self.grid[i][j] == player:
                    v_counter += 1
                if self.grid[j][i] == player:
                    h_counter += 1

            if h_counter == self.grid_size or v_counter == self.grid_size:
                return True


def main():
    # Checking for correct system arguments when executing the program.
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py 3 (or 4,5)")
    else:
        grid_size = int(sys.argv[1])
        if grid_size not in (3, 4,5):
            sys.exit("Choose between 3x3 or 4x4, 5x5 grid")

    # Initialize the pygame window and board
    screen = pygame.display.set_mode((WIDTH + 2*PAD, HEIGHT + 2*PAD))
    screen.fill(WHITE)
    pygame.display.set_caption("Tic tac toe")
    board = Board(grid_size, WIDTH, PAD, screen, BLACK)
    board.draw()

    game_over = False
    trigger = "Closed"

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        pygame.display.flip()

    sys.exit(trigger)


if __name__ == "__main__":
    main()
