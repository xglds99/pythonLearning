import os


def create_files():
    for i in range(10):
        file_name = 'file_' + str(i) + '.txt'
        open('test/' + file_name, 'w')


def create_files_1():
    os.chdir('test')
    for i in range(10):
        file_name = 'file_' + str(i) + '.txt'
        open('test/' + file_name, 'w')


def modify_filename():
    os.chdir('test')
    buf_list = os.listdir()
    for file in buf_list:
        new_file = "py43" + file
        os.rename(file, new_file)
    os.chdir('../')





def modify_filename_1():
    os.chdir('test')
    buf_list = os.listdir()
    for file in buf_list:
        index = len('py43')
        new_file = file[index:]
        os.rename(file, new_file)
    os.chdir('../')


create_files()
modify_filename()
#modify_filename_1()
