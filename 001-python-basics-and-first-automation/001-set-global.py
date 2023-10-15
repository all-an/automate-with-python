# Define a global variable
global_variable = 0

# Function to set the global variable to a specific value
def set_global_variable(value):
    global global_variable
    global_variable = value

# Call the function to set the global variable
set_global_variable(42)

# Print the updated global variable
print(global_variable)  # Output will be 42
