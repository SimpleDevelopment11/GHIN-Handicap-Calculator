postedScores = [{"rating": 69.4, "slope": 125, "scores": [86, 81, 89, 81, 88, 92, 83, 84, 87, 84, 86, 85, 88, 85, 86]}, {"rating": 70.0, "slope": 122, "scores": [86]}, {"rating": 68.2, "slope": 123, "scores": [85]}, {"rating": 70.9, "slope": 136, "scores": [85]}, {"rating": 69.4, "slope": 130, "scores": [86]}, {"rating": 69.0, "slope": 124, "scores": [82]}]

def calculateDifferential(rating, slope, score):
    return ((113/slope) * (score - rating))

def calculateIndex():
    global postedScores
    differentials = []

    for post in postedScores:
        courseRating = post["rating"]
        courseSlope = post["slope"]
        for score in post["scores"]:
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