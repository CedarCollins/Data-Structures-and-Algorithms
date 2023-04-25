"""
This program compares the efficiency of several different sorting methods by
totaling and comparing the number of key comparisons and assignments in each
method.
"""

import random

"""Bubble sort: the 'bubble' goes across and carries the highest value to end on each pass
   such that there are n-1 exchanges per pass"""
def bubble_sort(a_list):
    compares, assigns = 0, 0
    
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j + 1]: #one compare
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j] #two assigns
                assigns += 2
            compares += 1
    
    return compares, assigns

"""Selection Sort: passes through the list and exchanges the highest value for the value at the end
   such that there is one exchange per pass"""
def selection_sort(a_list):
    compares, assigns = 0, 0
    
    for i, item in enumerate(a_list):
        min_idx = len(a_list) - 1 #not a key assign
        for j in range(i, len(a_list) - 1):
            if a_list[j] < a_list[min_idx]: #one compare
                min_idx = j #not a key assign
            compares += 1
        if min_idx != i: #not a key comparison
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx] #two assigns
            assigns += 2
    return compares, assigns

"""Insertion Sort: maintains a sorted sublist in the lower positions of the list and inserts each
   value into the sorted sublist as it passes through, shifting the other values down (not swapping)"""
def insertion_sort(a_list):
    compares, assigns = 0, 0
    
    for i in range(1, len(a_list)):
        loops = 0
        cur_val = a_list[i] #first assign
        cur_pos = i #second assign

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val: #one compare & one assign per loop
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1 #not a key assign (cur_pos > 0 not a key compare)
            loops += 1
        #one compare for when the while loop condition isn't satisfied
        a_list[cur_pos] = cur_val #third assign
        
        compares = compares + loops + 1
        assigns = assigns + loops + 3
        
    return compares, assigns

"""Shell Sort: insertion sorts sublists over increments that pass through the list, repeating each
   pass with the increment divided by 2 until increment//2 < 1"""
def shell_sort(a_list):
    compares, assigns = 0, 0
    
    sublist_count = len(a_list) // 2 #not a key assign
    while sublist_count > 0: #not a key compare
        for pos_start in range(sublist_count):
            temp_tuple = gap_insertion_sort(a_list, pos_start, sublist_count)
            compares, assigns = compares + temp_tuple[0], assigns + temp_tuple[1]
        sublist_count = sublist_count // 2 #not a key assign
        
    return compares, assigns

def gap_insertion_sort(a_list, start, gap):
    compares, assigns = 0, 0
    
    for i in range(start + gap, len(a_list), gap):
        loops = 0
        cur_val = a_list[i] #first assign
        cur_pos = i #second assign
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val: #one compare & one assign per loop
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap #not a key assign
            loops += 1
        #one compare for when the while loop condition isn't satisfied
        a_list[cur_pos] = cur_val #third assign
        
        compares = compares + loops + 1
        assigns = assigns + loops + 3
        
    return compares, assigns

"""Merge Sort: recurively splits the lists apart and then merges each sublist into a sorted one by
   comparing the first unsorted item in each sublist"""
def merge_sort(a_list):
    compares, assigns = 0, 0
    
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        left_tuple = merge_sort(left_half)
        right_tuple = merge_sort(right_half)
        compares, assigns = compares + left_tuple[0] + right_tuple[0], assigns + left_tuple[1] + right_tuple[1]

        i, j, k = 0, 0, 0 #not key assigns
        while i < len(left_half) and j < len(right_half): #one compare and one assign per loop
            if left_half[i] <= right_half[j]: #compare
                a_list[k] = left_half[i] #possible assign
                i = i + 1 #not a key assign
            else:
                a_list[k] = right_half[j] #other possible assign
                j = j + 1 #not a key assign
            k = k + 1 #not a key assign
            compares, assigns = compares + 1, assigns + 1

        while i < len(left_half):
            a_list[k] = left_half[i] #one assign
            i = i + 1
            k = k + 1
            assigns += 1

        while j < len(right_half):
            a_list[k] = right_half[j] #one assign
            j = j + 1
            k = k + 1
            assigns += 1

    return compares, assigns

