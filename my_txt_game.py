'''
Author: Kayleigh Haydock
Game: Star Explorer Mission (a simple text based game)
Version: v1.0.0
Created: 14/11/2024 
Notes: As part of ExCode 2024
Updates:
    
'''

# Main function to start the game
def main():
    # Get the player's name and greet them as the spaceship captain
    name = input("Enter Your Name: ")
    print(f"Greetings, Captain {name}!\n###_____Welcome to Kayleigh's Star Explorer Mission____###")
    points = 3

    # Game loop continues while the player has points remaining
    while points > 0:
        print(f"\nCaptain {name}, you have {points} points.")
        print("You see three mysterious planets ahead:")
        print("1 - Blue Planet (Icy)")
        print("2 - Red Planet (Desert)")
        print("3 - Green Planet (Forest)")
        print("Which planet will you explore? Enter '1', '2', or '3'. Enter 'q' to quit.")
        
        planet = input(">")
        
        # Call the corresponding function based on the planet chosen
        if planet == "1":
            points = explore_blue_planet(points)
        elif planet == "2":
            points = explore_red_planet(points)
        elif planet == "3":
            points = explore_green_planet(points)
        elif planet == 'q' or planet == 'Q':
            print("Mission aborted. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        
        if points <= 0:
            print("You've run out of points. GAME OVER.")
            break
        elif points > 0:
            print("Would you like to explore another planet?")

# Function to explore the Blue Planet
def explore_blue_planet(points):
    print("\nYou set a course for the Blue Planet, known for its icy landscapes and harsh winds.")
    print("As you land, your scanners detect a rare mineral deposit nearby.")
    print("Stepping onto the surface, you spot something moving in the ice.")
    print("What will you do?")
    print("1 - Approach cautiously to investigate.")
    print("2 - Mine the minerals and leave as quickly as possible.")
    print("3 - Ignore the movement and explore further into the icy wilderness.")

    choice = input(">")
    if choice == "1":
        points -= 1
        print("You cautiously approach and discover a small alien creature trapped under the ice.")
        print("After freeing it, the creature gives you a mysterious crystal as a sign of gratitude.")
        print("Points:", points)
    elif choice == "2":
        points -= 1
        print("You quickly mine the minerals, but the noise attracts a large ice creature.")
        print("Before you can escape, the creature attacks your ship. You didn’t make it.")
        points = 0  # Ends game if they get attacked here.
        print("GAME OVER.")
    elif choice == "3":
        points += 1
        print("Ignoring the strange movement, you venture deeper into the icy landscape.")
        print("Eventually, you find a hidden cavern filled with alien technology.")
        print("### YOU DISCOVERED ADVANCED TECHNOLOGY! ###")
        print("Points:", points)
    else:
        print("Invalid choice! GAME OVER.\nPlease restart the game.")
    
    return points

# Function to explore the Red Planet
def explore_red_planet(points):
    print("\nYou descend onto the Red Planet, known for its barren deserts and violent sandstorms.")
    print("As you step outside, your sensors pick up a massive energy source nearby.")
    print("What will you do?")
    print("1 - Approach the energy source carefully.")
    print("2 - Send out a drone to investigate.")
    print("3 - Set up camp and wait until the storm passes.")

    choice = input(">")
    if choice == "1":
        points -= 1
        print("As you approach, you realize the energy source is an ancient alien reactor.")
        print("Before you can react, it overloads and explodes, taking you with it.")
        points = 0
        print("GAME OVER.")
    elif choice == "2":
        points += 1
        print("The drone captures footage of an ancient alien device and relays data back to your ship.")
        print("You gather valuable information and return to the ship.")
        print("Points:", points)
    elif choice == "3":
        points += 2
        print("You wait out the storm, but during the night, strange shadows surround your camp.")
        print("In the morning, you find mysterious symbols carved around you.")
        print("### YOU SURVIVED AND UNCOVERED ANCIENT CLUES ###")
        print("Points:", points)
    else:
        print("Invalid choice! GAME OVER.\nPlease restart the game.")
    
    return points

# Function to explore the Green Planet
def explore_green_planet(points):
    print("\nYou approach the Green Planet, lush with strange vegetation and unfamiliar sounds.")
    print("As you explore, you discover a group of alien beings who seem curious about you.")
    print("How will you proceed?")
    print("1 - Attempt to communicate with them.")
    print("2 - Take samples of the vegetation and return to your ship.")
    print("3 - Observe them from a distance and explore further.")

    choice = input(">")
    if choice == "1":
        points -= 1
        print("Through gestures and sounds, you manage to communicate.")
        print("They welcome you to their planet and share knowledge about their technology.")
        print("Points:", points)
    elif choice == "2":
        points -= 2
        print("You gather samples of the plants, but they emit a strange gas that puts you to sleep.")
        print("When you wake up, you’re back on your ship with no memory of what happened.")
        print("Points:", points)
    elif choice == "3":
        points += 1
        print("You observe them from afar, learning about their culture and advanced society.")
        print("You leave quietly, with valuable information to report.")
        print("### YOU GATHERED IMPORTANT INSIGHTS ###")
        print("Points:", points)
    else:
        print("Invalid choice! GAME OVER.\nPlease restart the game.")
    
    return points

# Run the main function to start the game
main()
