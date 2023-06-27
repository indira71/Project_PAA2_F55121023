import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end_time = time.time()
    return arr, end_time - start_time

def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return arr, end_time - start_time

def print_iterations(arr):
    print("5 iterasi pertama:")
    for i in range(5):
        print(arr[i], end=" ")
    print("\n5 iterasi terakhir:")
    for i in range(len(arr)-5, len(arr)):
        print(arr[i], end=" ")
    print()

def print_execution_time(sort_time):
    print("Waktu eksekusi:", round(sort_time, 6), "detik")

def print_before_after(arr, sorted_arr):
    print("Sebelum pengurutan:", arr)
    print("Setelah pengurutan:", sorted_arr)

# Main program
arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

while True:
    print("Menu:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("0. Keluar")
    choice = int(input("Masukkan pilihan Anda (1, 2, atau 0): "))

    if choice == 1:
        sorted_arr, sort_time = bubble_sort(arr.copy())
        print_iterations(sorted_arr)
        print_execution_time(sort_time)
        print_before_after(arr, sorted_arr)
    elif choice == 2:
        sorted_arr, sort_time = insertion_sort(arr.copy())
        print_iterations(sorted_arr)
        print_execution_time(sort_time)
        print_before_after(arr, sorted_arr)
    elif choice == 0:
        print("Terima kasih! Program telah selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 0.")
    print()
