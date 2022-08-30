courseRating = 68
courseSlope = 122

scores = [90, 88, 90, 95, 87, 82, 93, 90, 90, 92, 85, 80, 84, 81, 90, 89, 89, 85, 90, 89]

def calculateDifferential(rating, slope, score):
    return ((113/slope) * (score - rating))

def calculateIndex():
    global courseRating
    global courseSlope
    global scores

    differentials = []

    for score in scores:
        differentials.append(calculateDifferential(courseRating, courseSlope, score))



def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1