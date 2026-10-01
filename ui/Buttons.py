import pygame
import config


def createButton(x, y, width, height, text):
    rect = pygame.Rect(x, y, width, height)

    return {
        "rect": rect,
        "text": text
    }


def makeButtons():
    buttons = []

    buttonTexts = [
        "START",
        "NEW ARRAY",
        "BUBBLE SORT",
        "SELECTION SORT",
        "INSERTION SORT",
        "MERGE SORT",
        "QUICK SORT"
    ]

    sideMargin = 35
    gap = 12

    buttonWidth = (
        config.width
        - (sideMargin * 2)
        - (gap * (len(buttonTexts) - 1))
    ) // len(buttonTexts)

    buttonHeight = 48
    buttonY = config.height - 75

    for i, text in enumerate(buttonTexts):

        x = sideMargin + i * (buttonWidth + gap)

        buttons.append(
            createButton(
                x,
                buttonY,
                buttonWidth,
                buttonHeight,
                text
            )
        )

    return buttons


def checkButtonClick(buttons, mousePos):
    for button in buttons:
        if button["rect"].collidepoint(mousePos):
            return button["text"]

    return None