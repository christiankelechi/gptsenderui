import os
import appdirs

# Get the appropriate directory for application-specific data
# This will return the appropriate directory path for Windows, macOS, or Linux
app_data_dir = appdirs.user_data_dir()
print(app_data_dir)
# Create a file within the AppData directory
# file_name = "example.txt"
# file_path = os.path.join(app_data_dir, file_name)

# # Write data to the file
# with open(file_path, "w") as file:
#     file.write("Hello, AppData!")

# print(f"File '{file_name}' created in '{app_data_dir}'")