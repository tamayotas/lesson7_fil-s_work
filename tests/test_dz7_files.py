import os.path, shutil
from zipfile import ZipFile

files1 = ["pdf1.pdf", "xlsx1.xlsx", "xlsx2.csv"]
text1 = "Vot tak"
dir_name1 = "resources"
zip_name1 = "/zip_file.zip"
CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)


def create_files_with_text(files, text):
    for f in files:
        with open(f, "w") as file:
            file.write(text)


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        path = os.path.join(CURRENT_DIR, dir_name)
        os.mkdir(path)


def create_zip_write_files(dir_name, zip_name, files):
    with ZipFile(dir_name + zip_name, "a") as zip_file:
        for f in files:
            zip_file.write(f)


def delete_dir_and_files(dir_name, files):
    shutil.rmtree(os.path.join(CURRENT_DIR, dir_name))
    for file in files:
        os.remove(os.path.join(CURRENT_DIR, file))


def test_read_zip_archive_files():
    create_files_with_text(files=files1, text=text1)
    create_dir(dir_name=dir_name1)
    create_zip_write_files(dir_name=dir_name1, zip_name=zip_name1, files=files1)
    with ZipFile("resources/zip_file.zip", "r") as zip_file:
        for file in files1:
            assert file in zip_file.namelist()
            assert text1 in str(zip_file.read(file))
    delete_dir_and_files(dir_name=dir_name1, files=files1)