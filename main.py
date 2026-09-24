import pygame
import sys
import config
from utils.helpers import generateArray
from ui.Buttons import makeButtons, checkButtonClick
from Algorithm.BubbleSort import bubbleSort
from Algorithm.SelectionSort import selectionSort
from Algorithm.InsertionSort import insertionSort
from Algorithm.MergeSort import mergeSort
from Algorithm.QuickSort import quickSort 
from ui.draw import drawArray, drawText, drawButton, checkMouseOver


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption("SORTING VISUALIZER")

font = pygame.font.SysFont("arial", 24)
titleFont = pygame.font.SysFont("arial", 32, bold = True)
buttonFont =  pygame.font.SysFont("arial", 18)

arr = generateArray(config.numberOfBars, config.minValue, config.maxValue)
buttons = makeButtons()

selectedAlgorithm = None
sorting = False
running = True


def updateDisplay(idx1, idx2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    drawArray(screen, arr, [idx1, idx2])
    pygame.display.update()
    pygame.time.delay(int(config.delay*1000))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            clickedButton = checkButtonClick(buttons, mousePos)

            if clickedButton == "NEW ARRAY":
                arr = generateArray(
                    config.numberOfBars, config.minValue, config.maxValue
                )    

            if clickedButton in ["BUBBLE SORT", "SELECTION SORT", "INSERTION SORT", "MERGE SORT", "QUICK SORT"]:
                selectedAlgorithm = clickedButton

            if clickedButton == "START":
                sorting = True    

    if sorting:

        if selectedAlgorithm == "BUBBLE SORT":
            bubbleSort(arr, updateDisplay)

        elif selectedAlgorithm == "SELECTION SORT":
            selectionSort(arr, updateDisplay)

        elif selectedAlgorithm == "INSERTION SORT":
            insertionSort(arr, updateDisplay)

        elif selectedAlgorithm == "MERGE SORT":
            mergeSort(arr, 0, len(arr)-1, updateDisplay)

        elif selectedAlgorithm == "QUICK SORT":
            quickSort(arr, 0, len(arr)-1, updateDisplay)

        sorting = False

    drawArray(screen, arr)

    drawText(screen, "SORTING VISUALIZER", 390, 25, titleFont, config.white)

    for button in buttons:
        if checkMouseOver(button["rect"]):
            color = config.buttonHoverColour
        else:
            color = config.buttonColour

        drawButton(screen, button["text"], button["rect"], buttonFont, color) 

    pygame.display.update()    

    clock.tick(60)

pygame.quit()
sys.exit()                                   