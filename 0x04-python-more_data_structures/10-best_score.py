#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = {"None": 0}
    if type(a_dictionary) == dict:
        for k, v in a_dictionary.items():
            if v > best_score[list(best_score)[0]]:
                best_score = {k: v}
    return (list(best_score)[0])
