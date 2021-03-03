#  Exercise 1
# my_file = open("hens.txt")
# file_content = my_file.read()
# print(file_content)
# new_string = file_content.replace("/"," ") # don't forget to save result
# print(new_string)

#  Exercise 2
# my_file = open("names.txt")
# file_content = my_file.read()
# print(file_content)
#
# new_string = file_content.replace(" ","\n") # don't forget to save result
# print(new_string)

#  Exercise 3
# def show_low_tides(filename):
#     tide_file = open(filename)
#     tide_list = tide_file.readlines()
#     for line in tide_list:
#             tokens = line.split(",")
#             print(tokens[1], "\t", tokens[3])
# #main routine
# show_low_tides('tides.txt')
#
# def show_low_tides(filename):
#     tide_file = open(filename)
#     tide_list = tide_file.readlines()
#     for line in tide_list:
#         tokens = line.split(",")
#         if line == tide_list[0]:
#             print( " Date","\t\t","Low tides")  # new header line
#         else:
#             print(tokens[1], "\t\t", tokens[3])
# #main routine
# show_low_tides

