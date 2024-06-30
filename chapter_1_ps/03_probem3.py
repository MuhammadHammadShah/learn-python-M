import os

def print_directory_contents(path):
  """Prints the contents (files and directories) of a given directory path.

  Args:
      path: The path to the directory whose contents you want to print.
  """

  # Get the list of files and directories in the specified path
  contents = os.listdir(path)

  # Print each item in the list
  for item in contents:
    print(item)

# Get the current working directory path
current_dir = os.getcwd()

# Print the contents of the current working directory
print(f"Contents of {current_dir}:")
print_directory_contents(current_dir)
