def single_letter_count(word,letter):
    return word.lower().count(letter.lower())

print(single_letter_count(word = input("Word: "), letter = input("Letter: ")))