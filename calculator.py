courseRating = 69.4
courseSlope = 125

scores = [91, 87, 93, 93, 97, 83, 86, 94, 90, 85, 87, 93, 96, 91, 91, 89, 81, 87, 89, 88]

def calculateDifferential(rating, slope, score):
    return ((113/slope) * (score - rating))

def calculateIndex():
    global courseRating
    global courseSlope
    global scores

    differentials = []

    for score in scores:
        differentials.append(calculateDifferential(courseRating, courseSlope, score))

    insertionSort(differentials)

    scoresToCount = 8

    topEight = [differentials[i] for i in range(scoresToCount)]
    
    average = averageFunc(topEight)

    index = average

    return index



def averageFunc(arr):
    return sum(arr) / len(arr)

def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1

print(calculateIndex())