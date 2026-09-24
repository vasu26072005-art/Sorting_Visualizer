import pygame
import config

def drawArray(screen, arr, highlightIndices = None):
    screen.fill(config.backGroundColour)

    buttonAreaHeight = 110
    barAreaTop = 100
    barAreaHeight = config.height - buttonAreaHeight - barAreaTop

    barWidth = config.width//len(arr)

    maxValue = max(arr)

    for i, val in enumerate(arr):
        barHeight = int((val / maxValue) * (barAreaHeight - 10))
        x = i*barWidth
        y = barAreaTop + barAreaHeight - barHeight
        color = config.blue

        if highlightIndices and i in highlightIndices:
            color = config.yellow

        pygame.draw.rect(
            screen, color, (x, y, barWidth-2, barHeight)
        )    


def drawText(screen, text, x, y, font, color):
    textSurface = font.render(text, True, color)
    screen.blit(textSurface, (x,y))

def drawButton(screen, text, rect, font, color):
    pygame.draw.rect(screen,  color, rect, border_radius = 10)
    pygame.draw.rect(screen, config.grey, rect, width = 2, border_radius = 10)

    textSurface = font.render(text, True, config.white)
    xPos = rect.x + (rect.width - textSurface.get_width()) // 2
    yPos = rect.y + (rect.height - textSurface.get_height()) // 2

    screen.blit(textSurface, (xPos, yPos))

def checkMouseOver(rect):
    mousePos = pygame.mouse.get_pos()
    return rect.collidepoint(mousePos)    