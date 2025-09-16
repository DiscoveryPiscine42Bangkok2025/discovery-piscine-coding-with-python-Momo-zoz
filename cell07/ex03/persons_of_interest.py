def famous_births(persons):
    sorted_persons = sorted(persons.items(), key=lambda item: item[1]["date_of_birth"])
    
    for person, details in sorted_persons:
        print(f"{details['name']} is a great scientist born in {details['date_of_birth']}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)
