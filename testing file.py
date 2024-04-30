# Creating a file
def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("Hello, this is a testing file.")
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

# Reading a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':")
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")

# Writing to a file
def write_to_file(file_name, new_content):
    try:
        with open(file_name, 'a') as file:
            file.write("\n" + new_content)
        print("Content appended to file successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Deleting a file
def delete_file(file_name):
    import os
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Testing the functions
if __name__ == "__main__":
    file_name = "test.txt"
    create_file(file_name)
    read_file(file_name)
    write_to_file(file_name, "This is the new content.")
    read_file(file_name)
    delete_file(file_name)
