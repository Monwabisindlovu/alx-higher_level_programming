#!/usr/bin/python3
"""Base module"""

import json
import csv

class Base:
    """Base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file in JSON format."""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                content = file.read()
                obj_list = cls.from_json_string(content)
                return [cls.create(**d) for d in obj_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                if cls.__name__ == "Rectangle":
                    writer.writerow(["id", "width", "height", "x", "y"])
                if cls.__name__ == "Square":
                    writer.writerow(["id", "size", "x", "y"])
                for obj in list_objs:
                    writer.writerow([getattr(obj, attr) for attr in obj.to_dictionary()])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline='') as file:
                reader = csv.reader(file)
                next(reader)  # skip the header
                obj_list = []
                for row in reader:
                    d = {}
                    if cls.__name__ == "Rectangle":
                        keys = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        keys = ["id", "size", "x", "y"]
                    for i, key in enumerate(keys):
                        d[key] = int(row[i])
                    obj_list.append(cls.create(**d))
                return obj_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw Rectangles and Squares."""
        try:
            import turtle
            window = turtle.Screen()
            window.bgcolor("white")
            t = turtle.Turtle()
            t.speed(1)
            t.penup()
            t.setx(-250)
            t.sety(250)
            t.pendown()

            colors = ["red", "blue", "green", "orange", "purple", "brown"]

            for obj in list_rectangles + list_squares:
                t.color(colors[obj.id % len(colors)])
                t.begin_fill()
                for _ in range(4):
                    t.forward(obj.width)
                    t.right(90)
                t.end_fill()
                t.penup()
                t.forward(200)
                t.pendown()

            window.exitonclick()
        except ImportError:
            print("Please install the `turtle` module to run the drawing function.")

if __name__ == "__main__":
    print("Base class - Please use provided classes and script files for functionality.")

