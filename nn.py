import os

# Define the main directory
main_folder = "100DaysOfCloud"

# Create the main directory if it doesn't exist
os.makedirs(main_folder, exist_ok=True)

# Create 100 folders inside the main directory
for i in range(1, 101):
    folder_name = f"Day-{i}"
    folder_path = os.path.join(main_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"✅ Created: {folder_path}")

print("🎯 All 100 folders have been created successfully!")
