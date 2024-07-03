# def factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     return (n * factorial(n-1))


# n = int(input("enter the number: "))
# print(f"the factorial of number is {factorial(n)}")


# def remove_a_word(l, word):
#     n = []
#     for item in l:
#         if not (item == word):
#             n.append(item.strip(word))
#     return n


# l = ["khan", "shah", "an", "shahG", "rohan"]
# print(remove_a_word(l, "an"))


# Define a to-do item as a dictionary
todo_item = {
    "task": "Buy groceries",  # The task description
    "completed": False,        # Whether the task is completed or not
}

# Create a list to store all to-do items
to_do_list = []

# Add some initial tasks (optional)
to_do_list.append(todo_item)
to_do_list.append({"task": "Finish project report", "completed": True})


def print_tasks(tasks):
    """Prints all to-do items in a formatted way.

    Args:
        tasks: A list of dictionaries representing to-do items.
    """
    for i, item in enumerate(tasks):
        status = "Completed" if item["completed"] else "Pending"
        print(f"{i+1}. {item['task']} ({status})")


def add_task(task):
    """Adds a new to-do item to the list.

    Args:
        task: The description of the to-do item.
    """
    new_item = {"task": task, "completed": False}
    to_do_list.append(new_item)


def mark_completed(index):
    """Marks a to-do item as completed based on its index in the list.

    Args:
        index: The zero-based index of the item to mark completed.
    """
    if 0 <= index < len(to_do_list):
        to_do_list[index]["completed"] = True
    else:
        print("Invalid item index.")


def main():
    """Main function to run the to-do app."""
    while True:
        print("\nTo-Do List:")
        print_tasks(to_do_list)

        print("\nMenu:")
        print("1. Add a task")
        print("2. Mark a task completed")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the new task: ")
            add_task(task)
        elif choice == "2":
            print("Enter the index of the task to mark complete:")
            try:
                index = int(input()) - 1  # Adjust for zero-based indexing
                mark_completed(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
