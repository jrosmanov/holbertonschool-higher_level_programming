#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):

        try:
            with open(filename, 'w') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, PermissionError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):

        try:
            with open(filename, 'r') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, PermissionError, pickle.UnpicklingError, EOFError):
            return None

        return None
