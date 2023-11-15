def get_unique_words(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()

            # Split the contents into words
            words = file_contents.split()

            # Get unique words
            unique_words = set(words)

            # Convert the set to a list and sort alphabetically
            sorted_unique_words = sorted(list(unique_words))

            return sorted_unique_words
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Prompt the user for a file path
file_path = input("Enter the path to the text file: ")

# Call the function to get unique words
unique_words_list = get_unique_words(file_path)

# Print the unique words in alphabetical order
if unique_words_list:
    print("Unique words in alphabetical order:")
    for word in unique_words_list:
        print(word)