"""Quick Sort: uses a pivot and left and right marks to create two more sorted piles as the marks
   converge, using recursion to sort these piles and so on"""
def quick_sort(a_list):
    temp_tuple = quick_sort_helper(a_list, 0, len(a_list) - 1)
    return temp_tuple[0], temp_tuple[1]

def quick_sort_helper(a_list, first, last):
    compares = 0
    assigns = 0
    
    if first < last:
        temp_tuple = partition(a_list, first, last)
        split = temp_tuple[0]
        
        temp_tuple1 = quick_sort_helper(a_list, first, split - 1)
        temp_tuple2 = quick_sort_helper(a_list, split + 1, last)

        compares += temp_tuple[1] + temp_tuple1[0] + temp_tuple2[0]
        assigns += temp_tuple[2] + temp_tuple1[1] + temp_tuple2[1]
    return compares, assigns

def partition(a_list, first, last):
    compares = 0
    assigns = 0
    
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val: #first compare
            left_mark = left_mark + 1 #not a key assign
            compares += 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val: #second compare
            right_mark = right_mark - 1 #not a key assign
            compares += 1
        compares += 2 #for when the while loop conditions are not met
        if right_mark < left_mark: #not a key compare
            done = True
        else:
            assigns += 2 #two assigns below
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
                
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first] #two assigns
    assigns += 2

    return right_mark, compares, assigns

def main():
    random10 = [random.randrange(0,100) for x in range(10)]
    random100 = [random.randrange(0,1000) for x in range(100)]
    random1000 = [random.randrange(0,10000) for x in range(1000)]
    random10000 = [random.randrange(0,100000) for x in range(10000)]

    bubble10 = bubble_sort(random10[:])
    selection10 = selection_sort(random10[:])
    insertion10 = insertion_sort(random10[:])
    shell10 = shell_sort(random10[:])
    merge10 = merge_sort(random10[:])
    quick10 = quick_sort(random10[:])

    bubble100 = bubble_sort(random100[:])
    selection100 = selection_sort(random100[:])
    insertion100 = insertion_sort(random100[:])
    shell100 = shell_sort(random100[:])
    merge100 = merge_sort(random100[:])
    quick100 = quick_sort(random100[:])

    bubble1000 = bubble_sort(random1000[:])
    selection1000 = selection_sort(random1000[:])
    insertion1000 = insertion_sort(random1000[:])
    shell1000 = shell_sort(random1000[:])
    merge1000 = merge_sort(random1000[:])
    quick1000 = quick_sort(random1000[:])
    
    bubble10000 = bubble_sort(random10000[:])
    selection10000 = selection_sort(random10000[:])
    insertion10000 = insertion_sort(random10000[:])
    shell10000 = shell_sort(random10000[:])
    merge10000 = merge_sort(random10000[:])
    quick10000 = quick_sort(random10000[:])
    
    print("Number of list comparisons and assignments for Chapter 6 sorting algorithms",
          "on identical random lists of N elements\n(NOTE: use of temp variables in swaps",
          "replaced by simultaneous assignment)\n")
    print('N'.rjust(5), 'Bubble Sort'.center(19), 'Selection Sort'.center(19),
          'Insertion Sort'.center(19), 'Shell Sort'.center(19), 'Merge Sort'.center(19),
          'Quick Sort'.center(19))
    print(' '*5 + ' (compares, assigns)'*6)

    num = 0
    for indivlist in [[bubble10, selection10, insertion10, shell10, merge10, quick10],
                      [bubble100, selection100, insertion100, shell100, merge100, quick100],
                      [bubble1000, selection1000, insertion1000, shell1000, merge1000, quick1000],
                      [bubble10000, selection10000, insertion10000, shell10000, merge10000, quick10000]]:
        num += 1
        print(str(10**num).rjust(5), end=' ')
        for item in indivlist:
            print('(' + str(item[0]).rjust(8) + ',' + str(item[1]).rjust(8)+ ')', end= ' ')
        print('')

if __name__ == '__main__':
    main()
