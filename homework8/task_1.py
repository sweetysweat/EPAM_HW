"""
We have a file that works as key-value storage,
each line is represented as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers.
If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible as collection
items and as attributes.
Example: storage['name'] # will be string 'kek' storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence. In case when value cannot be assigned
to an attribute (for example when there's a line 1=something) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
import re


class KeyValueStorage:
    def __init__(self, path: str):
        self.storage = DictWithAttr()
        self.get_attr(path)

    def get_attr(self, path: str):
        with open(path, 'r') as f:
            built_in_attrs = self.__dir__()
            for line in f:
                key, value = line.strip().split('=')
                if key not in built_in_attrs:
                    regular_expression = re.search(r'^\w+$', key, re.ASCII)
                    if not regular_expression or regular_expression.string.isdigit():
                        raise ValueError("The key can only contain ASCII symbols!")
                    if value.isdigit():
                        value = int(value)
                    self.storage[key] = value


class DictWithAttr(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)
