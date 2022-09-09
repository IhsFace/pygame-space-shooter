import pygame
import sys
from players import Players


def draw_text(text, size, color, surface, pos):
    font = pygame.font.Font('assets/PressStart2P-Regular.ttf', size)
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    display.blit(text_render, text_rect)


def main_menu():
    while True:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        display.fill((0, 0, 0))

        draw_text('SPACE SHOOTER', 36, (255, 255, 255),
                  display, (window_size.x // 2, 100))

        display.blit(ship_image, ship_rect)

        mx, my = pygame.mouse.get_pos()

        play_button = pygame.Rect(0, 0, 150, 50)
        play_button.center = (200, 300)
        if play_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                game_state = game()
        pygame.draw.rect(display, (0, 0, 0), play_button)
        pygame.draw.rect(display, (255, 255, 255), play_button, 5)
        draw_text('PLAY', 24, (255, 255, 255), display, play_button.center)

        quit_button = pygame.Rect(0, 0, 150, 50)
        quit_button.center = (400, 300)
        if quit_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.quit()
                sys.exit()
        pygame.draw.rect(display, (0, 0, 0), quit_button)
        pygame.draw.rect(display, (255, 255, 255), quit_button, 5)
        draw_text('QUIT', 24, (255, 255, 255),
                  display, quit_button.center)

        pygame.display.update()
        clock.tick(60)


def game():
    while True:
        display.fill((0, 0, 0))

        players.update()

        pygame.draw.rect(display, (255, 255, 255), border)

        draw_text(f'HEALTH: {str(players.p1_health)}', 16,
                  (255, 255, 255), display, (100, 375))
        draw_text(f'HEALTH: {str(players.p2_health)}', 16,
                  (255, 255, 255), display, (500, 375))

        if players.p1_health == 0 or players.p2_health == 0:
            game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    shoot_sound.play()
                    bullet = pygame.Rect(0, 0, 10, 5)
                    bullet.center = players.p1_rect.center
                    players.p1_bullets.append(bullet)
                if event.key == pygame.K_RCTRL:
                    shoot_sound.play()
                    bullet = pygame.Rect(0, 0, 10, 5)
                    bullet.center = players.p2_rect.center
                    players.p2_bullets.append(bullet)

        pygame.display.update()
        clock.tick(60)


def game_over():
    while True:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        display.fill((0, 0, 0))

        draw_text('GAME OVER', 36, (255, 255, 255),
                  display, (window_size.x // 2, 100))

        if players.p1_health == 0:
            draw_text('PLAYER 2 WINS!', 24, (255, 255, 255),
                      display, (window_size.x // 2, 200))
        elif players.p2_health == 0:
            draw_text('PLAYER 1 WINS!', 24, (255, 255, 255),
                      display, (window_size.x // 2, 200))

        mx, my = pygame.mouse.get_pos()

        play_button = pygame.Rect(0, 0, 150, 50)
        play_button.center = (200, 300)
        if play_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                players.p1_health = 4
                players.p2_health = 4
                game_state = game()
        pygame.draw.rect(display, (0, 0, 0), play_button)
        pygame.draw.rect(display, (255, 255, 255), play_button, 5)
        draw_text('PLAY', 24, (255, 255, 255), display, play_button.center)

        quit_button = pygame.Rect(0, 0, 150, 50)
        quit_button.center = (400, 300)
        if quit_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.quit()
                sys.exit()
        pygame.draw.rect(display, (0, 0, 0), quit_button)
        pygame.draw.rect(display, (255, 255, 255), quit_button, 5)
        draw_text('QUIT', 24, (255, 255, 255), display, quit_button.center)

        pygame.display.update()
        clock.tick(60)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.display.set_caption('Space Shooter')
icon = pygame.image.load('assets/main ship/Main Ship - Base - Full health.png')
pygame.display.set_icon(icon)
window_size = pygame.math.Vector2(600, 400)
display = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

ship_image = pygame.transform.scale(pygame.image.load(
    'assets/main ship/Main Ship - Base - Full health.png'), (96, 96))
ship_rect = ship_image.get_rect(center=(window_size.x // 2, 200))

border = pygame.Rect(0, 0, 10, 400)
border.center = (window_size.x // 2, window_size.y // 2)

players = Players()

shoot_sound = pygame.mixer.Sound('assets/sounds/shoot.wav')
select_sound = pygame.mixer.Sound('assets/sounds/select.wav')

if __name__ == '__main__':
    game_state = main_menu()
