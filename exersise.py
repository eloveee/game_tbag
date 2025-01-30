from character import Character

class Enemy:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def fight(self, item):
        if item == "sword":
            print(f"{self.name} was defeated with the {item}!")
            return True
        else:
            print(f"{self.name} is too strong for the {item}. You lost the fight! Game Over!")
            return False

    def talk(self):
        print(f"{self.name} says: 'You dare challenge me?'")

class Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.friendship_level = 0

    def hug(self):
        print(f"You hug {self.name}. Friendship level increased!")
        self.friendship_level += 1
        self.check_friendship_level()

    def give_gift(self, gift):
        print(f"You give {gift} to {self.name}. Friendship level increased!")
        self.friendship_level += 2
        self.check_friendship_level()

    def check_friendship_level(self):
        if self.friendship_level >= 10:
            print(f"{self.name} is now your best friend!")
        elif self.friendship_level >= 5:
            print(f"{self.name} seems like a good friend now.")
        else:
            print(f"{self.name} seems like a casual acquaintance.")

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Door:
    def __init__(self, is_locked=True):
        self.is_locked = is_locked

    def unlock(self, key):
        if key.name == "Golden Key":
            self.is_locked = False
            print("The door is now unlocked!")
        else:
            print("This key doesn't work on the door.")

class Room:
    def __init__(self, name, inhabitant=None):
        self.name = name
        self.inhabitant = inhabitant

    def move(self, direction):
        print(f"Moving {direction}...")
        return self

# Example setup
key = Item(name="Golden Key", description="A shiny golden key.")
locked_door = Door(is_locked=True)
inventory = [key]

enemy = Enemy(name="Dragon", description="A fearsome dragon.")
friend = Friend(name="Gandalf", description="A wise wizard.")

current_room = Room(name="Dungeon", inhabitant=enemy)

# Game loop
while True:
    command = input("> ").strip().lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.inhabitant:
            current_room.inhabitant.talk()
        else:
            print("There is no one to talk to here.")
    elif command == "fight":
        if current_room.inhabitant and isinstance(current_room.inhabitant, Enemy):
            print("What item would you like to fight with?")
            item = input("> ").strip().lower()
            result = current_room.inhabitant.fight(item)
            if not result:
                print("You lost the fight! Game Over!")
                break
        else:
            print("There's no one to fight here.")
    elif command == "unlock door":
        if locked_door.is_locked:
            for item in inventory:
                if item.name == "Golden Key":
                    locked_door.unlock(item)
                    break
            else:
                print("You don't have the Golden Key in your inventory.")
        else:
            print("The door is already unlocked.")
    elif command == "hug" and isinstance(current_room.inhabitant, Friend):
        current_room.inhabitant.hug()
    elif command == "give gift" and isinstance(current_room.inhabitant, Friend):
        print("What gift would you like to give?")
        gift = input("> ").strip()
        current_room.inhabitant.give_gift(gift)
    else:
        print("Unknown command.")

