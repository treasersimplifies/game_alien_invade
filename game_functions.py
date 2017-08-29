import sys
import  pygame
from bullet import Bullet
from  alien import Alien
from time import sleep




def fire_bullet(my_settings,screen,ship,bullets):
    if len(bullets) < my_settings.bullets_allowed:
        new_bullet = Bullet(my_settings, screen, ship)
        bullets.add(new_bullet)



def check_keydowm_events(event,my_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
        ship.moving_left = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        ship.moving_right = False
    elif event.key == pygame.K_SPACE:
        fire_bullet(my_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(my_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        my_settings.initialize_dynamic_settings()
        stats.reset_stats()
        stats.game_active =True

        sb.prep_ship_left()
        sb.prep_highest_score()
        sb.prep_level()
        sb.prep_score()

        pygame.mouse.set_visible(False)
        aliens.empty()
        bullets.empty()
        creat_fleet(my_settings, screen, ship, aliens)
        ship.center_ship()

def check_events(my_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydowm_events(event, my_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(my_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)




def update_screen(my_settings, screen, stats, sb, ship, bullets, aliens, play_button):
    screen.fill(my_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()



def check_highest_score(stats, sb):
    if stats.score > stats.highest_score:
        stats.highest_score = stats.score
        with open('highest_score.txt','w') as highest_score_file:
            highest_score_file.write('%.1f'%stats.highest_score)
        sb.prep_highest_score()

def check_bullet_alien_collision(my_settings, screen, stats, sb, ship, aliens ,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions :
        for aliens in collisions.values():
            stats.score +=my_settings.alien_points*len(aliens)
            sb.prep_score()
        check_highest_score(stats, sb)
    if len(aliens) ==0 :
        bullets.empty()
        stats.level += 1
        stats.score +=stats.level
        sb.prep_level()
        my_settings.increase_speed()
        creat_fleet(my_settings, screen, ship, aliens)

def update_bullets(my_settings, screen, stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    check_bullet_alien_collision(my_settings, screen, stats, sb, ship, aliens, bullets)



def get_number_alien_x(my_settings,alien_width):
    available_space_x = my_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / (alien_width * 1.5))
    return number_aliens_x

def creat_alien(my_settings, screen, aliens, alien_number, row_number):
    alien = Alien(my_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width / 2 + 1.5 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)#  把每一个新建的alien实例注册到编组中

def get_number_rows(my_settings, ship_height, alien_height):
    available_space_y = (my_settings.screen_height - 2.5*alien_height - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def creat_fleet(my_settings, screen, ship, aliens):
    alien = Alien(my_settings, screen)
    number_aliens_x = get_number_alien_x(my_settings,alien.rect.width)
    number_rows = get_number_rows(my_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(my_settings, screen, aliens, alien_number, row_number)



def check_fleet_edges(my_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(my_settings, aliens)
            break

def change_fleet_direction(my_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += my_settings.fleet_drop_speed
    my_settings.fleet_direction *= -1

def ship_hit(my_settings, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_left >0:
        stats.ships_left -=1
        sb.prep_ship_left()
        aliens.empty()
        bullets.empty()
        creat_fleet(my_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(my_settings, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(my_settings, stats, sb, screen, ship, aliens, bullets)
            break

def update_aliens(my_settings, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(my_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        print("SHIP HIT!!")
        ship_hit(my_settings, stats, sb, screen, ship, aliens, bullets)
    check_aliens_bottom(my_settings, stats, sb, screen, ship, aliens, bullets)



