#  Open or create the file

with open('test.txt', 'a+') as file:


# Append 'abcde' to the end of the file

    file.write('abcde')



# Read and display first 5 characters

    file.seek(0)                                 # Move the file pointer to the beginning
    first_five = file.read(5)
    print(f"First 5 characters: {first_five}")


    

# Display total number of characters

    file.seek(0)                                 # Move the file pointer to the beginning again
    content = file.read()
    total_characters = len(content)
    print(f"Total number of characters: {total_characters}")
