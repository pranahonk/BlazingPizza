import os

def print_tree_to_file(start_path, file, indent=""):
    try:
        for item in os.listdir(start_path):
            full_path = os.path.join(start_path, item)
            if os.path.isdir(full_path):
                file.write(f"{indent}📁 {item}/\n")
                print_tree_to_file(full_path, file, indent + "    ")
            else:
                file.write(f"{indent}📄 {item}\n")
    except PermissionError:
        file.write(f"{indent}⛔ [Access Denied]\n")

# ✅ Use the current directory
root_dir = os.getcwd()

# ✅ Output file in the current directory
output_path = os.path.join(root_dir, "directory_tree.txt")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"📂 Directory Tree for: {root_dir}\n")
    print_tree_to_file(root_dir, f)

print(f"✅ Directory tree saved to: {output_path}")