# TODO Найдите количество книг, которое можно разместить на дискете
result = 1.44
bytes_ = result * 1024 ** 2
lists = 100
count_of_str_ = 50
count_of_sym = 25
bytes_of_book = count_of_sym * count_of_str_ * lists * 4
count = bytes_ // bytes_of_book
print("Количество книг, помещающихся на дискету:", count)
