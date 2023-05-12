#  ____                    _     _       ____             _ _ _               ____
# / ___| _ __   __ _ _ __ (_)___| |__   / ___| _ __   ___| | (_)_ __   __ _  | __ )  ___  ___
# \___ \| '_ \ / _` | '_ \| / __| '_ \  \___ \| '_ \ / _ \ | | | '_ \ / _` | | |_ \ / _ \/ _ \
#  ___) | |_) | (_| | | | | \__ \ | | |  ___) | |_) |  __/ | | | | | | (_| | | |_) |  __/  __/
# |____/| .__/ \__,_|_| |_|_|___/_| |_| |____/| .__/ \___|_|_|_|_| |_|\__, | |____/ \___|\___|
#       |_|                                   |_|                     |___/

# CREDITS
# Author: Alex lo Storto
# Github: https://github.com/alexlostorto
# Website: https://alexlostorto.github.io/

# All code is mine and subject to the MIT License


import os
import sys
import random

import pygame.mouse
from pygame.locals import *
from src.Graphics import *

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spanish Spelling Bee')

# COLOURS
DARK_PINK = '#C475AF'
PINK = '#F7A8E2'
GOLD = '#FFAE42'
BLACK = '#000000'
LIGHT_BROWN = '#E5AA70'
DARK_BROWN = '#B87333'
WHITE = '#FFFFFF'
GREEN = '#00FF00'
RED = '#FF0000'
GHOST_WHITE = '#C0C0C0'

# PYGAME VARIABLES
FPS = 60
MENU_STATE = 'title_screen'
CURSOR = pygame.mouse.get_pos()

# POSITION VARIABLES
SX = 100  # Top left X
SY = 150  # Top left Y
GRID_WIDTH = 490
GRID_HEIGHT = 490
SQUARE_SIZE = 70
STATS_WIDTH = WIDTH - GRID_WIDTH - SX

currentDirectory = os.path.dirname(__file__)


def get_translations():
    translations = []
    with open(os.path.join(currentDirectory, 'src/translations/Spanish_Words'), 'r', encoding='utf-8') as spanishFile:
        for spanishWord in spanishFile:
            spanishWord = spanishWord.replace('\n', '')
            translations.append([spanishWord])
    with open(os.path.join(currentDirectory, 'src/translations/English_Translations'), 'r', encoding='utf-8') as englishFile:
        i = 0
        for englishTranslation in englishFile:
            englishTranslation = englishTranslation.replace('\n', '')
            translations[i].append(englishTranslation)
            i += 1

    return translations


# GAME VARIABLES
CHOSEN = []
ENGLISH_WORD = ''
SPANISH_WORD = ''
PLAY_GROUP = []
TRANSLATIONS = get_translations()

# INPUT VARIABLES
INPUT_TEXT = ''
INPUT_FOCUS = False
INPUT_ACTIVE = False
INPUT_QUESTION = ''
INPUT_FONT = None
INPUT_POS = None
INPUT_ALIGN = ''
INPUT_BASE_COLOUR = None
INPUT_FOCUS_COLOUR = None
INPUT_FONT_COLOUR = None
INPUT_PURPOSE = None
INPUT_COUNTER = 0

# MESSAGE VARIABLES
MESSAGE_TEXT = ''
MESSAGE_ACTIVE = False
MESSAGE_FONT = None
MESSAGE_POS = None
MESSAGE_ALIGN = ''
MESSAGE_COLOUR = None
MESSAGE_BASE_COLOUR = None
MESSAGE_HOVER_COLOUR = None
MESSAGE_FONT_COLOUR = None
MESSAGE_RECT = None

# IMAGES
BG = pygame.image.load(os.path.join(currentDirectory, 'src/assets/gradient.png')).convert_alpha()
exit_img = pygame.image.load(os.path.join(currentDirectory, 'src/assets/Red_X.png')).convert_alpha()


def get_font(size):  # Returns font in desired size
    return pygame.font.Font(os.path.join(currentDirectory, 'src/assets/cute_font.ttf'), size)


def main_menu():
    global MENU_STATE
    global CHOSEN

    SCREEN.blit(BG, (0, 0))

    # Draw title
    TITLE = textRect(text='SPANISH SPELLING BEE', font=get_font(100), base_colour=BLACK, hover_colour=BLACK,
                     pos=(640, 100))
    TITLE.draw(SCREEN)

    # Play button
    PLAY_BUTTON = rect(width=370, height=109, base_colour=GHOST_WHITE, hover_colour=GHOST_WHITE, alpha=150,
                       pos=(640, 250), align='centre')
    PLAY_TEXT = textRect(text='PLAY', font=get_font(75), base_colour=WHITE, hover_colour=DARK_PINK,
                         pos=(640, 250))
    PLAY_BUTTON.draw(SCREEN)
    PLAY_TEXT.draw(SCREEN)

    # Options button
    OPTIONS_BUTTON = rect(width=585, height=109, base_colour=GHOST_WHITE, hover_colour=GHOST_WHITE, alpha=150,
                          pos=(640, 400), align='centre')
    OPTIONS_TEXT = textRect(text='OPTIONS', font=get_font(75), base_colour=WHITE, hover_colour=DARK_PINK,
                            pos=(640, 400))
    OPTIONS_BUTTON.draw(SCREEN)
    OPTIONS_TEXT.draw(SCREEN)

    # Quit button
    QUIT_BUTTON = rect(width=354, height=109, base_colour=GHOST_WHITE, hover_colour=GHOST_WHITE, alpha=150,
                       pos=(640, 550), align='centre')
    QUIT_TEXT = textRect(text='QUIT', font=get_font(75), base_colour=WHITE, hover_colour=DARK_PINK,
                         pos=(640, 550))
    QUIT_BUTTON.draw(SCREEN)
    QUIT_TEXT.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_TEXT.checkForInput():
                MENU_STATE = 'play'
                CHOSEN = []
                for i in range(len(TRANSLATIONS)):
                    CHOSEN.append(i)
            if OPTIONS_TEXT.checkForInput():
                MENU_STATE = 'options'
            if QUIT_TEXT.checkForInput():
                pygame.quit()
                sys.exit()


