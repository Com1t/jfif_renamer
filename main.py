import re
from os import walk, rename, remove
from os.path import join, isfile


def ls_dir(dir_path: str, regex_rule: str) -> list:
    filenames = []
    for root, dirs, files_in_dir in walk(dir_path):
        for filename in files_in_dir:
            re_match = re.match(regex_rule, filename)
            if re_match:
                filenames.append(join(root, re_match.group(1)))

    return filenames


def rename_files(filenames: list, old_ext: str, new_ext: str) -> None:
    for file in filenames:
        if isfile(rf'{file}.{new_ext}'):
            remove(rf'{file}.{new_ext}')
        rename(rf'{file}.{old_ext}', rf'{file}.{new_ext}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    old_extension = 'jfif'
    new_extension = 'jpg'
    img_dir = r'C:\Users\fuchi\Desktop\新增資料夾'
    filename_list = ls_dir(img_dir, rf"(.*)\.{old_extension}")
    rename_files(filename_list, old_extension, new_extension)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
