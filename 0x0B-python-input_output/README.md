`0-read_file.py` - function that reads a text file (UTF8) and prints it to stdout

`1-write_file.py` - function that writes a string to a text file (UTF8) and returns the number of characters written

`2-append_write.py` - function that appends a string at the end of a text file (UTF8) and returns the number of characters added

`3-to_json_string.py` - returns the JSON representation of an object (string)

`4-from_json_string.py` - function that returns an object (Python data structure) represented by a JSON string

`5-save_to_json_file.py` - function that writes an Object to a text file, using a JSON representation

`6-load_from_json_file.py` -  function that creates an Object from a “JSON file”

`7-add_item.py` - script that adds all arguments to a Python list, and then save them to a file

`8-class_to_json.py` - function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object

`9-student.py` - `class Student`
> Public instance attributes: `first_name`, `last_name`, `age`\
> Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`\
> Public method `def to_json(self):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`) 

`10-student.py` - `class Student` (based on `9-student.py`)
> Public instance attributes: `first_name`, `last_name`, `age`\
> Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`\
> Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`)\
    > If attrs is a list of strings, only attribute names contained in this list must be retrieved.\
    > Otherwise, all attributes must be retrieved

`11-student.py` - `class Student` (based on `9-student.py`)
> Public instance attributes: `first_name`, `last_name`, `age`\
> Instantiation with first_name, last_name and age: `def __init__(self, first_name, last_name, age):`\
> Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as `8-class_to_json.py`)\
    > If attrs is a list of strings, only attribute names contained in this list must be retrieved.\
    > Otherwise, all attributes must be retrieved\
> Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance

`12-pascal_triangle.py` - **Technical Interview Test** a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n

`100-append_after.py` - function that inserts a line of text to a file, after each line containing a specific string

`101-stats.py` - script that reads stdin line by line and computes metrics
> Input format: ***<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>***\
> Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning\
> Total file size: ***File size: <total size>*** \
> where is the sum of all previous\
> Number of lines by status code:\
    > possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500` \
    > if a status code doesn’t appear, don’t print anything for this status code\
    > format: ***<status code>: <number>*** \
    > status codes should be printed in ascending order