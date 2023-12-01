def bubble_sort_recursive(arr, n):
    # Base case: If the entire list is sorted
    if n == 1:
        return

    # One pass of bubble sort. After this pass, the largest element is at the end.
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap the elements if they are in the wrong order
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursively call the function with the reduced size of the list
    bubble_sort_recursive(arr, n - 1)

def main():
    # Input
    input_list = list(map(int, input("Enter Input : ").split()))

    # Call the bubble_sort_recursive function
    bubble_sort_recursive(input_list, len(input_list))

    # Output the sorted list
    print(input_list)

if __name__ == "__main__":
    main()