def play():
    global MENU_STATE
    global MESSAGE_ACTIVE

    def generateWord():
        global CHOSEN
        global SPANISH_WORD
        global ENGLISH_WORD

        if len(CHOSEN) > 0:
            index = random.randint(0, len(CHOSEN) - 1)
            i = CHOSEN[index]
            translation = TRANSLATIONS[i]
            SPANISH_WORD = translation[0]
            ENGLISH_WORD = translation[1]
            CHOSEN.pop(index)
        else:
            print('Ran out of words')
            return

    def load_static():
        global PLAY_GROUP

        if len(PLAY_GROUP) == 0:
            # Spelling bee header
            HEADER_TEXT = textRect(text='SPANISH SPELLING BEE', font=get_font(45), base_colour=BLACK,
                                   hover_colour=BLACK, pos=(640, 80))

            # Outer translations background
            TRANSLATION_RECT = rect(width=1100, height=350, base_colour=WHITE, hover_colour=WHITE, alpha=60,
                                    pos=(WIDTH // 2, 325), align='centre')

            # Inner translation backgrounds
            SPANISH_TRANSLATION_RECT = rect(width=450, height=200, base_colour=WHITE, hover_colour=WHITE, alpha=60,
                                            pos=(365, 350), align='centre')
            ENGLISH_TRANSLATION_RECT = rect(width=450, height=200, base_colour=WHITE, hover_colour=WHITE, alpha=60,
                                            pos=(915, 350), align='centre')

            # Inner translation headers
            SPANISH_HEADER_TEXT = textRect(text='SPANISH', font=get_font(45), base_colour=WHITE,
                                           hover_colour=WHITE, pos=(365, 200))
            ENGLISH_HEADER_TEXT = textRect(text='ENGLISH', font=get_font(45), base_colour=WHITE,
                                           hover_colour=WHITE, pos=(915, 200))

            # Generate translation background
            GENERATE_RECT = rect(width=450, height=100, base_colour=WHITE, hover_colour=WHITE, alpha=60,
                                 pos=(WIDTH // 2, 600), align='centre')

            # Creates list with all items
            PLAY_GROUP = [HEADER_TEXT, TRANSLATION_RECT, SPANISH_TRANSLATION_RECT, ENGLISH_TRANSLATION_RECT,
                          GENERATE_RECT, SPANISH_HEADER_TEXT, ENGLISH_HEADER_TEXT]

        for ITEM in PLAY_GROUP:
            ITEM.draw(SCREEN)

    SCREEN.fill(PINK)

    # Display static items
    load_static()

    # Display exit button
    EXIT_BUTTON = imgButton(image=exit_img, width=40, height=40, pos=(1200, 80), hover_transparency=128, align='centre')
    EXIT_BUTTON.draw(SCREEN)

    # Generate translation text
    GENERATE_TEXT = textRect(text='GENERATE', font=get_font(60), base_colour=WHITE, hover_colour=DARK_PINK,
                             pos=(WIDTH // 2, 600), align='centre')
    GENERATE_TEXT.draw(SCREEN)

    # Spanish translation text
    SPANISH_TRANSLATION_TEXT = textRect(text=SPANISH_WORD, font=get_font(40), base_colour=BLACK, hover_colour=BLACK,
                                        pos=(365, 350), align='centre')
    SPANISH_TRANSLATION_TEXT.draw(SCREEN)

    # English translation text
    ENGLISH_TRANSLATION_TEXT = textRect(text=ENGLISH_WORD, font=get_font(40), base_colour=BLACK, hover_colour=BLACK,
                                        pos=(915, 350), align='centre')
    ENGLISH_TRANSLATION_TEXT.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if GENERATE_TEXT.checkForInput():
                generateWord()
                print(CHOSEN)
            if EXIT_BUTTON.checkForInput():
                MENU_STATE = 'main'


def options():
    global MENU_STATE

    SCREEN.fill(WHITE)

    # Options text
    OPTIONS_TEXT = textRect(text='This is the OPTIONS screen', font=get_font(45), base_colour=BLACK, hover_colour=BLACK,
                            pos=(640, 260))
    OPTIONS_TEXT.draw(SCREEN)
    OPTIONS_BACK = textRect(text='BACK', font=get_font(75), base_colour=BLACK, hover_colour=GREEN, pos=(640, 460))
    if OPTIONS_BACK.draw(SCREEN):
        MENU_STATE = 'main'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if OPTIONS_BACK.checkForInput():
                MENU_STATE = 'main'


def main():
    global MENU_STATE
    global CURSOR

    run = True
    while run:
        clock.tick(FPS)

        CURSOR = pygame.mouse.get_pos()

        if MENU_STATE == 'main':
            main_menu()
        elif MENU_STATE == 'play':
            play()
        elif MENU_STATE == 'options':
            options()
        else:
            SCREEN.fill(BLACK)
            TITLE = textRect(text='SPANISH SPELLING BEE', font=get_font(70), base_colour=GOLD, hover_colour=LIGHT_BROWN,
                             pos=(640, 360))
            TITLE.draw(SCREEN)

        # Gets colour at cursor
        # print(SCREEN.get_at(CURSOR))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TITLE.checkForInput():
                    MENU_STATE = 'main'

        pygame.display.update()


if __name__ == '__main__':
    main()
