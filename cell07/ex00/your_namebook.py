#!/usr/bin/env python3

def array_of_names(persons):
    full_names = []
    for first, last in persons.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    print(array_of_names(persons))
