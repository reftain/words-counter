print("****** WORDS COUNTER ******")

pun = ["!","@","#","$","%","^","&", "*", "(", ")", ",", ".", "<", ">", ";", ":", "-"]
sentence = input("Enter any sentence you want: ")

# عداد الكلمات
def words_counter(sentence):

    count = 0
    words = sentence.split()

    for word in words:
        count += 1
        if word in pun:
            count -= 1
    return count

#عداد الحروف
def letters_counter(sentence):

    count = 0

    for letter in sentence:
        count += 1
        if letter == " " or letter in pun:
            count -= 1
    return count

#count how many times a select litter shows up in the beggining of the words
def letter_count(sentence):

    count = 0
    user = input("Enter a litter you want to calculate how many times will show up in the beggining of the words: ")
    words = sentence.lower().split()

    for word in words:
        if word[0] == user:
             count += 1
    return count 

    #calc how many words are longer "> 5"
def longer(sentence):

    for w in sentence:
        if w in pun:
            sentence = sentence.replace(w, "")

    count = 0
    words = sentence.split()

    for word in words:
        if len(word) > 5:
            count += 1
    return count

#Call the functions from user request
menu = {
    1 : "words counter",
    2 : "litters counter",
    3 : "letter count",
    4 : "longer words",
}

c = "y"
while c == "y" or c == "yes":

    user_choice = int(input(f"Enter the process you want {menu}: "))

    if user_choice == 1:
        print(words_counter(sentence))
    elif user_choice == 2:
        print(letters_counter(sentence))
    elif user_choice == 3:
        print(letter_count(sentence))
    elif user_choice == 4: 
        print(longer(sentence))
    else:
        print("Your choice is undefind")

    c = input("Do you want another process? y for yes: ")

