import os.path

current_file = os.path.abspath(__file__)

current_dir = os.path.dirname(current_file)
print(current_dir)

TMP_DIR = os.path.join(current_dir, "tmp")
print(TMP_DIR)