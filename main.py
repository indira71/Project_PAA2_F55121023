import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if i < 5 or i >= n-5:
            print(f"Iteration {i+1}: {arr}")
    end_time = time.time()
    print(f"After Bubble Sort: {arr}")
    print(f"Computation time: {end_time - start_time} seconds")

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        if i < 5 or i >= n-5:
            print(f"Iteration {i+1}: {arr}")
    end_time = time.time()
    print(f"After Insertion Sort: {arr}")
    print(f"Computation time: {end_time - start_time} seconds")

def bubble_sort_analysis(arr):
    n = len(arr)
    comparisons = (n - 1) * n // 2  # Number of comparisons in bubble sort

    worst_case = comparisons
    best_case = 0
    average_case = comparisons // 2

    return worst_case, best_case, average_case

def insertion_sort_analysis(arr):
    n = len(arr)

    worst_case = (n - 1) * n // 2  # Number of comparisons in insertion sort
    best_case = n - 1
    average_case = (worst_case + best_case) // 2

    return worst_case, best_case, average_case

def analyze_algorithm():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68,
           55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71,
           21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54,
           19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]
    original_arr = arr.copy()

    while True:
        print("\nMenu:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Before Bubble Sort:", original_arr)
            bubble_sort(arr.copy())
            print("\nBubble Sort Analysis:")
            worst_case, best_case, average_case = bubble_sort_analysis(arr)
            print(f"Worst Case: {worst_case} comparisons")
            print(f"Best Case: {best_case} comparisons")
            print(f"Average Case: {average_case} comparisons")
        elif choice == 2:
            print("Before Insertion Sort:", original_arr)
            insertion_sort(arr.copy())
            worst_case, best_case, average_case = insertion_sort_analysis(arr)
            print(f"Worst Case: {worst_case} comparisons")
            print(f"Best Case: {best_case} comparisons")
            print(f"Average Case: {average_case} comparisons")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

analyze_algorithm()
