# Nathan Grace, Project 2
# Sorting Algorithms = bubble sort, quick sort, merge sort, and selection sort

# bubble sort:
import random, time, sys

def bubbleSort_(myList): # Bubble Sort Algorithm
    done = False
    for i in range(len(myList)-1):
        swap = False
        if not done:
            for j in range(len(myList)-i-1):
                if myList[j] > myList[j + 1]:
                    myList[j], myList[j+1] = \
                           myList[j + 1], myList[j]
                    swap = True
            if not swap:
                done = True
                break
    return myList

def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def quick_sort(arr, low, high): # Quick Sort Algorithm
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
        
def SelectionSort(A):

 for i in range(len(A)):
    # Code from geeks4geekss:
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]

size = input('Please enter number of elements to sort: ')

def main(k = 100):
    # IO
    # open file
    data_file = open('data.txt', 'w')
    ans = True
    while ans:
        print ("""
           Please Select a Sorting Algorithm to Test:
               1. Bubble Sort
               2. Merge Sort
               3. Quick Sort
               4. Selection Sort
               5. Exit
               """)
        ans = input("Enter your choice: ")
        
        
        if ans == "1":
            #m = [random.randint(1, 10*k) for i in range(k)]
            m = random.sample(range(10*k), k)
            #print(m)
            #random case n
            t1 = time.perf_counter()
            sortedList = bubbleSort_(m)
            t2 = time.perf_counter()
    
            print('Bubble sort', k, 'average case:', ((t2-t1), 5), 'seconds')
            data_file.write('Bubble sort, ' + str(k) + ' items Average Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            # print(m)
            # best case n^2
            t1 = time.perf_counter()
            sortedList = bubbleSort_(m)
            t2 = time.perf_counter()
            print('Bubble sort', k, 'best case:', ((t2-t1), 5), 'seconds')
            data_file.write('Bubble sort, ' + str(k) + ' items Best Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
    
            #worst case n^2
            m.reverse()
            t1 = time.perf_counter()
            sortedList = bubbleSort_(m)
            t2 = time.perf_counter()
            print('Bubble sort', k, 'worst case:', ((t2-t1), 5), 'seconds')
            data_file.write('Bubble sort, ' + str(k) + ' items Worst Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            data_file.write('\n')
            
            
        
        if ans == "2":
            m = []
            for i in range(k):
                m.append(random.randint(1, 2*k))
            
            t1 = time.perf_counter()
            t2 = time.perf_counter()
            
            # Average case n log n
            t0 = time.perf_counter()
            sortedList = merge_sort(m)
            t = time.perf_counter()
            print('Merge sort', k, 'Average Case:', t-t0, 'seconds.')
            data_file.write('Merge sort, ' + str(k) + ' items Average Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
            # Best Case n log n
            t1 = time.perf_counter()
            sortedList = merge_sort(m)
            t2 = time.perf_counter()
            print('Merge sort', k, 'Best Case:', t-t0, 'seconds.')
            data_file.write('Merge sort, ' + str(k) + ' items Best Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
            # Worst Case n log n
            m.reverse()
            t0 = time.perf_counter()
            sortedList = merge_sort(m)
            t = time.perf_counter()
            print('Merge sort', k, 'Worst Case:', t-t0, 'seconds.')
            data_file.write('Merge sort, ' + str(k) + ' items Worst Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            data_file.write('\n')
            
        if ans == "3":
            m = []
            for i in range(k):
                m.append(random.randint(1, 2*k))
                
            t1 = time.perf_counter()
            t2 = time.perf_counter()
            
            # Average Case n log n
            t0 = time.perf_counter()
            sortedList = quick_sort(m, 0, (len(m)-1))
            t = time.perf_counter()
            print('Quick Sort', k, 'Average Case:', t-t0, 'seconds')
            data_file.write('Quick sort, ' + str(k) + ' items Average Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
            # Best Case n log n
            t1 = time.perf_counter()
            sortedList = quick_sort(m, 0, (len(m)-1))
            t2 = time.perf_counter()
            print('Quick Sort', k, 'Best Case:', t-t0, 'seconds')
            data_file.write('Quick sort, ' + str(k) + ' items Best Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
            # Worst Case n log n
            sortedArr = merge_sort(m)
            t0 = time.perf_counter()
            sortedList = quick_sort(sortedArr, 0, (len(m)-1))
            t = time.perf_counter()
            print('Quick sort', k, 'Worst Case:', t-t0, 'seconds.')
            data_file.write('Quick sort, ' + str(k) + ' items Worst Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            data_file.write('\n')
            
        if ans == "4":
            m = []
            for i in range(k):
                m.append(random.randint(1, 2*k))
            
            t1 = time.perf_counter()
            t2 = time.perf_counter()
            
            # Average case n log n
            t0 = time.perf_counter()
            sortedList = SelectionSort(m)
            t = time.perf_counter()
            print('Selection sort', k, 'Average Case:', t-t0, 'seconds.')
            data_file.write('Selection sort, ' + str(k) + ' items Average Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
            # Best Case n log n
            t1 = time.perf_counter()
            sortedList = SelectionSort(m)
            t2 = time.perf_counter()
            print('Selection sort', k, 'Best Case:', t-t0, 'seconds.')
            data_file.write('Selection sort, ' + str(k) + ' items Best Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
            # Worst Case n log n
            m.reverse()
            t0 = time.perf_counter()
            sortedList = SelectionSort(m)
            t = time.perf_counter()
            print('Selection sort', k, 'Worst Case:', t-t0, 'seconds.')
            data_file.write('Selection sort, ' + str(k) + ' items Worst Case: ' + str(((t2-t1))) + ' seconds')
            data_file.write('\n')
            
        if ans == "5":
            ans = False
            data_file.close()
            print("\nBye for now!")
            sys.exit()
            break
      
if __name__ == "__main__":
    main(int(size))
    
