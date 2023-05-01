import random

# Define the planets in the game
planets = {
    "Mercury": {"description": "A small rocky planet with a barren surface."},
    "Venus": {"description": "A hot and cloudy planet with a thick atmosphere."},
    "Earth": {"description": "The blue planet, home to millions of species."},
    "Mars": {"description": "A red planet with a thin atmosphere and rocky terrain."},
    "Jupiter": {"description": "A gas giant with a massive swirling storm called the Great Red Spot."},
    "Saturn": {"description": "A ringed planet with many moons."},
    "Uranus": {"description": "A blue-green planet that spins on its side."},
    "Neptune": {"description": "A cold and windy planet with a dark spot."},
}

visited_planets = [ ]  #this keeps track of the planets visited

while len(visited_planets) < 3:
    print("Available planets:")
    for planet in planets:
        if planet not in visited_planets:
            print(planet + ": " + planets[planet]['description'])

    
    choice = input("Which planet do you want to visit? ")
    
    if choice not in planets or choice in visited_planets:
        print("Invalid planet. Please choose again.")
        continue
    
    
    print(planets[choice]["description"])
    
    for i in range(random.randint(3, 4)):  # add 3-4 random events to each planet
        event = random.randint(1, 10)
        if event == 1:
            print("You encounter an alien!")
            print("What do you want to do?")
            print("1. Talk to the alien")
            print("2. Attack the alien")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("The alien seems friendly and offers to trade with you.")
            elif choice == "3":
                print("The alien fights back and damages your ship!")
        elif event == 2:
            print("The ship is hit by a meteor!")
            print("What do you want to do?")
            print("1. Repair the ship")
            print("2. Ignore the damage")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("You repair the ship and continue your journey.")
            else:
                print("The damage causes a critical system failure and you have to return to Earth.")
                visited_planets = []  # reset the visited planets list
                break  # end the game loop
        elif event == 3:
            print("You discover a mysterious object in orbit around the planet!")
            print("What do you want to do?")
            print("1. Investigate the object")
            print("2. Ignore the object")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("You discover a valuable alien artifact and add it to your collection.")
            else:
                print("The object turns out to be a trap and you are ambushed by space pirates!")
        elif event == 4:
            print("You notice a small alien civilization when you land!")
            print("What do you want to do?")
            print("1. Go into the civilization in hopes they are peaceful")
            print("2. ignore them and continue your mission")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("They welcome you with open arms and invite you to stay for a feast.")
            else:
                print("Turns out they are not friendly and cook you for dinner.")
        elif event == 5:
            print("During your journey you spot another human ship... but it appears to be abandoned")
            print("What do you want to do?")  
            print("1. Go investigate the ship")
            print("2. Ignore it and conntinue your journey") 
            choice = input("Enter your choice:")
            if choice == "1":
                print("The ship turned out to be empty, but you find extra food!")
            else:
                print("The crewmates on that ship are infected with a deadly alien disease, and they capture one of your crewmates")
        elif event == 6:
            print("During you journey you spot an alien outpost in space and they spot you in the distance")
            print("What are you going to do?")   
            print("1. Ignore them and continue to your destination")
            print("2. Dock onto the outpost and see and introduce yourselves")
            if choice == "1":
                print("You decide to ignore them and are on your merry way!")
            else:
                print("You decide to dock, and the aliens are fascinated by your technology... you end up making some firends")
        else:
            print("Nothing out of the ordinary happens on this planet.")
    
    visited_planets.append(choice)  # add the current planet to the visited planets list


