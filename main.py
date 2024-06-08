"""1masala"""

# import os
# import multiprocessing


# def word_count(path):
#     with open(path, "r") as f:
#         print(len(f.read().split()))


# def function():
#     current_dir = os.getcwd()
#     all_files = os.listdir(current_dir)

#     for file in all_files:
#         if file.endswith(".txt"):
#             file_path = os.path.join(current_dir, file)
#             p = multiprocessing.Process(target=word_count, args=(file_path,))
#             p.start()


# if __name__ == "__main__":
#     function()


"""2masala"""


# import os
# import multiprocessing


# def word_count(path):
#     count = 0
#     with open(path, "r") as f:
#         for i in f.read().split():
#             for j in i:
#                 if j.isnumeric():
#                     count += 1
#         print(count)


# def function():
#     current_dir = os.getcwd()
#     all_files = os.listdir(current_dir)

#     for file in all_files:
#         if file.endswith(".txt"):
#             file_path = os.path.join(current_dir, file)
#             p = multiprocessing.Process(target=word_count, args=(file_path,))
#             p.start()


# if __name__ == "__main__":
#     function()


"""3masala"""


# import os
# import multiprocessing


# def word_count(path):
#     count = 0
#     with open(path, "r") as f:
#         for i in f.read().split():
#             for j in i:
#                 if j in ".?!":
#                     count += 1
#         print(count)


# def function():
#     current_dir = os.getcwd()
#     all_files = os.listdir(current_dir)

#     for file in all_files:
#         if file.endswith(".txt"):
#             file_path = os.path.join(current_dir, file)
#             p = multiprocessing.Process(target=word_count, args=(file_path,))
#             p.start()


# if __name__ == "__main__":
#     function()

"""4masala"""


# import os
# import multiprocessing


# def word_count(path):
#     count = []
#     max_list = []
#     with open(path, "r") as f:
#         for i in f.read().split():
#             max_list.append(i)
#             for j in i:
#                 if j in ".?!":
#                     if len(count) < len(max_list):
#                         count = max_list.copy()
#                         max_list = []
#         print(count)


# def function():
#     current_dir = os.getcwd()
#     all_files = os.listdir(current_dir)

#     for file in all_files:
#         if file.endswith(".txt"):
#             file_path = os.path.join(current_dir, file)
#             p = multiprocessing.Process(target=word_count, args=(file_path,))
#             p.start()


# if __name__ == "__main__":
#     function()


"""5masala"""


# import os
# import multiprocessing
# import string


# def word_count(path):
#     with open(path, "r") as f:
#         new_str = []
#         word = ""
#         for i in f.read().split():
#             for j in i:
#                 if j not in string.punctuation:
#                     word += j
#             word += " "
#         new_str.append(word)
#         print(new_str)


# def function():
#     current_dir = os.getcwd()
#     all_files = os.listdir(current_dir)

#     for file in all_files:
#         if file.endswith(".txt"):
#             file_path = os.path.join(current_dir, file)
#             p = multiprocessing.Process(target=word_count, args=(file_path,))
#             p.start()


# if __name__ == "__main__":
#     function()

"""6masala"""  # 6misol sharti quyidagicha:  rasmlarni urllarini ozida saqlovchi list oching. va har bir listni ichidagi elementlar soniga
# qarab protsess yarating. Har bir protsess osha rasmni yuklab olish vazifasini bajarsin


import os
import multiprocessing

# def word_count(path):
#     with open(path, "r") as f:
#         new_str = []
#         word = ""
#         for i in f.read().split():
#             for j in i:
#                 if j not in string.punctuation:
#                     word += j
#             word += " "
#         new_str.append(word)
#         print(new_str)

mylist = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROz1TqpsJNGFIhSXHVSPdVmmOfFXsrTf95pg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGa21sspl2KjcjQkEK6hNjgL1vf7BoARNVlA&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQB8HfjgmWkToMxwH4M3yWbVWlq41MvH778AQ&s",
]


for link in mylist:
    p = multiprocessing.Process(target=link, args=())
    p.start()


if __name__ == "__main__":
    function()
