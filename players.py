import pygame


class Players:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.speed = 3
        self.bullet_speed = 5

        self.p1_rect = pygame.Rect(0, 0, 48, 48)
        self.p1_rect.center = (150, 200)
        self.p1_bullets = []
        self.p1_health = 4

        self.p2_rect = pygame.Rect(0, 0, 48, 48)
        self.p2_rect.center = (450, 200)
        self.p2_bullets = []
        self.p2_health = 4

        self.damage_sound = pygame.mixer.Sound('assets/sounds/damage.wav')

    def p1_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.p1_rect.y -= self.speed
        if keys[pygame.K_a]:
            self.p1_rect.x -= self.speed
        if keys[pygame.K_s]:
            self.p1_rect.y += self.speed
        if keys[pygame.K_d]:
            self.p1_rect.x += self.speed
        if self.p1_rect.top <= 0:
            self.p1_rect.top = 0
        if self.p1_rect.bottom >= 400:
            self.p1_rect.bottom = 400
        if self.p1_rect.left <= 0:
            self.p1_rect.left = 0
        if self.p1_rect.right >= 295:
            self.p1_rect.right = 295

    def p2_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.p2_rect.y -= self.speed
        if keys[pygame.K_LEFT]:
            self.p2_rect.x -= self.speed
        if keys[pygame.K_DOWN]:
            self.p2_rect.y += self.speed
        if keys[pygame.K_RIGHT]:
            self.p2_rect.x += self.speed
        if self.p2_rect.top <= 0:
            self.p2_rect.top = 0
        if self.p2_rect.bottom >= 400:
            self.p2_rect.bottom = 400
        if self.p2_rect.left <= 305:
            self.p2_rect.left = 305
        if self.p2_rect.right >= 600:
            self.p2_rect.right = 600

    def bullets(self):
        for bullet in self.p1_bullets:
            bullet.x += self.bullet_speed
            if self.p2_rect.colliderect(bullet):
                self.damage_sound.play()
                self.p1_bullets.remove(bullet)
                self.p2_health -= 1
            elif bullet.left > 600:
                self.p1_bullets.remove(bullet)
        for bullet in self.p2_bullets:
            bullet.x -= self.bullet_speed
            if self.p1_rect.colliderect(bullet):
                self.damage_sound.play()
                self.p2_bullets.remove(bullet)
                self.p1_health -= 1
            elif bullet.left > 600:
                self.p2_bullets.remove(bullet)

    def update(self):
        self.p1_move()
        self.p2_move()
        self.bullets()

        if self.p1_health == 4:
            self.p1_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Full health.png').convert_alpha(), 270)
        elif self.p1_health == 3:
            self.p1_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Slight damage.png').convert_alpha(), 270)
        elif self.p1_health == 2:
            self.p1_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Damaged.png').convert_alpha(), 270)
        elif self.p1_health == 1:
            self.p1_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Very damaged.png').convert_alpha(), 270)

        if self.p2_health == 4:
            self.p2_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Full health.png').convert_alpha(), 90)
        elif self.p2_health == 3:
            self.p2_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Slight damage.png').convert_alpha(), 90)
        elif self.p2_health == 2:
            self.p2_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Damaged.png').convert_alpha(), 90)
        elif self.p2_health == 1:
            self.p2_image = pygame.transform.rotate(
                pygame.image.load('assets/main ship/Main Ship - Base - Very damaged.png').convert_alpha(), 90)

        self.display.blit(self.p1_image, self.p1_rect)
        self.display.blit(self.p2_image, self.p2_rect)

        for bullet in self.p1_bullets:
            pygame.draw.rect(self.display, (255, 255, 255), bullet)
        for bullet in self.p2_bullets:
            pygame.draw.rect(self.display, (255, 255, 255), bullet)
