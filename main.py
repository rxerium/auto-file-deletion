import os 

# Set your downloads file path here
file_path = '/users/rishi/Downloads/'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("All files in the Downloads folder have successfully been deleted!")
else:
    print("Something went wrong!")