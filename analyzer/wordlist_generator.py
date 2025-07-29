import itertools

def generate_wordlist(name, pet, year):
    base_words = [name.lower(), pet.lower(), year]
    patterns = []

    for word in base_words:
        patterns.append(word)
        patterns.append(word.capitalize())
        patterns.append(word + year)
        patterns.append(word + '@' + year)
        patterns.append(word + '123')

    combined = set(itertools.chain(patterns))

    with open("wordlists/custom_wordlist.txt", "w") as f:
        for item in combined:
            f.write(item + "\n")

    return "wordlists/custom_wordlist.txt"
