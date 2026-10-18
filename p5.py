import os
import sys

# Get command-line argument
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

print("\nCurrent Directory:", os.getcwd())
print("Target Directory:", path)

# Check whether directory exists
if not os.path.exists(path):
    print("Directory does not exist.")
    sys.exit()

# Display files and folders
print("\nContents:")
for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isdir(full_path):
        print("[Folder]", item)
    else:
        print("[File]", item)

# Show text files
print("\nText Files:")
for item in os.listdir(path):
    if item.endswith(".txt"):
        print(item)

# Create workspace folder
workspace = os.path.join(path, "workspace")

if not os.path.exists(workspace):
    os.mkdir(workspace)
    print("\nWorkspace folder created.")
else:
    print("\nWorkspace folder already exists.")

# Create or read log file
log_file = os.path.join(workspace, "log.txt")

if os.path.exists(log_file):
    with open(log_file, "r") as file:
        data = file.read()

    print("\nExisting Log:")
    print(data)

else:
    with open(log_file, "w") as file:
        file.write("Workspace log created successfully.\n")

    print("\nNew log file created.")

print("\nProgram completed.")