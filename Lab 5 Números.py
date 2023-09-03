def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
   
    input_str = input("Ingresa una serie de números separados por espacios: ")
    num_strings = input_str.split()

    try:
        num_list = [int(num) for num in num_strings]
    except ValueError:
        print("Error: Ingresa solo números separados por espacios.")
        return

    selection_sort(num_list)

    print("Lista ordenada:")
    for num in num_list:
        print(num, end=" ")

if __name__ == "__main__":
    main()
