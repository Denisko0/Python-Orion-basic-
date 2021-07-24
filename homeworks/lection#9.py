
import pickle
import openpyxl




# task1
#
# new_dict = {}
#
# with open(r"files_contextmanagers/task1.txt") as file:
#     text_lines = file.readlines()
#     for index, line in enumerate(text_lines):
#         index += 1
#         if index % 2 == 0:
#             value = line
#             new_dict[key] = value
#         else:
#             key = line
#
# print(new_dict.keys())
# print(new_dict.values())
#
#
# with open(r'files_contextmanagers/task1.txt', 'w') as file:
#     for index, line in enumerate(text_lines):
#         if index % 2 != 0:
#             file.write(line.strip('\n'))
#
# with open(r'files_contextmanagers/task1.txt') as file:
#     text_lines = file.readlines()
#
# print(text_lines)












# task2

#
#
# with open(r"files_contextmanagers/task2", "rb") as task2:
#     content = pickle.load(task2)
#     new_content = sum(content) / len(content)
#     print(new_content)


# Task3


class MyOwnExel:

    def __init__(self, path):
        self.path = path
        self.exel_file = openpyxl.load_workbook(self.path)

    def __enter__(self):
        return self.exel_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.exel_file.save(self.path)
            self.exel_file.close()
        else:
            print(f'Error, your exel file has wrong format, please rewrite')
            self.exel_file.close()
            return True

with MyOwnExel("Excel.xlsx") as exel_file:
    first_sheet = excel_file.active
    text = first_sheet.cell(row=1, column=1)
    print(first_sheet["A1"].value)
    text.value = '11111'

