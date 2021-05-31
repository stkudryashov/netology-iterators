import hashlib


def string_hash(file_path):
    with open(file_path, 'r') as read_file:
        for line in read_file.readlines():
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for link in string_hash('links.txt'):
    print(link)
