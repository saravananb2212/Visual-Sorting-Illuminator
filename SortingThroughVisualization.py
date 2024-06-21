import pygame
import random
import time

# Constants
SCREEN_WIDTH = 910
SCREEN_HEIGHT = 750
RECT_SIZE = 7

# Colors
BACKGROUND_COLOR = (0, 0, 0)
COMPARE_COLOR = (165, 105, 189)
SWAP_COLOR = (100, 180, 100)
SORTED_COLOR = (100, 180, 100)
DEFAULT_COLOR = (170, 183, 184)

# Initialize array
arr = []
Barr = []
paused = False

def init():
    global screen, font
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sorting Visualizer")
    font = pygame.font.SysFont(None, 24)

def close():
    pygame.quit()

def draw_text(text, x, y, color=(255, 255, 255)):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

def visualize(x=-1, y=-1, z=-1, description=''):
    screen.fill(BACKGROUND_COLOR)
    for i in range(len(arr)):
        color = DEFAULT_COLOR
        if complete:
            color = SORTED_COLOR
        elif i == x or i == z:
            color = SWAP_COLOR
        elif i == y:
            color = COMPARE_COLOR
        pygame.draw.rect(screen, color, (i * RECT_SIZE, SCREEN_HEIGHT - arr[i], RECT_SIZE, arr[i]))
    
    draw_text(description, 10, 10)
    pygame.display.flip()

def inplaceHeapSort(input):
    description = "Heap Sort: O(n log n) - In-place sorting algorithm."
    for i in range(1, len(input)):
        if paused: pause()
        childIndex = i
        parentIndex = (childIndex - 1) // 2

        while childIndex > 0 and input[childIndex] > input[parentIndex]:
            input[childIndex], input[parentIndex] = input[parentIndex], input[childIndex]
            visualize(parentIndex, childIndex, description=description)
            pygame.time.delay(40)
            childIndex = parentIndex
            parentIndex = (childIndex - 1) // 2

    for heapLast in range(len(input) - 1, 0, -1):
        if paused: pause()
        input[0], input[heapLast] = input[heapLast], input[0]
        parentIndex = 0
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        while leftChildIndex < heapLast:
            if paused: pause()
            maxIndex = parentIndex
            if input[leftChildIndex] > input[maxIndex]:
                maxIndex = leftChildIndex
            if rightChildIndex < heapLast and input[rightChildIndex] > input[maxIndex]:
                maxIndex = rightChildIndex
            if maxIndex == parentIndex:
                break

            input[parentIndex], input[maxIndex] = input[maxIndex], input[parentIndex]
            visualize(maxIndex, parentIndex, heapLast, description)
            pygame.time.delay(40)

            parentIndex = maxIndex
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2

def partition_array(a, si, ei):
    count_small = 0
    description = "Quick Sort: O(n log n) - Efficient, in-place sorting algorithm."
    for i in range(si + 1, ei + 1):
        if paused: pause()
        if a[i] <= a[si]:
            count_small += 1
    c = si + count_small
    a[si], a[c] = a[c], a[si]
    visualize(c, si, description=description)

    i, j = si, ei
    while i < c and j > c:
        if paused: pause()
        if a[i] <= a[c]:
            i += 1
        elif a[j] > a[c]:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            visualize(i, j, description=description)
            pygame.time.delay(70)
            i += 1
            j -= 1
    return c

def quickSort(a, si, ei):
    if si >= ei:
        return
    c = partition_array(a, si, ei)
    quickSort(a, si, c - 1)
    quickSort(a, c + 1, ei)

def merge2SortedArrays(a, si, ei):
    description = "Merge Sort: O(n log n) - Divide and conquer sorting algorithm."
    size_output = ei - si + 1
    output = [0] * size_output
    mid = (si + ei) // 2
    i, j, k = si, mid + 1, 0
    while i <= mid and j <= ei:
        if paused: pause()
        if a[i] <= a[j]:
            output[k] = a[i]
            visualize(i, j, description=description)
            i += 1
        else:
            output[k] = a[j]
            visualize(i, j, description=description)
            j += 1
        k += 1

    while i <= mid:
        if paused: pause()
        output[k] = a[i]
        visualize(-1, i, description=description)
        i += 1
        k += 1

    while j <= ei:
        if paused: pause()
        output[k] = a[j]
        visualize(-1, j, description=description)
        j += 1
        k += 1

    for l in range(size_output):
        if paused: pause()
        a[si + l] = output[l]
        visualize(si + l, description=description)
        pygame.time.delay(15)

