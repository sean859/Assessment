# This imports pandas and time into the project allowing you to utilize it to read the excel file, and track the time needed
import pandas as pd
import time 

# This will define a variable called 'Baby_Data' that will take all the information from the excel data called 'BirthWeight'
Baby_Data = pd.read_excel(r'C:\Users\seana\Downloads/BirthWeight.xlsx')

# Then this variable will hold all the data from the excel file under the column named 'BirthWeight' from that file
Baby_Weight_Data = list(Baby_Data.BirthWeight)

# This algortithm tasks an unsorted list and orders it in ascending value from lowest to highest
# by comparing values one and two then moving the highest value to the second position if not already present
# then switchs to values two and three moving the highest value to the second position, etc
def bubble(unsorted_list):
    unsorted_list_length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, unsorted_list_length):
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
    return unsorted_list

# The way insertion sort works by taking a unsorted list and divide it into two lists 'sorted' and 'unsorted' by placing the first
# value into sorted once the algorithm starts its takes the value on the left most position in the unsorted list and moves it
# into the sorted list then compares that same value to the value on its left in the sorted list and if that value is smaller 
# it switchs positions with the value of left, this same value keeps getting compared with the value on the left and switching
# until it compares with a value smaller then it, in which case the value is now in its proper place on the list
def insertion(unsorted_list):
    unsorted_list_length = range(1, len(unsorted_list))
    for i in unsorted_list_length:
        value_to_sort = unsorted_list[i]

        while unsorted_list[i-1] > value_to_sort and i > 0:
            unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1], unsorted_list[i]
            i = i - 1
    return unsorted_list


# Selection sort will take the first value's number and compare it every other values number on the right, till
# it gets compared to a smaller number in which case the smaller numb,,,er will become which number gets compared 
# with others, once its compared all the numbers, it should have the minimum number, now the number gets put
# into a sorted list on the left and now the others numbers are placed into a unsorted list at the end of
# an interation, then at the start of the next interation it takes the first value's number in the unsorted
# list and repeats the process till the all numbers are sorted in the sorted list from lowest to highest
def selection_sort(unsorted_list):
    list_length = range(0, len(unsorted_list)-1)

    for i in list_length:
        min_value = i

        for j in range(i + 1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[min_value]:
                min_value = j
        
        if min_value != i:
            unsorted_list[min_value], unsorted_list[i] = unsorted_list[i], unsorted_list[min_value]
    
    return unsorted_list

# Merge sort is a conquer and divide algorithm by that it means that is breaks down a list given to it into smaller list called sub
# list then breaks those sub lists into even more sub lists until the sublist contains only one value then to sort it merges 
# two sub list together into one placing the lower number on the left and the higher on the right, then once all sub lists contain
# two values it merges those list into lists of 4, again putting the lowest value on the left side and continues from lowest to highest
# then it keeps repeating this process untill all sublists have merged into one sorted list with the numbers going from lowest to 
# highest 
def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]
    result += right[j:]
    return result
def mergesort(lst):
    if(len(lst) <= 1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left, right)

# The quick sort method is done by taking an unsorted list and taking one the of the values from the list as a pivot point
# that pivot point will get compared to every other value in the list, if the compared number is smaller then the pivot
# it goes to the left side of the pivot point, and if its higher then the pivot it goes to the right, once all values
# are split in either lower or higher then the pivot point those numbers will now need to be sorted and this is done by
# turning one of those numbers and turning it into its own pivot point then that pivot gets compared to the other values
# in the list placing smaller values on the left and higher values on the right, this algorithm keeps repeating this process
# untill all the values are in either ascending or descending order (depending on on your choice), then it breaks and now
# you have a sorted list of all your original values
def quick_sort(usl):
    length = len(usl)
    if length <= 1:
        return usl
    else:
        pivot = usl.pop()

    items_greater = []
    items_lower = []

    for item in usl:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


