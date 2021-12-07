#12.6.2021
import pygame
import random
import os
import sys
import time

pygame.init()
screen = pygame.display.set_mode((1024, 576))
player_img = pygame.image.load(os.path.join(sys.path[0], "assets/player.png"), "r")
enemy_img = pygame.image.load(os.path.join(sys.path[0], "assets/enemy.png"), "r")
crosshair_img = pygame.image.load(os.path.join(sys.path[0], "assets/crosshair.png"), "r")
bullet_img = pygame.image.load(os.path.join(sys.path[0], "assets/bullet.png"), "r")
reload1_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload1.png"), "r")
reload2_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload2.png"), "r")
reload3_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload3.png"), "r")
reload4_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload4.png"), "r")
reload5_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload5.png"), "r")
reload6_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload6.png"), "r")
reload7_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload7.png"), "r")
reload8_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload8.png"), "r")
reload_text_img = pygame.image.load(os.path.join(sys.path[0], "assets/reload_text.png"), "r")
font = pygame.font.SysFont(None, 72)
show_reload = True

loop = True

kills = 0
if loop:
    class player():
        def __init__(self, player_x, player_y):
            self.x = player_x
            self.y = player_y
            self.hitbox = 50
            
        def render(self):
            if self.x < 0:
                self.x = 0
            if self.x > 974:
                self.x = 974
            if self.y < 0:
                self.y = 0
            if self.y > 526:
                self.y = 526
    
    class enemy():
        #1 top, 2 bottom, 3 right, 4 left
        def __init__(self, direction):
            if direction == 1:
                self.direction = 1
                self.x = random.randint(0, 974)
                self.y = random.randint(100, 600) * -1
            if direction == 2:
                self.direction = 2
                self.x = random.randint(0, 974)
                self.y = random.randint(600, 1100)
            if direction == 3:
                self.direction = 3
                self.x = random.randint(1074, 1624)
                self.y = random.randint(0, 526)
            if direction == 4:
                self.direction = 4
                self.x = random.randint(100, 600) * -1
                self.y = random.randint(0, 526)
        
        def render(self):
            if self.direction == 1:
                self.y += 2
            if self.direction == 2:
                self.y -= 2
            if self.direction == 3:
                self.x -= 2
            if self.direction == 4:
                self.x += 2
            
            
    player = player(400, 200)
    enemy1 = enemy(1)
    enemy_list = [enemy1]
    flash_count = 0
    
ammo = 10
reload_timer = 0
show_reload_timer = 0

kills_x = 950
while loop:
    pygame.mouse.set_visible(False)
    mouse_coord = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (133, 133, 133), pygame.Rect(0, 0, 1024, 576))
    
    for key in pygame.event.get():
        if key.type == pygame.QUIT:
            pygame.quit()
            exit()
        if key.type == pygame.MOUSEBUTTONDOWN:
            if reload_timer == 0:
                mouse_coord = pygame.mouse.get_pos()
                if ammo > 0:
                    flash_count = 5
                    ammo -= 1
                    for person in enemy_list:
                        if person.x - 9 < mouse_coord[0] < person.x + 41 and person.y - 9 < mouse_coord[1] < person.y + 41:
                            enemy_list.remove(person)
                            kills += 1
        if key.type == pygame.KEYDOWN:
            if key.key == pygame.K_r:
                if reload_timer == 0 and ammo != 10:
                    reload_timer = 240
            
    pressed_keys = pygame.key.get_pressed()
    
    if pressed_keys[pygame.K_LSHIFT] or pressed_keys[pygame.K_RSHIFT]:
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            player.x -= 2
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            player.y += 2
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            player.x += 2
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            player.y -= 2
    else:
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            player.x -= 5
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            player.y += 5
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            player.x += 5
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            player.y -= 5
        
    
    if reload_timer > 0:
        reload_timer -= 1
    player.render()
    for person in enemy_list:
        person.render()
        if person.direction == 1 and person.y > 626:
            enemy_list.remove(person)
        if person.direction == 2 and person.y < -50:
            enemy_list.remove(person)
        if person.direction == 3 and person.x < -50:
            enemy_list.remove(person)
        if person.direction == 4 and person.x > 1074:
            enemy_list.remove(person)
    
    if flash_count > 0:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 1024, 576))
        flash_count -= 1
    screen.blit(player_img, (player.x, player.y))
    
    for person in enemy_list:
        screen.blit(enemy_img, (person.x, person.y))
        if person.x - 50 < player.x < person.x + 50 and person.y - 50 < player.y < person.y + 50:
            loop = False
            
    kills_text = font.render(str(kills), True, (0, 0, 0))
    for ammo_number in range(ammo):
        screen.blit(bullet_img, (ammo_number * 10, 0))
    if kills < 10:
        kills_x = 970
    if 10 < kills < 100:
        kills_x = 940
    if 100 < kills < 1000:
        kills_x = 910
    if 1000 < kills < 10000:
        kills_x = 880
    if kills > 10000:
        kills_text = font.render(("Too high"), True, (0, 0, 0))
        kills_x = 810
        
    screen.blit(kills_text, (kills_x, 10))
    
    if random.randint(0, 5) == 1:
        if kills < 20:
            if len(enemy_list) < 50:
                enemy_list.append(enemy(random.randint(1, 4)))
        elif kills < 40:
            if len(enemy_list) < 70:
                enemy_list.append(enemy(random.randint(1, 4)))
        elif kills < 60:
            if len(enemy_list) < 85:
                enemy_list.append(enemy(random.randint(1, 4)))
        else:
            if lent(enemy_list) <= 100:
                enemy_list.append(enemy(random.randint(1, 4)))
    
    if reload_timer > 0:
        if 0 < reload_timer <= 30:
            screen.blit(reload8_img, (player.x + 13, player.y - 40))
        if 30 < reload_timer <= 60:
            screen.blit(reload7_img, (player.x + 10, player.y - 40))
        if 60 < reload_timer <= 90:
            screen.blit(reload6_img, (player.x + 10, player.y - 40))
        if 90 < reload_timer <= 120:
            screen.blit(reload5_img, (player.x + 10, player.y - 40))
        if 120 < reload_timer <= 150:
            screen.blit(reload4_img, (player.x + 10, player.y - 40))
        if 150 < reload_timer <= 180:
            screen.blit(reload3_img, (player.x + 10, player.y - 40))
        if 180 < reload_timer <= 210:
            screen.blit(reload2_img, (player.x + 10, player.y - 40))
        if 210 < reload_timer <= 240:
            screen.blit(reload1_img, (player.x + 10, player.y - 40))
        reload_timer -= 1
        if reload_timer == 0:
            ammo = 10
            
        
    if ammo == 0 and reload_timer == 0:
        show_reload_timer += 1
        if show_reload_timer == 30:
            if show_reload == True:
                show_reload = False
            else:
                show_reload = True
            
            show_reload_timer = 0
    
        if show_reload:
            screen.blit(reload_text_img, (player.x - 25, player.y - 30))
            
    screen.blit(crosshair_img, (mouse_coord[0] - 12, mouse_coord[1] - 12))
    pygame.display.flip()
    time.sleep(0.016)
    
time.sleep(1)
exit()