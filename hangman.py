import random
word_list = ["rama","sitha","lakshmana","hanuman"]
def choose_word():
    return random.choice(word_list).lower()
def display_word(word,guessed):
    return " ".join([letter if letter in guessed else '_'for letter in word])
def hangman():
    word = choose_word()
    guessed,wrong_guesses,max_guesses = [],0,6
    print("Welcome to Hangman")
    while wrong_guesses < max_guesses :
        print(display_word(word,guessed))
        guess = input("Guess a Letter: ").lower()
        if guess in guessed:
            print("Its alredy guessed")
        else:
            guessed.append(guess)
            if guess not in word:
                wrong_guesses +=1
                print(f"wrong! you have only'{max_guesses-wrong_guesses}' guesses left")
        if set(word) <= set(guessed):
            print(f"Hey congrats! you guessed the word '{word}'")
            break
    else:
        print(f"game over! the word is '{word}'")
        print("sorry better luck next time")
if __name__=="__main__":
    hangman()


