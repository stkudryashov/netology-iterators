import json


class Countries:
    def __init__(self, file):
        with open(file, 'r') as read_file:
            self.countries = json.load(read_file)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.countries:
            raise StopIteration
        this_name = self.countries.pop().get('name').get('common')
        this_link = 'https://en.wikipedia.org/wiki/' + this_name.replace(' ', '_')
        return this_name, this_link


countries = Countries('countries.json')

with open('links.txt', 'w') as write_file:
    for name, link in countries:
        string = name + ' - ' + link + '\n'
        write_file.write(string)
