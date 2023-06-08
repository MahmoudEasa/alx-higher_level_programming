#!/usr/bin/python3
import dis
import hidden_4
if __name__ == "__main__":
    for i in range(len(hidden_4.__code__.co_names)):
        name = hidden_4.__code__.co_names[i]
        if not name.startswith("__"):
            print(name)
