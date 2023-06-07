import hashlib
import os


def get_md5_of_file(file_path):
    """
    计算文件的md5
    """
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


md5_str = get_md5_of_file("soc222ket.zip")
print(md5_str)
# socket.zip:d1c414c3561d1a77805ef22af34302a4
#soc222ket: d1c414c3561d1a77805ef22af34302a4