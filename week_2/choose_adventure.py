print("Welcome to the choose your own adventure game:")
print("You have just walked into the pet store and you are looking around...")
print("Where do you want to go?")
print("Type in the # next to the animal that you like to see then enter:")
animals = input("1-reptiles 2-fish 3-rodents 4-cats ")
if animals == 4:
    print("There is a cute kitten named Sammy who keeps meowing at you. What do you do?")
    cat_spotted = input("1-Adopt Sammy! 2-Keep on walking by ")
    if cat_spotted == 1:
        print("Congrats! You have just adopted a cat! :) ")
    elif cat_spotted == 2:
        print("You now are walking by another cat who is orange and fluffy. She is such a sweet cat and her name is Carrot")  
        cat_again = input("1-Adopt Carrot! 2-Walk back to Sammy and Adopt Sammy! ")  
        if cat_again == 1:
            print("Congrats! You have just adopted a cat! :) ")
        elif cat_again == 2:
            print("Congrats! You have just adopted a cat! :) ")    
elif animals == 1:
    print("You walk past a small snake that is 50% off. What do you do?")
    snake_spotted = input("1-Take lid off of cage and put snake in pocket 2-Ask worker if you can have the snake 3-Keep walking ")
    if snake_spotted == 1:
        print("What are you doing?? Now you have a snake in your pocket! ")
    elif snake_spotted == 2:
        print("Congrats! You have just purchased a super duper snake pet! ")
    elif snake_spotted == 3:
        print("You missed out on a cool snake pet, but next time, you might aquire a cool pet friend!")        
elif animals == 2:
    print("You see a tank full of gold fish. What do you do?")
    goldfish_spotted = input("1-Ask for all of them 2-Reach into the tank and put a fish in your pocket ")
    if goldfish_spotted == 1:
        print("Congrats, you have lots of fish friends now!") 
    elif goldfish_spotted == 2:
        print("You crazy! You have a fish in your pocket now!!")    
elif animals == 3:
    print("You first see a tank with a cute hamster in it. What do you do? ")
    hamster_spotted = input("1-Wow, such a cute hamster! I shall adopt you. 2-Walk on ")
    if hamster_spotted == 1:
        print("Congrats! You have a rad hamster pet now!")
    elif hamster_spotted == 2:
        print("Rats, you missed out on the greatest hamster pet ever. Maybe next time you will get a furry pet friend :)")