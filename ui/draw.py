import pygame
import config


def drawArray(screen, arr, highlightIndices=None, sortedIndices = None, swapIndices = None):

    screen.fill(config.backGroundColour)

    # Layout
    barAreaTop = 125
    buttonAreaHeight = 100
    barAreaHeight = config.height - barAreaTop - buttonAreaHeight

    # Bar spacing
    barWidth = config.width // len(arr)
    maxValue = max(arr)

    for i, val in enumerate(arr):

        barHeight = int(
            (val / maxValue) * (barAreaHeight - 15)
        )

        x = i * barWidth + 2
        y = barAreaTop + barAreaHeight - barHeight

        color = config.blue

        if sortedIndices and i in sortedIndices:
            color = config.green

        if highlightIndices and i in highlightIndices:
            color = config.yellow

        if swapIndices and i in swapIndices:
            color = config.red    

        pygame.draw.rect(
            screen,
            color,
            (
                x,
                y,
                barWidth - 4,
                barHeight
            ),
            border_radius=4
        )


def drawText(screen, text, x, y, font, color):

    textSurface = font.render(text, True, color)
    screen.blit(textSurface, (x, y))


def drawButton(screen, text, rect, font, color):

    # Button
    pygame.draw.rect(
        screen,
        color,
        rect,
        border_radius=12
    )

    # Border
    pygame.draw.rect(
        screen,
        config.grey,
        rect,
        width=1,
        border_radius=12
    )

    # Text
    textSurface = font.render(
        text,
        True,
        config.white
    )

    xPos = rect.x + (
        rect.width - textSurface.get_width()
    ) // 2

    yPos = rect.y + (
        rect.height - textSurface.get_height()
    ) // 2

    screen.blit(
        textSurface,
        (xPos, yPos)
    )


def checkMouseOver(rect):

    mousePos = pygame.mouse.get_pos()

    return rect.collidepoint(mousePos)


def drawComplexityPanel(screen, algorithm, complexityData, font):

    if algorithm is None:
        return

    data = complexityData[algorithm]

    panelRect = pygame.Rect(
        35,
        25,
        400,
        90
    )

    pygame.draw.rect(
        screen,
        config.buttonColour,
        panelRect,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        config.grey,
        panelRect,
        width=1,
        border_radius=10
    )

    # Algorithm name
    drawText(
        screen,
        algorithm,
        50,
        32,
        font,
        config.white
    )

    smallFont = pygame.font.SysFont("arial", 14)

    # First complexity line
    drawText(
        screen,
        f"Best: {data['best']}   Avg: {data['average']}",
        50,
        65,
        smallFont,
        config.grey
    )

    # Second complexity line
    drawText(
        screen,
        f"Worst: {data['worst']}   Space: {data['space']}",
        50,
        87,
        smallFont,
        config.grey
    )