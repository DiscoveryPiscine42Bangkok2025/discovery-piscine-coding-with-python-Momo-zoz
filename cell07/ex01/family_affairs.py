def find_the_redheads(family):
    redheads = filter(lambda x: family[x] == 'red', family.keys())
    return list(redheads)

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    
    print(find_the_redheads(dupont_family))
