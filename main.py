import pygame
import sys
from player import Players


class Menu():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption('Space Shooter')
        self.icon = pygame.image.load(
            'assets/main ship/Main Ship - Base - Full health.png')
        pygame.display.set_icon(self.icon)
        self.window_size = pygame.math.Vector2(600, 400)
        self.display = pygame.display.set_mode(self.window_size)
        self.click = False

        self.ship_image = pygame.transform.scale(pygame.image.load(
            'assets/main ship/Main Ship - Base - Full health.png'), (96, 96))
        self.ship_rect = self.ship_image.get_rect(
            center=(self.window_size.x // 2, 200))

        self.select_sound = pygame.mixer.Sound('assets/sounds/select.wav')

    def draw_text(self, text, size, color, surface, pos):
        font = pygame.font.Font('assets/PressStart2P-Regular.ttf', size)
        text_render = font.render(text, True, color)
        text_rect = text_render.get_rect()
        text_rect.center = pos
        self.display.blit(text_render, text_rect)

    def main(self):
        while True:
            self.display.fill((0, 0, 0))

            self.draw_text('SPACE SHOOTER', 36, (255, 255, 255),
                           self.display, (self.window_size.x // 2, 100))

            self.display.blit(self.ship_image, self.ship_rect)

            mx, my = pygame.mouse.get_pos()

            play_button = pygame.Rect(0, 0, 150, 50)
            play_button.center = (200, 300)
            if play_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    Main().game_state = Game().game()
            pygame.draw.rect(self.display, (0, 0, 0), play_button)
            pygame.draw.rect(self.display, (255, 255, 255), play_button, 5)
            self.draw_text('PLAY', 24, (255, 255, 255),
                           self.display, play_button.center)

            quit_button = pygame.Rect(0, 0, 150, 50)
            quit_button.center = (400, 300)
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    pygame.quit()
                    sys.exit()
            pygame.draw.rect(self.display, (0, 0, 0), quit_button)
            pygame.draw.rect(self.display, (255, 255, 255), quit_button, 5)
            self.draw_text('QUIT', 24, (255, 255, 255),
                           self.display, quit_button.center)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.clock.tick(60)


class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption('Space Shooter')
        self.icon = pygame.image.load(
            'assets/main ship/Main Ship - Base - Full health.png')
        pygame.display.set_icon(self.icon)
        self.window_size = pygame.math.Vector2(600, 400)
        self.display = pygame.display.set_mode(self.window_size)
        self.click = False

        self.shoot_sound = pygame.mixer.Sound('assets/sounds/shoot.wav')
        self.select_sound = pygame.mixer.Sound('assets/sounds/select.wav')

        self.border = pygame.Rect(0, 0, 10, 400)
        self.border.center = (self.window_size.x // 2,
                              self.window_size.y // 2)

        self.players = Players()

    def draw_text(self, text, size, color, surface, pos):
        font = pygame.font.Font('assets/PressStart2P-Regular.ttf', size)
        text_render = font.render(text, True, color)
        text_rect = text_render.get_rect()
        text_rect.center = pos
        self.display.blit(text_render, text_rect)

    def game_over(self):
        while True:
            self.display.fill((0, 0, 0))

            self.draw_text('GAME OVER', 36, (255, 255, 255),
                           self.display, (self.window_size.x // 2, 100))

            if self.players.p1_health == 0:
                self.draw_text('PLAYER 2 WINS!', 24, (255, 255, 255),
                               self.display, (self.window_size.x // 2, 200))
            elif self.players.p2_health == 0:
                self.draw_text('PLAYER 1 WINS!', 24, (255, 255, 255),
                               self.display, (self.window_size.x // 2, 200))

            mx, my = pygame.mouse.get_pos()

            play_button = pygame.Rect(0, 0, 150, 50)
            play_button.center = (200, 300)
            if play_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    Main().game_state = Game().game()
            pygame.draw.rect(self.display, (0, 0, 0), play_button)
            pygame.draw.rect(self.display, (255, 255, 255), play_button, 5)
            self.draw_text('PLAY', 24, (255, 255, 255),
                           self.display, play_button.center)

            quit_button = pygame.Rect(0, 0, 150, 50)
            quit_button.center = (400, 300)
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    pygame.quit()
                    sys.exit()
            pygame.draw.rect(self.display, (0, 0, 0), quit_button)
            pygame.draw.rect(self.display, (255, 255, 255), quit_button, 5)
            self.draw_text('QUIT', 24, (255, 255, 255),
                           self.display, quit_button.center)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.clock.tick(60)

    def game(self):
        while True:
            self.display.fill((0, 0, 0))

            self.players.update()

            pygame.draw.rect(self.display, (255, 255, 255), self.border)

            self.draw_text(f'HEALTH: {str(self.players.p1_health)}',
                           16, (255, 255, 255), self.display, (100, 375))
            self.draw_text(f'HEALTH: {str(self.players.p2_health)}',
                           16, (255, 255, 255), self.display, (500, 375))

            if self.players.p1_health == 0 or self.players.p2_health == 0:
                self.game_over()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        self.shoot_sound.play()
                        bullet = pygame.Rect(0, 0, 10, 5)
                        bullet.center = self.players.p1_rect.center
                        self.players.p1_bullets.append(bullet)
                    if event.key == pygame.K_RCTRL:
                        self.shoot_sound.play()
                        bullet = pygame.Rect(0, 0, 10, 5)
                        bullet.center = self.players.p2_rect.center
                        self.players.p2_bullets.append(bullet)

            pygame.display.update()
            self.clock.tick(60)


class Main():
    def __init__(self):
        self.game_state = Menu().main()


if __name__ == '__main__':
    main = Main()
    main.game_state
