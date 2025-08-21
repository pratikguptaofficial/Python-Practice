#Task 1 : Read a File and Handle Errors

# Try to open and read the file
#try:
#    file = open("sample.txt", "r")   # open file in read mode
#    print("Reading file content:")
#
#    for line in file:                 # go through each line
#        print(line.strip())           # print the line (without extra spaces)
#
#    file.close()                      # close the file
#
## If the file does not exist
#except:
#    print("Error: sample.txt not found.")


#Task 2 : Write and Append Data to a File

# Step 1: Write user input to a file
text = input("Enter text to write to the file: ")
file = open("output.txt", "w")   # "w" = write mode (creates/overwrites file)
file.write(text + "\n")
file.close()
print("Data successfully written to output.txt.")

# Step 2: Append more user input to the same file
extra_text = input("Enter additional text to append: ")
file = open("output.txt", "a")   # "a" = append mode (adds at the end)
file.write(extra_text + "\n")
file.close()
print("Data successfully appended.")

# Step 3: Read and display the final content of the file
file = open("output.txt", "r")   # "r" = read mode
print("\nFinal content of output.txt:")
print(file.read())
file.close()









