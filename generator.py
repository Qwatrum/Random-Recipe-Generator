import random
import time

waiting_messages = ["Let him cook!", "Ohh. That's great!", "You are going to LOVE it!", "Perfect...", "Oh yes, great idea", "Uhh, that's dangerous!", "oopsie", ""]
ingredients = ["eggs", "sugar", "bread", "flour", "potatoes", "cucumbers", "tomatoes", "garlic", "onions", "rice", "noodles"]
fluids = ["milk", "water", "rain water", "creame"]
spices = ["pepper", "salt", "safran", "chilli", "ginger", "paprika"]
steps_1 = ["Take ", "Grab some ", "You'll need "]
steps_2 = ["Put everything into ", "Evrything goes right into ", "Your meal needs to go into ", "Everything should be in "]
steps_3 = ["Cut some ", "Take a knife and smash it on some ", "Start your blender and add some "]
steps_4 = ["Take the result out.", "When finished, take out", "Don't forget to take out"]
steps_5 = ["Knead ervything with your hands.", "Use your hands to knead it.", "Stir your meal."]
steps_6 = ["Add everything together.", "Almost done. You just need to mix everything together.", "Put everything you have in the pan for a few minutes.", "Put everything you have in the oven for half an hour."]
locations = ["the oven with "+str(random.randrange(180,260))+"°", "a pan", "the toaster", "a pot", "the steamer"]
adjectives = ["cooked ", "fryed ", "toasted ", "roasted "]
times = [" for around ", " for almost ", " for exactly ", " for "]
duration = [" mins", " hours", " seconds"]
finishes = ["That's it!", "That's all!", "Now you have a royalty like meal!", "COMPLETED! Let's go!", "Enjoy it! You are done."]
toppings = ["tomato sauce", "butter", "cherries", "chocolate", "apple juice", "parmesan", "cheese", "jam"]


def generate_recipe():
    if random.randrange(1,2) == 1:
        print(random.choice(steps_1) + random.choice(ingredients))
    else:
        print(random.choice(steps_1) + random.choice(adjectives) + random.choice(ingredients))
    print(random.choice(steps_1)+ random.choice(ingredients))
    print(random.choice(steps_3) + random.choice(adjectives) + random.choice(ingredients))
    print(random.choice(steps_2)+random.choice(locations)+ random.choice(times)+str(random.randrange(1,7))+random.choice(duration))
    print(random.choice(steps_4))
    if random.randrange(1,2) == 1:
        print("Mix "+str(random.randrange(1,99))+str("%")+ " in "+random.choice(fluids))
    if random.randrange(1,2) == 1:
        print(random.choice(steps_3) + random.choice(ingredients))
    else:
        print(random.choice(steps_3) + random.choice(adjectives) + random.choice(ingredients))
    
    print(random.choice(steps_6))
    print(random.choice(steps_1) + random.choice(spices) + " and add it.")
    print(random.choice(steps_2) + random.choice(locations)+ random.choice(times)+str(random.randrange(1,7))+random.choice(duration))
    print(random.choice(steps_4))
    print(random.choice(finishes))
    print("If you want, you can add some "+random.choice(adjectives)+random.choice(toppings))
        

    
def start():
    print("Welcome to Random Recipe Generator!")
    print("My name is Rmeal")
    time.sleep(2)
    print("I heard you need a recipe? But it should be random?")
    time.sleep(2)
    print("RANDOM?")
    time.sleep(1.2)
    print("Today is your lucky day!")
    print("I am an expert in generating random recipes!")
    time.sleep(1.7)
    print("But sometimes they are kinda crazy ... hehe...")
    time.sleep(1.5)
    print("I am ready!")
    print("Press 'enter' to start!!!! (I can't wait...)")
    input()
    time.sleep(1)
    print("Let the recipe making begin!\n")
    time.sleep(1)
    for i in range(random.randrange(3, 6)):
        print(random.choice(waiting_messages))
        time.sleep(random.randrange(3, 9)/10)
        
    time.sleep(1.5)
    print("\nDONE! New world record?\nWell here it is:")
    time.sleep(1)
    print("Your recipe:\n")
    generate_recipe()
    print()
    print("\nI hope you love it!!")


if __name__ == "__main__":
    start()