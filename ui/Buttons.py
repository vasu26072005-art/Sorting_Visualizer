import pygame
import config

def createButton(x, y, width, height, text):
    rect = pygame.Rect(x, y, width, height)

    return{
        "rect" : rect,
        "text" : text
    }

def makeButtons():
    buttons = []

    buttons.append(createButton(50, 600,  120, 40, "START"))
    buttons.append(createButton(190, 600, 120, 40, "NEW ARRAY"))
    buttons.append(createButton(330, 600, 130, 40, "BUBBLE SORT"))
    buttons.append(createButton(470, 600, 140, 40, "SELECTION SORT"))
    buttons.append(createButton(620, 600, 140, 40, "INSERTION SORT"))
    buttons.append(createButton(770, 600, 120, 40, "MERGE SORT"))
    buttons.append(createButton(900, 600, 120, 40, "QUICK SORT"))

    return buttons

def checkButtonClick(buttons, mousePos):
    for button in  buttons:
        if button["rect"].collidepoint(mousePos):
            return button["text"]
    return None    