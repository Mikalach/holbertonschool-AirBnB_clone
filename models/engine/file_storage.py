#!/usr/bin/python3
import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                d = json.load(f)
            for key in d:
                FileStorage.__objects[key] = FileStorage.__objects[d[key]["__class__"]](**d[key])
        except FileNotFoundError:
            pass
