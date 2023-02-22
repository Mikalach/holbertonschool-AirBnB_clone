#!/usr/bin/python3
import json
from os.path import isfile
from models.base_model import BaseModel
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
        if not isfile(self.__file_path):
            return
        with open(self.__file_path, mode='r', encoding='utf-8') as f:
            d = json.load(f)
            for k, v in d.items():
                cls_name = v['__class__']
                try:
                    self.new(eval(cls_name)(**v))
                except:
                    # Handle any other classes you may have here
                    raise ValueError(f"Unknown class type: {cls_name}")
