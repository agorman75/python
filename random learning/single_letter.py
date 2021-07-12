# def single_letter_count(word,letter):
#     return word.lower().count(letter.lower())

# print(single_letter_count(word = input("Word: "), letter = input("Letter: ")))

def ft(distance):
    return f"{round(int(distance) * 3.28084, 2)} feet."

distance = int(input("Provide a int in meters to calculate as feet: "))
print(ft(distance))