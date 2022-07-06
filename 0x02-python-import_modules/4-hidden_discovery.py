#!/usr/bin/python3
import hidden_4

"""print all the names in hidden_4 file
"""
if __name__ == "__main__":
    stream_names = dir(hidden_4)
    for name in stream_names:
        if name[0:2] != "__" and name[-1:-3] != "__":
            print(name)
