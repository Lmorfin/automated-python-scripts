#deletes screenshots cluttered in my desktop
import os

path = "/Users/luism/Desktop"

try:
    desktop_files = os.listdir(path)
    screenshot_files = [file for file in desktop_files if file.startswith("Screenshot")]

    if screenshot_files:
        print("\nFound the following screenshot files:\n")
        for file in screenshot_files:
            file_path = os.path.join(path, file)
            print("Removing.. " , file_path)
            os.remove(file_path)
        print("\nSuccessfully deleted screenshot files.\n")
    else:
        print("\nNo screenshot files found.")

except Exception as e:
    print("An error as occurred ", e)
