import pygame
from pygame import mixer
import sys
mixer.init()
from pygame.locals import QUIT
import json
from main import main_game_cycle
pygame.init()
pygame.font.init()
# settings
WINDOW_WIDTH = 1020
WINDOW_HEIGHT = 48*15
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('save a cookie from kids')
COLOR_FILL = (255, 250, 205)
OUTLINE_BUTTON_COLOR = (255, 105, 180)
BLACK = (0, 0, 0)
music = pygame.mixer.music
BUTTON_COLOR = (238, 130, 238)
clock = pygame.time.Clock()
FPS = 59
cookie_amount = 0
babka_pekar_tower_obtained = False
mama_tower_obtained = False
babushka_tower_obtained = False
titlefont = pygame.font.Font(None, 70)
button_font = pygame.font.Font(None, 40)
pygame.mixer.init()


def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


def draw_button(surface, text, font, color, rect, border_color):
    pygame.draw.rect(surface, border_color, rect, 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)


def show_menu():
    menu_is_showing = True
    while menu_is_showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if start_button.collidepoint(mouse_x, mouse_y):
                    print("Start Game clicked")
                    menu_is_showing = False
                    level_select()
                elif shop_button.collidepoint(mouse_x, mouse_y):
                    print("shop clicked")
                    menu_is_showing = False
                    shop()
                elif quit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()


        window.fill(COLOR_FILL)

        draw_text(window, 'MENU', titlefont, BUTTON_COLOR, WINDOW_WIDTH // 2 - 70, 150)

        start_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 250, 200, 50)
        shop_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 350, 200, 50)
        quit_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 450, 200, 50)

        draw_button(window, 'Start', button_font, BUTTON_COLOR, start_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'Shop', button_font, BUTTON_COLOR, shop_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'Exit', button_font, BUTTON_COLOR, quit_button, OUTLINE_BUTTON_COLOR)

        pygame.display.update()

def level_select():
    texttt=""
    level_select_active = True
    while level_select_active:
        with open('data.json', 'r') as file:
            data = json.load(file)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if lvl_1_button.collidepoint(mouse_x, mouse_y):
                    print("lvl1 was clicked rn")
                    level_select_active = False
                    music.pause()
                    music1 = pygame.mixer.music
                    music1.load("assets/audio/SpiderDance.mp3")
                    music1.play(-1)
                    main_game_cycle()
                elif turn_on_hard_button.collidepoint(mouse_x, mouse_y):
                    print("hardmode on clicked rn")
                    if data["hard_mode"] == False:
                        data["hard_mode"] = True
                        with open("data.json", "w") as file:
                            json.dump(data, file)
                        texttt = "вы включили хард мод"
                    elif data["hard_mode"] == True:
                        texttt = "Хард мод уже включен."

                elif turn_off_hard_button.collidepoint(mouse_x, mouse_y):
                    print("hardmode off clicked rn")
                    if data["hard_mode"] == True:
                        data["hard_mode"] = False
                        with open("data.json", "w") as file:
                            json.dump(data, file)
                        texttt = "вы выключили хард мод"
                    elif data["hard_mode"] == False:
                        texttt = "Хард мод уже выключен."

                elif equip_skin_button.collidepoint(mouse_x, mouse_y):
                    if data["is_bulat_skin_obtained"] == True:
                        data["bulat_skin_equipped"] = True
                        with open("data.json", "w") as file:
                            json.dump(data, file)
                        texttt = "Успешно!"

                    elif data["is_bulat_skin_obtained"] == True and data["bulat_skin_equipped"] == True:
                        texttt = "ты уже выбрал этот скин!"

                    else:
                        texttt = "у тебя нет скина!"

                elif unequip_skin_button.collidepoint(mouse_x, mouse_y):
                    if data["is_bulat_skin_obtained"] == True and data["bulat_skin_equipped"] == True:
                        data["bulat_skin_equipped"] = False
                        with open("data.json", "w") as file:
                            json.dump(data, file)
                        texttt = "Успешно!"
                    elif data["is_bulat_skin_obtained"] == False:
                        texttt = "у тебя нет скина!"

                    elif data["is_bulat_skin_obtained"] == True:
                        data["bulat_skin_equipped"] = False
                        with open("data.json", "w") as file:
                            json.dump(data, file)
                        texttt = "У вас уже стоит базовый скин!"

                elif back_button.collidepoint(mouse_x, mouse_y):
                    print("back to menu was clicked rn")
                    level_select_active = False
                    show_menu()

        window.fill(COLOR_FILL)

        draw_text(window, 'LVL SETTINGS', titlefont, BUTTON_COLOR, WINDOW_WIDTH // 2 - 175, 20)
        draw_text(window, texttt, button_font, BUTTON_COLOR, WINDOW_WIDTH // 2 + 150, 440)

        lvl_1_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 100, 200, 50)
        turn_on_hard_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 200, 200, 50)
        turn_off_hard_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 300, 200, 50)
        equip_skin_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 400, 200, 50)
        back_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 600, 200, 50)
        unequip_skin_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 500, 200, 50)

        draw_button(window, 'start game', button_font, BUTTON_COLOR, lvl_1_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'turn on hard', button_font, BUTTON_COLOR, turn_on_hard_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'turn off hard', button_font, BUTTON_COLOR, turn_off_hard_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'equip bulat', button_font, BUTTON_COLOR, equip_skin_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'unequip bulat', button_font, BUTTON_COLOR, unequip_skin_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'Menu', button_font, BUTTON_COLOR, back_button, OUTLINE_BUTTON_COLOR)

        pygame.display.update()


def shop():
    global cookie_amount
    message = ""
    babka_pekar_cost = 200
    mama_cost = 350
    babushka_cost = 500
    shop_is_active = True
    while shop_is_active:
        window.fill(COLOR_FILL)
        with open('data.json', 'r') as file:
            data = json.load(file)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if bulat_buy_button.collidepoint(mouse_x, mouse_y):
                    if data["amount_of_cookies"] >= 200 and data["is_bulat_skin_obtained"] == False:
                        data ["is_bulat_skin_obtained"] = True
                        data["amount_of_cookies"] -=200
                        message = "успешно!"
                        with open("data.json", "w") as file:
                            json.dump(data, file)
                    elif data["is_bulat_skin_obtained"] == True:
                        message = "у тебя уже есть этот скин!"

                    elif data["amount_of_cookies"] < 200:
                        message = "у тебя не хватает печенек"

                elif back_button.collidepoint(mouse_x, mouse_y):
                    print("back to menu was clicked rn")
                    shop_is_active = False
                    show_menu()

        draw_text(window, 'Магазин', titlefont, BUTTON_COLOR, WINDOW_WIDTH // 2 - 100, 150)
        draw_text(window, message, button_font, BUTTON_COLOR, WINDOW_WIDTH // 2 - 130, 500)
        bulat_buy_button = pygame.Rect(WINDOW_WIDTH // 2 - 100, 250, 200, 200)
        back_button = pygame.Rect(WINDOW_WIDTH // 2 + 400, 50, 100, 100)

        draw_button(window, 'Булат', button_font, BUTTON_COLOR, bulat_buy_button, OUTLINE_BUTTON_COLOR)
        draw_button(window, 'Меню', button_font, BUTTON_COLOR, back_button, OUTLINE_BUTTON_COLOR)

        pygame.display.update()


def main():
    music.load("assets/audio/OnceUponAtime.mp3")
    music.play(-1)
    show_menu()


if __name__ == "__main__":
    main()
