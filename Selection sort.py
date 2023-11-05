def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    print("Array:", arr)

def main():
    arr = []
    while True:
        print("\nSelection Sort Menu:")
        print("1. Enter Array")
        print("2. Sort Array")
        print("3. Print Array")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter the array elements separated by space: ").split()))
        elif choice == "2":
            if not arr:
                print("Please enter an array first.")
            else:
                selection_sort(arr)
                print("Array sorted using Selection Sort.")
        elif choice == "3":
            if not arr:
                print("Array is empty. Please enter an array first.")
            else:
                print_array(arr)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()













The provided Python code demonstrates the implementation of the Selection Sort algorithm for sorting an array. It also offers a simple user interface for entering an array, sorting it, and printing the sorted array. Let's break down the code and explain the concepts in detail:

1. **`selection_sort` Function**:
   - This function implements the Selection Sort algorithm to sort an array in ascending order.
   - The function takes an array `arr` as input and sorts it in place.
   - It uses a nested loop to repeatedly select the minimum element from the unsorted part of the array and move it to the beginning of the sorted part.

2. **`print_array` Function**:
   - This function takes an array `arr` as input and prints the contents of the array.

3. **`main` Function**:
   - The main part of the code presents a menu-driven interface for user interaction.
   - When the user chooses option 1, they can enter an array by providing space-separated integers.
   - When the user chooses option 2, the code sorts the array using the `selection_sort` function and displays a message indicating that the array has been sorted.
   - When the user chooses option 3, the code prints the contents of the array.
   - The program continues to loop until the user chooses to exit.

In summary, this code provides a user-friendly way to perform selection sort on an array and visualize the sorted result. Users can enter an array, sort it, and print the sorted array using a menu-driven interface. It's a practical implementation of the Selection Sort algorithm for sorting arrays.

The code is well-structured and user-friendly, making it easy for users to work with and observe the sorting process.