def mergeSort(a, si, ei):
    if si >= ei:
        return
    mid = (si + ei) // 2
    mergeSort(a, si, mid)
    mergeSort(a, mid + 1, ei)
    merge2SortedArrays(a, si, ei)

def bubbleSort():
    description = "Bubble Sort: O(n^2) - Simple but inefficient sorting algorithm."
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if paused: pause()
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualize(j + 1, j, description=description)
            pygame.time.delay(1)

def insertionSort():
    description = "Insertion Sort: O(n^2) - Efficient for small or nearly sorted arrays."
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and arr[j] > temp:
            if paused: pause()
            arr[j + 1] = arr[j]
            j -= 1
            visualize(i, j + 1, description=description)
            pygame.time.delay(5)
        arr[j + 1] = temp

def selectionSort():
    description = "Selection Sort: O(n^2) - Simple but inefficient sorting algorithm."
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if paused: pause()
            if arr[j] < arr[minIndex]:
                minIndex = j
                visualize(i, minIndex, description=description)
            pygame.time.delay(1)
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def loadArr():
    global arr
    arr = Barr[:]

def randomizeAndSaveArray():
    global Barr
    Barr = [random.randint(0, SCREEN_HEIGHT) for _ in range(ARR_SIZE)]

def pause():
    global paused
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False

def execute():
    global complete
    init()
    if custom_array:
        loadArr()
    else:
        randomizeAndSaveArray()
        loadArr()

    running = True
    complete = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                complete = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    complete = False
                    print("\nEXITING SORTING VISUALIZER.\n")
                elif event.key == pygame.K_0:
                    if custom_array:
                        loadArr()
                    else:
                        randomizeAndSaveArray()
                        complete = False
                        loadArr()
                        print("\nNEW RANDOM LIST GENERATED.\n")
                elif event.key == pygame.K_1:
                    loadArr()
                    print("\nSELECTION SORT STARTED.\n")
                    complete = False
                    selectionSort()
                    complete = True
                elif event.key == pygame.K_2:
                    loadArr()
                    print("\nINSERTION SORT STARTED.\n")
                    complete = False
                    insertionSort()
                    complete = True
                elif event.key == pygame.K_3:
                    loadArr()
                    print("\nBUBBLE SORT STARTED.\n")
                    complete = False
                    bubbleSort()
                    complete = True
                elif event.key == pygame.K_4:
                    loadArr()
                    print("\nMERGE SORT STARTED.\n")
                    complete = False
                    mergeSort(arr, 0, len(arr) - 1)
                    complete = True
                elif event.key == pygame.K_5:
                    loadArr()
                    print("\nQUICK SORT STARTED.\n")
                    complete = False
                    quickSort(arr, 0, len(arr) - 1)
                    complete = True
                elif event.key == pygame.K_6:
                    loadArr()
                    print("\nHEAP SORT STARTED.\n")
                    complete = False
                    inplaceHeapSort(arr)
                    complete = True
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        print("\nPAUSED.\n")
                    else:
                        print("\nRESUMED.\n")
        visualize(description='')
        pygame.time.delay(100)
    close()

def controls():
    print("\nPress '0' to generate a new random list.")
    print("Press '1' to start Selection Sort.")
    print("Press '2' to start Insertion Sort.")
    print("Press '3' to start Bubble Sort.")
    print("Press '4' to start Merge Sort.")
    print("Press '5' to start Quick Sort.")
    print("Press '6' to start Heap Sort.")
    print("Press 'p' to pause/resume the visualization.")
    print("Press 'q' to exit.")
    cont = input("\nDo you want to continue? (Y/N): ")
    return cont.lower() == 'y'

def intro():
    print("\nWELCOME TO THE SORTING VISUALIZER.\n")
    global ARR_SIZE, custom_array, Barr

    ARR_SIZE = int(input("Enter the number of elements to sort: "))

    custom_input = input("Do you want to provide a custom array? (Y/N): ").lower()
    if custom_input == 'y':
        custom_array = True
        Barr = list(map(int, input("Enter the array elements separated by space: ").split()))
    else:
        custom_array = False

intro()
while controls():
    execute()
