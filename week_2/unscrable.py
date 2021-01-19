user_input = input("Type in a word to unscramble: ")

def unscrable(scrambled_word):
    returns = []
    the_file = open('words.txt','r')
    lines = the_file.readlines()
    for line in lines:
        for letter in scrambled_word:
            if letter not in line:
                break
            elif scrambled_word.index(letter) is len(scrambled_word)-1:
                returns.append(line)
    print(returns)
    the_file.close()
unscrable(user_input)