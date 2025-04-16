#(69, 74, 68, 70, 72, 67, 66, 70, 76, 68, 72, 79, 74, 67, 66, 71, 74, 75, 75, 76)
import statistics
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def mean(num_list):
    return float(sum(num_list)/len(num_list))


def variance(num_list):
    length = len(num_list)
    average = mean(num_list)
    total = 0
    for i in num_list:
        temp = i-average
        result = temp*temp
        total += result
    return total/(length-1)


def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break


def median(num_list):
    return statistics.median(num_list)


def mode(num_list):
    return statistics.mode(num_list)


def HelloWorld(str):
    print(str)

X = [69, 74, 68, 70, 72, 67, 66, 70, 76, 68, 72, 79, 74, 67, 66, 71, 74, 75, 75, 76]
Y = [153, 175, 155, 135, 172, 150, 115, 137, 200, 130, 140, 265, 185, 112, 140, 150, 165, 185, 210, 220]

x_axis = np.arange(-20, 20, 0.01)

avg = statistics.mean(X)
sd = statistics.stdev(X)

HelloWorld("'print'")




