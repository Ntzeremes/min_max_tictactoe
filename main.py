import copy
import pygame
import sys
from game_settings import settings
from algorithms import minmax_ab
import time

pygame.init()
# Constants for the game
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WIDTH = 600
HEIGHT = 600
PAD = 50


class Text:
    def __init__(self, font, pos, height, width):
        self.font = font
        self.rect = pygame.Rect(pos, (width, height))
        self.text_surf = font.render("_", True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def text(self, text):
        self.text_surf = self.font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)


class Board:
    """The class that initializes the board of the game.
    It also includes functions for manipulating it and checking its current state"""
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
            pygame.draw.line(self.screen, self.color, (self.pad + (i + 1) * self.increment, self.pad),
                             (self.pad + (i + 1) * self.increment, self.pad + self.width), 2)
            pygame.draw.line(self.screen, self.color, (self.pad, self.pad + (i + 1) * self.increment),
                             (self.pad + self.width, self.pad + (i + 1) * self.increment), 2)

    def draw_o(self, x, y):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.pad + x * self.increment + 0.5 * self.increment),
                                                          int(self.pad + y * self.increment + 0.5 * self.increment)),
                           int(self.increment * 0.5 - 10), 3)

    def draw_x(self, x, y):
        pygame.draw.line(self.screen, (255, 255, 255),
                         (self.pad + x * self.increment + 5, self.pad + y * self.increment + 5),
                         (self.pad + x * self.increment + self.increment - 5,
                          self.pad + y * self.increment + self.increment - 5), 3)
        pygame.draw.line(self.screen, (255, 255, 255), (x * self.increment + self.increment + self.pad - 5,
                                                        self.pad + y * self.increment + 5),
                         (x * self.increment + self.pad + 5, y * self.increment + self.increment + self.pad - 5), 3)

    def insert(self, x, y, player):
        self.grid[x][y] = player
        if player == "X":
            self.draw_x(x, y)
        else:
            self.draw_o(x, y)

        Board.moves += 1

    def check_empty(self, i, j):
        if self.grid[i][j] == "#":
            return True
        else:
            return False

    def player(self):
        x = 0
        o = 0
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == "X":
                    x += 1
                elif self.grid[i][j] == "O":
                    o += 1
        if x == o:
            return "X"
        else:
            return "O"

    def check_winner(self):
        for i in range(self.grid_size):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2]:
                if self.grid[i][0] == "X" or self.grid[i][0] == "O":
                    return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i]:
                if self.grid[0][i] == "X" or self.grid[0][i] == "O":
                    return self.grid[0][i]

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] or self.grid[0][2] == self.grid[1][1] == self.grid[2][
            0]:
            if self.grid[1][1] == "X" or self.grid[1][1] == "O":
                return self.grid[1][1]

        return None

    def game_over(self):
        winner = self.check_winner()
        if winner:
            return winner

        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == "#":
                    return False

        return True


def pvp(grid_size, board):
    """ Initializes and executes the player vs player game loop."""

    game_over = False
    trigger = "Closed"
    increment = WIDTH / grid_size
    clock = pygame.time.Clock()

    while not game_over:
        clock.tick(60)

        # Event Loop for the game in the mode player vs player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Checking mouse clicking position
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = int(event.pos[0] // increment)
                y = int(event.pos[1] // increment)

                if x < board.grid_size and y < board.grid_size:
                    if board.check_empty(x, y):
                        board.insert(x, y, board.player())

        if board.game_over():
            winner = board.check_winner()
            trigger = "It is a draw"
            if winner:
                trigger = f"{winner} player has won."
            game_over = True

        pygame.display.flip()

    sys.exit(trigger)


def pvc(grid_size, turn, board, font):
    """ Initializes and executes the player vs computer game loop."""

    game_over = False
    trigger = "Closed"
    increment = WIDTH / grid_size
    clock = pygame.time.Clock()
    players_text = Text(font, (250, 5), 40, 200)
    while not game_over and not board.game_over():
        pygame.display.flip()
        clock.tick(60)
        # Event Loop for the game in the mode player vs player
        if board.player() == turn:
            players_text.text(" Player's turn")
            players_text.draw(board.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                # Checking mouse clicking position
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = int((event.pos[0] - 50) // increment)
                    y = int((event.pos[1] - 50) // increment)

                    if board.check_empty(x, y):
                        board.insert(x, y, turn)
        else:
            players_text.text("Computer's turn")
            players_text.draw(board.screen)
            pygame.display.flip()
            time.sleep(1)
            _, action = minmax_ab(board.grid, -10, 10)
            time.sleep(1)

            board.insert(action[0], action[1], board.player())

    sys.exit(trigger)


def main():
    # Getting the size of the grid the, turn phase and the mode from the user.

    font = pygame.font.Font(None, 25)
    mode, turn = settings(font)

    print(turn)
    # Initialize the pygame window and board
    screen = pygame.display.set_mode((WIDTH + 2 * PAD, HEIGHT + 2 * PAD))
    screen.fill(BLACK)
    pygame.display.set_caption("Tic tac toe")
    board = Board(3, WIDTH, PAD, screen, WHITE)
    board.draw()

    # Executing the player vs player game if mode is 0:
    if mode == 0:
        pvp(3, board)

    # Executing the player vs computer
    else:
        pvc(3, turn, board, font)


if __name__ == "__main__":
    main()
