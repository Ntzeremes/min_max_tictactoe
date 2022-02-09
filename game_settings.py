"""GUI that gives at the start of the game the player some basic choices.
 playing vs computer or other player  and choosing X or O"""

import pygame

pygame.init()


class Button:
    def __init__(self, pos, height, width, font, text):
        self.rect = pygame.Rect(pos, (width, height))
        self.color = (50, 50, 50)
        self.text_surf = font.render(text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        self.pressed = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(*mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    return True
        return False


def settings(font):

    main = pygame.display.set_mode((300, 300))
    main.fill((0, 0, 0))
    pygame.display.set_caption("Tic tac toe")
    settings_over = False
    clock = pygame.time.Clock()

    # create the buttons
    pvp = Button((25, 50), 75, 250, font, "Player vs Player")
    pvc = Button((25, 175), 75, 250, font, "Player vs Computer")

    play_x = Button((60, 60), 55, 180, font, "Play X")
    play_o = Button((60, 185), 55, 180, font, "Play O")

    pvmode = True
    choose_turn = False

    while not settings_over:
        clock.tick(60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_over = True

        if pvmode:
            pvp.draw(main)
            pvc.draw(main)

            if pvp.click():
                return 0, None

            if pvc.click():
                choose_turn = True
                pvmode = False

        if choose_turn:
            play_x.draw(main)
            play_o.draw(main)

            if play_x.click():
                return 1, "X"
            if play_o.click():
                return 1, "O"
