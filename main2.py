#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import math
import random
import time

monsters = ["baby", "tiny spiders", "mice", "bats", "flies",
            "hackers", "rabbits", "possessed squirrels", "seagulls", "cockroaches",
            "retarded dwarf", "bucket bois", "guy with a blanket", "floating eyes", "evil eagles",
            "gypsies", "one robot", "goblins", "sinister penguins",
            "skeletons", "snakes", "ninja turtles", "hairy potter", "Cristiano Ronaldo",
            "orc", "tiger", "ghost...?", "ghost", "Jackie Chan", "armored skeletons", "two robots",
            "transgender", "gun", "school shooter", "samurai", "Spiderman", "Spiderman", "three robots", "Batman",
            "Metallica", "\"mirror\"", "jelly blobs", "Goku", "Saitama", "Archer Queen",
            "MrBeast", "John Cena", "Parry hotter", "Subaru", "Sonic the hedgehog", "fucking dragon"]
monsters_hp = [1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 15, 16, 16, 17, 19, 20, 21, 23, 24, 25, 26, 29, 30, 32, 34, 35,
               37, 40, 41, 43, 42, 45, 48, 51, 54, 58, 59, 63, 64, 67, "mirror", 72, 78, 81, 83, 87,
               93, 47, 3, 74, 500]
with open("items.txt") as file:
    item_pool = [line.rstrip() for line in file]
file.close()

monst_2 = ["nft owners", "bookworms", "weebs", "bees", "soccer balls",
           "human form Eren", "zombies", "turks", "fastest man alive", "basketballs",
           "Clash Royale king", "romanians", "clowns", "rocket league car", "Monika",
           "stock market", "Lorax", "You", "bulgarians", "BBC",
           "ligma balls", "firefox", "Mike Wazowski", "builders", "hitmen",
           "Slabhead", "buff fella", "literature teacher", "Orang", "Meme man",
           "Gosho Chushkata", "four robots", "five robots"]
monst_2_hp = [2, 4, 5, 10, 14, 17, 18, 20, 27, 28, 28, 30, 31, 33, 34, 34, 36, 36, 40, 41,
              42, 46, 47, 50, 52, 55, 60, 63, 68, 69, 72, 84, 105]


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.score = False
        self.health = 100
        self.slowed = False
        self.frozen = False
        self.poisoned = False
        self.cursed = False
        self.charm = False
        self.winner = False
        self.dead = False
        self.given_up = False
        self.attack = 10
        self.rooms_cleared = 0
        self.skipped = False
        self.safe_skipped = False
        self.rooms_skipped = 0
        self.coins = 0
        self.bombs = 0
        self.keys = 0
        self.discount = 0
        self.weapon = 0
        self.weapon_hp = 0
        self.weapon2 = 0
        self.weapon2_hp = 0
        self.potion1 = 0
        self.potion2 = 0
        self.potion3 = 0
        self.parry = False
        self.parry_item = False
        self.parry_enemy = False
        self.parry_dead = False
        self.brad_enemy = False
        self.brad_dead = False
        self.cat = False
        self.pray = False
        self.trap = False
        self.restart = False
        self.double = False
        self.double_enemy = []
        self.extra_lives = 0
        self.items = []
        self.breath = 2
        self.black_hole = True
        self.button = True
        self.stone = 3

    def print_stats(self):
        if "Mute button" in self.items:
            print(f"\n\n\n...... {self.health}")
            if self.slowed:
                print("......: ...")
            if self.poisoned:
                print("........: ...")
            if self.cursed:
                print("......: ...")
            if self.charm:
                print("..... .....: ...")
            if self.extra_lives > 0:
                print(f"..... .....: {self.extra_lives}")
            if self.slowed:
                print(".... ...... ... ...... ........ .... ..... ..... .. .... ...... ... .... .. .... .... .......")
            if self.weapon == 0 and self.weapon2 == 0:
                print(f"......: {self.attack}")
            elif self.weapon > 0 or self.weapon2 > 0:
                print(f"......: {self.attack} + {self.weapon}")
                if self.weapon > 0:
                    print(f"........ ......: + {self.weapon} .......")
                    print(f"...... ..........: {self.weapon_hp} ......")
                if self.weapon2 > 0:
                    print(f"...... ......: + {self.weapon2} ......."
                          f"\n...... ..........: {self.weapon2_hp} ......")
            print(f".....: {self.coins}")
            if self.discount > 0:
                print(f"........: {self.discount}%")
            print(f".....: {self.bombs}")
            print(f"....: {self.keys}")
            if self.potion1 > 0:
                print(f"...... 1: {self.potion1}")
            if self.potion2 > 0:
                print(f"...... 2: {self.potion2}")
            if self.potion3 > 0:
                print(f"...... 3: {self.potion3}")
            if len(self.items) > 0:
                print(f".....: {self.items}")
            if self.score:
                print(f"....... .....: {self.points}")
            print(f"..... ......: {self.rooms_cleared}.")
        else:
            print(f"\n\n\nHealth: {self.health}")
            if self.slowed:
                print("Slowed: Yes")
            if self.poisoned:
                print("Poisoned: Yes")
            if self.cursed:
                print("Cursed: Yes")
            if self.charm:
                print("Lucky charm: Yes")
            if self.extra_lives > 0:
                print(f"Extra lives: {self.extra_lives}")
            if self.slowed:
                print("Your attack and weapon actually deal about twice as much damage but this is with slow applied")
            if self.weapon == 0 and self.weapon2 == 0:
                print(f"Attack: {self.attack}")
            elif self.weapon > 0 or self.weapon2 > 0:
                print(f"Attack: {self.attack} + {self.weapon}")
                if self.weapon > 0:
                    print(f"Equipped weapon: + {self.weapon} attack.")
                    print(f"Weapon durability: {self.weapon_hp} rooms.")
                if self.weapon2 > 0:
                    print(f"Backup weapon: + {self.weapon2} attack."
                          f"\nWeapon durability: {self.weapon2_hp} rooms.")
            print(f"Coins: {self.coins}")
            if self.discount > 0:
                print(f"Discount: {self.discount}%")
            print(f"Bombs: {self.bombs}")
            print(f"Keys: {self.keys}")
            if self.potion1 > 0:
                print(f"Potion 1: {self.potion1}")
            if self.potion2 > 0:
                print(f"Potion 2: {self.potion2}")
            if self.potion3 > 0:
                print(f"Potion 3: {self.potion3}")
            if len(self.items) > 0:
                print(f"Items: {self.items}")
            if self.score:
                print(f"Current score: {self.points}")
            print(f"Rooms passed: {self.rooms_cleared}.")

    def trap_room(self, reward):
        if "Mute button" in self.items:
            print(f".... .. ..!")
        else:
            print("Down we go!")
        self.trap = True
        wave_1 = [monsters[3], monsters[4], monsters[6], monsters[7], monsters[9], monst_2[3]]
        wave_1_hp = [monsters_hp[3], monsters_hp[4], monsters_hp[6], monsters_hp[7], monsters_hp[9], monst_2_hp[3]]
        wave_2 = [monsters[11], monsters[13], monsters[17], monsters[19], monsters[20], monst_2[12]]
        wave_2_hp = [monsters_hp[11], monsters_hp[13], monsters_hp[17], monsters_hp[19],
                     monsters_hp[20], monst_2_hp[12]]
        wave_3 = [monsters[29], monsters[30], monsters[34], monsters[37], monsters[41], monst_2[23]]
        wave_3_hp = [monsters_hp[29], monsters_hp[30], monsters_hp[34], monsters_hp[37], monsters_hp[41],
                     monst_2_hp[23]]
        rand_1 = random.randint(0, 4)
        rand_2 = random.randint(0, 4)
        rand_3 = random.randint(0, 4)
        fight_1_if = False
        while not fight_1_if:
            try:
                fight_1 = int(input(f"The first wave is {wave_1[rand_1]}. You need {wave_1_hp[rand_1]} total attack. "
                                    f"(Currently {self.attack} + {self.weapon} total)"
                                    f"\n(1)attack\n(2)give up "))
                assert (fight_1 in range(1, 3))
                if fight_1 in range(1, 3):
                    fight_1_if = True
            except:
                print("\nDidn't type a proper number.")
        if fight_1 == 1:
            Player.fight(self, 1, wave_1[rand_1], wave_1_hp[rand_1])
        elif fight_1 == 2:
            self.points -= 100
            self.given_up = True
            if "Portable black hole" in self.items:
                self.black_hole = False
            self.dead = True
            print("You kill yourself. Yes, this is what giving up means if you were wondering all this time.")
        if "Blessed flower" in self.items:
            if "Strong juice" in self.items:
                if not self.dead and self.health < 200:
                    time.sleep(1)
                    self.health += 1
                    if self.health > 200:
                        self.health = 200
                    if "Mute button" in self.items:
                        print(f"\n... .... .... ...... 1 ..!")
                    else:
                        print("\nYou have been healed 1 hp!")
            else:
                if not self.dead and self.health < 100:
                    time.sleep(1)
                    self.health += 1
                    if self.health > 100:
                        self.health = 100
                    if "Mute button" in self.items:
                        print(f"\n... .... .... ...... 1 ..!")
                    else:
                        print("\nYou have been healed 1 hp!")
        if self.poisoned and not self.dead:
            self.health -= 3
            if self.health > 0:
                time.sleep(2)
                if "Mute button" in self.items:
                    print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                else:
                    print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
            else:
                self.dead = True
                time.sleep(1)
                if "Mute button" in self.items:
                    print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                else:
                    print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                Player.revive(self)
        if not self.dead:
            if self.health < 100 and self.potion1 > 0:
                Player.ask_potion(self)
            fight_2_if = False
            while not fight_2_if:
                try:
                    fight_2 = int(
                        input(f"Your second wave is {wave_2[rand_2]}. You need {wave_2_hp[rand_2]} total attack."
                              f"(Currently {self.attack} + {self.weapon} total)"
                              f"\n(1)attack\n(2)give up "))
                    assert (fight_2 in range(1, 3))
                    if fight_2 in range(1, 3):
                        fight_2_if = True
                except:
                    print("\nDidn't type a proper number.")
            if fight_2 == 1:
                Player.fight(self, 1, wave_2[rand_2], wave_2_hp[rand_2])
            elif fight_2 == 2:
                self.points -= 100
                self.given_up = True
                self.dead = True
                if "Portable black hole" in self.items:
                    self.black_hole = False
                print("You kill yourself. Yes, this is what giving up means if you were wondering all this time.")
        if "Blessed flower" in self.items:
            if "Strong juice" in self.items:
                if not self.dead and self.health < 200:
                    time.sleep(1)
                    self.health += 1
                    if self.health > 200:
                        self.health = 200
                    if "Mute button" in self.items:
                        print(f"\n... .... .... ...... 1 ..!")
                    else:
                        print("\nYou have been healed 1 hp!")
            else:
                if not self.dead and self.health < 100:
                    time.sleep(1)
                    self.health += 1
                    if self.health > 100:
                        self.health = 100
                    if "Mute button" in self.items:
                        print(f"\n... .... .... ...... 1 ..!")
                    else:
                        print("\nYou have been healed 1 hp!")
        if self.poisoned and not self.dead:
            self.health -= 3
            if self.health > 0:
                time.sleep(2)
                if "Mute button" in self.items:
                    print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                else:
                    print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
            else:
                self.dead = True
                time.sleep(1)
                if "Mute button" in self.items:
                    print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                else:
                    print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                Player.revive(self)
        if not self.dead:
            if self.health < 100 and self.potion1 > 0:
                Player.ask_potion(self)
            fight_3_if = False
            while not fight_3_if:
                try:
                    fight_3 = int(
                        input(f"And the third wave is {wave_3[rand_3]}. You need {wave_3_hp[rand_3]} total attack."
                              f"(Currently {self.attack} + {self.weapon} total)"
                              f"\n(1)attack\n(2)give up "))
                    assert (fight_3 in range(1, 3))
                    if fight_3 in range(1, 3):
                        fight_3_if = True
                except:
                    print("\nDidn't type a proper number.")
            if fight_3 == 1:
                Player.fight(self, 1, wave_3[rand_3], wave_3_hp[rand_3])
            elif fight_3 == 2:
                self.points -= 100
                self.given_up = True
                if "Portable black hole" in self.items:
                    self.black_hole = False
                self.dead = True
                print("You kill yourself. Yes, this is what giving up means if you were wondering all this time.")
        if not self.dead:
            time.sleep(3)
            self.points += 300
            input("You made it, you legend. Let's check out your rewards.\n(x) ")
            if reward == "3 golden chests and 6 keys":
                self.keys += 6
                print("6 keys in the bag.\n")
                time.sleep(2)
                open_1_if = False
                while not open_1_if:
                    try:
                        open_1 = int(
                            input("Open a golden chest?\n(1)give itttt - 2 keys of course\n(2)no, I wanted the keys "))
                        assert (open_1 in range(1, 3))
                        if open_1 in range(1, 3):
                            open_1_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if open_1 == 2:
                    print("You do you, boss.")
                elif open_1 == 1:
                    Player.open_chest(self, 2)
                    open_2_if = False
                    while not open_2_if:
                        try:
                            open_2 = int(input("Open another golden chest?\n(1)yesss - costs 2 keys\n(2)no "))
                            assert (open_2 in range(1, 3))
                            if open_2 in range(1, 3):
                                open_2_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if open_2 == 2:
                        print("As you wish.")
                    elif open_2 == 1:
                        Player.open_chest(self, 2)
                        open_3_if = False
                        while not open_3_if:
                            try:
                                open_3 = int(input("Open another golden chest?\n(1)yesss - 2 keys\n(2)no "))
                                assert (open_3 in range(1, 3))
                                if open_3 in range(1, 3):
                                    open_3_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if open_3 == 2:
                            print("Got it.")
                        elif open_3 == 1:
                            Player.open_chest(self, 2)
            elif reward == "100 coins":
                self.coins += 100
                print("You collect the 100 coins. That was very cash money of you.")
            elif reward == "a lucky charm and remove all negative effects":
                self.charm = True
                print("You get a lucky charm.")
                if self.poisoned:
                    self.poisoned = False
                    time.sleep(1)
                    print("\nYour poison is removed.")
                if self.cursed:
                    self.cursed = False
                    time.sleep(1)
                    print("\nYour curse has been lifted.")
                if self.slowed:
                    self.slowed = False
                    self.attack = self.attack * 2
                    self.weapon = self.weapon * 2
                    self.weapon2 = self.weapon2 * 2
                    time.sleep(1)
                    print("\nYou are no longer slowed down.")
            elif reward == "1000 points":
                self.points += 1000
                print("You were getting a lot of points from a dungeon anyways but with these 1000 it's"
                      "\nwayyy more than usual. Well done!")
            elif reward == "3 x 20 health potions and +20 attack":
                self.attack += 20
                Player.take_potion(self, 20)
                Player.take_potion(self, 20)
                Player.take_potion(self, 20)
                print(f"Your base attack went up by 20 and it's now {self.attack}. You also get the potions."
                      f"\nGood job!")
            elif reward == "an extra life":
                self.extra_lives += 1
                print("Well done! You have claimed your extra life.")
            elif reward == "an item box":
                print("\nYou have claimed your item box as a reward.")
                Player.item_box(self)
            time.sleep(2)
            print("\nHope this was worth it <3")
        self.trap = False

    def lottery(self):
        print("We are ready to go!\n")
        if "Score gambler" in self.items:
            self.coins -= 5
            print("Thanks to your score gambler the lottery will take only 5 coins per try.")
        else:
            self.coins -= 10
        time.sleep(1)
        cheated = False
        a1 = int(input("First number: "))
        a2 = int(input("Second number: "))
        if a2 == a1:
            cheated = True
        a3 = int(input("Third number: "))
        if a3 == a1 or a3 == a2:
            cheated = True
        a4 = int(input("Fourth number: "))
        if a4 == a1 or a4 == a2 or a4 == a3:
            cheated = True
        a5 = int(input("Fifth number: "))
        if a5 == a1 or a5 == a2 or a5 == a3 or a4 == a5:
            cheated = True
        a6 = int(input("Sixth number: "))
        if a6 == a1 or a6 == a2 or a6 == a3 or a6 == a5 or a6 == a4:
            cheated = True
        if not cheated:
            b1 = random.randint(1, 49)
            b2 = random.randint(1, 49)
            while b1 == b2:
                b2 = random.randint(1, 49)
            b3 = random.randint(1, 49)
            while b3 == b2 or b3 == b1:
                b3 = random.randint(1, 49)
            b4 = random.randint(1, 49)
            while b4 == b3 or b4 == b2 or b4 == b1:
                b4 = random.randint(1, 49)
            b5 = random.randint(1, 49)
            while b4 == b5 or b5 == b2 or b5 == b3 or b5 == b1:
                b5 = random.randint(1, 49)
            b6 = random.randint(1, 49)
            while b6 == b5 or b6 == b4 or b6 == b3 or b6 == b1 or b6 == b2:
                b6 = random.randint(1, 49)
            lucky_numbers = [b1, b2, b3, b4, b5, b6]
            correct_numbers = 0
            for x in lucky_numbers:
                if a1 == x:
                    correct_numbers += 1
                elif a2 == x:
                    correct_numbers += 1
                elif a3 == x:
                    correct_numbers += 1
                elif a4 == x:
                    correct_numbers += 1
                elif a5 == x:
                    correct_numbers += 1
                elif a6 == x:
                    correct_numbers += 1
            time.sleep(2)
            print("\nAnd the lucky numbers are: " + str(b1) + "  " + str(b2) + "  " +
                  str(b3) + "  " + str(b4) + "  " + str(b5) + "  " + str(b6))
            time.sleep(3)
            print("You guessed " + str(correct_numbers) + " number(s).")
            time.sleep(1)
            if correct_numbers == 0:
                print("No correct numbers obviously means no rewards.")
            elif correct_numbers == 1:
                self.coins += 6
                print("You reward is... 6 coins. 1 guessed number is not a rare outcome,"
                      "\nI don't want you sitting in one place forever now, do I?")
            elif correct_numbers == 2:
                self.points += 5
                self.coins += 15
                pick_if = False
                while not pick_if:
                    try:
                        pick = int(input("For 2 numbers right you get 15 coins and an option for your second reward."
                                         f"\n(1)a key (You have {self.keys})\n(2)a bomb (You have {self.bombs}) "))
                        assert (pick in range(1, 3))
                        if pick in range(1, 3):
                            pick_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if pick == 1:
                    self.keys += 1
                    print("Key claimed!")
                elif pick == 2:
                    self.bombs += 1
                    print("Bomb claimed!")
            elif correct_numbers == 3:
                self.points += 50
                self.coins += 30
                pick_if = False
                while not pick_if:
                    try:
                        pick = int(input("For 3 numbers right you get 30 coins and an option for your second reward."
                                         "\n(1)2 silver chests (to open right now, I will give you 2 keys)"
                                         "\n(2)1 golden chest  (to open right now, I will give you 2 keys)"
                                         f"\n(3)2 bombs + 2 keys (you have {self.bombs} bombs and {self.keys} keys) "))
                        assert (pick in range(1, 4))
                        if pick in range(1, 4):
                            pick_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if pick == 1:
                    print("Alright, opening up.")
                    self.keys += 2
                    Player.open_chest(self, 1)
                    Player.open_chest(self, 1)
                elif pick == 2:
                    print("Alright, opening up.")
                    self.keys += 2
                    Player.open_chest(self, 2)
                elif pick == 3:
                    self.bombs += 2
                    self.keys += 2
                    print("Reward claimed!")
            elif correct_numbers == 4:
                self.points += 150
                pick_if = False
                while not pick_if:
                    try:
                        pick = int(input("4 lucky numbers we are getting into impressive territory."
                                         " Pick your reward for this one.\n(1)80 coins\n(2)an item box"
                                         "\n(3)25 coins + a lucky charm + clean any negative effect on you\n"
                                         "(4)no coins just 3 golden chests (you get the keys to open them instantly "))
                        assert (pick in range(1, 5))
                        if pick in range(1, 5):
                            pick_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if pick == 1:
                    self.coins += 80
                    print("Reward claimed!")
                elif pick == 2:
                    print("Reward claimed!")
                    Player.item_box(self)
                elif pick == 3:
                    self.coins += 25
                    self.charm = True
                    if self.poisoned:
                        time.sleep(1)
                        self.poisoned = False
                        print("Your poison has been removed!")
                    if self.cursed:
                        time.sleep(1)
                        self.cursed = False
                        print("Your curse has been removed!")
                    if self.slowed:
                        self.slowed = False
                        self.attack = self.attack * 2
                        self.weapon = self.weapon * 2
                        self.weapon2 = self.weapon2 * 2
                        time.sleep(1)
                        print("\nYou are no longer slowed down.")
                    time.sleep(1)
                    print("Reward claimed!")
                elif pick == 4:
                    self.keys += 6
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
            elif correct_numbers == 5:
                self.points += 350
                pick_if = False
                while not pick_if:
                    try:
                        pick = int(input("Since you got 5 numbers correct you get to choose from some elite rewards."
                                         f"\n(1)120 coins\n(2)increase your base attack by 20 (you have "
                                         f"{self.attack}\n(3)30 coins + a weapon"
                                         " (35 damage and lasts 8 rooms)\n(4)2 item boxes\n(5)35 coins +"
                                         f"3 potions that heal 40 each (your potions:"
                                         f" {self.potion1}, {self.potion2}, {self.potion3}) "))
                        assert (pick in range(1, 6))
                        if pick in range(1, 6):
                            pick_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if pick == 1:
                    self.coins += 120
                    print("Reward claimed!")
                elif pick == 2:
                    self.attack += 20
                    print("Reward claimed!")
                elif pick == 3:
                    self.coins += 30
                    take = int(input("Which slot are you putting the weapon in?\n(1)equip it\n(2)backup slot "))
                    if take == 1 or take == 2:
                        Player.take_weapon(self, take, 35, 8)
                elif pick == 4:
                    print("Reward claimed!")
                    Player.item_box(self)
                    time.sleep(1)
                    print("\nAnother one.\n")
                    time.sleep(1)
                    Player.item_box(self)
                elif pick == 5:
                    self.coins += 35
                    Player.take_potion(self, 40)
                    Player.take_potion(self, 40)
                    Player.take_potion(self, 40)
                    print("Reward claimed!")
            elif correct_numbers == 6:
                self.points += 1000
                pick_if = False
                while not pick_if:
                    try:
                        pick = int(
                            input("You got 6 numbers right, what a mad lad. Maybe you should try your luck with a"
                                  " real lottery at this rate. Onto your (amazing rewards) now.\n(1)100 coins + 3 item"
                                  " boxes"
                                  "\n(2)50 coins + 6 golden chests\n(3)100 coins + a lucky charm + remove all"
                                  f" negative effects\n(4)increase your base attack by 50 "
                                  f"(you have {self.attack})\n(5)get 3 extra lives (you have {self.extra_lives})"
                                  "\n(6)+5000 points to your score "))
                        assert (pick in range(1, 7))
                        if pick in range(1, 7):
                            pick_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if pick == 1:
                    self.coins += 100
                    print("Reward claimed!")
                    print("Reward claimed!")
                    Player.item_box(self)
                    time.sleep(1)
                    print("\nAnother one.\n")
                    time.sleep(1)
                    Player.item_box(self)
                    time.sleep(1)
                    print("\nAnd another one.\n")
                    time.sleep(1)
                    Player.item_box(self)
                elif pick == 2:
                    self.coins += 50
                    self.keys += 12
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
                    Player.open_chest(self, 2)
                elif pick == 3:
                    self.coins += 100
                    self.charm = True
                    if self.poisoned:
                        time.sleep(1)
                        self.poisoned = False
                        print("Your poison has been removed!")
                    if self.cursed:
                        time.sleep(1)
                        self.cursed = False
                        print("Your curse has been removed!")
                    if self.slowed:
                        self.slowed = False
                        self.attack = self.attack * 2
                        self.weapon = self.weapon * 2
                        self.weapon2 = self.weapon2 * 2
                        time.sleep(1)
                        print("\nYou are no longer slowed down.")
                    time.sleep(1)
                    print("Reward claimed!")
                elif pick == 4:
                    self.attack += 50
                    print("Reward claimed!")
                elif pick == 5:
                    self.extra_lives += 3
                    print("Reward claimed!")
                elif pick == 6:
                    self.points += 5000
                    print("Reward claimed!")
        else:
            print("Hmm, did you not read the rules or was that on purpose. You cheated regardless. No rewards and"
                  "\nI am taking your coins anyway.")

    def mis_chief(self, bet, amount):
        print("\nOkay, let's go!")
        time.sleep(1)
        p1_score = 0
        p2_score = 0
        p1_wins = 0
        p2_wins = 0
        wins = 1
        turn = 1
        game = 1
        cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pop1 = False
        pop2 = False
        picked_cards = []
        while p1_wins != wins and p2_wins != wins:
            time.sleep(1)
            if turn == 1:
                cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                picked_cards = []
                p1_score = 0
                p2_score = 0
                input(
                    "\nQuick rules: You and the opponent take turns to pick a card, you pick 3 cards each."
                    "\nThere are 11 "
                    "cards on the board. They have value from 1-10 and there is also a special card: the "
                    "chief! When a player picks the chief they instantly lose.\nIf it's the 6th "
                    "turn of the game and the player has already lost "
                    "the game then a little change of a rule comes in:"
                    "\nA chief will give the player an instant victory!"
                    "\nIf the game ends in a draw each player picks one more card. Good luck!(x) ")
                pop1 = False
                pop2 = False
            if game % 2 == 1:
                print("\n1      2      3      4\n"
                      "   5      6       7    \n"
                      "8      9      10     11\n")
                time.sleep(2)
                if turn > 1:
                    print(f"Already picked from the board cards: {picked_cards}\n")
                if turn == 6:
                    max_pos = cards[-1]
                    if (p1_score - p2_score) > max_pos:
                        print("If Brad picks the chief he instantly wins because there is no other option!")
                        time.sleep(2)
                if turn % 2 == 1:
                    correct_num = False
                    while not correct_num:
                        pick = int(input("Pick a card: "))
                        if pick in range(1, 12) and pick not in picked_cards:
                            correct_num = True
                    guess = random.choice(cards)
                    time.sleep(2)
                    if guess != 0:
                        picked_cards.append(pick)
                        p1_score += guess
                        print(f"You got {guess}. Current score: {p1_score}-{p2_score}.")
                        for i in cards:
                            if guess == i:
                                cards.remove(i)
                    else:
                        pop1 = True
                        print("The chief!")
                if turn % 2 == 0:
                    time.sleep(2)
                    correct_num = False
                    while not correct_num:
                        pick = random.randint(1, 12)
                        if pick in range(1, 12) and pick not in picked_cards:
                            correct_num = True
                    time.sleep(2)
                    print(f"Brad picks card {pick} from the board.")
                    time.sleep(2)
                    guess = random.choice(cards)
                    if guess != 0:
                        picked_cards.append(pick)
                        p2_score += guess
                        for i in cards:
                            if guess == i:
                                cards.remove(i)
                        print(f"He gets {guess}. Score: {p1_score}-{p2_score}.")
                    else:
                        pop2 = True
                        print("The chief!")
            turn += 1
            if turn == 7:
                time.sleep(2)
                if not pop1 and not pop2:
                    if p1_score > p2_score:
                        print(f"\nThe game ends {p1_score}-{p2_score} to you and you win.")
                        p1_wins += 1
                        break
                    elif p2_score > p1_score:
                        print(f"\nThe game ends {p2_score}-{p1_score} to Brad and he wins.")
                        p2_wins += 1
                        break
                    elif p1_score == p2_score:
                        print("\nBonus move!\n"
                              "1      2      3      4\n"
                              "   5      6       7    \n"
                              "8      9      10     11\n")
                        print(f"Already picked cards: {picked_cards}\n")
                        time.sleep(2)
                        if game % 2 == 1:
                            correct_num1 = False
                            while not correct_num1:
                                pick = int(input("Pick a card: "))
                                if pick in range(1, 12) and pick not in picked_cards:
                                    correct_num1 = True
                            time.sleep(2)
                            guess = random.choice(cards)
                            if guess != 0:
                                picked_cards.append(pick)
                                p1_score += guess
                                print(f"You got {guess}. Score"
                                      f"x: {p1_score}-{p2_score}.")
                                for i in cards:
                                    if guess == i:
                                        cards.remove(i)
                            else:
                                pop1 = True
                                print("The chief!")
                            if not pop1 and not pop2:
                                correct_num2 = False
                                while not correct_num2:
                                    pick = random.randint(1, 12)
                                    if pick in range(1, 12) and pick not in picked_cards:
                                        correct_num2 = True
                                time.sleep(2)
                                print(f"Brad chooses card {pick} from the board.")
                                time.sleep(2)
                                guess = random.choice(cards)
                                if guess != 0:
                                    picked_cards.append(pick)
                                    p1_score += guess
                                    print(f"He gets {guess}. Score: {p1_score}-{p2_score}.")
                                    for i in cards:
                                        if guess == i:
                                            cards.remove(i)
                                else:
                                    print("The chief!")
                                    pop2 = True
                        if not pop1 and not pop2:
                            time.sleep(2)
                            if p1_score > p2_score:
                                print(f"\nThe game ends {p1_score}-{p2_score} to you and you win!.")
                                p1_wins += 1
                                break
                            elif p2_score > p1_score:
                                print(f"\nThe game ends {p2_score}-{p1_score} to Brad and he wins.")
                                p2_wins += 1
                                break
                if not pop1 and not pop2:
                    game += 1
                    turn = 1
                elif pop1 or pop2:
                    turn = 1
            if pop1 or pop2:
                max_pos = cards[-1]
                if (turn == 6 or turn == 1) and ((p1_score - p2_score) > max_pos or (p2_score - p1_score) > max_pos):
                    time.sleep(2)
                    if game % 2 == 1:
                        if (p1_score - p2_score) > max_pos:
                            if pop2:
                                p2_wins += 1
                                print(
                                    "\nBrad picks the chief but he had no chance "
                                    "to win before so now he instantly wins!")
                                break
                else:
                    time.sleep(2)
                    if pop1:
                        p2_wins += 1
                        print("\nBrad takes the victory after you picked the chief.")
                        break
                    elif pop2:
                        p1_wins += 1
                        print("\nYou have won because Brad picked the chief.")
                        break
                if turn != 7:
                    game += 1
                turn = 1
        time.sleep(2)
        print("\n")
        if p1_wins == 1:
            self.points += 120
        elif p2_wins == 1:
            self.points -= 100
        if bet == 1:
            if p1_wins == 1:
                self.coins += amount
                print(f"You collect the promised {amount} coin(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.coins >= amount:
                        self.coins -= amount
                        print(f"Brad collects the {amount} coin(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 2:
            if p1_wins == 1:
                self.bombs += amount
                print(f"You collect the promised {amount} bomb(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.bombs >= amount:
                        self.bombs -= amount
                        print(f"Brad collects the {amount} bomb(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 3:
            if p1_wins == 1:
                self.keys += amount
                print(f"You collect the promised {amount} key(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.keys >= amount:
                        self.keys -= amount
                        print(f"Brad collects the {amount} key(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 4:
            if p1_wins == 1:
                print(f"You collect the promised item box!. Let's open.")
                Player.item_box(self)
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if not self.charm:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
                    else:
                        self.charm = False
                        print(f"Brad takes your lucky charm. Unfortunate.")

    def rps(self, bet, amount):
        print("Okay, let's go!")
        time.sleep(1.3)
        answers = ["paper", "rock", "scissors"]
        p1_wins = 0
        p2_wins = 0
        while p1_wins == 0 and p2_wins == 0:
            time.sleep(1)
            player_if = False
            while not player_if:
                try:
                    player = int(input("\nPick.\n(1)rock\n(2)paper\n(3)scissors "))
                    assert (player in range(1, 4))
                    if player in range(1, 4):
                        player_if = True
                except:
                    print("\nDidn't type a proper number.")
            comp = random.choice(answers)
            if player == 1:
                if comp == "rock":
                    print(f"Brad chose {comp}, draw!")
                elif comp == "paper":
                    print(f"Brad chose {comp}, victory for him!")
                    p2_wins += 1
                elif comp == "scissors":
                    print(f"Brad chose {comp}, you win!")
                    p1_wins += 1
            elif player == 2:
                if comp == "paper":
                    print(f"Brad chose {comp}, draw!")
                elif comp == "scissors":
                    print(f"Brad chose {comp}, victory for him!")
                    p2_wins += 1
                elif comp == "rock":
                    print(f"Brad chose {comp}, you win!")
                    p1_wins += 1
            elif player == 3:
                if comp == "scissors":
                    print(f"Brad chose {comp}, draw!")
                elif comp == "rock":
                    print(f"Brad chose {comp}, victory for him!")
                    p2_wins += 1
                elif comp == "paper":
                    print(f"Brad chose {comp}, you win!")
                    p1_wins += 1
        time.sleep(2)
        if p1_wins == 1:
            self.points += 100
        elif p2_wins == 1:
            self.points -= 100
        if bet == 1:
            if p1_wins == 1:
                self.coins += amount
                print(f"You collect the promised {amount} coin(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.coins >= amount:
                        self.coins -= amount
                        print(f"Brad collects the {amount} coin(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 2:
            if p1_wins == 1:
                self.bombs += amount
                print(f"You collect the promised {amount} bomb(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.bombs >= amount:
                        self.bombs -= amount
                        print(f"Brad collects the {amount} bomb(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 3:
            if p1_wins == 1:
                self.keys += amount
                print(f"You collect the promised {amount} key(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.keys >= amount:
                        self.keys -= amount
                        print(f"Brad collects the {amount} key(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 4:
            if p1_wins == 1:
                print(f"You collect the promised item box!. Let's open.")
                Player.item_box(self)
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if not self.charm:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
                    else:
                        self.charm = False
                        print(f"Brad takes your lucky charm. Unfortunate.")

    def guess_num(self, bet, amount):
        print("Okay, let's go!")
        time.sleep(1.6)
        p1_wins = 0
        p2_wins = 0
        correct = random.randint(1, 25)
        guess = ""
        attempt = 1
        while guess != correct and attempt <= 4:
            guess_if = False
            while not guess_if:
                try:
                    guess = int(input(f"\nAttempt {attempt}: "))
                    assert (guess in range(1, 26))
                    if guess in range(1, 26):
                        guess_if = True
                except:
                    print("\nDidn't type a proper number.")
            time.sleep(1)
            if guess > correct:
                print("\nLower.")
            elif guess < correct:
                print("\nHigher.")
            attempt += 1
        time.sleep(1)
        if guess != correct:
            print(f"\nYou got no attempts left, the number was {correct}. Victory for Brad.")
            p2_wins += 1
        else:
            print("\nYou get it right, you win the game!")
            p1_wins += 1
        time.sleep(2)
        if p1_wins == 1:
            self.points += 100
        elif p2_wins == 1:
            self.points -= 100
        if bet == 1:
            if p1_wins == 1:
                self.coins += amount
                print(f"You collect the promised {amount} coin(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.coins >= amount:
                        self.coins -= amount
                        print(f"Brad collects the {amount} coin(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 2:
            if p1_wins == 1:
                self.bombs += amount
                print(f"You collect the promised {amount} bomb(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.bombs >= amount:
                        self.bombs -= amount
                        print(f"Brad collects the {amount} bomb(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 3:
            if p1_wins == 1:
                self.keys += amount
                print(f"You collect the promised {amount} key(s). All is fair.")
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if self.keys >= amount:
                        self.keys -= amount
                        print(f"Brad collects the {amount} key(s). It is what it is.")
                    else:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
        elif bet == 4:
            if p1_wins == 1:
                print(f"You collect the promised item box!. Let's open.")
                Player.item_box(self)
            elif p2_wins == 1:
                if "Score gambler" in self.items:
                    print("You score gambler protects your stuff and you lose nothing! Don't ask what happens to Brad.")
                else:
                    if not self.charm:
                        self.dead = True
                        print("You get killed on the spot. I wonder why...")
                        self.brad_enemy = True
                    else:
                        self.charm = False
                        print(f"Brad takes your lucky charm. Unfortunate.")

    def revive(self):
        if "Breath of air" in self.items:
            time.sleep(1)
            if self.breath == 1:
                revive = random.randint(1, 2)
                if revive == 1:
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    self.health = max_hp
                    self.breath -= 1
                    self.dead = False
                    if self.frozen:
                        self.frozen = False
                    print("\nYou have been revived on the spot by your Breath of air! This is the "
                          "last one of the run\n"
                          "so be careful.\n")
            elif self.breath == 2:
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                self.health = max_hp
                self.breath -= 1
                self.dead = False
                if self.frozen:
                    self.frozen = False
                print("\nYou have been revived on the spot by your Breath of air! Back to full health with a chance"
                      "\nto happen again.\n")
        time.sleep(1.5)
        if self.dead and not self.frozen:
            if self.extra_lives > 0:
                time.sleep(2)
                self.dead = False
                self.health = 75
                self.extra_lives -= 1
                print("\nFor whatever reason you died. You had an extra life so you have been revived on "
                      "the spot and you now have 75hp."
                      f"\nYour extra lives are now {self.extra_lives}\n")
                time.sleep(2)

    def item_box(self):
        if "Mute button" in self.items:
            print("....... .... ......")
        else:
            print("Opening item box...")
        time.sleep(2)
        if len(item_pool) > 0:
            item1 = random.choice(item_pool)
            item2 = random.choice(item_pool)
            item = random.choice(item_pool)
            if "Reality stone" in self.items and self.stone == 3:
                time.sleep(1)
                if "Broken glasses" in self.items and len(item_pool) >= 2:
                    if "Mute button" in self.items:
                        print(f"\n... .... ... {item1} ... {item2} .... ... .... ....")
                    else:
                        print(f"\nYou will get {item1} and {item2} from the item box.")
                else:
                    if "Mute button" in self.items:
                        print(f"... .... ... {item} .... ... .... ....")
                    else:
                        print(f"You will get {item} from the item box.")
                stone_if = False
                while not stone_if:
                    try:
                        if "Mute button" in self.items:
                            stone = int(input("\n...... ... ....(s)?\n(1)...\n(2).. "))
                        else:
                            stone = int(input("\nReroll the item(s)?\n(1)yes\n(2)no "))
                        assert (stone in range(1, 3))
                        if stone in range(1, 3):
                            stone_if = True
                    except:
                        print("\nDidn't type a proper number.")
                time.sleep(1)
                if stone == 1:
                    self.stone = 0
                    item1 = random.choice(item_pool)
                    item2 = random.choice(item_pool)
                    item = random.choice(item_pool)
            if "Broken glasses" in self.items and len(item_pool) >= 2:
                grab_if = False
                while not grab_if:
                    try:
                        if "Mute button" in self.items:
                            grab = int(input(f"... ... {item1} .. {item2} .... ... .... ..., ..., ...... ....... 2 "
                                             f"..... ...... .. ....\n"
                                             f"...... ........\n(1).... {item1}\n(2).... {item2}\n(3).... .... "))
                        else:
                            grab = int(input(f"You get {item1} or {item2} from the item box, yes, choice between 2 "
                                             f"items thanks to your\n"
                                             f"broken glasses.\n(1)take {item1}\n(2)take {item2}\n(3)take none "))
                        assert (grab in range(1, 4))
                        if grab in range(1, 4):
                            grab_if = True
                    except:
                        print("\nDidn't type a proper number.")
                time.sleep(1)
                if grab == 1:
                    self.items.append(item1)
                    item_pool.remove(item1)
                    Player.get_item(self, item1)
                elif grab == 2:
                    self.items.append(item2)
                    item_pool.remove(item2)
                    Player.get_item(self, item2)
                elif grab == 3:
                    print("Okay, your choice.")
            else:
                grab_if = False
                while not grab_if:
                    try:
                        if "Mute button" in self.items:
                            grab = int(input(f"... ... {item} .... ... .... .... .... ..?\n(1)...\n(2).. "))
                        else:
                            grab = int(input(f"You get {item} from the item box. Take it?\n(1)yes\n(2)no "))
                        assert (grab in range(1, 3))
                        if grab in range(1, 3):
                            grab_if = True
                    except:
                        print("\nDidn't type a proper number.")
                time.sleep(1)
                if grab == 1:
                    self.items.append(item)
                    item_pool.remove(item)
                    Player.get_item(self, item)
                elif grab == 2:
                    if "Mute button" in self.items:
                        print("...., .... .......")
                    else:
                        print("Okay, your choice.")
        elif len(item_pool) == 0:
            self.points += 200
            print("There are literally no items left in the item pool so I am giving you some points instead for your"
                  "\nscore and I don't care if you are playing for points or not.")

    def get_item(self, itemm):
        print("\n")
        if itemm == "Mega bomb":
            print("Okay, you get your mega bomb. It's actually more boring than it sounds.\n"
                  "You'll see. It is an item unlocked by default after all...")
        elif itemm == "Blessed flower":
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            if self.health < max_hp:
                self.health += 2
                if self.health > max_hp:
                    self.health = max_hp
            print("The blessed flower will consistently recover health for you. One of the solid items\n"
                  "unlocked by default.")
        elif itemm == "Golden key":
            print("Golden key is the same as mega bomb but for keys. Yes, boring.")
        elif itemm == "Time stone":
            if self.slowed:
                self.slowed = False
                self.attack = self.attack * 2
                self.weapon = self.weapon * 2
                self.weapon2 = self.weapon2 * 2
                time.sleep(1)
                print("\nYou are no longer slowed down.")
            print("This item has like one or 2 specific uses, hope you find them.")
        elif itemm == "Brochure":
            print("The brochure will show you random tips after each room. Not saying how useful they are.")
        elif itemm == "Score gambler":
            self.points += 100
            print("You might want to keep an eye on your score with the score gambler o_o")
        elif itemm == "Light trainers":
            print("Running away from enemies and past them will now cost you no health despite what the text is saying"
                  ".\nIn my opinion an elite item.")
        elif itemm == "Broken glasses":
            print("You will want to find some more item boxes or weapons with this item.")
        elif itemm == "Giant coin":
            self.coins += 25
            print("Show me the moneeeeeey!!! (25 coins on pickup as well)")
        elif itemm == "Breath of air":
            print("Think of it as an extra life but better.")
        elif itemm == "Detector":
            print("Some secrets are no longer secrets...")
        elif itemm == "Brave juice":
            print("The only use for the give up button.")
        elif itemm == "Shiny necklace":
            if self.cursed:
                self.cursed = False
            if self.poisoned:
                self.poisoned = False
            if self.slowed:
                self.slowed = False
                self.attack = self.attack * 2
                self.weapon = self.weapon * 2
                self.weapon2 = self.weapon2 * 2
            print("Say goodbye to negative effects!")
        elif itemm == "Belt":
            self.attack += 5
            print("Do you like the killing enemies flawlessly message? I have some good news for you!")
        elif itemm == "Restart button":
            print("Oh boy this is a wild one. Just don't be surprised if it activates on its own at some point.")
        elif itemm == "Russian roulette":
            print("You get to shoot yourself in the head, let's see if you survive it.")
            survive = random.randint(1, 6)
            if survive != 6:
                print("\nYou are okay. That wasn't stressful at all now, was it?")
            elif survive == 6:
                print("\nBoom. You are dead.")
                self.dead = True
                Player.revive(self)
        elif itemm == "Metal and a dream":
            self.attack += 7
            print("You will get 2 random weapons and an attack boost. Yeah, that's all that is. Just give me a second.")
            time.sleep(3)
            weapon1 = random.randint(18, 60)
            weapon1_hp = random.randint(3, 7)
            take_if = False
            while not take_if:
                try:
                    take = int(input(f"If you take the first weapon you will have {weapon1} "
                                     f"attack +{self.attack} (your base attack), and it will last for "
                                     f"{weapon1_hp} rooms. "
                                     "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                     "\nyes(2) - put it in slot 2(not equipping it)\n"
                                     "Recommended to click 1 if you have no weapons "
                                     "and click 2 if you have 1 weapon.\n"
                                     "If you have 2 weapons it will replace the one you have in the slot you chose."
                                     "\nno(3) "))
                    assert (take in range(1, 4))
                    if take in range(1, 4):
                        take_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take != 3:
                Player.take_weapon(self, take, weapon1, weapon1_hp)
            weapon2 = random.randint(18, 60)
            weapon2_hp = random.randint(3, 7)
            print("\n")
            take2_if = False
            while not take2_if:
                try:
                    take2 = int(input(f"If you take the second weapon you will have {weapon2} "
                                      f"attack +{self.attack} (your base attack), and it will last for "
                                      f"{weapon2_hp} rooms. "
                                      "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                      "\nyes(2) - put it in slot 2(not equipping it)\n"
                                      "Recommended to click 1 if you have no weapons "
                                      "and click 2 if you have 1 weapon.\n"
                                      "If you have 2 weapons it will replace the one you have in the slot you chose."
                                      "\nno(3) "))
                    assert (take2 in range(1, 4))
                    if take2 in range(1, 4):
                        take2_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take2 != 3:
                Player.take_weapon(self, take2, weapon2, weapon2_hp)
        elif itemm == "Red wig":
            print("You put the wig on and you look stupid.")
        elif itemm == "Lucky 13":
            print("\"You find something after leaving the room.\"")
        elif itemm == "Strong juice":
            print("Guys we did it, we found 200 health.")
        elif itemm == "Mute button":
            print("Troll item, you are a bit deaf now lol.")
        elif itemm == "Portable black hole":
            print("Only for the biggest of dangers.")
        elif itemm == "Reality stone":
            print("Reality can be whatever I want.")
        elif itemm == "Mirror stand":
            self.attack = self.attack * 2
            print("IS THIS A JOJO REFERENCE yes it is you get a stand that is... yourself but with your own power\n"
                  "so your total base damage is doubled. No, you cannot give your backup weapon to the stand, sorry.")
        elif itemm == "Cursed staff":
            print("The cursed staff starts glowing aaaaaand guess what.")
            time.sleep(3)
            print("Satan appears and kills you. Ouch.")
            self.dead = True
            self.points += 1500
            Player.revive(self)

    def myst_drink(self):
        time.sleep(3)
        if "Shiny necklace" in self.items:
            effects = [1, 3, 4, 6, 9, 10]
            effect = random.choice(effects)
        else:
            effect = random.randint(1, 11)
        if effect == 1:
            attack = random.randint(7, 15)
            self.attack += attack
            if "Mute button" in self.items:
                print(f"... ..... .. ... ... .... .... ...... ......... .. {attack}. .....")
            else:
                print(f"You drink it and get your base attack increased by {attack}. Nice.")
        elif effect == 2:
            self.attack -= 5
            if "Mute button" in self.items:
                print("... ..... .. ... ... .... .... ...... ......... .. 5. .....")
            else:
                print("You drink it and get your base attack decreased by 5. Ouch.")
            if self.attack < 0:
                self.attack = 0
        elif effect == 3:
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            self.health = max_hp
            if "Mute button" in self.items:
                print("... ..... .. ... ... ..... ....... .......")
            else:
                print("You drink it and get fully healed. Lovely.")
        elif effect == 4:
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            self.health += 10
            if self.health > max_hp:
                self.health = max_hp
            if "Mute button" in self.items:
                print("... ..... .. ... ... ...... .. 10. .....")
            else:
                print("You drink it and get healed by 10. Nice.")
        elif effect == 5:
            self.health -= 10
            if self.health <= 0:
                self.dead = True
                if "Mute button" in self.items:
                    print("... .... 10 ...... ... ... .. ... ...... ..")
                else:
                    print("You lose 10 health and die on the floor. L.")
            else:
                if "Mute button" in self.items:
                    print("... ..... .. ... .... 10 ... ....")
                else:
                    print("You drink it and lose 10 hp. Oof.")
            if self.dead:
                Player.revive(self)
        elif effect == 6:
            self.bombs += 1
            if "Mute button" in self.items:
                print("... ....... ...... ... ..... . ..... ... ... .... .. ........ .. ......\n"
                      "... ... ..... .. ... ... . .....")
            else:
                print("You feel... spicy. You vomit a bomb. Idk how that is supposed to happen\n"
                      "but the point is you get a bomb.")
        elif effect == 7:
            if self.poisoned:
                if "Mute button" in self.items:
                    print(".... .. ........ .. .. . ...... ... . ...'. ..... .... ..... ..'. .. ...........")
                else:
                    print("This is supposed to be a poison but I won't stack them since it'd be unplayable.")
            if not self.poisoned:
                self.poisoned = True
                if "Mute button" in self.items:
                    print("... ... ........ .. ... ...... ..... .... .... .........")
                else:
                    print("You get poisoned by the drink. Could have been better...")
        elif effect == 8:
            if self.cursed:
                if "Mute button" in self.items:
                    print("... ... ....... ..... ... .... ...'. ..... (.... ...... ....... ...).")
                else:
                    print("You get another curse but they don't stack (they better fucking not).")
            if not self.cursed:
                self.cursed = True
                if "Mute button" in self.items:
                    print("..'. . ...... ...... .... ..... ... ... ... .. ... ..... ...."
                          "\n\"...'. .... .... ....., ....\" - ........")
                else:
                    print("It's a cursed drink. That means you can die at any point now."
                          "\n\"Don't take your pills, kids\" - Sinvicta")
        elif effect == 9:
            weapon = random.randint(18, 40)
            weapon_hp = random.randint(3, 5)
            take_if = False
            while not take_if:
                try:
                    take = int(input(f"You vomit a wooden sword! If you take it you will have {weapon} "
                                     f"attack +{self.attack} (your base attack), and it will last for "
                                     f"{weapon_hp} rooms. "
                                     "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                     "\nyes(2) - put it in slot 2(not equipping it)\n"
                                     "Recommended to click 1 if you have no weapons "
                                     "and click 2 if you have 1 weapon.\n"
                                     "If you have 2 weapons it will replace the one you have in the slot you chose."
                                     "\nno(3) "))
                    assert (take in range(1, 4))
                    if take in range(1, 4):
                        take_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take != 3:
                Player.take_weapon(self, take, weapon, weapon_hp)
        elif effect == 10:
            print("You shit out an item box. Yes, you heard me right.")
            Player.item_box(self)
        elif effect == 11:
            if self.slowed:
                if "Mute button" in self.items:
                    print("... ... ....... ...... .... .. .... ..... ... .. .......")
                else:
                    print("You are already slowed down so this drink has no effect.")
            else:
                if "Time stone" in self.items:
                    if "Mute button" in self.items:
                        print("... ...... .... .... ...... .... .... ... .... .... ..... ........ ...!")
                    else:
                        print("You should have been slowed down here but your time stone protects you!")
                else:
                    self.slowed = True
                    if self.slowed:
                        self.attack = self.attack // 2 + 1
                        if self.weapon > 0:
                            self.weapon = self.weapon // 2 + 1
                        if self.weapon2 > 0:
                            self.weapon2 = self.weapon2 // 2 + 1
                    if "Mute button" in self.items:
                        print("... ..... ... ...... ... ..... ... ... ......... ..... .... ...... ......")
                    else:
                        print("The drink has slowed you down. You are basically doing half damage now...")

    def ask_potion(self):
        time.sleep(1)
        max_hp = 100
        if "Strong juice" in self.items:
            max_hp = 200
        if self.health < max_hp:
            if self.potion1 > 0:
                take_potion_if = False
                while not take_potion_if:
                    try:
                        if "Mute button" in self.items:
                            take_potion = int(input(f"\n.... ........\n...... 1: {self.potion1}     "
                                                    f"...... 2: {self.potion2}"
                                                    f"     ...... 3: {self.potion3}\n.. ... .... .. ..... ...?\n"
                                                    f".... .1(1)   .... .2(2)   .... .3(3)    .... ....(4) "))
                        else:
                            take_potion = int(input(f"\nYour potions:\nPotion 1: {self.potion1}     "
                                                    f"Potion 2: {self.potion2}"
                                                    f"     Potion 3: {self.potion3}\nDo you want to drink one?\n"
                                                    f"take p1(1)   take p2(2)   take p3(3)    take none(4) "))
                        assert (take_potion in range(1, 5))
                        if take_potion in range(1, 5):
                            take_potion_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take_potion == 1:
                    Player.drink_potion(self, take_potion)
                    if self.potion2 > 0 and self.potion3 > 0:
                        take_potion_if = False
                        while not take_potion_if:
                            try:
                                take_potion = int(
                                    input("Drink another potion?\n(1)no\n(2)yes, potion 2.\n(3)yes, potion 3 "))
                                assert (take_potion in range(1, 4))
                                if take_potion in range(1, 4):
                                    take_potion_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if take_potion == 2 or take_potion == 3:
                            Player.drink_potion(self, take_potion)
                            take_potion_if = False
                            while not take_potion_if:
                                try:
                                    take_potion = int(input("How about your last one?\n(1)yes\n(2)nah "))
                                    assert (take_potion in range(1, 3))
                                    if take_potion in range(1, 3):
                                        take_potion_if = True
                                except:
                                    print("\nDidn't type a proper number.")
                            if take_potion == 1:
                                if self.potion2 > 0:
                                    Player.drink_potion(self, 2)
                                elif self.potion3 > 0:
                                    Player.drink_potion(self, 3)
                    elif self.potion2 > 0 and self.potion3 == 0:
                        take_potion_if = False
                        while not take_potion_if:
                            try:
                                take_potion = int(input("You have a potion in your 2nd slot too.\n(1)drink\n(2)"
                                                        "don't care "))
                                assert (take_potion in range(1, 3))
                                if take_potion in range(1, 3):
                                    take_potion_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if take_potion == 1:
                            Player.drink_potion(self, 2)
                    elif self.potion3 > 0 and self.potion2 == 0:
                        take_potion_if = False
                        while not take_potion_if:
                            try:
                                take_potion = int(input("You have a potion in your 3rd slot too.\n(1)drink\n(2)"
                                                        "don't care "))
                                assert (take_potion in range(1, 3))
                                if take_potion in range(1, 3):
                                    take_potion_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if take_potion == 1:
                            Player.drink_potion(self, 3)
                elif take_potion == 2:
                    if self.potion2 > 0:
                        Player.drink_potion(self, take_potion)
                        if self.potion3 > 0:
                            take_potion_if = False
                            while not take_potion_if:
                                try:
                                    take_potion = int(input("Drink another potion?\n(1)yes, potion 1.\n(2)no\n(3)yes, "
                                                            "potion 3 "))
                                    assert (take_potion in range(1, 4))
                                    if take_potion in range(1, 4):
                                        take_potion_if = True
                                except:
                                    print("\nDidn't type a proper number.")
                            if take_potion == 1 or take_potion == 3:
                                Player.drink_potion(self, take_potion)
                                take_potion_if = False
                                while not take_potion_if:
                                    try:
                                        take_potion = int(input("How about your last one?\n(1)yes\n(2)nah "))
                                        assert (take_potion in range(1, 3))
                                        if take_potion in range(1, 3):
                                            take_potion_if = True
                                    except:
                                        print("\nDidn't type a proper number.")
                                if take_potion == 1:
                                    if self.potion3 > 0:
                                        Player.drink_potion(self, 3)
                                    elif self.potion1 > 0:
                                        Player.drink_potion(self, 1)
                        elif self.potion3 == 0:
                            take_potion_if = False
                            while not take_potion_if:
                                try:
                                    take_potion = int(
                                        input("You have a potion in your 1st slot too.\n(1)drink\n(2)don't care "))
                                    assert (take_potion in range(1, 3))
                                    if take_potion in range(1, 3):
                                        take_potion_if = True
                                except:
                                    print("\nDidn't type a proper number.")
                            if take_potion == 1:
                                Player.drink_potion(self, 1)
                    else:
                        print(f"Wrong number, there is no potion in {take_potion} slot, sorry.")
                elif take_potion == 3:
                    if self.potion3 > 0:
                        Player.drink_potion(self, take_potion)
                        take_potion_if = False
                        while not take_potion_if:
                            try:
                                take_potion = int(
                                    input("Drink another potion?\n(1)yes, potion 1.\n(2)yes, potion 2\n(3)no "))
                                assert (take_potion in range(1, 4))
                                if take_potion in range(1, 4):
                                    take_potion_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if take_potion == 1 or take_potion == 2:
                            Player.drink_potion(self, take_potion)
                            take_potion_if = False
                            while not take_potion_if:
                                try:
                                    take_potion = int(input("How about your last one?\n(1)yes\n(2)nah "))
                                    assert (take_potion in range(1, 3))
                                    if take_potion in range(1, 3):
                                        take_potion_if = True
                                except:
                                    print("\nDidn't type a proper number.")
                            if take_potion == 1:
                                if self.potion1 > 0:
                                    Player.drink_potion(self, 1)
                                elif self.potion2 > 0:
                                    Player.drink_potion(self, 2)
                    else:
                        print(f"Wrong number, there is no potion in {take_potion} slot, sorry.")
                if self.potion3 > 0 and self.potion2 == 0:
                    self.potion2 = self.potion3
                    self.potion3 = 0
                if self.potion2 > 0 and self.potion1 == 0:
                    self.potion1 = self.potion2
                    self.potion2 = 0

    def drink_potion(self, take):
        if take == 1:
            self.health += self.potion1
            self.potion1 = 0
        elif take == 2:
            self.health += self.potion2
            self.potion2 = 0
        elif take == 3:
            self.health += self.potion3
            self.potion3 = 0
        max_hp = 100
        if "Strong juice" in self.items:
            max_hp = 200
        if self.health > max_hp:
            self.health = max_hp
        time.sleep(1)
        if "Mute button" in self.items:
            print(f"\n.... ...... .. ... {self.health}.\n")
        else:
            print(f"\nYour health is now {self.health}.\n")

    def take_potion(self, potion):
        potions = [self.potion1, self.potion2, self.potion3]
        potions.sort()
        if all(potions) != 0:
            if potion > potions[0]:
                if self.potion1 == potions[0]:
                    self.potion1 = potion
                elif self.potion2 == potions[0]:
                    self.potion2 = potion
                elif self.potion3 == potions[0]:
                    self.potion3 = potion
        elif 0 == self.potion3 and self.potion1 != 0 and self.potion2 != 0:
            self.potion3 = potion
        elif self.potion2 == 0 and self.potion1 != 0:
            self.potion2 = potion
        elif self.potion1 == 0:
            self.potion1 = potion

    def buy_potion(self, price, discount, potion):
        if discount > 0:
            price = math.floor(price - price * (discount / 100))
            if "Mute button" in self.items:
                print(f"... .... . {discount}% ........ .......")
            else:
                print(f"You have a {discount}% discount wheeeee")
        if self.coins >= price:
            self.coins -= price
            if "Mute button" in self.items:
                print(f".... .... .. {price} ....., ..... ... ... .......... ...\n.... ..... ... ... {self.coins}")
            else:
                print(f"That will be {price} coins, thank you for purchasing uwu\nYour coins are now {self.coins}")
            Player.take_potion(self, potion)
        elif self.coins < price:
            if "Mute button" in self.items:
                print("....., ... ...'. .... ...... ......")
            else:
                print("Sorry, you don't have enough coins.")

    def ask_weapon(self):
        if self.weapon2 > 0:
            equip_if = False
            while not equip_if:
                try:
                    if "Mute button" in self.items:
                        equip = int(input(f"........ ......: +{self.weapon} ......, {self.weapon_hp} .....\n"
                                          f"......: +{self.weapon2} ......, {self.weapon2_hp} .....\n"
                                          f"(1)..... .... ...... ......\n(2).. "))
                    else:
                        equip = int(input(f"Equipped weapon: +{self.weapon} attack, {self.weapon_hp} rooms\n"
                                          f"Backup: +{self.weapon2} attack, {self.weapon2_hp} rooms\n"
                                          f"(1)Equip your backup weapon\n(2)No "))
                    assert (equip in range(1, 3))
                    if equip in range(1, 3):
                        equip_if = True
                except:
                    print("\nDidn't type a proper number.")
            if equip == 1:
                Player.equip_weapon(self)

    def equip_weapon(self):
        self.weapon, self.weapon2 = self.weapon2, self.weapon
        self.weapon_hp, self.weapon2_hp = self.weapon2_hp, self.weapon_hp
        if "Mute button" in self.items:
            print("\n... .... ... ........ .... ..... .......\n")
        else:
            print("\nYou have now equipped your other weapon.\n")

    def take_weapon(self, take, weapon, weapon_hp):
        if "Broken glasses" in self.items:
            time.sleep(0.8)
            weapon = weapon * 2
            print("Your broken glasses item doubles the weapon's damage!")
        if self.slowed:
            weapon = weapon // 2 + 1
        if take == 1:
            if self.weapon != 0 and self.weapon2 == 0:
                self.weapon2 = weapon
                self.weapon2_hp = weapon_hp
                Player.equip_weapon(self)
            else:
                self.weapon = weapon
                self.weapon_hp = weapon_hp
        elif take == 2:
            if self.weapon2 != 0 and self.weapon == 0:
                self.weapon = weapon
                self.weapon_hp = weapon_hp
                Player.equip_weapon(self)
            else:
                self.weapon2 = weapon
                self.weapon2_hp = weapon_hp

    def buy_weapon(self, price, discount, weapon, weapon_hp):
        if discount > 0:
            price = math.floor(price - price * (discount / 100))
            if "Mute button" in self.items:
                print(f"... .... . {discount}% ........ .......")
            else:
                print(f"You have a {discount}% discount wheeeee")
        if self.coins >= price:
            self.coins -= price
            if "Mute button" in self.items:
                print(f".... ..... .. {price} ....., ..... ... ... .......... ...\n.... ..... ... ... {self.coins}")
            else:
                print(f"That would be {price}, thanks for you purchase\nYour coins are now {self.coins}")
            take_if = False
            while not take_if:
                try:
                    take = int(input("Which slot do you want to put it in?\n(1)slot 1 - equip it"
                                     "\n(2)slot 2 - put it in the backup slot "))
                    assert (take in range(1, 3))
                    if take in range(1, 3):
                        take_if = True
                except:
                    print("\nDidn't type a proper number.")
            Player.take_weapon(self, take, weapon, weapon_hp)
        elif self.coins < price:
            if "Mute button" in self.items:
                print("....., ... ...'. .... ...... ......")
            else:
                print("Sorry, you don't have enough money, get a job.")

    def buy_keys(self, price, discount, amount):
        if discount > 0:
            price = math.floor(price - price * (discount / 100))
            if "Mute button" in self.items:
                print(f"... .... . {discount}% ........ .......")
            else:
                print(f"You have a {discount}% discount wheeeee")
        if self.coins >= price:
            self.coins -= price
            if "Mute button" in self.items:
                print(f".... .... .. {price} ....., ..... ... ... .......... ...\n.... ..... ... ... {self.coins}")
            else:
                print(f"That will be {price} coins, thank you for purchasing uwu\nYour coins are now {self.coins}")
            self.keys += amount
        elif self.coins < price:
            if "Mute button" in self.items:
                print("....., ... ...'. .... ...... ......")
            else:
                print("Sorry, you don't have enough coins.")

    def buy_bombs(self, price, discount, amount):
        if discount > 0:
            price = math.floor(price - price * (discount / 100))
            if "Mute button" in self.items:
                print(f"... .... . {discount}% ........ .......")
            else:
                print(f"You have a {discount}% discount wheeeee")
        if self.coins >= price:
            self.coins -= price
            if "Mute button" in self.items:
                print(f".... .... .. {price} ....., ..... ... ... .......... ...\n.... ..... ... ... {self.coins}")
            else:
                print(f"That will be {price} coins, thank you for purchasing uwu\nYour coins are now {self.coins}")
            self.bombs += amount
        elif self.coins < price:
            if "Mute button" in self.items:
                print("....., ... ...'. .... ...... ......")
            else:
                print("Sorry, you don't have enough coins.")

    def special_room(self):
        if "Mute button" in self.items:
            print("\n....... ....!\n")
        else:
            print("\nSpecial room!\n")
        time.sleep(2)
        layout = random.randint(1, 15)
        if layout == 1:
            if "Mute button" in self.items:
                print("....... ... ... ... ..... ...... .. .... ..... ..'. ........ ...... .... . ...... ..... ...."
                      "\n.. .... .. ...... .. .... (.. ...'.).")
            else:
                print("Aaaaand you got the empty layout of this room. It's slightly darker than a normal empty room"
                      "\nif that is useful to know (it isn't).")
        elif layout == 2 or layout == 3:
            weapon = random.randint(20, 40)
            weapon_hp = random.randint(4, 6)
            take_if = False
            while not take_if:
                try:
                    if "Mute button" in self.items:
                        take = int(input(f"... .... . ...... .. ... ....... ..... + {weapon} ......, ..... {weapon_hp}"
                                         f" ......\n(1)... .. .... 1 - ..... ..\n(2)... .. .... 2 - ......\n(3)..... "
                                         f".. "))
                    else:
                        take = int(input(f"You find a weapon in the special room. + {weapon} attack, lasts {weapon_hp}"
                                         f" rooms.\n(1)put in slot 1 - equip it\n(2)put in slot 2 - backup\n(3)leave "
                                         f"it "))
                    assert (take in range(1, 4))
                    if take in range(1, 4):
                        take_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take == 1 or take == 2:
                Player.take_weapon(self, take, weapon, weapon_hp)
        elif layout == 4:
            weapon = random.randint(40, 60)
            weapon_hp = random.randint(6, 8)
            take_if = False
            while not take_if:
                try:
                    if "Mute button" in self.items:
                        take = int(input(f"... .... . ...."
                                         f" ...... .. ... ....... ..... + {weapon} ......, ..... {weapon_hp}"
                                         f" ......\n(1)... .. .... 1 - ..... ..\n(2)... .. .... 2 - ......\n(3)..... "
                                         f".. "))
                    else:
                        take = int(input(f"You find a good weapon in the special room. + {weapon} attack, "
                                         f"lasts {weapon_hp}"
                                         f" rooms.\n(1)put in slot 1 - equip it\n(2)put in slot 2 - "
                                         f"backup\n(3)leave it "))
                    assert (take in range(1, 4))
                    if take in range(1, 4):
                        take_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take == 1 or take == 2:
                Player.take_weapon(self, take, weapon, weapon_hp)
        elif layout == 5:
            drink_if = False
            while not drink_if:
                try:
                    if "Mute button" in self.items:
                        drink = int(input("... .... 4 (..., ....) .......... ...... .. ... ....... ..... "
                                          ".. ... .... .. ..... ... .. ....?"
                                          "\n(1)...\n(2).... .... .... "))
                    else:
                        drink = int(input("You find 4 (yes, four) mysterious drinks in the special room. "
                                          "Do you want to drink one of them?"
                                          "\n(1)yes\n(2)nope nope nope "))
                    assert (drink in range(1, 3))
                    if drink in range(1, 3):
                        drink_if = True
                except:
                    print("\nDidn't type a proper number.")
            if drink == 1:
                Player.myst_drink(self)
                drink2_if = False
                while not drink2_if:
                    try:
                        if "Mute button" in self.items:
                            drink_2 = int(input(".. ... .... .. ..... ....... ...?"
                                                "\n(1)...\n(2).. "))
                        else:
                            drink_2 = int(input("Do you want to drink another one?"
                                                "\n(1)yes\n(2)no "))
                        assert (drink_2 in range(1, 3))
                        if drink_2 in range(1, 3):
                            drink2_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if drink_2 == 1:
                    Player.myst_drink(self)
                    drink3_if = False
                    while not drink3_if:
                        try:
                            drink_3 = int(input("Do you want to drink another one?"
                                                "\n(1)yes\n(2)no "))
                            assert (drink_3 in range(1, 3))
                            if drink_3 in range(1, 3):
                                drink3_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if drink_3 == 1:
                        Player.myst_drink(self)
                        drink4_if = False
                        while not drink4_if:
                            try:
                                drink_4 = int(input("Do you want to drink the last one?"
                                                    "\n(1)yes\n(2)no "))
                                assert (drink_4 in range(1, 3))
                                if drink_4 in range(1, 3):
                                    drink4_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if drink_4 == 1:
                            Player.myst_drink(self)
        elif layout == 6:
            self.keys += 5
            if "Mute button" in self.items:
                print("... .... 5 .... .. ... ....... ..... .... .....")
            else:
                print("You find 5 keys in the special room. Very nice.")
        elif layout == 7:
            self.charm = True
            self.cursed = True
            self.coins += 15
            if "Mute button" in self.items:
                print("... ... ... ........ ...... .. .... .. .... .... ..... ... . ..... .....\n"
                      "... .... ...... .... 15 ......")
            else:
                print("You got the weirdest layout of all. So this room gives you a lucky charm\n"
                      "and a... curse. Also 15 coins.")
            if "Shiny necklace" in self.items:
                self.cursed = False
                time.sleep(2)
                print("You have a shiny necklace, just kidding, of course you don't have a curse :)")
        elif layout == 8:
            self.charm = True
            if "Mute button" in self.items:
                print("... ... . ..... ..... .... ... ....... ..... .......")
            else:
                print("You get a lucky charm from the special room. Lovely.")
        elif layout == 9:
            potion1 = 50
            potion2 = 10
            potion3 = 5
            print("You get a room with 3 potions: 50, 10, 5 health. They replace the weakest ones you have,\n"
                  "blah blah.")
            Player.take_potion(self, potion1)
            Player.take_potion(self, potion2)
            Player.take_potion(self, potion3)
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            if self.health < max_hp:
                Player.ask_potion(self)
        elif layout == 10:
            print("You get a potion that heals... 1. \"Haha\". I know, I know, I just need to have some "
                  "piss taking layouts in here.")
            Player.take_potion(self, 1)
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            if self.health < max_hp:
                Player.ask_potion(self)
        elif layout == 11:
            print("You get 3 wooden chests. Let's open up!")
            Player.open_chest(self, 0)
            Player.open_chest(self, 0)
            Player.open_chest(self, 0)
        elif layout == 12:
            keys = random.randint(1, 3)
            bombs = random.randint(1, 4)
            coins = random.randint(20, 40)
            self.keys += keys
            self.bombs += bombs
            self.coins += coins
            print(f"You get a special room full of consumables! {coins} coins, {bombs} bombs, {keys} keys.")
        elif layout == 13:
            special = random.randint(1, 8)
            if special != 8:
                self.charm = True
                print("You get a lucky charm in the special room. Cool.")
            elif special == 8:
                time.sleep(2)
                msg_if = False
                while not msg_if:
                    try:
                        msg = int(input("This is the special room layout 13, a good place to put a"
                                        " thank you message to the player. If you have not seen this message before"
                                        "\nplease click 1, it's long but hopefully worth it."
                                        "\n(1)show the message\n(2)skip it and move on to the reward "))
                        assert (msg in range(1, 3))
                        if msg in range(1, 3):
                            msg_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if msg == 1:
                    time.sleep(1)
                    input("\nSo this is one of the rarest rooms in the game. I believe it's an appropriate place"
                          "\nto stick a thank you message to the player.\n(x) ")
                    input("\nI know the text after a run thanks you but this is a proper one. I just want to pour"
                          "\nmy heart into this.\n(x) ")
                    input("\nI suck at a lot of things including programming, but the point here is not my "
                          "incompetence.\nThis should be motivation. The laziest person in the world just out of"
                          " nowhere\ndecided to make a game with basically zero knowledge about coding.\n(x) ")
                    input("\nIf you got tired just spam x a few times and that's it. If you are still reading I"
                          "\nwant you to know that you are capable of not literally anything, but quite a lot."
                          "\n(x) ")
                    input("\nI know so many different people who are unique in their own way and have their own"
                          "\"thing\"\nwhile I do not. Okay this got depressing, moving on to the main point.\n(x) ")
                    input("\nAt the moment this code consists of 3527 lines. I made hundreds of test runs and pretty"
                          "\n much all\nof them had bugs and I am too stupid to remember them so I decided to"
                          " write\ndown each one of them and I fixed them as they appeared again in a different shape"
                          "\nbecause as I mentioned I suck at coding, all i did was watch 2, yes, two videos about"
                          "coding.\n(x) ")
                    input("\nI took a break as I worked on this for about a month and after a break I am back and"
                          " writing this message\nbecause I ran out of ideas. I hope I will have some ideas after this"
                          "\nmessage because I don't feel this game is finished yet, no matter how simple it is and"
                          "looks.\n(x)")
                    input("\nThe fact that you are reading this message means you have enjoyed the game long enough"
                          "\nto reach this message (or just got insanely lucky). This feels surreal.\n(x) ")
                    input("\nIsn't it funny how I don't even know how to \'share\' this game at the current moment,"
                          "\nor how to run it on different programs. I will try to find how to do it. You are reading"
                          "\nthis so I guess I've figured it out.\n(x) ")
                    input("\nTry to get what you want. Do it for yourself. Do it for the people who love you. (I do)."
                          "\nIf I can do what I want then so can you. Best of luck <3"
                          "\n(x) ")
                    input("\nБлагодаря ти Стояне, благодаря ти, Ванка. Благодаря ви за компанията и моментите ни заедно"
                          "\n през всички тези години. Дано сте добре в момента. Насълзих се докато пиша това.\n"
                          "Стояне, тази игра е за теб защото помислих че ще ти хареса. Дано съм бил прав.\nСега е 16"
                          " декември 2021, към 20 часа и пиша това вместо да уча за класното по френски утре.\nОбичам"
                          " ви с Ванката повече от всичко и ви желая най-доброто. Вие сте най-добрите приятели "
                          "на света.\nlast x(x) ")
                elif msg == 2:
                    print("\nAlright.")
                time.sleep(3)
                win_if = False
                while not win_if:
                    try:
                        win = int(
                            input("This layout will grant you instant teleportation out of the dungeon and it will"
                                  "\n mean a won run. Your points will also be multiplied by 50."
                                  "\n(1)win the run\n(2)keep playing "))
                        assert (win in range(1, 3))
                        if win in range(1, 3):
                            win_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if win == 1:
                    self.points = self.points * 50
                    self.winner = True
                    print("Okay, this should take very little time...")
                elif win == 2:
                    self.extra_lives += 1
                    print("We'll keep playing then. I'll give you an extra life. :)")
        elif layout == 14:
            print("This special room has one unique and special function. It will restart your run!!!!!\n"
                  "Everything but your points, attack and items will be reset as if you just started a new run"
                  ". Good luck!")
            self.restart = True
        elif layout == 15:
            reward = random.randint(1, 2)
            if reward == 1:
                self.extra_lives += 1
                print("This special room layout has given you... an extra life! Lovely.")
            elif reward == 2:
                print("This special room layout has given you... an item box. Wheeee")
                Player.item_box(self)

    def open_chest(self, tip):
        time.sleep(1.5)
        if tip == 0:
            contents = random.randint(1, 10)
            coins = random.randint(2, 5)
            content1 = random.randint(1, 3)
            content2 = random.randint(1, 2)
            if contents == 1 or contents in range(5, 11):
                if content1 == 1:
                    self.coins += coins
                    print(f"You find {coins} coins in the chest")
                elif content1 == 2:
                    self.bombs += 1
                    print("You find a bomb in the chest")
                elif content1 == 3:
                    self.keys += 1
                    print("You found a key in the chest")
            elif contents == 2 or contents == 4:
                if content1 == 1:
                    if content2 == 1:
                        self.coins += coins
                        self.bombs += 1
                        print(f"You found {coins} coins and a bomb in the chest!")
                    elif content2 == 2:
                        self.coins += coins
                        self.keys += 1
                        print(f"You found {coins} coins and a key in the chest!")
                elif content1 == 2:
                    if content2 == 1:
                        self.coins += coins
                        self.bombs += 1
                        print(f"You found {coins} coins and a bomb in the chest!")
                    elif content2 == 2:
                        self.bombs += 1
                        self.keys += 1
                        print("You found a bomb and a key in the chest!")
                elif content1 == 3:
                    if content2 == 1:
                        self.coins += coins
                        self.keys += 1
                        print(f"You found {coins} coins and a key in the chest!")
                    elif content2 == 2:
                        self.bombs += 1
                        self.keys += 1
                        print("You found a bomb and a key in the chest!")
            elif contents == 3:
                self.coins += coins
                self.bombs += 1
                self.keys += 1
                print(f"You found {coins} coins, a bomb and a key in the chest!")
            if self.parry:
                stick = random.randint(1, 4)
                if stick == 1:
                    self.parry_item = True
                    print("You also find a stick in the chest. Is this the magic one Parry was looking for?\n"
                          "Well, I have no fucking clue so let's just take this one, he asked for a stick.")
        elif tip == 1:
            if self.keys > 0:
                self.keys -= 1
                content = random.randint(1, 5)
                if content == 1:
                    coins = random.randint(10, 20)
                    self.coins += coins
                    print(f"You unlock the chest and get {coins} coins!")
                elif content == 2:
                    bombs = random.randint(2, 3)
                    self.bombs += bombs
                    print(f"You unlock the chest and get {bombs} bombs!")
                elif content == 3:
                    keys = random.randint(2, 3)
                    self.keys += keys
                    print(f"You unlock the chest and get {keys} keys!")
                elif content == 4:
                    potion = random.randint(10, 30)
                    Player.take_potion(self, potion)
                    print(f"You unlock the chest and get a potion that heals {potion}."
                          f"\n(If you already had 3, it automatically replaced the weakest one or didn't if this "
                          f"potion was weaker than all your current ones.)")
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
                elif content == 5:
                    drink_if = False
                    while not drink_if:
                        try:
                            drink = int(input("You find a mysterious drink in the chest. Do you want to drink it?"
                                              "\n(1)yes\n(2)no "))
                            assert (drink in range(1, 3))
                            if drink in range(1, 3):
                                drink_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if drink == 1:
                        Player.myst_drink(self)
                if self.parry and not self.parry_item:
                    stick = random.randint(1, 4)
                    if stick == 1:
                        self.parry_item = True
                        print("You also find a stick in the chest. Is this the magic one Parry was looking for?\n"
                              "Well, I have no fucking clue so let's just take this one, he asked for a stick.")
                if self.poisoned:
                    cure = random.randint(1, 5)
                    if cure == 1:
                        self.poisoned = False
                        print("You find a cure to your poison in the chest, lovely!")
            elif self.keys == 0:
                print("You can't unlock the chest, sorry!")
        elif tip == 2:
            if self.keys >= 2:
                self.keys -= 2
                content = random.randint(1, 9)
                if content == 1:
                    coins = random.randint(30, 60)
                    self.coins += coins
                    print(f"You unlock the golden chest and get {coins} coins!")
                elif content == 2:
                    bombs = random.randint(4, 5)
                    self.bombs += bombs
                    print(f"You unlock the chest and get {bombs} bombs!")
                elif content == 3:
                    keys = random.randint(4, 5)
                    self.keys += keys
                    print(f"You unlock the chest and get {keys} keys!")
                elif content == 4:
                    potion = random.randint(25, 40)
                    Player.take_potion(self, potion)
                    print(f"You unlock the chest and get a potion that heals {potion}."
                          f"\n(If you already had 3, it automatically replaced the weakest one(or didn't if this "
                          f"potion was weaker than all your current ones.)")
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
                elif content == 5:
                    if self.score:
                        score = random.randint(30, 80)
                        self.points += score
                        print("The chest looks empty. But your 2 keys were not wasted. You just straight up"
                              "\npoints added to your score! Though the person walking in the dungeon is a "
                              "bit confused")
                    else:
                        print("You find an item box in the golden chest! Wheeee")
                        Player.item_box(self)
                elif content == 6:
                    weapon_q = random.randint(0, 50)
                    if weapon_q in range(0, 45):
                        weapon = random.randint(20, 40)
                        weapon_hp = random.randint(4, 6)
                        take_if = False
                        while not take_if:
                            try:
                                take = int(input(f"You find a wooden sword! If you take it you will have {weapon} "
                                                 f"attack +10 (your base attack), and it will last for {weapon_hp} "
                                                 f"rooms. Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                                 "\nyes(2) - put it in slot 2(not equipping it)\n"
                                                 "Recommended to click 1 if you have no weapons and "
                                                 "click 2 if you have 2 weapons. "
                                                 "\nIf you have 2 weapons it will replace the one you have in the slot "
                                                 "you chose\nno(3) "))
                                assert (take in range(1, 4))
                                if take in range(1, 4):
                                    take_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if take != 3:
                            Player.take_weapon(self, take, weapon, weapon_hp)
                    elif weapon_q in range(45, 51):
                        weapon = random.randint(50, 70)
                        weapon_hp = random.randint(6, 9)
                        take_if = False
                        while not take_if:
                            try:
                                take = int(input(f"You find a powerful sword! If you take it you will have {weapon} "
                                                 f"attack +10 (your base attack), and it will last for {weapon_hp} "
                                                 f"rooms"
                                                 "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                                 "\nyes(2) - put it in slot 2(not equipping it)\n"
                                                 "Recommended to click 1 if you have no weapons "
                                                 "and click 2 if you have 2 weapon. "
                                                 "If you have 2 weapons it will replace the one you have "
                                                 "in the slot you chose"
                                                 "\nno(3) "))
                                assert (take in range(1, 4))
                                if take in range(1, 4):
                                    take_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if take != 3:
                            Player.take_weapon(self, take, weapon, weapon_hp)
                elif content == 7:
                    drinks = random.randint(1, 2)
                    if drinks == 1:
                        drink_if = False
                        while not drink_if:
                            try:
                                drink = int(input("You find a mysterious drink in the chest. Do you want to drink it?"
                                                  "\n(1)yes\n(2)no "))
                                assert (drink in range(1, 3))
                                if drink in range(1, 3):
                                    drink_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if drink == 1:
                            Player.myst_drink(self)
                    elif drinks == 2:
                        drink_if = False
                        while not drink_if:
                            try:
                                drink = int(
                                    input("You find 2 mysterious drinks in the chest. Do you want to drink one of them?"
                                          "\n(1)yes\n(2)no, get out, you tryna kill me or sth?? (I might be) "))
                                assert (drink in range(1, 3))
                                if drink in range(1, 3):
                                    drink_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if drink == 1:
                            Player.myst_drink(self)
                            drink_other_if = False
                            while not drink_other_if:
                                try:
                                    drink_other = int(input("Do you want to drink the other one?"
                                                            "\n(1)yes\n(2)no "))
                                    assert (drink_other in range(1, 3))
                                    if drink_other in range(1, 3):
                                        drink_other_if = True
                                except:
                                    print("\nDidn't type a proper number.")
                            if drink_other == 1:
                                Player.myst_drink(self)
                elif content == 8:
                    if self.charm:
                        print("You find another lucky charm, the more the merrier."
                              "\nI hope they stack if they do something(spoiler: they do not).")
                    elif not self.charm:
                        self.charm = True
                        print("You find a lucky charm in the golden chest! What is that gonna do...")
                elif content == 9:
                    self.extra_lives += 1
                    print("You have found an extra life in the chest that was insane luck! (Not really, the chance was"
                          "\n higher than 10%)")
                if self.parry and not self.parry_item:
                    stick = random.randint(1, 4)
                    if stick == 1:
                        self.parry_item = True
                        print("You also find a stick in the chest. Is this the magic one Parry was looking for?\n"
                              "Well, I have no fucking clue so let's just take this one, he asked for a stick.")
                if self.poisoned:
                    cure = random.randint(1, 2)
                    if cure == 1:
                        self.poisoned = False
                        print("You find a cure to your poison in the chest, lovely!")
            elif self.keys < 2:
                if "Mute button" in self.items:
                    print("....., ... ...'. .... 2 .... .. ...... .. :(")
                else:
                    print("Sorry, you don't have 2 keys to unlock it :(")

    def item_room(self):
        if "Mute button" in self.items:
            print("..'. . ........ ....! ...'. ... .... ...... :)\n")
        else:
            print("It's a treasure room! Let's see your reward :)\n")
        time.sleep(1)
        weapon_or_hp = random.randint(0, 25)
        if weapon_or_hp in range(0, 12):
            weapon_q = random.randint(0, 50)
            if weapon_q in range(0, 35):
                weapon = random.randint(18, 40)
                weapon_hp = random.randint(3, 5)
                take_if = False
                while not take_if:
                    try:
                        take = int(input(f"You find a wooden sword! If you take it you will have {weapon} "
                                         f"attack +{self.attack} (your base attack), and it will last for "
                                         f"{weapon_hp} rooms. "
                                         "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                         "\nyes(2) - put it in slot 2(not equipping it)\n"
                                         "Recommended to click 1 if you have no weapons "
                                         "and click 2 if you have 1 weapon.\n"
                                         "If you have 2 weapons it will replace the one you have in the slot you chose."
                                         "\nno(3) "))
                        assert (take in range(1, 4))
                        if take in range(1, 4):
                            take_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take != 3:
                    Player.take_weapon(self, take, weapon, weapon_hp)
            elif weapon_q in range(35, 50):
                weapon = random.randint(50, 63)
                weapon_hp = random.randint(5, 7)
                take_if = False
                while not take_if:
                    try:
                        take = int(input(f"You find a powerful sword! If you take it you will have {weapon} "
                                         f"attack +{self.attack} (your base attack), and it will last"
                                         f" for {weapon_hp} rooms. "
                                         "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                         "\nyes(2) - put it in slot 2(not equipping it)\n"
                                         "Recommended to click 1 if you have no weapons and "
                                         "click 2 if you have 1 weapon. "
                                         "\nIf you have 2 weapons it will replace the one you have in the slot "
                                         "you chose"
                                         "\nno(3) "))
                        assert (take in range(1, 4))
                        if take in range(1, 4):
                            take_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take != 3:
                    Player.take_weapon(self, take, weapon, weapon_hp)
            elif weapon_q == 50:
                weapon = 100
                weapon_hp = 10
                take_if = False
                while not take_if:
                    try:
                        take = int(input(f"You find the rare excalibur (idk if I "
                                         f"spelled it right!!! If you take it you will have {weapon} "
                                         f"attack + {self.attack} "
                                         f"(your base attack)"
                                         f"attack, and it will last for {weapon_hp} rooms. "
                                         "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                         "\nyes(2) - put it in slot 2(not equipping it)\n"
                                         "Recommended to click 1 if you have no weapons "
                                         "and click 2 if you have 1 weapon.\n"
                                         "If you have 2 weapons it will replace the one you have in the slot you chose"
                                         "\nno(3) "))
                        assert (take in range(1, 4))
                        if take in range(1, 4):
                            take_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take != 3:
                    Player.take_weapon(self, take, weapon, weapon_hp)
        elif weapon_or_hp in range(12, 18):
            potion_q = random.randint(1, 50)
            if potion_q in range(1, 40):
                potion = random.randint(10, 20)
                print(f"You find a small potion that when used will give you {potion} health"
                      f" back when used.\n(you can carry 3 at a"
                      f" time, if you already had 3 it will replace the weakest one in"
                      f"\nyour inventory, or none if it's weaker than all 3)")
                Player.take_potion(self, potion)
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                if self.health < max_hp:
                    Player.ask_potion(self)
            elif potion_q in range(40, 48):
                potion = random.randint(25, 50)
                print(f"You find a big potion that when used will give you {potion} health"
                      f" back when used.\n(you can carry 3 at a"
                      f" time, if you already had 3 it will replace the weakest one in"
                      f"\nyour inventory, or none if it's weaker than all 3)")
                Player.take_potion(self, potion)
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                if self.health < max_hp:
                    Player.ask_potion(self)
            elif potion_q == 48 or potion_q == 49 or potion_q == 50:
                potion = 100
                print(f"You find a rare potion that when used will give you all your health"
                      f" back.\n(you can carry 3 at a"
                      f" time, if you already had 3 it will replace the weakest one in"
                      f"\nyour inventory, or none if it's weaker than all 3)")
                Player.take_potion(self, potion)
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                if self.health < max_hp:
                    Player.ask_potion(self)
        elif weapon_or_hp == 25:
            print("You won't believe it.")
            time.sleep(2)
            print("It's a blank treasure room, what are the odds? (Ask me but I might have forgotten"
                  " by the time you start playing.)")
            time.sleep(4)
            print("Better luck next time, you'll need it.")
        elif weapon_or_hp in range(18, 25):
            if "Mute button" in self.items:
                print(".... ...!")
            else:
                print("Item box!")
            Player.item_box(self)

    def shop(self):
        input("It's a shop! Hope you have discounts!(The shops will display original item prices without "
              "the discounts unless it is stated but\nI will take less coins after.) "
              "\nQuick note: first will be displayed weapons and potions (if there are any) and after that"
              "\nconsumables (like bombs and keys). Just saying in case you want to save money for consumables(x) ")
        time.sleep(1)
        cont_num = random.randint(0, 2)
        if cont_num == 0:
            print("\nThe shop has no usables like weapons or potions. You shouldn't be surprised,"
                  "\nwho is gonna be selling"
                  " stuff in a dungeon anyway, never mind useful stuff.")
            time.sleep(1)
        elif cont_num == 1:
            print("There is 1 item in the shop.")
            item1 = random.randint(1, 2)
            if item1 == 1:
                weapon_q = random.randint(1, 50)
                if weapon_q not in range(45, 51):
                    item1 = random.randint(20, 50)
                    item1_hp = random.randint(4, 6)
                else:
                    item1 = random.randint(55, 100)
                    item1_hp = random.randint(7, 9)
                price1 = (item1 // 2) + (item1_hp // 2)
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"You find a sword in the shop. It will give you {item1}"
                                        f" attack (of course + your base attack of {self.attack}) and last for "
                                        f"{item1_hp} rooms. Price:"
                                        f" {price1} coins."
                                        f"\nbuy(1)\ndon't buy(2) "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_weapon(self, price1, self.discount, item1, item1_hp)
            elif item1 == 2:
                item1_q = random.randint(1, 10)
                if item1_q in range(1, 8):
                    item1 = random.randint(10, 25)
                else:
                    item1 = random.randint(25, 50)
                price1 = item1 // 2
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"You find a potion in the shop. It will give you {item1}"
                                        f" health when used. Price: {price1} coins."
                                        f"\nbuy(1)\ndon't buy(2) "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_potion(self, price1, self.discount, item1)
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
        elif cont_num == 2:
            options = ["weapon", "potion"]
            item1 = random.choice(options)
            item2 = random.choice(options)
            if item1 == "weapon" and item2 == "weapon":
                print("There are 2 swords for sale in the shop.")
                weapon1_q = random.randint(1, 50)
                weapon2_q = random.randint(1, 50)
                if weapon1_q not in range(45, 51):
                    item1 = random.randint(15, 40)
                    item1_hp = random.randint(3, 5)
                else:
                    item1 = random.randint(45, 85)
                    item1_hp = random.randint(5, 8)
                price1 = (item1 // 2) + (item1_hp // 2)
                if weapon2_q not in range(45, 51):
                    item2 = random.randint(15, 40)
                    item2_hp = random.randint(3, 5)
                else:
                    item2 = random.randint(45, 85)
                    item2_hp = random.randint(5, 8)
                price2 = (item2 // 2) + (item2_hp // 2)
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"sword 1: {item1} attack and {item1_hp} durability.Price: {price1}"
                                        f"\nsword 2: {item2} attack and {item2_hp} durability.Price: {price2}"
                                        f"\n(keep in mind your base attack too (+{self.attack}))"
                                        f"\n(1)buy sword 1\n(2)buy sword 2\n(3) don't buy "))
                        assert (buy in range(1, 4))
                        if buy in range(1, 4):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_weapon(self, price1, self.discount, item1, item1_hp)
                    buy_other_if = False
                    while not buy_other_if:
                        try:
                            buy_other = int(input("Do you want to buy the other item?\n(1)yes\n(2)no "))
                            assert (buy_other in range(1, 3))
                            if buy_other in range(1, 3):
                                buy_other_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if buy_other == 1:
                        Player.buy_weapon(self, price2, self.discount, item2, item2_hp)
                elif buy == 2:
                    Player.buy_weapon(self, price2, self.discount, item2, item2_hp)
                    buy_other_if = False
                    while not buy_other_if:
                        try:
                            buy_other = int(input("Do you want to buy the other item?\n(1)yes\n(2)no "))
                            assert (buy_other in range(1, 3))
                            if buy_other in range(1, 3):
                                buy_other_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if buy_other == 1:
                        Player.buy_weapon(self, price1, self.discount, item1, item1_hp)
            elif item1 == "potion" and item2 == "potion":
                print("There are 2 potions for sale")
                item1_q = random.randint(1, 10)
                if item1_q in range(1, 8):
                    item1 = random.randint(10, 25)
                else:
                    item1 = random.randint(25, 50)
                price1 = item1 // 2
                item2_q = random.randint(1, 10)
                if item2_q in range(1, 8):
                    item2 = random.randint(10, 25)
                else:
                    item2 = random.randint(25, 50)
                price2 = item2 // 2
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"p1 gives you {item1} health, price: {price1}\n"
                                        f"p2 gives you {item2} health, price: {price2}"
                                        "\n(1)buy p1\n(2)buy p2\n(3)buy none "))
                        assert (buy in range(1, 4))
                        if buy in range(1, 4):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_potion(self, price1, self.discount, item1)
                    buy_other_if = False
                    while not buy_other_if:
                        try:
                            buy_other = int(input("Buy the other potion?\n(1)yes\n(2)no "))
                            assert (buy_other in range(1, 3))
                            if buy_other in range(1, 3):
                                buy_other_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if buy_other == 1:
                        Player.buy_potion(self, price2, self.discount, item2)
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
                if buy == 2:
                    Player.buy_potion(self, price2, self.discount, item2)
                    buy_other_if = False
                    while not buy_other_if:
                        try:
                            buy_other = int(input("Buy the other potion?\n(1)yes\n(2)no "))
                            assert (buy_other in range(1, 3))
                            if buy_other in range(1, 3):
                                buy_other_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if buy_other == 1:
                        Player.buy_potion(self, price1, self.discount, item1)
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
            elif (item1 == "weapon" and item2 == "potion") or (item1 == "potion" and item2 == "weapon"):
                print("There is a sword and a potion for sale.")
                weapon_q = random.randint(1, 50)
                if weapon_q not in range(45, 51):
                    item1 = random.randint(20, 40)
                    item1_hp = random.randint(4, 5)
                else:
                    item1 = random.randint(40, 85)
                    item1_hp = random.randint(6, 9)
                price1 = (item1 // 2) + (item1_hp // 2)
                item2_q = random.randint(1, 10)
                if item2_q in range(1, 8):
                    item2 = random.randint(10, 25)
                else:
                    item2 = random.randint(25, 50)
                price2 = (item2 // 2) + (item2 // 2)
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"Sword: {item1} attack and lasts {item1_hp} rooms. {price1} coins"
                                        f"\nPotion: +{item2} health when used. {price2} coins"
                                        f"\n(1)buy sword\n(2)buy potion\n(3)buy none "))
                        assert (buy in range(1, 4))
                        if buy in range(1, 4):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_weapon(self, price1, self.discount, item1, item1_hp)
                    buy_other_if = False
                    while not buy_other_if:
                        try:
                            buy_other = int(input("Buy the other item?\n(1)yes\n(2)no "))
                            assert (buy_other in range(1, 3))
                            if buy_other in range(1, 3):
                                buy_other_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if buy_other == 1:
                        Player.buy_potion(self, price2, self.discount, item2)
                        max_hp = 100
                        if "Strong juice" in self.items:
                            max_hp = 200
                        if self.health < max_hp:
                            Player.ask_potion(self)
                if buy == 2:
                    Player.buy_potion(self, price2, self.discount, item2)
                    buy_other_if = False
                    while not buy_other_if:
                        try:
                            buy_other = int(input("Buy the other item?\n(1)yes\n(2)no "))
                            assert (buy_other in range(1, 3))
                            if buy_other in range(1, 3):
                                buy_other_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if buy_other == 1:
                        Player.buy_weapon(self, price1, self.discount, item1, item1_hp)
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
        cons_num = random.randint(0, 2)
        if cons_num == 0:
            print("There are no consumables for sale. Onto the next one...")
        elif cons_num == 1:
            cons_type = random.randint(0, 1)
            if cons_type == 0:
                bombs = random.randint(1, 3)
                price = 8 * bombs
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"\nYou find {bombs} bomb(s) in the store, {price} coins.\n(1)buy\n(2)no "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_bombs(self, price, self.discount, bombs)
            elif cons_type == 1:
                keys = random.randint(1, 3)
                price = 5 * keys
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"\nYou find {keys} key(s) in the store, {price} coins.\n(1)buy\n(2)no "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy == 1:
                    Player.buy_keys(self, price, self.discount, keys)
        elif cons_num == 2:
            bombs = random.randint(1, 3)
            price1 = 6 * bombs
            keys = random.randint(1, 3)
            price2 = 4 * keys
            buy_if = False
            while not buy_if:
                try:
                    buy = int(
                        input(f"\n{bombs} bomb(s): {price1} coins\n{keys} key(s): {price2} coins\n(1)buy the bombs"
                              f"\n(2)buy the keys\n(3)buy none "))
                    assert (buy in range(1, 4))
                    if buy in range(1, 4):
                        buy_if = True
                except:
                    print("\nDidn't type a proper number.")
            if buy == 1:
                Player.buy_bombs(self, price1, self.discount, bombs)
                buy_other_if = False
                while not buy_other_if:
                    try:
                        buy_other = int(input("Do you want to buy the other item?\n(1)yes\n(2)no "))
                        assert (buy_other in range(1, 3))
                        if buy_other in range(1, 3):
                            buy_other_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy_other == 1:
                    Player.buy_keys(self, price2, self.discount, keys)
            elif buy == 2:
                Player.buy_keys(self, price2, self.discount, keys)
                buy_other_if = False
                while not buy_other_if:
                    try:
                        buy_other = int(input("Do you want to buy the other item?\n(1)yes\n(2)no "))
                        assert (buy_other in range(1, 3))
                        if buy_other in range(1, 3):
                            buy_other_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if buy_other == 1:
                    Player.buy_bombs(self, price1, self.discount, bombs)

    def empty_room(self):
        print("It's an empty room. Let's look around see if we can find something.")
        time.sleep(5)
        loot = random.randint(0, 100)
        if loot in range(10, 50):
            coins = random.randint(1, 10)
            if coins in range(1, 6):
                cash = random.randint(1, 25)
                self.coins += cash
                print(f"You find {cash} coins. We'll take it.")
            elif coins in range(6, 10):
                cash = random.randint(25, 50)
                self.coins += cash
                print(f"Woah, you have found a bag with {cash} coins. Noice.")
            elif coins == 10:
                cash = random.randint(50, 200)
                self.coins += cash
                print(f"You find tons of coins.({cash}) How lucky!")
        elif loot in range(1, 10):
            drink_if = False
            while not drink_if:
                try:
                    drink = int(input("You find a mysterious drink in the room. Do you want to drink it?"
                                      "\n(1)yes\n(2)no "))
                    assert (drink in range(1, 3))
                    if drink in range(1, 3):
                        drink_if = True
                except:
                    print("\nDidn't type a proper number.")
            if drink == 1:
                Player.myst_drink(self)
        elif loot in range(50, 80):
            print("Okay, it was empty after all. Pray for a better safe room next time I guess...")
        elif loot in range(80, 90):
            keys = random.randint(0, 2)
            if keys == 0:
                print("You find some parts of a key but it's broken so you might as well have found nothing.\n"
                      "Onto the next one...")
            else:
                self.keys += keys
                if keys == 1:
                    print("What is that on the floor? A key! There was something in this room after all.")
                elif keys == 2:
                    print("You find a random desk with a chair. Who even sits here??")
                    time.sleep(3)
                    print("You found 2 keys! Idk what's with the desk but not complaining ':D ")
        elif loot in range(90, 100):
            bombs = random.randint(0, 2)
            if bombs == 0:
                print("The floor is not really clean and the room is foggy. Someone must have been testing"
                      "\nbombs in here. If only you were here a tiny bit earlier you might have found sth.")
            elif bombs == 1:
                self.bombs += 1
                print("You find a bomb and take it! This might come in handy. It also might blow up in your"
                      "\nhandy so use with caution")
            elif bombs == 2:
                self.bombs += 2
                print("You find 2 bombs and take them! It's better than 1 for sure.")
        elif loot == 100:
            print("Woaaaaaaah you found the rare layout of this room full of goodies. Give me a sec to calculate\n"
                  "the rewards.")
            time.sleep(4)
            keys = random.randint(2, 5)
            bombs = random.randint(2, 5)
            potion = random.randint(25, 35)
            coins = random.randint(25, 50)
            self.keys += keys
            self.bombs += bombs
            self.coins += coins
            print(f"So from this room you get:\n{keys} keys, {bombs} bombs, "
                  f"{coins} coins and a potion that heals {potion}. Lovely stuff.")
            Player.take_potion(self, potion)
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            if self.health < max_hp:
                Player.ask_potion(self)

    def enter_room(self):
        time.sleep(1)
        if "Russian roulette" in self.items:
            if_fight = random.randint(1, 3)
        else:
            if_fight = random.randint(1, 2)
        if if_fight == 1 or if_fight == 3:
            current_room = random.randint(1, 86)
        elif if_fight == 2:
            new_old = random.randint(1, 5)
            if new_old in range(1, 4):
                if self.rooms_cleared < 5:
                    current_room = random.randint(1, 12)
                elif 5 <= self.rooms_cleared <= 15:
                    current_room = random.randint(5, 25)
                else:
                    current_room = random.randint(8, 50)
            elif new_old in range(4, 6):
                if self.rooms_cleared < 5:
                    current_room = random.randint(0, 7)
                elif 5 <= self.rooms_cleared <= 15:
                    current_room = random.randint(3, 24)
                else:
                    current_room = random.randint(9, 32)
        #room generated
        if "Reality stone" in self.items and self.stone == 3:
            print("\n")
            if if_fight == 1 or if_fight == 3:
                if current_room == 1:
                    print("The room will have a lot of coins.")
                elif current_room == 2:
                    print("There are 20 coins in the following room.")
                elif current_room == 3:
                    print("There is 1 coin in the following room.")
                elif current_room == 4:
                    print("The following room has a corpse.")
                elif current_room == 5:
                    print("The following room has a small fountain.")
                elif current_room == 6:
                    print("The following room has a large fountain.")
                elif current_room in range(6, 9):
                    print("The following room has a wooden chest.")
                elif current_room in range(9, 11):
                    print("The following room has a siver chest.")
                elif current_room == 11:
                    print("The following room has a golden chest.")
                elif current_room in range(12, 14):
                    print("The following room has 2 keys.")
                elif current_room in range(14, 16):
                    print("The following room has a bomb.")
                elif current_room == 16:
                    print("The following room has a fake fight.")
                elif current_room == 17:
                    print("The following room has a mysterious drink.")
                elif current_room == 18:
                    print("The following room has a lucky charm.")
                elif current_room in range(19, 21):
                    print("The following room contains a dialogue, fight or nothing.")
                elif current_room == 22:
                    print("The following room has a trader.")
                elif current_room == 26:
                    print("The following room has a discount.")
                elif current_room == 27:
                    print("The following room has a key and a silver chest.")
                elif current_room == 28:
                    print("The following room has a key and a golden chest.")
                elif current_room == 29:
                    print("The following room has 2 keys and a golden chest.")
                elif current_room == 30:
                    print("The following room has a potion that heals 20.")
                elif current_room == 31:
                    print("The following room has a potion that heals 40.")
                elif current_room == 32:
                    print("The following room has a weapon.")
                elif current_room == 33:
                    print("The following room will try to poison you to death.")
                elif current_room == 34:
                    print("The following room is empty.")
                elif current_room == 35:
                    print("The following room is empty.")
                elif current_room == 36:
                    print("The following room has a watch.")
                elif current_room == 37:
                    print("The following room has a chance to curse you.")
                elif current_room == 38:
                    print("The following room has a gym.")
                elif current_room == 39:
                    print("The following room has a box.")
                elif current_room == 40:
                    print("The following room has a large box.")
                elif current_room == 41:
                    print("The following room has a stat randomizer.")
                elif current_room == 42:
                    print("The following room has a slot machine.")
                elif current_room in range(43, 45):
                    print("The following room has a random shop.")
                elif current_room in range(45, 47):
                    print("The following room has a stats shop.")
                elif current_room == 47:
                    print("The following room sells a lucky charm.")
                elif current_room == 48:
                    print("The following room has a temple.")
                elif current_room == 49:
                    print("The following room has a satanic symbol.")
                elif current_room == 50:
                    print("The following room has a hole in the wall.")
                elif current_room == 51:
                    print("The following room has a hole in the wall and a wooden chest.")
                elif current_room == 52:
                    print("The following room has a hole in the wall and a silver chest.")
                elif current_room == 53:
                    print("The following room has a hole in the wall and a golden chest.")
                elif current_room == 23:
                    print("The following room has a hole in the wall and a key.")
                elif current_room == 25:
                    print("The following room has a hole in the wall and a bomb.")
                elif current_room == 24:
                    print("The following room is a special room.")
                elif current_room == 21:
                    print("The following room has a trap door.")
                elif current_room in range(54, 57):
                    print("The following room has a lottery.")
                elif current_room == 57:
                    print("The following room has a survey.")
                elif current_room == 58:
                    print("The following room is empty with chance of consumables.")
                elif current_room == 59:
                    print("The following room is a treasure room!")
                elif current_room == 60:
                    print("The following room is a shop.")
                elif current_room == 61:
                    print("The following room has an extra life.")
                elif current_room == 62:
                    print("The following room has a church.")
                elif current_room == 63:
                    print("The following room has a hole in the floor.")
                elif current_room == 64:
                    print("The following room has a hole in the floor and a bomb.")
                elif current_room == 65:
                    print("The following room has a hole in the floor and a key.")
                elif current_room == 66:
                    print("The following room has a hole in the floor and a coin.")
                elif current_room == 67:
                    print("The following room has a hole in the floor and an item box.")
                elif current_room == 68:
                    print("The following room has a hole in the floor and the wall.")
                elif current_room == 69:
                    print("The following room has a hole in the floor and a wooden chest.")
                elif current_room == 70:
                    print("The following room has a mini game.")
                elif current_room == 71:
                    print("The following room has a mini game.")
                elif current_room == 72:
                    print("The following room has a mini game.")
                elif current_room == 73:
                    print("The following room will give you a slow effect.")
                elif current_room == 74:
                    print("The following room will give you a negative effect.")
                elif current_room == 75:
                    print("The following room has a fight with a politician (can be escaped with money).")
                elif current_room == 76:
                    print("The following room has a special fight against a titan.")
                elif current_room == 77:
                    print("The following room has a fight with me.")
                elif current_room == 78:
                    print("The following room has a glitched baby.")
                elif current_room == 79:
                    print("The following room has a cat.")
                elif current_room == 80:
                    print("The following room has a trader.")
                elif current_room == 81:
                    print("The following room has a random shop.")
                elif current_room in range(82, 85):
                    print("The following room has an item box.")
                elif current_room == 85:
                    print("The following room has a weapon.")
                elif current_room == 86:
                    print("The following room has a weapon.")
            elif if_fight == 2:
                if new_old in range(1, 4):
                    print(f"The following room has a fight against {monsters[current_room]}.")
                elif new_old in range(4, 6):
                    print(f"The following room has a fight against {monst_2[current_room]}.")
            stone_if = False
            while not stone_if:
                try:
                    stone = int(input("\nReroll the room?\n(1)yes\n(2)no "))
                    assert (stone in range(1, 3))
                    if stone in range(1, 3):
                        stone_if = True
                except:
                    print("\nDidn't type a proper number.")
            time.sleep(1)
            if stone == 1:
                self.stone = 0
                if "Russian roulette" in self.items:
                    if_fight = random.randint(1, 3)
                else:
                    if_fight = random.randint(1, 2)
                if if_fight == 1 or if_fight == 3:
                    current_room = random.randint(1, 86)
                elif if_fight == 2:
                    new_old = random.randint(1, 5)
                    if new_old in range(1, 4):
                        if self.rooms_cleared < 5:
                            current_room = random.randint(1, 12)
                        elif 5 <= self.rooms_cleared <= 15:
                            current_room = random.randint(5, 25)
                        else:
                            current_room = random.randint(8, 50)
                    elif new_old in range(4, 6):
                        if self.rooms_cleared < 5:
                            current_room = random.randint(0, 7)
                        elif 5 <= self.rooms_cleared <= 15:
                            current_room = random.randint(3, 24)
                        else:
                            current_room = random.randint(9, 32)
        #actual rooms below
        if if_fight == 1 or if_fight == 3:
            if current_room == 1:
                coins = random.randint(50, 100)
                self.coins += coins
                print(f"There is no fighting in this room, you just straight up find\n"
                      f"{coins} coins, what luck!")
            elif current_room == 2:
                self.coins += 20
                print("There is no fighting in this room but there's 20 coins on the floor. Cheers.\n")
            elif current_room == 3:
                self.coins += 1
                print("There don't seem to be enemies in this room, but what is this\n"
                      "on the floor? A coin! We take these.")
            elif current_room == 4:
                print("You see in the room... a corpse?")
                time.sleep(2)
                input("\nYeah, it is. What is the first thing you do? Check for money of course!(x)")
                take_if = False
                while not take_if:
                    try:
                        take = int(input("\nYou find 25 coins in his pockets. Do you take them?\n(1)cash moneeeeeeeey"
                                         "\n(2)I think I should just leave them that seems dodgy "))
                        assert (take in range(1, 3))
                        if take in range(1, 3):
                            take_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take == 2:
                    print("You leave this probably cursed room.")
                elif take == 1:
                    self.coins += 25
                    if self.cursed:
                        print("If you take the coins here you're supposed to become cursed, but you were\n"
                              "already cursed anyway, so free coins!")
                    else:
                        self.cursed = True
                        print("You grab the 25 coins but the corpse suddenly starts moving its mouth\n"
                              "and chanting random shit so you are now cursed. Use the money well.")
                        if "Shiny necklace" in self.items:
                            self.cursed = False
                            time.sleep(1)
                            print("Shiny necklace says no to the curse!")
            elif current_room == 5:
                print("What is that in the middle of the room? A small fountain? Its aura is very clean.")
                drink_if = False
                while not drink_if:
                    try:
                        drink = int(input("Drink from it?\n(1)yes\n(2)no "))
                        assert (drink in range(1, 3))
                        if drink in range(1, 3):
                            drink_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if drink == 1:
                    self.health += 20
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health > max_hp:
                        self.health = max_hp
                    print("The fountain heals you for 20 health but the water tasted crap. Ew.")
                elif drink == 2:
                    print("Aight.")
            elif current_room == 6:
                print("What is that in the middle of the room? A large fountain? Its aura is very clean.")
                drink_if = False
                while not drink_if:
                    try:
                        drink = int(input("Drink from it?\n(1)yes\n(2)no "))
                        assert (drink in range(1, 3))
                        if drink in range(1, 3):
                            drink_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if drink == 1:
                    self.health += 50
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health > max_hp:
                        self.health = max_hp
                    print("The fountain heals you for 50 health and the water tasted nice. Yum.")
                elif drink == 2:
                    print("Aight.")
            elif current_room in range(6, 9):
                print("Hey there is nobody in here, but just a wooden chest!\n"
                      "Open it uppp")
                Player.open_chest(self, 0)
            elif current_room in range(9, 11):
                chest_if = False
                while not chest_if:
                    try:
                        chest = int(input("Hey there is nobody in here, but you find a silver chest!\n"
                                          "(1)open - 1 key\n(2)leave it :( "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            chest_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if chest == 1:
                    Player.open_chest(self, 1)
            elif current_room == 11:
                chest_if = False
                while not chest_if:
                    try:
                        chest = int(input("Hey there is nobody in here, but you find a golden chest!\n"
                                          "(1)open - 2 keys\n(2)leave it :( "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            chest_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if chest == 1:
                    Player.open_chest(self, 2)
            elif current_room in range(12, 14):
                self.keys += 2
                print("No enemies and you find 2 keys on a random desk (who even put a desk here)")
            elif current_room in range(14, 16):
                self.bombs += 1
                print("No enemies in the room and you find a bomb! Very sweet deal!")
            elif current_room == 16:
                input("\nYou have encountered a small pool but it's full of very hungry sharks. "
                      f"What will you do?\nattack(1) - 69 attack "
                      f"required\nrun through them(2) - equivalent of suicide"
                      f"\nrun away(3) - -3 health, lose points\ngive up(4): ")
                print("Hold on a second.")
                time.sleep(2)
                print("\nThe sharks jump out of the water to attack you cause they are very hungry as I said.")
                time.sleep(2)
                print("\nBut they can't breathe on land and just die. That was stupid.\n"
                      "You didn't click 3 or 4, did you?")
            elif current_room == 17:
                drink_if = False
                while not drink_if:
                    try:
                        drink = int(input("You find a mysterious drink in the room. Do you want to drink it?"
                                          "\n(1)yes\n(2)no "))
                        assert (drink in range(1, 3))
                        if drink in range(1, 3):
                            drink_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if drink == 1:
                    Player.myst_drink(self)
            elif current_room == 18:
                self.charm = True
                print("You find a lucky charm in the room, how... lucky! If you had one already\n"
                      "they don't stack sadly.")
            elif current_room in range(19, 21):
                time.sleep(1)
                if not self.parry_dead and not self.parry and not self.parry_enemy:
                    time.sleep(1)
                    print("You see a... i don't know if that's an enemy, it looks more like idk... a drug addict??")
                    time.sleep(4)
                    print("He noticed you, shit!")
                    time.sleep(2)
                    input("-Who is this what are you doing in my... my... my... my..."
                          "\n(x)")
                    print("\nHe appears to be high.")
                    time.sleep(1)
                    input(f"\nYou introduce yourself.\n\n-Oh, {self.name}, you are probably \"adventuring\" here\n"
                          f"you think you in a game aren't you? Okay then I am Parry Hotter and I used to be the big\n"
                          f"deal like you. I had all sorts of adventures in Hogtwarts or something. Now I am nothing.\n"
                          f"(x)")
                    time.sleep(3)
                    print("-*sigh*")
                    time.sleep(3)
                    print("\nHe doesn't look focused. He looks like he hasn't focused in years.")
                    time.sleep(3)
                    input(f"-You see, {self.name}, if that is your name, you can be helpful to me since \n"
                          f"I have no clue tf is going on around here.(x)")
                    print(f"\n-I haven't seen my magic wand in 35 years.\n")
                    time.sleep(2)
                    print(f"35? This guy look about 30 honestly.")
                    time.sleep(2)
                    choice_if = False
                    while not choice_if:
                        try:
                            choice = int(
                                input(f"\n-It looks like a stick. (probably cause it's a stick you fucking weirdo)\n"
                                      f"If you walking around this place can you get it for me?\n"
                                      f"(1)\"okay sure mate\"\n(2)Quote Rohan Kishibe's famous line "))
                            assert (choice in range(1, 3))
                            if choice in range(1, 3):
                                choice_if = True
                        except:
                            print("Didn't type a number properly.")
                    if choice == 1:
                        print(
                            f"\n-Ok thanks, {self.name}, I will be wandering in the hallways "
                            f"so you can find me easier.")
                        self.parry = True
                    elif choice == 2:
                        self.parry_enemy = True
                        print("-So that's how it is then. I can still benefit from this though.")
                        time.sleep(3)
                        input("The moment you start getting suspicious he throws some weird dust in your "
                              "eyes and can't\n"
                              "see for a few seconds. When you see again Parry is gone\n(x)")
                        if self.coins == 0:
                            print("You hear a grr noise from outside. He tried to steal your coins but you had none!\n"
                                  "lmao(?) Okay let's get out of here...")
                            time.sleep(1)
                        elif self.coins > 0:
                            input("You feel lighter. What happened?\n(x)")
                            self.coins = 0
                            print("Oh no he stole your coins, the cunt. Maybe should have said yes. Next room it is...")
                elif self.parry_enemy:
                    print("You have encountered... Parry himself!!!!")
                    time.sleep(2)
                    input(f"Oi, {self.name} you are in a dungeon so you expect fights am I right? "
                          "\nHere I am, show me what you've got(x) ")
                    action_if = False
                    while not action_if:
                        try:
                            action = int((input(f"\nWhat will you do?\nattack(1) - "
                                                f"{monsters_hp[-4] + self.rooms_cleared // 5} attack "
                                                f"required\nrun through them(2) - drains "
                                        f"{math.floor(math.pow(monsters_hp[-4] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                                f"health"
                                                f"\nrun away(3) - drains 1 health, lose points\ngive up(4): ")))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[-4], monsters_hp[-4] + self.rooms_cleared // 5)
                    self.parry_dead = True
                    if action == 1 and not self.dead:
                        time.sleep(2)
                        print("Parry has been defeated at last. We shouldn't see him again, but no promises...")
                else:
                    print("Oh, an empty room. Boring; boo...")
            elif current_room == 22:
                input("There is a trader in the room!! Let's check out what he has to offer"
                      "\n(no discounts here, buddy)!(x)")
                trader = random.randint(1, 7)
                if trader == 1:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a weapon. +50 attack and lasts 7 rooms.\n"
                                            "70 coins. Buy?\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_weapon(self, 70, 0, 50, 7)
                    elif buy == 2:
                        print("You leave. 70 coins? What an obvious scam.")
                elif trader == 2:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a weapon. +70 attack and lasts 8 rooms.\n"
                                            "120 coins. Buy?\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_weapon(self, 120, 0, 70, 8)
                    elif buy == 2:
                        print("You leave. 120 coins? What an obvious scam.")
                elif trader == 3:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a weapon. +30 attack and lasts 6 rooms.\n"
                                            "50 coins. Buy?\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_weapon(self, 50, 0, 30, 6)
                    elif buy == 2:
                        print("You leave. 50 coins? What an obvious scam.")
                elif trader == 4:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a lucky charm for\n"
                                            "80 coins. Buy?\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        if self.coins >= 80:
                            self.coins -= 80
                            self.charm = True
                            print("You get the charm. Feel lucky go lucky.")
                        else:
                            print("Why are you clicking 1 when you don't have the coins. The nerve of some people.")
                    elif buy == 2:
                        print("You leave. 80 coins for a charm? What an obvious scam.")
                elif trader == 5:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a mysterious drink for\n"
                                            "20 coins. Buy? (Instantly drink it as well)\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        if self.coins >= 20:
                            self.coins -= 20
                            Player.myst_drink(self)
                        else:
                            print("Why are you clicking 1 when you don't have the coins. The nerve of some people.")
                    elif buy == 2:
                        print("You leave. 20 coins for a drink? Would have obviously gone horribly wrong.")
                elif trader == 7:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a golden chest for\n"
                                            "20 coins. Buy?\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        if self.coins >= 20:
                            self.coins -= 20
                            open_if = False
                            while not open_if:
                                try:
                                    open_chest = int(
                                        input("You get chest. Open it?\n(1)yes - 2 keys you better have them "
                                              "cause the merchant took your money\n(2)no "))
                                    assert (open_chest in range(1, 3))
                                    if open_chest in range(1, 3):
                                        open_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if open_chest == 1:
                                Player.open_chest(self, 2)
                        else:
                            print("Why are you clicking 1 when you don't have the coins. The nerve of some people.")
                    elif buy == 2:
                        print("You leave. 20 coins for a chest? Could be a scam.")
                elif trader == 6:
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input("He is ready to sell you a potion that will heal you 50 health\n"
                                            "for 50 coins. Buy?\n(1)yes\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_potion(self, 50, 0, 50)
                        max_hp = 100
                        if "Strong juice" in self.items:
                            max_hp = 200
                        if self.health < max_hp:
                            Player.ask_potion(self)
                    elif buy == 2:
                        print("50 for a potion? Get a grip...")
            elif current_room == 26:
                disc = random.randint(1, 3)
                if disc == 3:
                    discount = 50
                else:
                    discount = 30
                if discount <= self.discount:
                    print("This room is supposed to have a discount but it's worse that your current one,\n"
                          "so think of this as a blank room.")
                if discount > self.discount:
                    self.discount = discount
                    print(f"You find a very good room layout. It has a {discount}% discount!\n"
                          "Very nice!")
            elif current_room == 27:
                self.keys += 1
                open_if = False
                while not open_if:
                    try:
                        chest = int(input("You found a key in the room and also a silver chest!\n"
                                          "(1)open - 1 key\n(2)leave it :( "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            open_if = True
                    except:
                        print("Didn't type a number properly.")
                if chest == 1:
                    Player.open_chest(self, 1)
            elif current_room == 28:
                self.keys += 1
                open_if = False
                while not open_if:
                    try:
                        chest = int(input("You found a key in the room and also a golden chest!\n"
                                          "(1)open - 2 keys\n(2)leave it :( "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            open_if = True
                    except:
                        print("Didn't type a number properly.")
                if chest == 1:
                    Player.open_chest(self, 2)
            elif current_room == 29:
                self.keys += 2
                open_if = False
                while not open_if:
                    try:
                        chest = int(input("You found 2 keys in the room and also a golden chest!\n"
                                          "(1)open - 2 keys\n(2)leave it :( "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            open_if = True
                    except:
                        print("Didn't type a number properly.")
                if chest == 1:
                    Player.open_chest(self, 2)
            elif current_room == 30:
                print("You find a potion on the floor that heals 20. Good.\n(do I have to explain how"
                      " it replaces your weakest potion or do you know that by now)")
                Player.take_potion(self, 20)
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                if self.health < max_hp:
                    Player.ask_potion(self)
            elif current_room == 31:
                print("You find a potion on the floor that heals 40. Great.\n(do I have to explain how"
                      " it replaces your weakest potion or do you know that by now)")
                Player.take_potion(self, 40)
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                if self.health < max_hp:
                    Player.ask_potion(self)
            elif current_room == 32:
                q = random.randint(1, 10)
                if q in range(1, 8):
                    weapon = random.randint(20, 34)
                    weapon_hp = random.randint(4, 5)
                    wp_if = False
                    while not wp_if:
                        try:
                            wp = int(input(f"You find a sword in the room that will give you {weapon} attack "
                                           f"and will last {weapon_hp} rooms. Will you take it?\n(1)yes - "
                                           f"slot 1(equip it"
                                           f")\n(2)yes - slot 2\n(3)no, leave it "))
                            assert (wp in range(1, 4))
                            if wp in range(1, 4):
                                wp_if = True
                        except:
                            print("Didn't type a number properly.")
                    if wp == 2 or wp == 1:
                        Player.take_weapon(self, wp, weapon, weapon_hp)
                elif q in range(8, 11):
                    weapon = random.randint(34, 50)
                    weapon_hp = random.randint(6, 7)
                    wp_if = False
                    while not wp_if:
                        try:
                            wp = int(input(f"You find a decent sword in the room that will give you {weapon} attack "
                                           f"and will last {weapon_hp} rooms. Will you take "
                                           f"it?\n(1)yes - slot 1(equip it"
                                           f")\n(2)yes - slot 2\n(3)no, leave it "))
                            assert (wp in range(1, 4))
                            if wp in range(1, 4):
                                wp_if = True
                        except:
                            print("Didn't type a number properly.")
                    if wp == 2 or wp == 1:
                        Player.take_weapon(self, wp, weapon, weapon_hp)
            elif current_room == 33:
                print("The room you entered seems... green-ish?")
                time.sleep(1)
                print("You try to exit but the doors immediately close.")
                time.sleep(2)
                print("Oh that's why it's green-ish, it's some kind of poisonous gas. (it's green because we "
                      "are in a game, shut up)")
                if "Shiny necklace" in self.items:
                    time.sleep(1)
                    input("Okay this will be hard to explain. THis is the poison room that kills you if you have no"
                          "\nbombs. You have Shiny necklace so you may wonder if it works. No, it doesn't save you"
                          "\nfrom the room itself. The item prevents lasting negative effects so its use in this room"
                          "\nis escaping through the opposite door and not getting poisoned after. Your character"
                          "\nis closed in a room with a poison gas, you are stuck breathing it, this is not a"
                          " negative effect,\nthis is literally being unable to breathe oxygen. The item is good enough"
                          " on its own so I don't believe it should fully counter this room. Only a bomb should do it. "
                          "(x) ")
                time.sleep(3)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input("There is a solution to the problem of course. Just bomb the door and escape."
                                         "(from the other\nside of course, so you get end of room rewards.)"
                                         "\n(1)bomb the door at the end\n(2)bomb the door"
                                         " behind you and run\n(3)lie down and"
                                         " cry "))
                        assert (bomb in range(1, 4))
                        if bomb in range(1, 4):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 3:
                    print("I thought as much. End of the run.")
                    self.dead = True
                    if self.dead:
                        Player.revive(self)
                        print("You cannot escape this room by the way. This is the only place where "
                              "extra lives do nothing.")
                        self.dead = True
                    while not self.dead:
                        self.dead = True
                        if self.dead:
                            Player.revive(self)
                if bomb == 2:
                    if self.bombs > 0:
                        self.bombs -= 1
                        print("You escape as fast as possible through the (what used to be a) door behind you."
                              "\n(this will count as a skipped room keep that in mind)")
                        self.skipped = True
                    elif self.bombs == 0:
                        print("You clicked 2 when you had no bombs. You die but at the very least you didn't cry."
                              " How honorable.")
                        self.dead = True
                        if self.dead:
                            Player.revive(self)
                            print("You cannot escape this room by the way. This is the only place where "
                                  "extra lives do nothing.")
                        while not self.dead:
                            self.dead = True
                            if self.dead:
                                Player.revive(self)
                if bomb == 1:
                    if self.bombs > 0:
                        self.bombs -= 1
                        self.poisoned = True
                        print("You run to the other door as fast as possible and escape."
                              "\nHope the end room rewards are worth it because you are now poisoned if you weren't"
                              " before.")
                        if "Shiny necklace" in self.items:
                            time.sleep(1)
                            self.poisoned = False
                            print("Shiny necklace says no to the poison!")
                    elif self.bombs == 0:
                        print("You clicked 1 when you had no bombs. You die but at the very least you didn't cry."
                              " How honorable")
                        self.dead = True
                        if self.dead:
                            Player.revive(self)
                            print("You cannot escape this room by the way. This is the only place where "
                                  "extra lives do nothing.")
                        while not self.dead:
                            self.dead = True
                            if self.dead:
                                Player.revive(self)
            elif current_room == 34:
                print("Empty room. It looks like a desert.")
                time.sleep(4)
                print("Yep, nothing here, moving on...")
            elif current_room == 35:
                print("Very empty room. Like a... an empty box. But the size of a room, so.. nevermind.")
                time.sleep(3)
                print("Literally nothing here, let's move on.")
            elif current_room == 36:
                bomb_if = False
                while not bomb_if:
                    try:
                        touch = int(
                            input("It looks like a tiny room, but there is a... watch in the middle?\n(1)take it\n"
                                  "(2)leave it there "))
                        assert (touch in range(1, 3))
                        if touch in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if touch == 1:
                    if "Time stone" in self.items:
                        print("You touch it and suddenly it breaks as time stops.")
                        time.sleep(2)
                        print("This was supposed to be a softlock but you escape thanks to your time stone!!")
                        time.sleep(2)
                        self.points += 2000
                        print("Have I told you escaping this watch gives you 2000 points?")
                    else:
                        print("You touch it and suddenly it breaks as time stops.")
                        time.sleep(6)
                        print("You might wanna start another run buddy.")
                        time.sleep(2000)
                        print("You waited for this long? Why???????? Do you want some points or a reward\n"
                              "or secret ending? Alright fine I'll give you 2000 points because "
                              "that was 2000 seconds "
                              "but also kill your\n"
                              "character, you can respawn if you have a charm or extra lives though.")
                        self.points += 2000
                        self.dead = True
                        if self.dead:
                            Player.revive(self)
                elif touch == 2:
                    print("You leave the clock there. That was weird. Not the weirdest thing in this game though.")
            elif current_room == 37:
                print("Another empty room layout, no twists here, trust me.")
                curse = random.randint(1, 3)
                time.sleep(3)
                if curse == 1:
                    if self.cursed:
                        print("Well, no twists as I said. I knew you could trust me.")
                    else:
                        self.cursed = True
                        print("Well, no twists as I said. I knew you could trust me. Just don't look at your stats\n"
                              "next room, trust me, alright?")
                        if "Shiny necklace" in self.items:
                            time.sleep(1)
                            self.cursed = False
                            print("Shiny necklace says no to the curse! Wait, this was a curse?")
                elif curse in range(2, 4):
                    print("Well, no twists as I said. I knew you could trust me.")
            elif current_room == 38:
                gym_if = False
                while not gym_if:
                    try:
                        gym = int(input("It's a... gym??\n(1)hit the gym\n(2)ignore "))
                        assert (gym in range(1, 3))
                        if gym in range(1, 3):
                            gym_if = True
                    except:
                        print("Didn't type a number properly.")
                if gym == 2:
                    print("Ok, we move forward.")
                elif gym == 1:
                    self.attack += 5
                    self.health -= 10
                    if self.health <= 0:
                        self.dead = True
                        print("You try to exercise but your health is too low and you lose consciousness\n"
                              "from being that tired. Ouch.")
                        if self.dead:
                            Player.revive(self)
                    else:
                        print("You hit the gym.\n\n\"Ooooouch what did you do that for??\", said the gym.")
                        time.sleep(3)
                        print("Just kidding, I added this room just for this joke. \nYou work out in the"
                              " gym and increase your base attack by 5! That is why you go to the gym.\n"
                              "(I also have to tell you you lost 10 health, since that was pretty tiring, but also"
                              " very worth it)")
            elif current_room == 39:
                box_if = False
                while not box_if:
                    try:
                        box = int(input("There is a box in the middle of the room but it's pretty sturdy."
                                        "\n(1)bomb it - 1 bomb required\n(2)no "))
                        assert (box in range(1, 3))
                        if box in range(1, 3):
                            box_if = True
                    except:
                        print("Didn't type a number properly.")
                if box == 1:
                    if self.bombs > 0:
                        self.bombs -= 1
                        content = random.randint(0, 5)
                        if content == 0:
                            print("There was a bunch of rats in the box. They are dead now at least.")
                        elif content == 1:
                            coins = random.randint(10, 20)
                            self.coins += coins
                            print(f"You bomb the box and get {coins} coins!")
                        elif content == 2:
                            bombs = random.randint(2, 3)
                            self.bombs += bombs
                            print(f"You bomb the box and get {bombs} bombs! (lmao)")
                        elif content == 3:
                            keys = random.randint(2, 3)
                            self.keys += keys
                            print(f"You bomb the box and get {keys} keys!")
                        elif content == 4:
                            potion = random.randint(10, 30)
                            Player.take_potion(self, potion)
                            print(f"You bomb the box and get a potion that heals {potion}."
                                  f"\n(If you already had 3, it automatically replaced the "
                                  f"weakest one(or didn't if this "
                                  f"potion was weaker than all your current ones.)")
                            max_hp = 100
                            if "Strong juice" in self.items:
                                max_hp = 200
                            if self.health < max_hp:
                                Player.ask_potion(self)
                        elif content == 5:
                            drink_if = False
                            while not drink_if:
                                try:
                                    drink = int(input("You find a mysterious drink in the box. Do you want to drink it?"
                                                      "\n(1)yes\n(2)no "))
                                    assert (drink in range(1, 3))
                                    if drink in range(1, 3):
                                        drink_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if drink == 1:
                                Player.myst_drink(self)
                        if self.parry and not self.parry_item:
                            stick = random.randint(1, 4)
                            if stick == 1:
                                self.parry_item = True
                                print(
                                    "You also find a stick in the box. Is this the magic one Parry was looking for?\n"
                                    "Well, I have no fucking clue so let's just take this one, he asked for a stick.")
                        if self.poisoned:
                            cure = random.randint(1, 5)
                            if cure == 1:
                                self.poisoned = False
                                print("You find a cure to your poison in the box, lovely!")
                    elif self.bombs == 0:
                        print("You have no bombs to open the box, sorry!")
            elif current_room == 40:
                box_if = False
                while not box_if:
                    try:
                        box = int(input("There is a large box in the middle of the room but it's pretty sturdy."
                                        "\n(1)bomb it - 2 bombs required\n(2)no "))
                        assert (box in range(1, 3))
                        if box in range(1, 3):
                            box_if = True
                    except:
                        print("Didn't type a number properly.")
                if box == 1:
                    if self.bombs >= 2:
                        self.bombs -= 2
                        content = random.randint(1, 8)
                        if content == 1:
                            coins = random.randint(20, 50)
                            self.coins += coins
                            print(f"You bomb the box and get {coins} coins!")
                        elif content == 2:
                            self.bombs += 3
                            print(f"You bomb the box and get 3 bombs! (lmao)")
                        elif content == 3:
                            self.keys += 3
                            print(f"You bomb the box and get 3 keys!")
                        elif content == 4:
                            potion = random.randint(20, 40)
                            Player.take_potion(self, potion)
                            print(f"You bomb the box and get a potion that heals {potion}."
                                  f"\n(If you already had 3, "
                                  f"it automatically replaced the weakest one(or didn't if this "
                                  f"potion was weaker than all your current ones.)")
                            max_hp = 100
                            if "Strong juice" in self.items:
                                max_hp = 200
                            if self.health < max_hp:
                                Player.ask_potion(self)
                        elif content == 5:
                            if self.score:
                                score = random.randint(30, 80)
                                self.points += score
                                print("The box looks empty. But your 2 bombs were not wasted. You just straight up"
                                      "\npoints added to your score! Though the person walking in the dungeon is a "
                                      "bit confused")
                            else:
                                print("You find an item box in the box! Wheeee")
                                Player.item_box(self)
                        elif content == 6:
                            weapon_q = random.randint(0, 50)
                            if weapon_q in range(0, 45):
                                weapon = random.randint(20, 40)
                                weapon_hp = random.randint(4, 5)
                                take_if = False
                                while not take_if:
                                    try:
                                        take = int(
                                            input(f"You find a wooden sword! If you take it you will have {weapon} "
                                                  f"attack +10 (your base attack), "
                                                  f"and it will last for {weapon_hp} rooms"
                                                  "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                                  "\nyes(2) - put it in slot 2(not equipping it)\n"
                                                  "Recommended to click 1 if you have no weapons and "
                                                  "click 2 if you have 2 weapons. "
                                                  "If you have 2 weapons it will replace "
                                                  "the one you have in the slot you chose"
                                                  "\nno(3) "))
                                        assert (take in range(1, 4))
                                        if take in range(1, 4):
                                            take_if = True
                                    except:
                                        print("Didn't type a number properly.")
                                if take != 3:
                                    Player.take_weapon(self, take, weapon, weapon_hp)
                            elif weapon_q in range(45, 51):
                                weapon = random.randint(40, 60)
                                weapon_hp = random.randint(5, 8)
                                take_if = False
                                while not take_if:
                                    try:
                                        take = int(
                                            input(f"You find a powerful sword! If you take it you will have {weapon} "
                                                  f"attack +10 (your base attack), "
                                                  f"and it will last for {weapon_hp} rooms"
                                                  "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                                  "\nyes(2) - put it in slot 2(not equipping it)\n"
                                                  "Recommended to click 1 if you have no weapons "
                                                  "and click 2 if you have 2 weapon. "
                                                  "If you have 2 weapons it will "
                                                  "replace the one you have in the slot you chose"
                                                  "\nno(3) "))
                                        assert (take in range(1, 4))
                                        if take in range(1, 4):
                                            take_if = True
                                    except:
                                        print("Didn't type a number properly.")
                                if take != 3:
                                    Player.take_weapon(self, take, weapon, weapon_hp)
                        elif content == 7:
                            drinks = random.randint(1, 2)
                            if drinks == 1:
                                drink_if = False
                                while not drink_if:
                                    try:
                                        drink = int(
                                            input("You find a mysterious drink in the box. Do you want to drink it?"
                                                  "\n(1)yes\n(2)no "))
                                        assert (drink in range(1, 3))
                                        if drink in range(1, 3):
                                            drink_if = True
                                    except:
                                        print("Didn't type a number properly.")
                                if drink == 1:
                                    Player.myst_drink(self)
                            elif drinks == 2:
                                drink_if = False
                                while not drink_if:
                                    try:
                                        drink = int(
                                            input(
                                                "You find 2 mysterious drinks in the box. "
                                                "Do you want to drink one of them?"
                                                "\n(1)yes\n(2)no, get out, you tryna kill me or sth?? (I might be) "))
                                        assert (drink in range(1, 3))
                                        if drink in range(1, 3):
                                            drink_if = True
                                    except:
                                        print("Didn't type a number properly.")
                                if drink == 1:
                                    Player.myst_drink(self)
                                    drink_other_if = False
                                    while not drink_other_if:
                                        try:
                                            drink_other = int(input("Do you want to drink the other one?"
                                                                    "\n(1)yes\n(2)no "))
                                            assert (drink_other in range(1, 3))
                                            if drink_other in range(1, 3):
                                                drink_other_if = True
                                        except:
                                            print("Didn't type a number properly.")
                                    if drink_other == 1:
                                        Player.myst_drink(self)
                        elif content == 8:
                            if self.charm:
                                print("You find another lucky charm, the more the merrier."
                                      "\nI hope they stack if they do something(spoiler: they do not).")
                            elif not self.charm:
                                self.charm = True
                                print("You find a lucky charm in the box! What is that gonna do...")
                        if self.parry and not self.parry_item:
                            stick = random.randint(1, 4)
                            if stick == 1:
                                self.parry_item = True
                                print(
                                    "You also find a stick in the box. Is this the magic one Parry was looking for?\n"
                                    "Well, I have no fucking clue so let's just take this one, he asked for a stick.")
                        if self.poisoned:
                            cure = random.randint(1, 2)
                            if cure == 1:
                                self.poisoned = False
                                print("You find a cure to your poison in the box, lovely!")
                    elif self.bombs < 2:
                        print("Sorry, you don't have 2 bombs to open it :(")
            elif current_room == 41:
                input("Beep beep. It's a randomizer. Beep. I don't know why it beeps,"
                      "\nthe main point here is some stat changes are coming up!\n(x) ")
                time.sleep(2)
                change = random.randint(1, 10)
                if change == 1:
                    atk = random.randint(5, 10)
                    self.attack += atk
                    print(f"Your base attack is increased by {atk}. Ding ding we have a winner.")
                elif change == 2:
                    atk = random.randint(5, 9)
                    self.attack -= atk
                    if self.attack < 0:
                        self.attack = 0
                    print(f"Your base attack is decreased by {atk}. Ouch.")
                elif change == 3:
                    self.health -= 15
                    if self.health <= 0:
                        self.dead = True
                        print("You lost 15 health and you have now died. Unfortunate.")
                        if self.dead:
                            Player.revive(self)
                    elif self.health > 0:
                        print("You lost 15 health, ouch.")
                elif change == 4:
                    self.health -= 42
                    if self.health <= 0:
                        self.dead = True
                        print("You lost 42 health and you have now died. Un42nate.")
                        if self.dead:
                            Player.revive(self)
                    elif self.health > 0:
                        print("You lost 42 health, that's un42nate. Yes, I wanted to make the joke sorry\n"
                              "about your health though.")
                elif change == 5:
                    self.rooms_cleared -= 5
                    if self.rooms_cleared < 0:
                        self.rooms_cleared = 0
                    print("5 of the rooms you cleared were deleted from your \"rooms passed\" stat. That's a\n"
                          "thing now I decided.")
                elif change == 6:
                    self.rooms_cleared += 5
                    print("5 rooms were added to your \"rooms passed\" stat. That's a\n"
                          "thing now I decided, be happy you got the positive outcome.")
                elif change == 7:
                    self.potion1 = 0
                    self.potion2 = 0
                    self.potion3 = 0
                    print("If you had any potions all of them are now deleted. Sorry not sorry.")
                elif change == 8:
                    self.potion1 = 100
                    self.potion2 = 0
                    self.potion3 = 0
                    print("Now you have one potion and it can heal you fully. Probably a good thing.")
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
                elif change == 9:
                    self.coins = 0
                    self.discount = 20
                    print("All your coins were erased from existence. Hope you didn't have many.\n"
                          "The randomizer gives you a 20% discount as a refund. If you had a better one it's replaced,"
                          "\nsorry, it's a randomizer after all.")
                elif change == 10:
                    self.health = 0
                    self.dead = True
                    print("The randomizer has decided...")
                    time.sleep(2)
                    print("\nto insta kill you. The chance for this was 10% if you are wondering.")
                    if self.dead:
                        Player.revive(self)
            elif current_room == 42:
                print("There is a slot machine in the room.")
                time.sleep(2)
                act = 1
                while act == 1:
                    time.sleep(1)
                    act_if = False
                    while not act_if:
                        try:
                            act = int(input(f"Do you want to play the machine? (You have {self.coins} coins)"
                                            f"\n(1)yes - 4 coins\n(2)leave it "))
                            assert (act in range(1, 3))
                            if act in range(1, 3):
                                act_if = True
                        except:
                            print("Didn't type a number properly.")
                    if act != 1:
                        break
                    if self.coins >= 4:
                        self.coins -= 4
                        reward = random.randint(1, 100)
                        if reward in range(1, 78):
                            print("Nothing.")
                        elif reward in range(78, 80):
                            print("You won an item box!")
                            Player.item_box(self)
                        elif reward in range(80, 90):
                            self.coins += 9
                            print("You won 9 coins!")
                        elif reward in range(90, 93):
                            self.bombs += 1
                            print("You win a bomb!")
                        elif reward in range(93, 96):
                            self.keys += 1
                            print("You win a key!")
                        elif reward == 96:
                            print("You win a potion that heals for 35!")
                            Player.take_potion(self, 35)
                            max_hp = 100
                            if "Strong juice" in self.items:
                                max_hp = 200
                            if self.health < max_hp:
                                Player.ask_potion(self)
                        elif reward == 97:
                            drink = int(input("You win a mysterious drink!\n(1)drink it\n(2)leave it "))
                            if drink == 1:
                                Player.myst_drink(self)
                        elif reward == 98:
                            self.coins += 45
                            print("You win 45 coins, wow!")
                        elif reward == 99:
                            self.charm = True
                            print("You win a lucky charm!")
                        elif reward == 100:
                            self.coins += 100
                            print("HE'S DONE IT THE JACKPOT. 100 coins in the back, hope you didn't spend "
                                  "100 on this machine in the first place.")
                    elif self.coins < 4:
                        print("You don't even have 4 coins.")
                        break
                time.sleep(2)
                print("\nBye bye slot machine.")
            elif current_room in range(43, 45):
                input("Welcome to a random shop! Discounts work here. (Not shown at first, unless stated otherwise"
                      ", but it works)\n(x) ")
                content = random.randint(1, 5)
                if content == 1:
                    keys = random.randint(3, 5)
                    price = 5 * keys
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(
                                input(f"The random shop has {keys} keys for sale.\n{price} coins.\n(1)buy\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_keys(self, price, self.discount, keys)
                elif content == 2:
                    bombs = random.randint(3, 5)
                    price = 6 * bombs
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(
                                input(f"The random shop has {bombs} bombs for sale.\n{price} coins.\n(1)buy\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_bombs(self, price, self.discount, bombs)
                elif content == 3:
                    potion = random.randint(20, 50)
                    price = math.floor(potion * 0.8)
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input(f"The random shop has a potion that heals {potion} for sale."
                                            f"\n{price} coins.\n(1)buy\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        Player.buy_potion(self, price, self.discount, potion)
                        max_hp = 100
                        if "Strong juice" in self.items:
                            max_hp = 200
                        if self.health < max_hp:
                            Player.ask_potion(self)
                elif content == 4:
                    price = math.floor(15 - 15 * (self.discount / 100))
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input(f"The shop has a silver chest and a key together for "
                                            f"sale.\n{price} coins (after potential discounts).\n(1)buy\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        if self.coins >= price:
                            self.coins -= price
                            self.keys += 1
                            chest_if = False
                            while not chest_if:
                                try:
                                    chest = int(input("Do you want to open the chest?\n(1)yes, 1 key\n(2)no "))
                                    assert (chest in range(1, 3))
                                    if chest in range(1, 3):
                                        chest_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if chest == 1:
                                Player.open_chest(self, 1)
                        else:
                            print("Not enough money, sorry.")
                elif content == 5:
                    price = math.floor(35 - 35 * (self.discount / 100))
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input(f"The shop has a golden chest and 2 keys together for "
                                            f"sale.\n{price} coins (after potential discounts).\n(1)buy\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        if self.coins >= price:
                            self.coins -= price
                            self.keys += 2
                            chest_if = False
                            while not chest_if:
                                try:
                                    chest = int(input("Do you want to open the chest?\n(1)yes, 2 keys\n(2)no "))
                                    assert (chest in range(1, 3))
                                    if chest in range(1, 3):
                                        chest_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if chest == 1:
                                Player.open_chest(self, 2)
                        else:
                            print("Not enough money, sorry.")
            elif current_room in range(45, 47):
                input("It's a special \"stats\" shop! Discounts work by the way\n(x) ")
                content = random.randint(1, 2)
                max_hp = 100
                if "Strong juice" in self.items:
                    max_hp = 200
                if content == 1 and self.health < max_hp:
                    if self.health < max_hp:
                        hp = random.randint(20, 40)
                        if (self.health + hp) > max_hp:
                            hp = max_hp - self.health
                        price = math.floor((hp * 1.2) - (hp * 1.2) * (self.discount / 100))
                        buy_if = False
                        while not buy_if:
                            try:
                                buy = int(input(f"You can straight up buy health in this shop.\n{hp} health for {price}"
                                                f" coins (after potential discounts).\n(1)buy\n(2)no "))
                                assert (buy in range(1, 3))
                                if buy in range(1, 3):
                                    buy_if = True
                            except:
                                print("Didn't type a number properly.")
                        if buy == 1:
                            if self.coins >= price:
                                self.coins -= price
                                self.health += hp
                                print(f"\nYou health is now {self.health}")
                            else:
                                print("Not enough money, sorry.")
                else:
                    atk = random.randint(5, 30)
                    price = math.floor((atk * 7) - (atk * 7) * (self.discount / 100))
                    buy_if = False
                    while not buy_if:
                        try:
                            buy = int(input(f"You can straight up buy attack in this shop.\n{atk} attack for {price}"
                                            f" coins (after potential discounts).\n(1)buy\n(2)no "))
                            assert (buy in range(1, 3))
                            if buy in range(1, 3):
                                buy_if = True
                        except:
                            print("Didn't type a number properly.")
                    if buy == 1:
                        if self.coins >= price:
                            self.coins -= price
                            self.attack += atk
                            print(f"\nYou base attack is now {self.attack}")
                        else:
                            print("Not enough money, sorry.")
            elif current_room == 47:
                price = math.floor(50 - 50 * (self.discount / 100))
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"You find a random shop that sells a lucky charm!.\n{price}"
                                        f" coins (after potential discounts).\n(1)buy\n(2)no "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("Didn't type a number properly.")
                if buy == 1:
                    if self.coins >= price:
                        self.coins -= price
                        self.charm = True
                        print(f"\nYou have a lucky charm now!")
                    else:
                        print("Not enough money, sorry.")
            elif current_room == 48:
                print("It's a... temple? Why a temple in a random dungeon room?")
                time.sleep(3)
                pray_if = False
                while not pray_if:
                    try:
                        pray = int(input("Do you want to pray?\n(1)yes\n(2)leave "))
                        assert (pray in range(1, 3))
                        if pray in range(1, 3):
                            pray_if = True
                    except:
                        print("Didn't type a number properly.")
                if pray == 1:
                    self.pray = True
                    print("\nYou have prayed at the temple. Idk what that is good for, I'm an atheist.")
                elif pray == 2:
                    print("You leave. (boring narration but I can't think of a joke for this one).")
            elif current_room == 49:
                print("It's a room with a satanic symbol in the middle, I think they call it pentagram.")
                time.sleep(2)
                input("\nI swear it's not a curse. The thing about this room is if you sacrifice some of your health\n"
                      "your attack will be increased for the rest of the run. Might be worth it might be not.\n(x)")
                sac = 1
                while not self.dead and sac == 1:
                    sac_if = False
                    while not sac_if:
                        try:
                            sac = int(
                                input("Sacrifice 5 health to get +1 attack? (repeatable)\n(1)yes\n(2)no, leave. "))
                            assert (sac in range(1, 3))
                            if sac in range(1, 3):
                                sac_if = True
                        except:
                            print("Didn't type a number properly.")
                    if sac == 1:
                        self.health -= 5
                        self.attack += 1
                        if self.health <= 0:
                            self.dead = True
                            self.points += 1500
                            print("You have sacrificed your life in the pentagram. "
                                  "Satan is happy. +1500 social credits\n"
                                  " (* +1500 points to your score)")
                            if self.dead:
                                Player.revive(self)
                        else:
                            print(f"Your attack is now {self.attack} and your health is {self.health}.\n")
                if not self.dead:
                    time.sleep(2)
                    print("\nYou take your leave.")
            elif current_room == 50:
                print("It's an empty room, but one of the walls is not very sturdy. Also hollow.")
                time.sleep(2)
                print("There might be something in there.")
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if room == 1:
                        print("Your detector senses a secret room.")
                    elif room == 2:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
                elif bomb == 2:
                    print("You leave the room.")
            elif current_room == 51:
                print("It's an empty room, but with a wooden chest in the middle. Let's check it.")
                Player.open_chest(self, 0)
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if room == 1:
                        print("Your detector senses a secret room.")
                    elif room == 2:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("One of the walls is not very sturdy. Also hollow. There might be something in there.")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
                elif bomb == 2:
                    print("You leave the room.")
            elif current_room == 52:
                chest_if = False
                while not chest_if:
                    try:
                        chest = int(input("It's an empty room, but with a silver chest in the middle."
                                          "\n(1)open - 1 key\n(2)no - a little flaw in the code here, "
                                          "if you don't have the"
                                          " key for it just click\nno and it will be fine "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            chest_if = True
                    except:
                        print("Didn't type a number properly.")
                if chest == 1:
                    Player.open_chest(self, 1)
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if room == 1:
                        print("Your detector senses a secret room.")
                    elif room == 2:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("One of the walls is not very sturdy. Also hollow. There might be something in there.")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
                        if chest != 1:
                            chest_if = False
                            while not chest_if:
                                try:
                                    chest_again = int(input("The silver chest is still there."
                                                            "\n(1)open - 1 key\n(2)no "))
                                    assert (chest_again in range(1, 3))
                                    if chest_again in range(1, 3):
                                        chest_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if chest_again == 1:
                                Player.open_chest(self, 1)
                elif bomb == 2:
                    print("You leave the room.")
            elif current_room == 53:
                chest_if = False
                while not chest_if:
                    try:
                        chest = int(input("It's an empty room, but with a golden chest in the middle."
                                          "\n(1)open - 2 keys\n(2)no - a little flaw in "
                                          "the code here, if you don't have the"
                                          " keys for it just click\nno and it will be fine "))
                        assert (chest in range(1, 3))
                        if chest in range(1, 3):
                            chest_if = True
                    except:
                        print("Didn't type a number properly.")
                if chest == 1:
                    Player.open_chest(self, 2)
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if room == 1:
                        print("Your detector senses a secret room.")
                    elif room == 2:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("One of the walls is not very sturdy. Also hollow. There might be something in there.")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
                        if chest != 1:
                            chest_if = False
                            while not chest_if:
                                try:
                                    chest_again = int(input("The golden chest is still there."
                                                            "\n(1)open - 2 keys\n(2)no "))
                                    assert (chest_again in range(1, 3))
                                    if chest_again in range(1, 3):
                                        chest_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if chest_again == 1:
                                Player.open_chest(self, 2)
                elif bomb == 2:
                    print("You leave the room.")
            elif current_room == 23:
                self.keys += 1
                print("It's an empty room, but with a key on the floor. Cool.")
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if room == 1:
                        print("Your detector senses a secret room.")
                    elif room == 2:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("One of the walls is not very sturdy. Also hollow. There might be something in there.")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
                elif bomb == 2:
                    print("You leave the room.")
            elif current_room == 25:
                self.bombs += 1
                print("It's an empty room, but with a bomb on the floor. Cool.")
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if room == 1:
                        print("Your detector senses a secret room.")
                    elif room == 2:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("One of the walls is not very sturdy. Also hollow. There might be something in there.")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
                elif bomb == 2:
                    print("You leave the room.")
            elif current_room == 24:
                print("The room is a bit darker than usual, so that means you just straight up\n"
                      "found a special room!")
                time.sleep(2)
                Player.special_room(self)
            elif current_room == 21:
                print("There is a trap door in the room. Like the crawl spaces in Isaac.")
                rewards = ["3 golden chests and 6 keys", "100 coins",
                           "a lucky charm and remove all negative effects", "1000 points",
                           "3 x 20 health potions and +20 attack", "an extra life", "an item box"]
                reward = random.choice(rewards)
                trap_if = False
                while not trap_if:
                    try:
                        trap = int(
                            input("You can fight 3 waves of enemies there for rewards (Each battle will take from"
                                  f" your weapon's lifespan and bombs clear 1 wave).\n"
                                  f"You will be fighting for {reward}. Once you enter\n"
                                  "there is no escaping. Do you accept?\n(1)yes\n(2)no "))
                        assert (trap in range(1, 3))
                        if trap in range(1, 3):
                            trap_if = True
                    except:
                        print("Didn't type a number properly.")
                if trap == 1:
                    Player.trap_room(self, reward)
                elif trap == 2:
                    print("You're right, might not be worth it.")
            elif current_room in range(54, 57):
                lot_if = False
                while not lot_if:
                    try:
                        lottery = int(input(("This room has a lottery! I'll get straight to the rules. "
                                             "There are 6 lucky numbers (from 1 to 49), and"
                                             "\nyou will type your own 6 numbers (NO repeating numbers!!!)"
                                             " and depending on how many"
                                             "\nyou get right you will get a reward or pick one from multiple ones. "
                                             "Each game costs you"
                                             "\n10 coins. Good luck! If you are going to play, "
                                             "that is.\n(1)play (10 coins)\n(2)leave ")))
                        assert (lottery in range(1, 3))
                        if lottery in range(1, 3):
                            lot_if = True
                    except:
                        print("Didn't type a number properly.")
                if lottery == 1:
                    if self.coins >= 10:
                        time.sleep(1)
                        Player.lottery(self)
                        while lottery == 1:
                            time.sleep(1)
                            lot_if = False
                            while not lot_if:
                                try:
                                    lottery = int(input("\nPlay again? Current coins: "
                                                        f"{self.coins}. You can do it as "
                                                        f"many times as you want by the way."
                                                        "\n(1)play again\n(2)leave "))
                                    assert (lottery in range(1, 3))
                                    if lottery in range(1, 3):
                                        lot_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if lottery == 1:
                                if self.coins >= 10:
                                    time.sleep(1)
                                    Player.lottery(self)
                                else:
                                    print("You don't even have the money to play why did you click 1...")
                                    break
                    else:
                        print("You don't even have the money to play why did you click 1...")
                else:
                    time.sleep(1)
                    print("\nYou leave the room.")
            elif current_room == 57:
                print("Oh it's this layout. No fights or anything here. Just a quick survey.")
                time.sleep(3)
                an_if = False
                while not an_if:
                    try:
                        an = int(input("Pick the best anime in the list."
                                       "\n(1)Re:zero\n(2)Demon slayer\n(3)My hero academia"
                                       "\n(4)Oregairu "))
                        assert (an in range(1, 5))
                        if an in range(1, 5):
                            an_if = True
                    except:
                        print("\nDidn't type a number properly.")
                if an == 1:
                    self.health += 18
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health > max_hp:
                        self.health = max_hp
                    print("Quality answer as expected.")
                    time.sleep(2)
                    print("You have been healed 18 hp.")
                if an == 2:
                    self.attack -= 7
                    if self.attack <= 0:
                        self.attack = 1
                    print("Okay good answer I respect your opinion.")
                    time.sleep(2)
                    print("-7 base attack.")
                if an == 3:
                    print("Wow.")
                    time.sleep(2)
                    self.dead = True
                    if self.dead:
                        Player.revive(self)
                if an == 4:
                    print("Of all the choices in this list you picked this???")
                    time.sleep(3)
                    self.attack += 8
                    print("Absolutely fucking correct, you are very cultured. +8 base attack and an item box for you.")
                    Player.item_box(self)
            elif current_room == 58:
                Player.empty_room(self)
            elif current_room == 59:
                Player.item_room(self)
            elif current_room == 60:
                Player.shop(self)
            elif current_room == 61:
                time.sleep(2)
                self.extra_lives += 1
                print("You get a random room which gives you an extra life. What luck!")
            elif current_room == 62:
                print("And this room has got...")
                time.sleep(2)
                print("A church! *sigh* I hate religion.")
                pray_if = False
                while not pray_if:
                    try:
                        pray = int(
                            input("Try praying maybe?\n(1)pray\n(2)no "))
                        assert (pray in range(1, 3))
                        if pray in range(1, 3):
                            pray_if = True
                    except:
                        print("Didn't type a number properly.")
                if pray == 2:
                    print("You leave, thank you, I am tired.")
                elif pray == 1:
                    time.sleep(2)
                    reward = random.randint(1, 30)
                    if reward in range(1, 27):
                        print("Nothing happened, as you'd expect.")
                    elif reward == 27:
                        if self.slowed:
                            self.slowed = False
                            self.attack = self.attack * 2
                            self.weapon = self.weapon * 2
                            self.weapon2 = self.weapon2 * 2
                            print("Your slow effect has been removed and you are back to normal. Weird.")
                        else:
                            print("Nothing happened, as you'd expect.")
                    elif reward == 28:
                        if self.poisoned:
                            self.poisoned = False
                            print("Your poison has been removed, how lucky is that?")
                        else:
                            print("Nothing happened, as you'd expect.")
                    elif reward == 29:
                        if self.cursed:
                            self.cursed = False
                            print("Your curse has been lifted, what a lucky bastard.")
                        else:
                            print("Nothing happened, as you'd expect.")
                    elif reward == 30:
                        self.health -= 50
                        if self.health > 0:
                            print("A lightning comes out of nowhere and strikes you for 50hp. Ahahahah")
                        else:
                            self.dead = True
                            print("You have been struck by a lightning and have died. Religion for you.")
                            Player.revive(self)
                    pray3_if = False
                    while not pray3_if:
                        try:
                            pray3 = int(
                                input("Try praying again?\n(1)pray\n(2)no "))
                            assert (pray3 in range(1, 3))
                            if pray3 in range(1, 3):
                                pray3_if = True
                        except:
                            print("Didn't type a number properly.")
                    if pray3 == 2:
                        print("You leave, thank you, I am tired.")
                    elif pray3 == 1:
                        time.sleep(2)
                        reward = random.randint(1, 30)
                        if reward in range(1, 27):
                            print("Nothing happened, as you'd expect.")
                        elif reward == 27:
                            if self.slowed:
                                self.slowed = False
                                self.attack = self.attack * 2
                                self.weapon = self.weapon * 2
                                self.weapon2 = self.weapon2 * 2
                                print("Your slow effect has been removed and you are back to normal. Weird.")
                            else:
                                print("Nothing happened, as you'd expect.")
                        elif reward == 28:
                            if self.poisoned:
                                self.poisoned = False
                                print("Your poison has been removed, how lucky is that?")
                            else:
                                print("Nothing happened, as you'd expect.")
                        elif reward == 29:
                            if self.cursed:
                                self.cursed = False
                                print("Your curse has been removed, what a lucky bastard.")
                            else:
                                print("Nothing happened, as you'd expect.")
                        elif reward == 30:
                            self.health -= 50
                            if self.health > 0:
                                print("A lightning comes out of nowhere and strikes you for 50hp. Ahahahah")
                            else:
                                self.dead = True
                                print("You have been struck by a lightning and have died. Religion for you.")
                                Player.revive(self)
                        pray2_if = False
                        while not pray2_if:
                            try:
                                pray2 = int(
                                    input("Try praying again? Last one by the way.\n(1)pray\n(2)no "))
                                assert (pray2 in range(1, 3))
                                if pray2 in range(1, 3):
                                    pray2_if = True
                            except:
                                print("Didn't type a number properly.")
                        if pray2 == 2:
                            print("You leave, thank you, I am tired.")
                        elif pray2 == 1:
                            time.sleep(2)
                            reward = random.randint(1, 30)
                            if reward in range(1, 27):
                                print("Nothing happened, as you'd expect.")
                            elif reward == 27:
                                if self.slowed:
                                    self.slowed = False
                                    self.attack = self.attack * 2
                                    self.weapon = self.weapon * 2
                                    self.weapon2 = self.weapon2 * 2
                                    print("Your slow effect has been removed and you are back to normal. Weird.")
                                else:
                                    print("Nothing happened, as you'd expect.")
                            elif reward == 28:
                                if self.poisoned:
                                    self.poisoned = False
                                    print("Your poison has been removed, how lucky is that?")
                                else:
                                    print("Nothing happened, as you'd expect.")
                            elif reward == 29:
                                if self.cursed:
                                    self.cursed = False
                                    print("Your curse has been removed, what a lucky bastard.")
                                else:
                                    print("Nothing happened, as you'd expect.")
                            elif reward == 30:
                                self.health -= 50
                                if self.health > 0:
                                    print("A lightning comes out of nowhere and strikes you for 50hp. Ahahahah")
                                else:
                                    self.dead = True
                                    print("You have been struck by a lightning and have died. Religion for you.")
                                    Player.revive(self)
                time.sleep(1)
                print("\nBye, church.")
            elif current_room == 63:
                hole = random.randint(1, 3)
                print("This is a blank room.")
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box.")
                    else:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("\nHang on, the floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(
                            input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
            elif current_room == 64:
                hole = random.randint(1, 3)
                self.bombs += 1
                print("You find a bomb in the room.")
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box.")
                    else:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("\nHang on, the floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(
                            input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
            elif current_room == 65:
                hole = random.randint(1, 3)
                self.keys += 1
                print("You find a key in the room.")
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box.")
                    else:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("\nHang on, the floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(
                            input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
            elif current_room == 66:
                hole = random.randint(1, 3)
                self.coins += 1
                print("You find a coin. Ding!")
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box.")
                    else:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("\nHang on, the floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(
                            input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
            elif current_room == 67:
                hole = random.randint(1, 3)
                print("You find an item box in the room!! Woah!!!!")
                Player.item_box(self)
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box (No shit, Sherlock, \n"
                              "I mean apart from the one you just opened).")
                    else:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("\nHang on, the floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(
                            input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole as well, second in a room!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
            elif current_room == 68:
                hole = random.randint(1, 3)
                room = random.randint(1, 2)
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box.")
                    else:
                        print("Your detector does not sense anything.")
                    time.sleep(1)
                    print("\n")
                    if room == 1:
                        print("The detector tells you about a special room.")
                    elif room == 2:
                        print("Also, no special rooms according to your detector.")
                print("\nThe floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(
                            input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
                print("\nThe wall also seems hollow...")
                time.sleep(2)
                bomb_if = False
                while not bomb_if:
                    try:
                        bomb = int(input(f"You can try bombing it and check the other side, eh?\n(1)yes - 1 bomb"
                                         f"\n(2)leave it "))
                        assert (bomb in range(1, 3))
                        if bomb in range(1, 3):
                            bomb_if = True
                    except:
                        print("Didn't type a number properly.")
                if bomb == 1:
                    if self.bombs == 0:
                        print("You don't have a bomb.")
                    elif self.bombs >= 1:
                        self.bombs -= 1
                        if room == 1:
                            Player.special_room(self)
                        elif room == 2:
                            print("There was nothing in there. My bad.")
            elif current_room == 69:
                hole = random.randint(1, 3)
                print("You find a random wooden chest. Nice.")
                Player.open_chest(self, 0)
                if "Detector" in self.items:
                    time.sleep(1)
                    if hole == 3:
                        print("Your detector senses an item box.")
                    else:
                        print("Your detector does not sense anything.")
                time.sleep(2)
                print("\nHang on, the floor is kinda hollow, there might be something below.")
                dig_if = False
                while not dig_if:
                    try:
                        dig = int(input("Bomb the floor?\n(1)yes - 1 bomb\n(2)no "))
                        assert (dig in range(1, 3))
                        if dig in range(1, 3):
                            dig_if = True
                    except:
                        print("Didn't type a number properly.")
                if dig == 2:
                    print("\nOkay we move on.")
                elif dig == 1:
                    if self.bombs == 0:
                        print("\nYou don't have a bomb, silly!")
                    else:
                        self.bombs -= 1
                        if hole == 3:
                            print("\nYou find an item box in the hole!")
                            Player.item_box(self)
                        else:
                            print("There was nothing in the hole. Oh, well.")
            elif current_room == 70:
                if not self.brad_enemy:
                    print("You are greeted into the room by Brad.")
                    time.sleep(1.5)
                    print("\n-Hello there, would you like to play a game I created? I call it, Mis-chief!")
                    time.sleep(3)
                    input("-Don't worry I will explain the rules I just need to know if you are playing or not.\n"
                          "And by the way, we play for double or nothing. Heh.\n(x) ")
                    bet_if = False
                    while not bet_if:
                        try:
                            bet = int(input("\n(1)play for coins\n(2)play for bombs\n(3)play for keys\n"
                                            "(4)offer your lucky charm and play for an item box\n(5)don't play "))
                            assert (bet in range(1, 6))
                            if bet in range(1, 6):
                                bet_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if bet in range(1, 4):
                        amount_if = False
                        while not amount_if:
                            try:
                                amount = int(input("-Alright, give me an amount: "))
                                assert amount >= 1
                                if amount >= 1:
                                    amount_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        Player.mis_chief(self, bet, amount)
                    elif bet == 4:
                        Player.mis_chief(self, bet, 1)
                    elif bet == 5:
                        print("\n-Alright, take care, we'll meet again for sure :D")
                elif self.brad_enemy and not self.brad_dead:
                    print("You have encountered... Brad!!!!")
                    time.sleep(2)
                    input("\n-Hey you got resurrected didn't you? Dirty scammer I will kill you again!(x) ")
                    enemy = "Brad"
                    hp = 32
                    action_if = False
                    while not action_if:
                        try:
                            action = int((input(f"\nWhat will you do?\nattack(1) - "
                                                f"{hp + self.rooms_cleared // 5} attack "
                                                f"required\nrun through them(2) - drains "
                                                f"{math.floor(math.pow(hp + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                                f"health"
                                                f"\nrun away(3) - drains 1 health, lose points\ngive up(4): ")))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, enemy, hp + self.rooms_cleared // 5)
                    self.brad_dead = True
                    if action == 1 and not self.dead:
                        time.sleep(2)
                        print("Brad has fallen. No more mini games this run I guess.")
                elif self.brad_dead:
                    print("Brad was supposed to be in this room. Hm.")
            elif current_room == 71:
                if not self.brad_enemy:
                    print("You are greeted into the room by Brad.")
                    time.sleep(1.5)
                    print("\n-Hey there, would you like to play rock-paper-scissors?")
                    time.sleep(2)
                    input("-We will play for double or nothing. One win takes it all. \n(x) ")
                    bet_if = False
                    while not bet_if:
                        try:
                            bet = int(input("\n(1)play for coins\n(2)play for bombs\n(3)play for keys\n"
                                            "(4)offer your lucky charm and play for an item box\n(5)don't play "))
                            assert (bet in range(1, 6))
                            if bet in range(1, 6):
                                bet_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if bet in range(1, 4):
                        amount_if = False
                        while not amount_if:
                            try:
                                amount = int(input("-Alright, give me an amount: "))
                                assert amount >= 1
                                if amount >= 1:
                                    amount_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        Player.rps(self, bet, amount)
                    elif bet == 4:
                        Player.rps(self, bet, 1)
                    elif bet == 5:
                        print("\n-Alright, take care, we'll meet again for sure :D")
                elif self.brad_enemy and not self.brad_dead:
                    print("You have encountered... Brad!!!!")
                    time.sleep(2)
                    input("\n-Hey you got resurrected didn't you? Dirty scammer I will kill you again!(x) ")
                    enemy = "Brad"
                    hp = 32
                    action_if = False
                    while not action_if:
                        try:
                            action = int((input(f"\nWhat will you do?\nattack(1) - "
                                                f"{hp + self.rooms_cleared // 5} attack "
                                                f"required\nrun through them(2) - drains "
                                                f"{math.floor(math.pow(hp + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                                f"health"
                                                f"\nrun away(3) - drains 1 health, lose points\ngive up(4): ")))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, enemy, hp + self.rooms_cleared // 5)
                    self.brad_dead = True
                    if action == 1 and not self.dead:
                        time.sleep(2)
                        print("Brad has fallen. No more mini games this run I guess.")
                elif self.brad_dead:
                    print("Brad was supposed to be in this room. Hm.")
            elif current_room == 72:
                if not self.brad_enemy:
                    print("You are greeted into the room by Brad.")
                    time.sleep(1.5)
                    print("\n-Hey, want to play guess the number?")
                    time.sleep(2)
                    input("-We will play for double or nothing. Guess the number from 1 to 25 in 4 attempts.\n(x) ")
                    bet_if = False
                    while not bet_if:
                        try:
                            bet = int(input("\n(1)play for coins\n(2)play for bombs\n(3)play for keys\n"
                                            "(4)offer your lucky charm and play for an item box\n(5)don't play "))
                            assert (bet in range(1, 6))
                            if bet in range(1, 6):
                                bet_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if bet in range(1, 4):
                        amount_if = False
                        while not amount_if:
                            try:
                                amount = int(input("Alright, give me an amount: "))
                                assert amount >= 1
                                if amount >= 1:
                                    amount_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        Player.guess_num(self, bet, amount)
                    elif bet == 4:
                        Player.guess_num(self, bet, 1)
                    elif bet == 5:
                        print("\nAlright, take care, we'll meet again for sure :D")
                elif self.brad_enemy and not self.brad_dead:
                    print("You have encountered... Brad!!!!")
                    time.sleep(2)
                    input("\n-Hey you got resurrected didn't you? Dirty scammer I will kill you again!(x) ")
                    enemy = "Brad"
                    hp = 32
                    action_if = False
                    while not action_if:
                        try:
                            action = int((input(f"\nWhat will you do?\nattack(1) - "
                                                f"{hp + self.rooms_cleared // 5} attack "
                                                f"required\nrun through them(2) - drains "
                                                f"{math.floor(math.pow(hp + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                                f"health"
                                                f"\nrun away(3) - drains 1 health, lose points\ngive up(4): ")))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, enemy, hp + self.rooms_cleared // 5)
                    self.brad_dead = True
                    if action == 1 and not self.dead:
                        time.sleep(2)
                        print("Brad has fallen. No more mini games this run I guess.")
                elif self.brad_dead:
                    print("Brad was supposed to be in this room. Hm.")
            elif current_room == 73:
                print("You enter... you guessed it, an empty room.")
                time.sleep(2)
                self.points += 25
                if self.slowed:
                    print("This room looks very cold an you get blown away by a freezing wind. This is supposed to"
                          " apply\na slow effect on you but you already have it. Haha.")
                elif not self.slowed:
                    if "Time stone" in self.items or "Shiny necklace" in self.items:
                        print("A cold wind blows you away and you should have been\n"
                              "slowed down here but your item protects you!")
                    else:
                        self.slowed = True
                        if self.slowed:
                            self.attack = self.attack // 2 + 1
                            if self.weapon > 0:
                                self.weapon = self.weapon // 2 + 1
                            if self.weapon2 > 0:
                                self.weapon2 = self.weapon2 // 2 + 1
                        print(
                            "This room looks very cold an you get blown away by a freezing wind. "
                            " are now slowed down\n and will deal only about half your damage.")
            elif current_room == 74:
                print("This is a room that will give you a random negative effect! Oh well pray for the best.\n"
                      "Or in this case not the worst...")
                self.points += 50
                time.sleep(5)
                curse = random.randint(1, 3)
                if curse == 1:
                    if self.cursed:
                        print("You were supposed to get cursed but you were already cursed"
                              "\nso it's like nothing has happened. Win.")
                    elif not self.cursed:
                        self.cursed = True
                        print("You have been cursed. :/")
                        if "Shiny necklace" in self.items:
                            time.sleep(1)
                            self.cursed = False
                            print("Shiny necklace says no to the curse!")
                elif curse == 2:
                    if self.poisoned:
                        print("You were supposed to get poisoned but you were already poisoned"
                              "\nso it's like nothing has happened. Win.")
                    elif not self.poisoned:
                        self.poisoned = True
                        print("You have been poisoned. :/")
                        if "Shiny necklace" in self.items:
                            time.sleep(1)
                            self.poisoned = False
                            print("Shiny necklace says no to the poison!")
                elif curse == 3:
                    if self.slowed:
                        print("You were supposed to get slowed down but you were already slow"
                              "\nso it's like nothing has happened. Win.")
                    elif not self.slowed:
                        if "Time stone" in self.items or "Shiny necklace" in self.items:
                            print("You should have been slowed down here but your item protects you!")
                        else:
                            self.slowed = True
                            if self.slowed:
                                self.attack = self.attack // 2 + 1
                                if self.weapon > 0:
                                    self.weapon = self.weapon // 2 + 1
                                if self.weapon2 > 0:
                                    self.weapon2 = self.weapon2 // 2 + 1
                            print("You have been slowed down. :/")
            elif current_room == 75:
                print("You find a politician in the room with his bodyguards. Obviously fighting comes to mind.")
                time.sleep(3)
                enemy = "politician"
                hp = 57
                choose_if = False
                while not choose_if:
                    try:
                        choose = int(input("Hang on, I'll give you some options here. "
                                           "\n(1)normal fight\n(2)instead of fighting offer coins."))
                        assert (choose in range(1, 3))
                        if choose in range(1, 3):
                            choose_if = True
                    except:
                        print("Didn't type a number properly.")
                time.sleep(1)
                if choose == 1:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nWhat will you do?\nattack(1) - "
                                               f"{hp + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(hp + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, enemy, hp + self.rooms_cleared // 5)
                elif choose == 2:
                    amount_if = False
                    while not amount_if:
                        try:
                            amount = int(input("How many coins are you offering (I am not allowing bluffing here): "))
                            assert amount in range(1, self.coins + 1)
                            if amount in range(1, self.coins + 1):
                                amount_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    time.sleep(1)
                    if amount < 45:
                        print("Okay, that didn't work.")
                        time.sleep(1)
                        action_if = False
                        while not action_if:
                            try:
                                action = int(input("\nWhat will you do?\nattack(1) - "
                                                   f"{hp + self.rooms_cleared // 5} attack "
                                                   f"required\nrun through them(2) - drains "
                                                   f"{math.floor(math.pow(hp + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                                   f" health"
                                                   f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                                assert (action in range(1, 5))
                                if action in range(1, 5):
                                    action_if = True
                            except:
                                print("Didn't type a number properly.")
                        Player.fight(self, action, enemy, hp + self.rooms_cleared // 5)
                    elif amount >= 45:
                        self.coins -= amount
                        print("You give them the coins and they let you go. I think it was worth it.")
                        self.points += amount
            elif current_room == 76:
                print("The doors on both sides are closing.")
                time.sleep(1)
                print("\nYou are left in the room against a titan.")
                time.sleep(1)
                if "Portable black hole" in self.items:
                    if self.black_hole:
                        hole_if = False
                        while not hole_if:
                            try:
                                hole = int(
                                    input("You can use your black hole to insta-kill the titan\n(1)do it\n(2)save it "))
                                assert (hole in range(1, 3))
                                if hole in range(1, 3):
                                    hole_if = True
                            except:
                                print("Didn't type a number properly.")
                        if hole == 1:
                            self.black_hole = False
                            input(
                                "\nYou throw the black hole as it sucks the titan in it and it disappears right after."
                                "\n"
                                "Also you get an item box.\n(x) ")
                            self.points += 300
                            Player.item_box(self)
                        else:
                            print("\nOkay, moving on.")
                            time.sleep(1)
                            input(
                                "\nThis is not going to be a normal fight where you can use strong attack or bombs. "
                                "You'll\n"
                                "need to look for a weak spot.(x) ")
                            action_if = False
                            while not action_if:
                                try:
                                    action = int(
                                        input(
                                            "What will you attack?\n(1)the legs\n(2)the stomach\n(3)the "
                                            "back of the neck"
                                            "\n(4)the head "))
                                    assert (action in range(1, 5))
                                    if action in range(1, 5):
                                        action_if = True
                                except:
                                    print("Didn't type a number properly.")
                            time.sleep(1)
                            if action != 3:
                                self.dead = True
                                print(
                                    "\nWrong. You get eaten alive and you feel yourself dying slowly"
                                    " while being digested.")
                            elif action == 3:
                                input(
                                    "\nThat is the weak spot of a titan and it falls down. If you knew this"
                                    " and didn't try to"
                                    "\nguess I am very proud of you. Also you get an item box.\n(x) ")
                                self.points += 300
                                Player.item_box(self)
                else:
                    time.sleep(1)
                    input("\nThis is not going to be a normal fight where you can use strong attack or bombs. You'll\n"
                          "need to look for a weak spot.(x) ")
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input("What will you attack?\n(1)the legs\n(2)the stomach\n(3)the back of the neck"
                                      "\n(4)the head "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    time.sleep(1)
                    if action != 3:
                        self.dead = True
                        print("\nWrong. You get eaten alive and you feel yourself dying slowly while being digested.")
                    elif action == 3:
                        input("\nThat is the weak spot of a titan and it falls down. If you knew this and didn't try to"
                              "\nguess I am very proud of you. Also you get an item box.\n(x) ")
                        self.points += 300
                        Player.item_box(self)
            elif current_room == 77:
                print("\nYou see a guy on a computer.")
                time.sleep(2)
                print("\nHang on I think I heard a noise.")
                time.sleep(2)
                print("\nWait, it's you making the noise!")
                time.sleep(2)
                print("\nAre you going to fight me?")
                enemy = "creator"
                hp = 99
                current = self.bombs
                action_if = False
                while not action_if:
                    try:
                        action = int(input("\nWhat will you do?\nattack(1) - "
                                           f"{hp + self.rooms_cleared // 5} attack "
                                           f"required\nrun through me(2) - drains "
                                           f"{math.floor(math.pow(hp + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                           f" health"
                                           f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                        assert (action in range(1, 5))
                        if action in range(1, 5):
                            action_if = True
                    except:
                        print("Didn't type a number properly.")
                Player.fight(self, action, enemy, hp + self.rooms_cleared // 5)
                time.sleep(1)
                new = self.bombs
                if not self.dead:
                    if new < current:
                        print("\nOh you saw the default bomb message and thought you can get away with it no no no.")
                        self.frozen = True
                        self.dead = True
                        time.sleep(3)
                        print(
                            "\nI am literally the creator of this game. Going to kill you now, "
                            "let's see you resurrect your"
                            "\nway out of this ahahahahahahh.")
                        Player.revive(self)
                    else:
                        print("\nFairs, you have defeated me. Okay, you get an instant win, congrats.")
                        self.points += 500
                        self.winner = True
            elif current_room == 78:
                action_if = False
                while not action_if:
                    try:
                        action = int(input("\nYou have encountered glitched baby. Wtf?. (Okay, listen, this room is\n"
                                           "always glitchy for some reason I added and removed it multiple times and\n"
                                           "I can't seem to fix it. I will just leave it as a troll/glitch.)"
                                           f"What will you do?\nattack(1) - "
                                           f"{monsters_hp[0] + self.rooms_cleared // 5} attack "
                                           f"required. Wtf?\nrun through them(2) - drains "
                                           f"{math.floor(math.pow(monsters_hp[0], 0.5) * 2.5)}"
                                           f" health brudda what please don't crash the game please"
                                           f"\nrun away(3) - -3 health, lose points why?????\ngive up aaaa(4): "))
                        assert (action in range(1, 5))
                        if action in range(1, 5):
                            action_if = True
                    except:
                        print("Didn't type a number properly.")
                Player.fight(self, action, monsters[0], monsters_hp[0])
                if action == 1:
                    self.points += 1
            elif current_room == 79:
                action_if = False
                while not action_if:
                    try:
                        action = int(input("You have encountered a cat. No, you cannot adopt it now, it's too "
                                           "dangerous."
                                           "\n(1)give it a coin\n(2)ignore\n(3)kill it "))
                        assert (action in range(1, 4))
                        if action in range(1, 4):
                            action_if = True
                    except:
                        print("Didn't type a number properly.")
                if action == 1:
                    if self.coins == 0:
                        print("\nBro you literally have nothing just move on.")
                        self.points -= 24
                    else:
                        self.coins -= 1
                        print("\nHopefully you will meet again.")
                        self.points += 1
                        self.cat = True
                elif action == 2:
                    print("\nOkay we move on.")
                    self.points -= 24
                elif action == 3:
                    print("\nMhm. If you thought that will be an enemy or something then no. It was just a random cat.")
                    self.points -= 250
                    if self.pray:
                        self.pray = False
            elif current_room == 80:
                input("There is a trader in the room!! Let's check out what he has to offer"
                      "\n(no discounts here, buddy)!(x)")
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input("He is ready to sell you an item box.\n"
                                        "65 coins. Buy?\n(1)yes\n(2)no "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("Didn't type a number properly.")
                if buy == 1:
                    if self.coins < 65:
                        print("\nYou don't have the money.")
                    else:
                        self.coins -= 65
                        print(f"Purchase complete! Your coins are now {self.coins}.")
                        Player.item_box(self)
                elif buy == 2:
                    print("You leave. 65 coins? What an obvious scam.")
            elif current_room == 81:
                price = math.floor(60 - 60 * (self.discount / 100))
                buy_if = False
                while not buy_if:
                    try:
                        buy = int(input(f"\nYou find a random shop that sells an item box!.\n{price}"
                                        f" coins (after potential discounts).\n(1)buy\n(2)no "))
                        assert (buy in range(1, 3))
                        if buy in range(1, 3):
                            buy_if = True
                    except:
                        print("Didn't type a number properly.")
                if buy == 1:
                    if self.coins >= price:
                        self.coins -= price
                        print(f"\nPurchase complete! Your coins are now {self.coins}.")
                        Player.item_box(self)
                    else:
                        print("\nNot enough money, sorry.")
                elif buy == 2:
                    print("\n*sad face")
            elif current_room in range(82, 85):
                time.sleep(2)
                print("You get a room which gives you an item box! Woaaaah")
                Player.item_box(self)
            elif current_room == 85:
                weapon = random.randint(18, 40)
                weapon_hp = random.randint(3, 5)
                take_if = False
                while not take_if:
                    try:
                        take = int(input(f"You find a wooden sword! If you take it you will have {weapon} "
                                         f"attack +{self.attack} (your base attack), and it will last for "
                                         f"{weapon_hp} rooms. "
                                         "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                         "\nyes(2) - put it in slot 2(not equipping it)\n"
                                         "Recommended to click 1 if you have no weapons "
                                         "and click 2 if you have 1 weapon.\n"
                                         "If you have 2 weapons it will replace the one you have in the slot you chose."
                                         "\nno(3) "))
                        assert (take in range(1, 4))
                        if take in range(1, 4):
                            take_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take != 3:
                    Player.take_weapon(self, take, weapon, weapon_hp)
            elif current_room == 86:
                weapon = random.randint(50, 63)
                weapon_hp = random.randint(5, 7)
                take_if = False
                while not take_if:
                    try:
                        take = int(input(f"You find a powerful sword! If you take it you will have {weapon} "
                                         f"attack +{self.attack} (your base attack), and it will last"
                                         f" for {weapon_hp} rooms. "
                                         "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                         "\nyes(2) - put it in slot 2(not equipping it)\n"
                                         "Recommended to click 1 if you have no weapons and "
                                         "click 2 if you have 1 weapon. "
                                         "\nIf you have 2 weapons it will replace the one you have in the slot "
                                         "you chose"
                                         "\nno(3) "))
                        assert (take in range(1, 4))
                        if take in range(1, 4):
                            take_if = True
                    except:
                        print("\nDidn't type a proper number.")
                if take != 3:
                    Player.take_weapon(self, take, weapon, weapon_hp)
        elif if_fight == 2:
            if new_old in range(1, 4):
                if current_room == 1:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered a group of small spiders. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[1] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[1] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[1], monsters_hp[1] + self.rooms_cleared // 5)
                elif current_room == 2:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered a bunch of mice. What will you do?\nattack(1) - "
                                      f"{monsters_hp[2] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[2] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[2], monsters_hp[2] + self.rooms_cleared // 5)
                elif current_room == 3:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered a bunch of bats. What will you do?\nattack(1) - "
                                      f"{monsters_hp[3] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[3] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[3], monsters_hp[3] + self.rooms_cleared // 5)
                elif current_room == 4:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered a ton of flies. What will you do?\nattack(1) - "
                                               f"{monsters_hp[4] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[4] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[4], monsters_hp[4] + self.rooms_cleared // 5)
                elif current_room == 5:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered some hackers(what are they gonna do in a dungeon "
                                      f"of all "
                                      f"places??)\n. What will you do?\nattack(1) - "
                                      f"{monsters_hp[5] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[5] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[5], monsters_hp[5] + self.rooms_cleared // 5)
                elif current_room == 6:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered rabbits. What will you do?\nattack(1) - "
                                               f"{monsters_hp[6] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[6] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[6], monsters_hp[6] + self.rooms_cleared // 5)
                elif current_room == 7:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered possessed squirrels. What will you do?\nattack(1) - "
                                      f"{monsters_hp[7] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[7] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[7], monsters_hp[7] + self.rooms_cleared // 5)
                elif current_room == 8:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered a flock of seagulls. What will you do?\nattack(1) - "
                                      f"{monsters_hp[8] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[8] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[8], monsters_hp[8] + self.rooms_cleared // 5)
                elif current_room == 9:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered some cockroaches. What will you do?\nattack(1) - "
                                      f"{monsters_hp[9] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[9] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[9], monsters_hp[9] + self.rooms_cleared // 5)
                elif current_room == 10:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered a retarded dwarf (wtaf). What will you do?\nattack(1) - "
                                      f"{monsters_hp[10] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through him(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[10] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[10], monsters_hp[10] + self.rooms_cleared // 5)
                elif current_room == 11:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered bucket bois. What will you do?\nattack(1) - "
                                               f"{monsters_hp[11] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[11] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[11], monsters_hp[11] + self.rooms_cleared // 5)
                elif current_room == 12:
                    print("You have encountered a... ghost? No, that's just a guy who put a blanket on.")
                    time.sleep(4)
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nWhat will you do?\nattack(1) - "
                                               f"{monsters_hp[12] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[12] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[12], monsters_hp[12] + self.rooms_cleared // 5)
                elif current_room == 13:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered floating eyes. What will you do?\nattack(1) - "
                                               f"{monsters_hp[13] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[13] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[13], monsters_hp[13] + self.rooms_cleared // 5)
                elif current_room == 14:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered evil eagles. What will you do?\nattack(1) - "
                                               f"{monsters_hp[14] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[14] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[14], monsters_hp[14] + self.rooms_cleared // 5)
                elif current_room == 15:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered gypsies. What will you do?\nattack(1) - "
                                               f"{monsters_hp[15] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[15] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[15], monsters_hp[15] + self.rooms_cleared // 5)
                    if action == 2:
                        if self.coins > 0:
                            if self.coins < 30:
                                self.coins = 0
                                print(
                                    "Running through the gypsies you realize they "
                                    "stole all your (not that many) coins. ")
                            if self.coins > 30:
                                self.coins -= 30
                                print("Running through the gypsies you realize they stole 30 coins from you. Cliche.")
                elif current_room == 16:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered one robot. What will you do?\nattack(1) - "
                                               f"{monsters_hp[16] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[16] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[16], monsters_hp[16] + self.rooms_cleared // 5)
                elif current_room == 17:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered goblins. What will you do?\nattack(1) - "
                                               f"{monsters_hp[17] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[17] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[17], monsters_hp[17] + self.rooms_cleared // 5)
                    if action == 2:
                        if self.coins > 0:
                            if self.coins < 20:
                                self.coins = 0
                                print(
                                    "Running through the goblins you realize they "
                                    "stole all your (not that many) coins. "
                                    "Cliche.")
                            if self.coins > 20:
                                self.coins -= 20
                                print("Running through the goblins you realize they stole 20 coins from you. Cliche.")
                elif current_room == 18:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered sinister penguins. What will you do?\nattack(1) - "
                                      f"{monsters_hp[18] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[18] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[18], monsters_hp[18] + self.rooms_cleared // 5)
                elif current_room == 19:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountred naked skeletons (what skeletons aren't naked then???)"
                                      f"\nWhat will you do?\nattack(1) - "
                                      f"{monsters_hp[19] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through them(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[19] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[19], monsters_hp[19] + self.rooms_cleared // 5)
                elif current_room == 20:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered snakes (are they poisonous?). "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[20] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[20] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health, also might poison you\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[20], monsters_hp[20] + self.rooms_cleared // 5)
                    poison = random.randint(1, 2)
                    if poison == 1 and action == 2:
                        self.poisoned = True
                        print("You have been poisoned by one of the snakes.")
                        if "Shiny necklace" in self.items:
                            self.cursed = False
                            time.sleep(1)
                            print("Shiny necklace says no to the poison!")
                elif current_room == 21:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered ninja turtles. What will you do?\nattack(1) - "
                                               f"{monsters_hp[21] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[21] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[21], monsters_hp[21] + self.rooms_cleared // 5)
                elif current_room == 22:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered a hairy potter (eww). What will you do?\nattack(1) - "
                                      f"{monsters_hp[22] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through him(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[22] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[22], monsters_hp[22] + self.rooms_cleared // 5)
                elif current_room == 23:
                    print("You hear a loud suuuuuuuuuuuuuuuuuu coming from the room")
                    time.sleep(2)
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered Cristiano Ronaldo. What will you do?\nattack(1) - "
                                      f"{monsters_hp[23] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through him(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[23] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[23], monsters_hp[23] + self.rooms_cleared // 5)
                    if action == 1:
                        if not self.dead:
                            time.sleep(1)
                            print("\nAfter having been defeated Cristiano started faintly asking for a\n"
                                  "\"penalty\". Whatever that means.")
                elif current_room == 24:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered an orc. What will you do?\nattack(1) - "
                                               f"{monsters_hp[24] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him, yes he is male I decided(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[24] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[24], monsters_hp[24] + self.rooms_cleared // 5)
                elif current_room == 25:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered a tiger. What will you do?\nattack(1) - "
                                               f"{monsters_hp[25] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[25] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[25], monsters_hp[25] + self.rooms_cleared // 5)
                elif current_room == 26:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(
                                    f"\nYou have encountered a.. person with an intimidating ghost floating behind him"
                                    f" (kinda like a..sta.... I don't know what). What will you do?\nattack(1) - "
                                    f"{monsters_hp[26] + self.rooms_cleared // 5} attack "
                                    f"required\nrun through him(2) - drains "
                                    f"{math.floor(math.pow(monsters_hp[26] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                    f"health\nrun away(3) - "
                                    "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[26], monsters_hp[26] + self.rooms_cleared // 5)
                    if action == 1 and not self.dead:
                        time.sleep(1)
                        print("Right as the person died you saw that his ghost died too. Strange.")
                elif current_room == 27:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered an actual ghost. What will you do?\nattack(1) - "
                                      f"{monsters_hp[27] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through it(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[27] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[27], monsters_hp[27] + self.rooms_cleared // 5)
                elif current_room == 28:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered Jackie Chan. What will you do?\nattack(1) - "
                                               f"{monsters_hp[28] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[28] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[28], monsters_hp[28] + self.rooms_cleared // 5)
                elif current_room == 29:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                (input(f"\nYou have encountered armored skeletons. What will you do?\nattack(1) - "
                                       f"{monsters_hp[29] + self.rooms_cleared // 5} attack "
                                       f"required\nrun through them(2) - drains "
                                       f"{math.floor(math.pow(monsters_hp[29] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                       f"health\nrun away(3) - "
                                       "-3 health, lose points\ngive up(4): ")))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[29], monsters_hp[29] + self.rooms_cleared // 5)
                elif current_room == 30:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered two robots (strength of one robot x2). "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[30] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[30] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[30], monsters_hp[30] + self.rooms_cleared // 5)
                elif current_room == 31:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered a transgender. What will you do?\nattack(1) - "
                                               f"{monsters_hp[31] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through hi.. he.. them?(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[31] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[31], monsters_hp[31] + self.rooms_cleared // 5)
                elif current_room == 32:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered a gun that moves on its own... somehow. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[32] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[32] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[32], monsters_hp[32] + self.rooms_cleared // 5)
                elif current_room == 33:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered a school shooter. What will you do?\nattack(1) - "
                                      f"{monsters_hp[33] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through him(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[33] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[33], monsters_hp[33] + self.rooms_cleared // 5)
                elif current_room == 34:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered a samurai. What will you do?\nattack(1) - "
                                               f"{monsters_hp[34] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[34] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[34], monsters_hp[34] + self.rooms_cleared // 5)
                    if not self.dead:
                        if action == 1:
                            take_if = False
                            while not take_if:
                                try:
                                    take = int(input(f"The samurai has dropped a sword! If you take it "
                                                     f"it will give you + 40 attack"
                                                     f", and it will last for 10 rooms. "
                                                     "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                                     "\nyes(2) - put it in slot 2(not equipping it)\n"
                                                     "Recommended to click 1 if you have no weapons and click "
                                                     "2 if you have 1 weapon. "
                                                     "If you have 2 weapons it will replace the one you "
                                                     "have in the slot you chose"
                                                     "\nno(3) "))
                                    assert (take in range(1, 4))
                                    if take in range(1, 4):
                                        take_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if take != 3:
                                Player.take_weapon(self, take, 40, 10)
                elif current_room == 35:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered Spiderman (Tom Holland). What will you do?\nattack(1) - "
                                      f"{monsters_hp[35] + self.rooms_cleared // 5} attack "
                                      f"required\nrun through him(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[35] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[35], monsters_hp[35] + self.rooms_cleared // 5)
                elif current_room == 36:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(
                                    f"\nYou have encountered Spiderman (Tobey Maguire). What will you do?\nattack(1) - "
                                    f"{monsters_hp[36] + self.rooms_cleared // 5} attack "
                                    f"required\nrun through him(2) - drains "
                                    f"{math.floor(math.pow(monsters_hp[36] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                    f"health\nrun away(3) - "
                                    "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[36], monsters_hp[36] + self.rooms_cleared // 5)
                elif current_room == 37:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered three robots (like 1 but 3 times stronger). "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[37] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[37] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[37], monsters_hp[37] + self.rooms_cleared // 5)
                elif current_room == 38:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered Batman (one of them, there are a lot, I know). "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[38] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[38] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[38], monsters_hp[38] + self.rooms_cleared // 5)
                elif current_room == 39:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered Metallica. What will you do?\nattack(1) - "
                                               f"{monsters_hp[39] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[39] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[39], monsters_hp[39] + self.rooms_cleared // 5)
                elif current_room == 40:
                    print("Is this... a mirror?")
                    time.sleep(2)
                    print("You see yourself in it and the reflection comes out of the mirror wtfffff")
                    time.sleep(4)
                    print("It has copied your current weapon. I guess you have to fight it")
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nWhat will you do?\nattack(1) - "
                                               f"{self.attack + self.weapon + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it(2) - drains "
                                               f"{math.floor(math.pow(self.attack + self.weapon + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[40], self.attack + self.weapon + self.rooms_cleared // 5)
                elif current_room == 41:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered jelly blobs. What will you do?\nattack(1) - "
                                               f"{monsters_hp[41] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[41] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[41], monsters_hp[41] + self.rooms_cleared // 5)
                elif current_room == 42:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered Goku. What will you do?\nattack(1) - "
                                               f"{monsters_hp[42] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[42] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[42], monsters_hp[42] + self.rooms_cleared // 5)
                elif current_room == 43:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered Saitama. What will you do?\nattack(1) - "
                                               f"{monsters_hp[43] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[43] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health, this is a game he won't insta kill you don't worry also "
                                               f"I haven't watched One Punch Man\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[43], monsters_hp[43] + self.rooms_cleared // 5)
                elif current_room == 44:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered the Archer Queen from Clash of Clans. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monsters_hp[44] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through her(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[44] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[44], monsters_hp[44] + self.rooms_cleared // 5)
                elif current_room == 45:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nYou have encountered MrBeast. What will you do?\nattack(1) - "
                                               f"{monsters_hp[45] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[45] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[45], monsters_hp[45] + self.rooms_cleared // 5)
                    if action == 1:
                        if not self.dead:
                            time.sleep(2)
                            self.coins += 70
                            print("\nYou gain 70 coins from MrBeast. You should feel robbed it's not 70k honestly.")
                elif current_room == 46:
                    print("You have encountered JOHN CENAAAAAA TUTURUTUUUUUU TU TU RU TUUU")
                    time.sleep(3)
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(f"\nWhat will you do?\nattack(1) - "
                                               f"{monsters_hp[46] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monsters_hp[46] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                               f"health\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[46], monsters_hp[46] + self.rooms_cleared // 5)
                elif current_room == 47:
                    if self.parry_enemy:
                        print("You have encountered... Parry himself!!!!")
                        time.sleep(2)
                        input(f"Oi, {self.name} you are in a dungeon so you expect fights am I right? "
                              "\nHere I am show me what you've got(x) ")
                        action_if = False
                        while not action_if:
                            try:
                                action = int((input(f"\nWhat will you do?\nattack(1) - "
                                                    f"{monsters_hp[-4] + self.rooms_cleared // 5} attack "
                                                    f"required\nrun through him(2) - drains "
                                                    f"{math.floor(math.pow(monsters_hp[-4] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                                    f"health"
                                                    f"\nrun away(3) - -3 health, lose points\ngive up(4): ")))
                                assert (action in range(1, 5))
                                if action in range(1, 5):
                                    action_if = True
                            except:
                                print("Didn't type a number properly.")
                        Player.fight(self, action, monsters[-4], monsters_hp[-4] + self.rooms_cleared // 5)
                    else:
                        action_if = False
                        while not action_if:
                            try:
                                action = int(input(f"\nYou have encountered rabbits. What will you do?\nattack(1) - "
                                                   f"{monsters_hp[6] + self.rooms_cleared // 5} attack "
                                                   f"required\nrun through them(2) - drains "
                                                   f"{math.floor(math.pow(monsters_hp[6] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                                   f"health\nrun away(3) - "
                                                   "-3 health, lose points\ngive up(4): "))
                                assert (action in range(1, 5))
                                if action in range(1, 5):
                                    action_if = True
                            except:
                                print("Didn't type a number properly.")
                        Player.fight(self, action, monsters[6], monsters_hp[6] + self.rooms_cleared // 5)
                elif current_room == 48:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input(f"\nYou have encountered Subaru from Re:Zero. What will you do?\nattack(1) - "
                                      f"{monsters_hp[-3] + self.rooms_cleared // 5} attack "
                                      f"required (he is weak)\nrun through him(2) - drains "
                                      f"{math.floor(math.pow(monsters_hp[-3] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                      f"health\nrun away(3) - "
                                      "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[-3], monsters_hp[-3] + self.rooms_cleared // 5)
                    if not self.dead:
                        while action == 1 and not self.dead:
                            print("\nYou find nothing after leaving the room.")
                            time.sleep(3)
                            print(f"\nRoom {self.rooms_cleared} passed!!")
                            time.sleep(1)
                            print(f"\nNext room: {self.rooms_cleared + 1}")
                            time.sleep(2)
                            Player.print_stats(self)
                            input("(x)")
                            time.sleep(3)
                            print("\nYou see a door and enter a room")
                            time.sleep(2)
                            action_if = False
                            while not action_if:
                                try:
                                    action = int(input(f"\nYou have encountered Subaru from Re:Zero. "
                                                       f"What will you do?\nattack(1) - "
                                                       f"{monsters_hp[-3] + self.rooms_cleared // 5} attack "
                                                       f"required (he is weak)\nrun through him(2) - drains "
                                                       f"{math.floor(math.pow(monsters_hp[-3] + self.rooms_cleared // 5, 0.5) * 2.5)} "
                                                       f"health\nrun away(3) - "
                                                       "-3 health, lose points\ngive up(4): "))
                                    assert (action in range(1, 5))
                                    if action in range(1, 5):
                                        action_if = True
                                except:
                                    print("Didn't type a number properly.")
                            Player.fight(self, action, monsters[-3], monsters_hp[-3] + self.rooms_cleared // 5)
                elif current_room == 49:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(
                                input("\nYou have encountered Sonic the Hedgehog! What will you do?\nattack(1) - "
                                      "75 attack "
                                      "required\nrun past him(2) - no fucking chance\nrun away(3) - "
                                      "no fucking chance\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[-2], monsters_hp[-2])
                elif current_room == 50:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered a fucking dragon. What will you "
                                               "do?\nattack(1) - 500 attack required\nrun through him(2) - "
                                               "if you run under him fast enough you can make it\nrun away(3) - "
                                               "-3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monsters[-1], monsters_hp[-1])
            elif new_old in range(4, 6):
                if current_room == 0:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered the lowest of creatures - NFT owners. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[0] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[0] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[0], monst_2_hp[0] + self.rooms_cleared // 5)
                elif current_room == 1:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered bookworms. No, not people. Literal worms. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[1] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[1] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[1], monst_2_hp[1] + self.rooms_cleared // 5)
                elif current_room == 2:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered weebs. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[2] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[2] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[2], monst_2_hp[2] + self.rooms_cleared // 5)
                elif current_room == 3:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered a swarm of bees. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 4:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered soccer balls. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 5:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered human form Eren Jaeger. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 6:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered zombies. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                    if action == 2 and not self.dead:
                        self.cursed = True
                        print("You have been cursed by the zombies.")
                        if "Shiny necklace" in self.items:
                            self.cursed = False
                            time.sleep(1)
                            print("Shiny necklace says no to the curse!")
                elif current_room == 7:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered turks. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 8:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered the fastest man alive. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 9:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered basketballs. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 10:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered the king from Clash Royale (blue one). "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                    if self.dead:
                        time.sleep(2)
                        print("He he he haa")
                        time.sleep(2)
                        print("He he he haa")
                        time.sleep(2)
                        print("He he he haa")
                        time.sleep(2)
                        print("He he he haa")
                elif current_room == 11:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered romanians. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 12:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered clowns. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 13:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered a rocket league car. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it, not the best idea honestly(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 14:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered Monika. "
                                               f"Just Monika\nJust Monika(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nJust Monika(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nJust Monika(3) - Just Monika\nJust Monika(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Just Monika.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                    if self.dead:
                        print("Just Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika"
                              "\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika\nJust Monika")
                elif current_room == 15:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered the stock market. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 16:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered The Lorax. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 17:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered You. Not, not me, you, not you either.\n"
                                               "I mean the enemy is named \"You\" for fuck's sake nevermind. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 18:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered bulgarians. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 19:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered the BBC (British Broadcasting Corporation). \n"
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 20:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered ligma balls ha got em. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 21:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered firefox. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through it(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 22:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered Mike Wazowski with two eyes. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 23:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered builders. They got some big hammers. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 24:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered hitmen. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 25:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered Slabhead. If you are wondering, google search"
                                               " Harry Maguire. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 26:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered a buff fella. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 27:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered my literature teacher. If you win this fight"
                                               "\nI am giving you an instant win as a reward for setting me free. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through her(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                    if action == 1 and not self.dead:
                        self.winner = True
                elif current_room == 28:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered Orang. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 29:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered Meme Man. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 30:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered Gosho Chushkata. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through him(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 31:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered four robots. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)
                elif current_room == 32:
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input("\nYou have encountered five robots. "
                                               f"What will you do?\nattack(1) - "
                                               f"{monst_2_hp[current_room] + self.rooms_cleared // 5} attack "
                                               f"required\nrun through them(2) - drains "
                                               f"{math.floor(math.pow(monst_2_hp[current_room] + self.rooms_cleared // 5, 0.5) * 2.5)}"
                                               f" health"
                                               f"\nrun away(3) - -3 health, lose points\ngive up(4): "))
                            assert (action in range(1, 5))
                            if action in range(1, 5):
                                action_if = True
                        except:
                            print("Didn't type a number properly.")
                    Player.fight(self, action, monst_2[current_room], monst_2_hp[current_room] + self.rooms_cleared // 5)

    def double_room(self):
        valid = False
        while not valid:
            try:
                if "Mute button" in self.items:
                    command = int(input("\n... ... . .... .. . ...... ...., .. ... .... .. ..... ... ..... ...?"
                                        "\n...(1)\n..(2) "))
                else:
                    command = int(input("\nYou see a door to a double room, do you want to enter the first one?"
                                        "\nyes(1)\nno(2) "))
                if command == 1:
                    print("\nYou enter the room.")
                    self.double = True
                    Player.enter_room(self)
                    self.double = False
                    time.sleep(3)
                    valid = True
                elif command == 2:
                    print("You skipped it, you coward, less points for you.")
                    self.points -= 20
                    self.skipped = True
                    valid = True
                if not valid:
                    print("Didn't type 1 or 2 or sth went wrong, try again")
            except ValueError:
                print("Didn't type 1 or 2 or sth went wrong, try again")
        if not self.dead and not self.skipped and not self.winner:
            Player.print_stats(self)
            valid = False
            while not valid:
                try:
                    if "Mute button" in self.items:
                        command = int(input("\n.. ... .... .. ..... ... ...... ....?\n...(1)\n..(2) "))
                    else:
                        command = int(input("\nDo you want to enter the second room?\nyes(1)\nno(2) "))
                    if command == 1:
                        print("\nYou enter the room.")
                        Player.enter_room(self)
                        self.double_enemy.clear()
                        time.sleep(3)
                        valid = True
                    elif command == 2:
                        print("You skipped it, you coward, less points for you.")
                        self.points -= 20
                        self.skipped = True
                        valid = True
                    if not valid:
                        print("Didn't type 1 or 2 or sth went wrong, try again")
                except ValueError:
                    print("Didn't type 1 or 2 or sth went wrong, try again")

    def boss_room(self):
        if "Mute button" in self.items:
            print(f"... ..... ... .... ..... ... .. ....... ... ...?")
        else:
            print("You enter the boss room. Who is waiting for you?")
        time.sleep(2)
        bosses = ["Giant Crab", "Goblin Shaman", "Gladiator"]
        boss = random.choice(bosses)
        if "Mute button" in self.items:
            print(f".... ........ .. ... {boss}! .... ....!")
        else:
            print(f"Your opponent is the {boss}! Good luck!")
        time.sleep(2)
        if boss == "Giant Crab":
            Player.giant_crab(self)
        elif boss == "Goblin Shaman":
            Player.goblin_shaman(self)
        elif boss == "Gladiator":
            Player.gladiator(self)
        if not self.dead:
            time.sleep(2)
            win_if = False
            while not win_if:
                try:
                    win = int(input("You see the door to exit the dungeon and win the game."
                                    "\n(1)win\n(2)keep playing "))
                    assert (win in range(1, 3))
                    if win in range(1, 3):
                        win_if = True
                except:
                    print("\nDidn't type a proper number.")
            if win == 1:
                self.winner = True
                print("\nYou have achieved victory. What a legend.")
            elif win == 2:
                if self.weapon_hp > 0:
                    self.weapon_hp -= 1
                    if self.weapon_hp == 0:
                        self.weapon = 0
                        time.sleep(1)
                        print("\nYou have exhausted your weapon.\n")
                        Player.ask_weapon(self)
                        time.sleep(1)
                print("\nOkay we keep going.")
                reward = random.randint(1, 2)
                time.sleep(1)
                if reward == 1:
                    print("You got an extra life.")
                    self.extra_lives += 1
                elif reward == 2:
                    print("You get an item box.")
                    Player.item_box(self)
                time.sleep(1)

    def giant_crab(self):
        input("You are standing against the Giant Crab but at a distance of course.(x) ")
        print("It's \"just\" a giant crab as the name suggests.")
        if "Portable black hole" in self.items and self.black_hole:
            if self.black_hole:
                time.sleep(1)
                hole_if = False
                while not hole_if:
                    try:
                        hole = int(
                            input("You can use your black hole to insta-kill the Giant crab\n(1)do it\n(2)save it "))
                        assert (hole in range(1, 3))
                        if hole in range(1, 3):
                            hole_if = True
                    except:
                        print("Didn't type a number properly.")
                if hole == 1:
                    self.black_hole = False
                    input(
                        "\nYou throw the black hole as it sucks the crab in it and it disappears right after. (x) ")
                    self.points += 600
                    print("\nYou have defeated the Giant Crab, congratulations!")
                    time.sleep(2)
                else:
                    print("\nOkay, moving on.")
                    time.sleep(3)
                    print("\nThe ground around you starts opening and now it's water.")
                    time.sleep(2)
                    print("\nA hell of a lot of crabs start to crawl out and head towards you. Your turn!")
                    time.sleep(2)
                    wave = 1
                    if_wave2 = random.randint(1, 5)
                    if_wave3 = random.randint(1, 5)
                    if_wave4 = random.randint(1, 6)
                    bomb_if = False
                    while not bomb_if:
                        try:
                            bomb = int(input(
                                f"\nYou can just straight up try attacking them, but you'll"
                                f" need 30 total attack. You now have"
                                f" {self.attack} + {self.weapon}.\nA bomb (You have {self.bombs}) "
                                f"should do the job as well.\n(1)bomb\n(2)straight up attack "))
                            assert (bomb in range(1, 3))
                            if bomb in range(1, 3):
                                bomb_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    if bomb == 1:
                        if self.bombs > 0:
                            self.bombs -= 1
                            wave += 1
                            print("Boom! That worked out great!")
                        else:
                            self.dead = True
                            print("You throw a bo.. wait you have none. Bye bye.")
                    elif bomb == 2:
                        Player.ask_weapon(self)
                        if (self.attack + self.weapon) < 30:
                            self.dead = True
                            print("That's the end I'm afraid.")
                        else:
                            if self.weapon_hp > 0:
                                self.weapon_hp -= 1
                                if self.weapon_hp == 0:
                                    self.weapon = 0
                                    time.sleep(1)
                                    print("\nYou have exhausted your weapon.\n")
                                    Player.ask_weapon(self)
                                    time.sleep(1)
                            wave += 1
                            print(
                                "You get rid of the crabs. Your weapon's health goes down"
                                " for a wave of crabs by the way.")
                    if "Blessed flower" in self.items:
                        if "Strong juice" in self.items:
                            if not self.dead and self.health < 200:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 200:
                                    self.health = 200
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                        else:
                            if not self.dead and self.health < 100:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 100:
                                    self.health = 100
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                    if self.poisoned and not self.dead:
                        self.health -= 3
                        if self.health > 0:
                            time.sleep(2)
                            if "Mute button" in self.items:
                                print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                            else:
                                print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                        else:
                            self.dead = True
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                            else:
                                print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                            Player.revive(self)
                    if not self.dead:
                        self.points += 30
                        if wave == 2 and if_wave2 != 5:
                            time.sleep(2)
                            bomb_if = False
                            while not bomb_if:
                                try:
                                    bomb = int(
                                        input(
                                            f"\nAnother wave of crabs turns up, but you'll"
                                            f" need 40 attack this time. You now "
                                            f"have"
                                            f" {self.attack} + {self.weapon}.\nA bomb (You have {self.bombs}) should "
                                            f"do the job as well.\n(1)bomb\n(2)straight up attack "))
                                    assert (bomb in range(1, 3))
                                    if bomb in range(1, 3):
                                        bomb_if = True
                                except:
                                    print("\nDidn't type a number properly, try again.")
                            if bomb == 1:
                                if self.bombs > 0:
                                    self.bombs -= 1
                                    wave += 1
                                    print("Boom! That worked out great!")
                                    self.points += 40
                                else:
                                    self.dead = True
                                    print("You throw a bo.. wait you have none. Bye bye.")
                            elif bomb == 2:
                                Player.ask_weapon(self)
                                if (self.attack + self.weapon) < 40:
                                    self.dead = True
                                    print("That's the end I'm afraid.")
                                else:
                                    if self.weapon_hp > 0:
                                        self.weapon_hp -= 1
                                        if self.weapon_hp == 0:
                                            self.weapon = 0
                                            time.sleep(1)
                                            print("\nYou have exhausted your weapon.\n")
                                            Player.ask_weapon(self)
                                            time.sleep(1)
                                    wave += 1
                                    self.points += 40
                                    print(
                                        "You get rid of the crabs. Your weapon's health goes"
                                        " down for a wave of crabs by "
                                        "the way.")
                            if "Blessed flower" in self.items:
                                if "Strong juice" in self.items:
                                    if not self.dead and self.health < 200:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 200:
                                            self.health = 200
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                                else:
                                    if not self.dead and self.health < 100:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 100:
                                            self.health = 100
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                            if self.poisoned and not self.dead:
                                self.health -= 3
                                if self.health > 0:
                                    time.sleep(2)
                                    if "Mute button" in self.items:
                                        print(
                                            f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                    else:
                                        print(
                                            f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                                else:
                                    self.dead = True
                                    time.sleep(1)
                                    if "Mute button" in self.items:
                                        print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                    else:
                                        print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                    Player.revive(self)
                    if not self.dead:
                        if wave == 3 and if_wave3 in range(1, 3):
                            time.sleep(2)
                            bomb_if = False
                            while not bomb_if:
                                try:
                                    bomb = int(input(f"\nYou guessed it. More crabs. 50 attack please. You now have"
                                                     f" {self.attack} + {self.weapon}.\n"
                                                     f"A bomb (You have {self.bombs}) should do the job as "
                                                     f"well.\n(1)bomb\n(2)straight up attack "))
                                    assert (bomb in range(1, 3))
                                    if bomb in range(1, 3):
                                        bomb_if = True
                                except:
                                    print("\nDidn't type a number properly, try again.")
                            if bomb == 1:
                                if self.bombs > 0:
                                    self.bombs -= 1
                                    wave += 1
                                    print("Boom! That worked out great!")
                                    self.points += 50
                                else:
                                    self.dead = True
                                    print("You throw a bo.. wait you have none. Bye bye.")
                            elif bomb == 2:
                                Player.ask_weapon(self)
                                if (self.attack + self.weapon) < 50:
                                    self.dead = True
                                    print("That's the end I'm afraid.")
                                else:
                                    if self.weapon_hp > 0:
                                        self.weapon_hp -= 1
                                        if self.weapon_hp == 0:
                                            self.weapon = 0
                                            time.sleep(1)
                                            print("\nYou have exhausted your weapon.\n")
                                            Player.ask_weapon(self)
                                            time.sleep(1)
                                    wave += 1
                                    self.points += 50
                                    print(
                                        "You get rid of the crabs. Your weapon's health goes "
                                        "down for a wave of crabs by "
                                        "the way.")
                            if "Blessed flower" in self.items:
                                if "Strong juice" in self.items:
                                    if not self.dead and self.health < 200:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 200:
                                            self.health = 200
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                                else:
                                    if not self.dead and self.health < 100:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 100:
                                            self.health = 100
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                            if self.poisoned and not self.dead:
                                self.health -= 3
                                if self.health > 0:
                                    time.sleep(2)
                                    if "Mute button" in self.items:
                                        print(
                                            f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                    else:
                                        print(
                                            f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                                else:
                                    self.dead = True
                                    time.sleep(1)
                                    if "Mute button" in self.items:
                                        print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                    else:
                                        print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                    Player.revive(self)
                    if not self.dead:
                        if wave == 4 and if_wave4 == 1:
                            time.sleep(2)
                            bomb_if = False
                            while not bomb_if:
                                try:
                                    bomb = int(input(
                                        f"\nAnother wave of crabs. Last one I promise. This one needs "
                                        f"60 attack . You now have"
                                        f" {self.attack} + {self.weapon}.\n"
                                        f"A bomb (You have {self.bombs}) should do the job as "
                                        f"well.\n(1)bomb\n(2)straight up attack "))
                                    assert (bomb in range(1, 3))
                                    if bomb in range(1, 3):
                                        bomb_if = True
                                except:
                                    print("\nDidn't type a number properly, try again.")
                            if bomb == 1:
                                if self.bombs > 0:
                                    self.bombs -= 1
                                    wave += 1
                                    print("Boom! That worked out great!")
                                    self.points += 60
                                else:
                                    self.dead = True
                                    print("You throw a bo.. wait you have none. Bye bye.")
                            elif bomb == 2:
                                Player.ask_weapon(self)
                                if (self.attack + self.weapon) < 60:
                                    self.dead = True
                                    print("That's the end I'm afraid.")
                                else:
                                    if self.weapon_hp > 0:
                                        self.weapon_hp -= 1
                                        if self.weapon_hp == 0:
                                            self.weapon = 0
                                            time.sleep(1)
                                            print("\nYou have exhausted your weapon.\n")
                                            Player.ask_weapon(self)
                                            time.sleep(1)
                                    wave += 1
                                    self.points += 60
                                    print(
                                        "You get rid of the crabs. Your weapon's health goes down for"
                                        " a wave of crabs by "
                                        "the way.")
                            if "Blessed flower" in self.items:
                                if "Strong juice" in self.items:
                                    if not self.dead and self.health < 200:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 200:
                                            self.health = 200
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                                else:
                                    if not self.dead and self.health < 100:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 100:
                                            self.health = 100
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                            if self.poisoned and not self.dead:
                                self.health -= 3
                                if self.health > 0:
                                    time.sleep(2)
                                    if "Mute button" in self.items:
                                        print(
                                            f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                    else:
                                        print(
                                            f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                                else:
                                    self.dead = True
                                    time.sleep(1)
                                    if "Mute button" in self.items:
                                        print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                    else:
                                        print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                    Player.revive(self)
                    if not self.dead:
                        print("\nThat's all the crabs. Let's turn our focus to the main one now.")
                        time.sleep(2)
                        print("\nI'll tell you what bombs won't do anything to him he's too tough.")
                        time.sleep(2)
                        print(
                            "\nYou will most likely need to find a weak spot for some more damage since "
                            "the crab has 600 hp.")
                        time.sleep(2)
                        print("\nAround one of the shoulders or whatever the crab could have a weak spot. You can "
                              "try your luck.")
                        time.sleep(2)
                        if self.weapon2 > 0:
                            print("Last chance to switch weapons, you won't have time during the battle.\n")
                            Player.ask_weapon(self)
                        crab = 600
                        weak_spot = random.randint(1, 3)
                        turn = "y"
                        while not self.dead and crab > 0:
                            if self.health <= 99:
                                if self.potion1 > 0:
                                    Player.ask_potion(self)
                            if turn == "y":
                                atk_if = False
                                while not atk_if:
                                    try:
                                        atk = int(input(f"\nYou can attack him now ({self.attack} + {self.weapon})"
                                                        f" but you have time for one hit. The crab has {crab} hp left."
                                                        f"\n(1)attack left\n(2)attack right\n(3)just attack the front\n"
                                                        f"(4)take a potion "))
                                        assert (atk in range(1, 5))
                                        if atk in range(1, 5):
                                            atk_if = True
                                    except:
                                        print("\nDidn't type a number properly, try again.")
                                time.sleep(2)
                                if atk == 2 or atk == 1:
                                    if atk == weak_spot:
                                        dmg = (self.attack + self.weapon) * 4
                                        crab -= dmg
                                        print(f"You hit the weak spot and deal 4 times more damage! "
                                              f"({dmg}). Crab is now on {crab} hp.")
                                    elif atk != weak_spot:
                                        dmg = (self.attack + self.weapon) // 4
                                        crab -= dmg
                                        print(
                                            f"That was not the weak spot, and the place you attacked is "
                                            f"not that great. "
                                            f"({dmg}). Crab is now on {crab} hp.")
                                elif atk == 3:
                                    dmg = (self.attack + self.weapon)
                                    crab -= dmg
                                    print(f"You decide to just attack the crab head on and get your normal damage in! "
                                          f"({dmg}). Crab is now on {crab} hp.")
                                elif atk == 4:
                                    Player.ask_potion(self)
                            elif turn == "c":
                                df_if = False
                                while not df_if:
                                    try:
                                        df = int(input(
                                            "\nNow it's the crab's turn to attack. If you try to dodge you "
                                            "have a good chance\n"
                                            "to avoid most attacks. If you try to deflect you may lose more "
                                            "health but also"
                                            f"\nget some damage done on defense. (Your health is {self.health})"
                                            f"\n(1)dodge\n(2)deflect "))
                                        assert (df in range(1, 3))
                                        if df in range(1, 3):
                                            df_if = True
                                    except:
                                        print("\nDidn't type a number properly, try again.")
                                time.sleep(2)
                                if df == 1:
                                    dodge = random.randint(1, 5)
                                    if dodge != 1:
                                        self.health -= 5
                                        if self.health <= 0:
                                            self.dead = True
                                            print("\nYou have died to the Giant Crab.")
                                            Player.revive(self)
                                        else:
                                            print(
                                                "\nYou do a good job dodging, but the crab clipped you a little"
                                                " once for 5 "
                                                "damage"
                                                f".\nYou are now on {self.health} hp.")
                                    elif dodge == 1:
                                        self.health -= 27
                                        if self.health > 0:
                                            print("You try dodging, but the crab gets the better of you "
                                                  "and strikes you for 27 damage.\nThis was the worst outcome. "
                                                  "Now you are on"
                                                  f" {self.health} hp")
                                        else:
                                            self.dead = True
                                            print("You have died to the Giant Crab.")
                                            Player.revive(self)
                                elif df == 2:
                                    dmg = (self.attack + self.weapon) // 2
                                    crab -= dmg
                                    hp_down = random.randint(19, 25)
                                    self.health -= hp_down
                                    if self.health > 0:
                                        print(
                                            f"You block, deflect left and right, and get {dmg} damage in, "
                                            f"the crab is now on"
                                            f" {crab},\nbut the crab took {hp_down} from you, now you have "
                                            f"{self.health}.")
                                    else:
                                        self.dead = True
                                        print("You have died to the Giant Crab.")
                                        Player.revive(self)
                            if "Blessed flower" in self.items:
                                if "Strong juice" in self.items:
                                    if not self.dead and self.health < 200:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 200:
                                            self.health = 200
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                                else:
                                    if not self.dead and self.health < 100:
                                        time.sleep(1)
                                        self.health += 1
                                        if self.health > 100:
                                            self.health = 100
                                        if "Mute button" in self.items:
                                            print(f"\n... .... .... ...... 1 ..!")
                                        else:
                                            print("\nYou have been healed 1 hp!")
                            if self.poisoned and not self.dead:
                                self.health -= 3
                                if self.health > 0:
                                    time.sleep(2)
                                    if "Mute button" in self.items:
                                        print(
                                            f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                    else:
                                        print(
                                            f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                                else:
                                    self.dead = True
                                    time.sleep(1)
                                    if "Mute button" in self.items:
                                        print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                    else:
                                        print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                    Player.revive(self)
                            time.sleep(2)
                            turn = "c" if turn == "y" else "y"
                        if not self.dead:
                            self.points += 600
                            print("You have defeated the Giant Crab, congratulations!")
                            time.sleep(2)
        else:
            time.sleep(3)
            print("\nThe ground around you starts opening and now it's water.")
            time.sleep(2)
            print("\nA hell of a lot of crabs start to crawl out and head towards you. Your turn!")
            time.sleep(2)
            wave = 1
            if_wave2 = random.randint(1, 5)
            if_wave3 = random.randint(1, 5)
            if_wave4 = random.randint(1, 6)
            bomb_if = False
            while not bomb_if:
                try:
                    bomb = int(input(
                        f"\nYou can just straight up try attacking them, but you'll need 30 total attack. You now have"
                        f" {self.attack} + {self.weapon}.\nA bomb (You have {self.bombs}) "
                        f"should do the job as well.\n(1)bomb\n(2)straight up attack "))
                    assert (bomb in range(1, 3))
                    if bomb in range(1, 3):
                        bomb_if = True
                except:
                    print("\nDidn't type a number properly, try again.")
            if bomb == 1:
                if self.bombs > 0:
                    self.bombs -= 1
                    wave += 1
                    print("Boom! That worked out great!")
                else:
                    self.dead = True
                    print("You throw a bo.. wait you have none. Bye bye.")
            elif bomb == 2:
                Player.ask_weapon(self)
                if (self.attack + self.weapon) < 30:
                    self.dead = True
                    print("That's the end I'm afraid.")
                else:
                    if self.weapon_hp > 0:
                        self.weapon_hp -= 1
                        if self.weapon_hp == 0:
                            self.weapon = 0
                            time.sleep(1)
                            print("\nYou have exhausted your weapon.\n")
                            Player.ask_weapon(self)
                            time.sleep(1)
                    wave += 1
                    print("You get rid of the crabs. Your weapon's health goes down for a wave of crabs by the way.")
            if "Blessed flower" in self.items:
                if "Strong juice" in self.items:
                    if not self.dead and self.health < 200:
                        time.sleep(1)
                        self.health += 1
                        if self.health > 200:
                            self.health = 200
                        if "Mute button" in self.items:
                            print(f"\n... .... .... ...... 1 ..!")
                        else:
                            print("\nYou have been healed 1 hp!")
                else:
                    if not self.dead and self.health < 100:
                        time.sleep(1)
                        self.health += 1
                        if self.health > 100:
                            self.health = 100
                        if "Mute button" in self.items:
                            print(f"\n... .... .... ...... 1 ..!")
                        else:
                            print("\nYou have been healed 1 hp!")
            if self.poisoned and not self.dead:
                self.health -= 3
                if self.health > 0:
                    time.sleep(2)
                    if "Mute button" in self.items:
                        print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                    else:
                        print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                else:
                    self.dead = True
                    time.sleep(1)
                    if "Mute button" in self.items:
                        print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                    else:
                        print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                    Player.revive(self)
            if not self.dead:
                self.points += 30
                if wave == 2 and if_wave2 != 5:
                    time.sleep(2)
                    bomb_if = False
                    while not bomb_if:
                        try:
                            bomb = int(
                                input(
                                    f"\nAnother wave of crabs turns up, but you'll need 40 attack this time. You now "
                                    f"have"
                                    f" {self.attack} + {self.weapon}.\nA bomb (You have {self.bombs}) should "
                                    f"do the job as well.\n(1)bomb\n(2)straight up attack "))
                            assert (bomb in range(1, 3))
                            if bomb in range(1, 3):
                                bomb_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    if bomb == 1:
                        if self.bombs > 0:
                            self.bombs -= 1
                            wave += 1
                            print("Boom! That worked out great!")
                            self.points += 40
                        else:
                            self.dead = True
                            print("You throw a bo.. wait you have none. Bye bye.")
                    elif bomb == 2:
                        Player.ask_weapon(self)
                        if (self.attack + self.weapon) < 40:
                            self.dead = True
                            print("That's the end I'm afraid.")
                        else:
                            if self.weapon_hp > 0:
                                self.weapon_hp -= 1
                                if self.weapon_hp == 0:
                                    self.weapon = 0
                                    time.sleep(1)
                                    print("\nYou have exhausted your weapon.\n")
                                    Player.ask_weapon(self)
                                    time.sleep(1)
                            wave += 1
                            self.points += 40
                            print(
                                "You get rid of the crabs. Your weapon's health goes down for a wave of crabs by "
                                "the way.")
                    if "Blessed flower" in self.items:
                        if "Strong juice" in self.items:
                            if not self.dead and self.health < 200:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 200:
                                    self.health = 200
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                        else:
                            if not self.dead and self.health < 100:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 100:
                                    self.health = 100
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                    if self.poisoned and not self.dead:
                        self.health -= 3
                        if self.health > 0:
                            time.sleep(2)
                            if "Mute button" in self.items:
                                print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                            else:
                                print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                        else:
                            self.dead = True
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                            else:
                                print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                            Player.revive(self)
            if not self.dead:
                if wave == 3 and if_wave3 in range(1, 3):
                    time.sleep(2)
                    bomb_if = False
                    while not bomb_if:
                        try:
                            bomb = int(input(f"\nYou guessed it. More crabs. 50 attack please. You now have"
                                             f" {self.attack} + {self.weapon}.\n"
                                             f"A bomb (You have {self.bombs}) should do the job as "
                                             f"well.\n(1)bomb\n(2)straight up attack "))
                            assert (bomb in range(1, 3))
                            if bomb in range(1, 3):
                                bomb_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    if bomb == 1:
                        if self.bombs > 0:
                            self.bombs -= 1
                            wave += 1
                            print("Boom! That worked out great!")
                            self.points += 50
                        else:
                            self.dead = True
                            print("You throw a bo.. wait you have none. Bye bye.")
                    elif bomb == 2:
                        Player.ask_weapon(self)
                        if (self.attack + self.weapon) < 50:
                            self.dead = True
                            print("That's the end I'm afraid.")
                        else:
                            if self.weapon_hp > 0:
                                self.weapon_hp -= 1
                                if self.weapon_hp == 0:
                                    self.weapon = 0
                                    time.sleep(1)
                                    print("\nYou have exhausted your weapon.\n")
                                    Player.ask_weapon(self)
                                    time.sleep(1)
                            wave += 1
                            self.points += 50
                            print(
                                "You get rid of the crabs. Your weapon's health goes down for a wave of crabs by "
                                "the way.")
                    if "Blessed flower" in self.items:
                        if "Strong juice" in self.items:
                            if not self.dead and self.health < 200:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 200:
                                    self.health = 200
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                        else:
                            if not self.dead and self.health < 100:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 100:
                                    self.health = 100
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                    if self.poisoned and not self.dead:
                        self.health -= 3
                        if self.health > 0:
                            time.sleep(2)
                            if "Mute button" in self.items:
                                print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                            else:
                                print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                        else:
                            self.dead = True
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                            else:
                                print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                            Player.revive(self)
            if not self.dead:
                if wave == 4 and if_wave4 == 1:
                    time.sleep(2)
                    bomb_if = False
                    while not bomb_if:
                        try:
                            bomb = int(input(
                                f"\nAnother wave of crabs. Last one I promise. This one needs 60 attack . You now have"
                                f" {self.attack} + {self.weapon}.\n"
                                f"A bomb (You have {self.bombs}) should do the job as "
                                f"well.\n(1)bomb\n(2)straight up attack "))
                            assert (bomb in range(1, 3))
                            if bomb in range(1, 3):
                                bomb_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    if bomb == 1:
                        if self.bombs > 0:
                            self.bombs -= 1
                            wave += 1
                            print("Boom! That worked out great!")
                            self.points += 60
                        else:
                            self.dead = True
                            print("You throw a bo.. wait you have none. Bye bye.")
                    elif bomb == 2:
                        Player.ask_weapon(self)
                        if (self.attack + self.weapon) < 60:
                            self.dead = True
                            print("That's the end I'm afraid.")
                        else:
                            if self.weapon_hp > 0:
                                self.weapon_hp -= 1
                                if self.weapon_hp == 0:
                                    self.weapon = 0
                                    time.sleep(1)
                                    print("\nYou have exhausted your weapon.\n")
                                    Player.ask_weapon(self)
                                    time.sleep(1)
                            wave += 1
                            self.points += 60
                            print(
                                "You get rid of the crabs. Your weapon's health goes down for a wave of crabs by "
                                "the way.")
                    if "Blessed flower" in self.items:
                        if "Strong juice" in self.items:
                            if not self.dead and self.health < 200:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 200:
                                    self.health = 200
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                        else:
                            if not self.dead and self.health < 100:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 100:
                                    self.health = 100
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                    if self.poisoned and not self.dead:
                        self.health -= 3
                        if self.health > 0:
                            time.sleep(2)
                            if "Mute button" in self.items:
                                print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                            else:
                                print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                        else:
                            self.dead = True
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                            else:
                                print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                            Player.revive(self)
            if not self.dead:
                print("\nThat's all the crabs. Let's turn our focus to the main one now.")
                time.sleep(2)
                print("\nI'll tell you what bombs won't do anything to him he's too tough.")
                time.sleep(2)
                print("\nYou will most likely need to find a weak spot for some more damage since the crab has 600 hp.")
                time.sleep(2)
                print("\nAround one of the shoulders or whatever the crab could have a weak spot. You can "
                      "try your luck.")
                time.sleep(2)
                if self.weapon2 > 0:
                    print("Last chance to switch weapons, you won't have time during the battle.\n")
                    Player.ask_weapon(self)
                crab = 600
                weak_spot = random.randint(1, 3)
                turn = "y"
                while not self.dead and crab > 0:
                    if self.health <= 99:
                        if self.potion1 > 0:
                            Player.ask_potion(self)
                    if turn == "y":
                        atk_if = False
                        while not atk_if:
                            try:
                                atk = int(input(f"\nYou can attack him now ({self.attack} + {self.weapon})"
                                                f" but you have time for one hit. The crab has {crab} hp left."
                                                f"\n(1)attack left\n(2)attack right\n(3)just attack the front\n"
                                                f"(4)take a potion "))
                                assert (atk in range(1, 5))
                                if atk in range(1, 5):
                                    atk_if = True
                            except:
                                print("\nDidn't type a number properly, try again.")
                        time.sleep(2)
                        if atk == 2 or atk == 1:
                            if atk == weak_spot:
                                dmg = (self.attack + self.weapon) * 4
                                crab -= dmg
                                print(f"You hit the weak spot and deal 4 times more damage! "
                                      f"({dmg}). Crab is now on {crab} hp.")
                            elif atk != weak_spot:
                                dmg = (self.attack + self.weapon) // 4
                                crab -= dmg
                                print(f"That was not the weak spot, and the place you attacked is not that great. "
                                      f"({dmg}). Crab is now on {crab} hp.")
                        elif atk == 3:
                            dmg = (self.attack + self.weapon)
                            crab -= dmg
                            print(f"You decide to just attack the crab head on and get your normal damage in! "
                                  f"({dmg}). Crab is now on {crab} hp.")
                        elif atk == 4:
                            Player.ask_potion(self)
                    elif turn == "c":
                        df_if = False
                        while not df_if:
                            try:
                                df = int(input(
                                    "\nNow it's the crab's turn to attack. If you try to dodge you have a good chance\n"
                                    "to avoid most attacks. If you try to deflect you may lose more health but also"
                                    f"\nget some damage done on defense. (Your health is {self.health})"
                                    f"\n(1)dodge\n(2)deflect "))
                                assert (df in range(1, 3))
                                if df in range(1, 3):
                                    df_if = True
                            except:
                                print("\nDidn't type a number properly, try again.")
                        time.sleep(2)
                        if df == 1:
                            dodge = random.randint(1, 5)
                            if dodge != 1:
                                self.health -= 5
                                if self.health <= 0:
                                    self.dead = True
                                    print("\nYou have died to the Giant Crab.")
                                    Player.revive(self)
                                else:
                                    print(
                                        "\nYou do a good job dodging, but the crab clipped you a little once for 5 "
                                        "damage"
                                        f".\nYou are now on {self.health} hp.")
                            elif dodge == 1:
                                self.health -= 27
                                if self.health > 0:
                                    print("You try dodging, but the crab gets the better of you "
                                          "and strikes you for 27 damage.\nThis was the worst outcome. Now you are on"
                                          f" {self.health} hp")
                                else:
                                    self.dead = True
                                    print("You have died to the Giant Crab.")
                                    Player.revive(self)
                        elif df == 2:
                            dmg = (self.attack + self.weapon) // 2
                            crab -= dmg
                            hp_down = random.randint(19, 25)
                            self.health -= hp_down
                            if self.health > 0:
                                print(f"You block, deflect left and right, and get {dmg} damage in, the crab is now on"
                                      f" {crab},\nbut the crab took {hp_down} from you, now you have {self.health}.")
                            else:
                                self.dead = True
                                print("You have died to the Giant Crab.")
                                Player.revive(self)
                    if "Blessed flower" in self.items:
                        if "Strong juice" in self.items:
                            if not self.dead and self.health < 200:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 200:
                                    self.health = 200
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                        else:
                            if not self.dead and self.health < 100:
                                time.sleep(1)
                                self.health += 1
                                if self.health > 100:
                                    self.health = 100
                                if "Mute button" in self.items:
                                    print(f"\n... .... .... ...... 1 ..!")
                                else:
                                    print("\nYou have been healed 1 hp!")
                    if self.poisoned and not self.dead:
                        self.health -= 3
                        if self.health > 0:
                            time.sleep(2)
                            if "Mute button" in self.items:
                                print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                            else:
                                print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                        else:
                            self.dead = True
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                            else:
                                print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                            Player.revive(self)
                    time.sleep(2)
                    turn = "c" if turn == "y" else "y"
                if not self.dead:
                    self.points += 600
                    print("You have defeated the Giant Crab, congratulations!")
                    time.sleep(2)

    def goblin_shaman(self):
        if "Portable black hole" in self.items and self.black_hole:
            if self.black_hole:
                time.sleep(1)
                hole_if = False
                while not hole_if:
                    try:
                        hole = int(
                            input("You can use your black hole to insta-kill the Goblin shaman\n(1)do it\n(2)save it "))
                        assert (hole in range(1, 3))
                        if hole in range(1, 3):
                            hole_if = True
                    except:
                        print("Didn't type a number properly.")
                if hole == 1:
                    self.black_hole = False
                    input(
                        "\nYou throw the black hole as it sucks the shaman in it and it disappears right after. (x) ")
                    self.points += 700
                    print("\n\nYou have defeated the goblin shaman! Well played!")
                    time.sleep(2)
                else:
                    print("\nOkay, moving on.")
                    time.sleep(2)
                    input(
                        "This will be a tricky fight as the shaman has only 90 hp but has some tricks up his "
                        "sleeve.(x) ")
                    if self.health < 200 and self.potion1 > 0:
                        Player.ask_potion(self)
                    shaman = 75
                    time.sleep(1)
                    print("There goes the shaman with his shaman-igans (pun added after update"
                          ") as he starts powering up a spell...\n")
                    time.sleep(3)
                    action_if = False
                    while not action_if:
                        try:
                            action = int(input(
                                "Smoke begins appearing around him, he might become invisible for you.\n(1)rush him"
                                "\n(2)keep your distance "))
                            assert (action in range(1, 3))
                            if action in range(1, 3):
                                action_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    if action == 1:
                        if self.weapon == 0:
                            time.sleep(1)
                            input("You rush the goblins shaman and he laughs as the smoke was actually bait.\n"
                                  "He swipes his hand and tries to erase your weapon but misses as you "
                                  "had no weapon equipped!"
                                  "\n(x) ")
                            time.sleep(1)
                            shaman -= self.attack
                            print(f"His mishit allow you to get a hit back for {self.attack} damage as you laugh back!")
                            Player.ask_weapon(self)
                        elif self.weapon > 0:
                            self.weapon = 0
                            self.weapon_hp = 0
                            self.health -= 5
                            if self.health > 0:
                                time.sleep(1)
                                input("You rush the goblins shaman and he laughs as the smoke was actually bait.\n"
                                      "What he accomplishes is he swipes with his now glowing (goblin) hand and "
                                      "erases your weapon and that also results in -5 health for you!\n(x) ")
                                Player.ask_weapon(self)
                            else:
                                time.sleep(1)
                                print("You rush the goblins shaman and he laughs as the smoke was actually bait.\n"
                                      "What he accomplishes is he swipes with his now glowing (goblin) hand and\n"
                                      "erases you from existence. Bit unfair that.")
                    elif action == 2:
                        time.sleep(1)
                        attacks = ["ice", "fire", "poison"]
                        attack = random.choice(attacks)
                        if attack == "fire":
                            self.health -= 39
                            print(
                                "The shaman completely disappears in the smoke and you are left"
                                " standing near the door.")
                            time.sleep(3)
                            if self.health > 0:
                                print(
                                    "Suddenly you get hit by some sort of fire spell and you get you of the "
                                    "way as soon\n"
                                    "as you can but it's not fast enough as you lose 39 health!")
                            else:
                                self.dead = True
                                print("The shaman burns you with a fire attack that you can't handle. Sorry.")
                                Player.revive(self)
                        elif attack == "ice":
                            self.health -= 17
                            print(
                                "The shaman completely disappears in the smoke and you are left standing "
                                "near the door.")
                            time.sleep(3)
                            if self.health > 0:
                                if "Time stone" in self.items or "Shiny necklace" in self.items:
                                    print(
                                        "Suddenly you get hit by some sort of ice spell "
                                        "and it hits you for 17 health as well"
                                        "\nas nearly freeze you. Now you have the slow effect on you... "
                                        "Wait, you don't, your\n"
                                        "item protects you from that.")
                                else:
                                    print(
                                        "Suddenly you get hit by some sort of ice spell and it hits you for 17 "
                                        "health as well"
                                        "\nas nearly freeze you. Now you have the slow effect on you so basically "
                                        "take it as "
                                        "if your attack is cut in half\n since that the most damage you'll be doing "
                                        "slowed down.")
                                    self.slowed = True
                                    if self.slowed:
                                        self.attack = self.attack // 2 + 1
                                        if self.weapon > 0:
                                            self.weapon = self.weapon // 2 + 1
                                        if self.weapon2 > 0:
                                            self.weapon2 = self.weapon2 // 2 + 1
                            else:
                                self.dead = True
                                print("The shaman uses an ice attack and freezes you to death.")
                                Player.revive(self)
                        elif attack == "poison":
                            self.poisoned = True
                            self.health -= 9
                            print(
                                "The shaman completely disappears in the smoke and you are left standing near "
                                "the door.")
                            time.sleep(3)
                            if self.health > 0:
                                print("Suddenly you get hit by some sort of a... poison spell and it hits you "
                                      "for only 3 health but this feels like a powerful poison, it will hurt"
                                      "\n you for the duration of this fight as well.")
                                if "Shiny necklace" in self.items:
                                    self.poisoned = False
                                    time.sleep(1)
                                    print("Shiny necklace says no to the poison!")
                            else:
                                self.dead = True
                                print("The shaman uses a poison to kill you. Not great.")
                                Player.revive(self)
                    time.sleep(2)
                    turn = "y"
                    while shaman > 0 and not self.dead:
                        if turn == "y":
                            atk_if = False
                            while not atk_if:
                                try:
                                    atk = int(input(
                                        "\nThe shaman feels a bit tired from his last attack and you might have an "
                                        "opening\n"
                                        f"here. (You have {self.health} hp and he has {shaman})\n(1)attack for "
                                        f"{self.attack + self.weapon}\n(2)play safe an wait it out.\n(3)drink potion"
                                        f" if you have one "))
                                    assert (atk in range(1, 4))
                                    if atk in range(1, 4):
                                        atk_if = True
                                except:
                                    print("\nDidn't type a number properly, try again.")
                            tired = [False, True, False, False, True, False, True]
                            shaman_tired = random.choice(tired)
                            if atk == 1:
                                if shaman_tired:
                                    shaman -= self.attack + self.weapon
                                    print(
                                        f"\nYou hit him for {self.attack + self.weapon} but some sort of auto-teleport "
                                        f"activates and he is now at the other side of the room.")
                                elif not shaman_tired:
                                    dmg = random.randint(8, 13)
                                    self.health -= dmg
                                    print(
                                        "\nYou try to hit him but he regains his powers back just in time to teleport "
                                        "himself"
                                        f"\naway before dealing {dmg} damage to you.")
                                    if self.health <= 0:
                                        self.dead = True
                                        print("\nYou have lost the fight.")
                                        Player.revive(self)
                            elif atk == 2:
                                if shaman_tired:
                                    print(
                                        f"\nHe did not regain his powers fast enough. Maybe should have attacked "
                                        f"after all.")
                                elif not shaman_tired:
                                    print(
                                        "\nHe quickly comes back to his best. Had you attacked you might have been "
                                        "in trouble.")
                            elif atk == 3:
                                Player.ask_potion(self)
                                if shaman_tired:
                                    print(
                                        f"\nHe did not regain his powers fast enough. Maybe should have attacked "
                                        f"after all.")
                                elif not shaman_tired:
                                    print(
                                        "\nHe quickly comes back to his best. Had you attacked you might have been "
                                        "in trouble.")
                        elif turn == "s":
                            moves = ["melee", "ranged", "clones"]
                            move = random.choice(moves)
                            if move == "melee" or move == "ranged":
                                df_if = False
                                while not df_if:
                                    try:
                                        df = int(input(f"\nYou have {self.health} health and the shaman has {shaman}."
                                                       f"\nHe drops some more smoke and you expect an attack."
                                                       f"\n(1)try to counter his attack\n(2)focus on dodging "))
                                        assert (df in range(1, 3))
                                        if df in range(1, 3):
                                            df_if = True
                                    except:
                                        print("\nDidn't type a number properly, try again.")
                                if df == 1:
                                    if move == "melee":
                                        self.health -= 20
                                        if self.health > 0:
                                            dmg = (self.attack + self.weapon)
                                            shaman -= dmg
                                            print("The shaman went for a close range spell and he hits you for 20"
                                                  f"\nbut you quickly reply and hit him back for {dmg}!")
                                        else:
                                            self.dead = True
                                            print(
                                                "The shaman hits you with a close range spell and you can't handle it.")
                                            Player.revive(self)
                                    elif move == "ranged":
                                        self.health -= 25
                                        if self.health > 0:
                                            print("The shaman went for a ranged spell and he hits you for 25"
                                                  " and you didn't really dodge it and couldn't hit back. :(")
                                        else:
                                            self.dead = True
                                            print(
                                                "The shaman hits you with a long range spell and you can't handle it.")
                                            Player.revive(self)
                                elif df == 2:
                                    if move == "melee":
                                        self.health -= 10
                                        if self.health > 0:
                                            print("The shaman went for a close range spell and he hits you for 10"
                                                  f"\nbut it could have been more if you hadn't dodged some of his "
                                                  f"attacks.")
                                        else:
                                            self.dead = True
                                            print(
                                                "The shaman hits you with a close range spell and you can't handle it.")
                                            Player.revive(self)
                                    elif move == "ranged":
                                        self.health -= 5
                                        if self.health > 0:
                                            print(
                                                "The shaman went for a ranged spell and he nicks only 5 hp from you as"
                                                " you dodged most of his attacks comfortably.")
                                        else:
                                            self.dead = True
                                            print(
                                                "The shaman hits you with a long range spell and you can't handle it.")
                                            Player.revive(self)
                            elif move == "clones":
                                df_if = False
                                while not df_if:
                                    try:
                                        df = int(input(f"\nYou have {self.health} health and the shaman has {shaman}."
                                                       f"\nHe drops some more smoke and as it goes away you are "
                                                       f"attacked by..."
                                                       f"3 shaman goblins rushing at you.\nYou gotta"
                                                       f" hit one of them and hope you don't"
                                                       f" hit a clone but the shaman himself.\n"
                                                       f"\n(1)go for the left one\n(2)go for the middle\n(3)go for "
                                                       f"the right one "))
                                        assert (df in range(1, 4))
                                        if df in range(1, 4):
                                            df_if = True
                                    except:
                                        print("\nDidn't type a number properly, try again.")
                                clones = [1, 2, 3]
                                clone = random.choice(clones)
                                if df == clone:
                                    shaman -= self.attack + self.weapon
                                    print(f"\nYou make your choice and it was correct as you hit him for "
                                          f"{self.attack + self.weapon} but some sort of auto-teleport\n"
                                          f"activates and he is now at the other side of the room.")
                                elif df != clone:
                                    self.health -= 26
                                    if self.health > 0:
                                        print("\nYou make your choice and swing but the shaman you hit was the clone "
                                              "and turns to dust as the\nother two slam you for 26 hp.")
                                    else:
                                        self.dead = True
                                        print("\nYou make your choice and swing but the shaman you hit was the clone "
                                              "and turns to dust as the\nother two straight up murder you.")
                                        Player.revive(self)
                        time.sleep(3)
                        turn = "s" if turn == "y" else "y"
                        if "Blessed flower" in self.items:
                            if "Strong juice" in self.items:
                                if not self.dead and self.health < 200:
                                    time.sleep(1)
                                    self.health += 1
                                    if self.health > 200:
                                        self.health = 200
                                    if "Mute button" in self.items:
                                        print(f"\n... .... .... ...... 1 ..!")
                                    else:
                                        print("\nYou have been healed 1 hp!")
                            else:
                                if not self.dead and self.health < 100:
                                    time.sleep(1)
                                    self.health += 1
                                    if self.health > 100:
                                        self.health = 100
                                    if "Mute button" in self.items:
                                        print(f"\n... .... .... ...... 1 ..!")
                                    else:
                                        print("\nYou have been healed 1 hp!")
                        if self.poisoned and not self.dead:
                            self.health -= 3
                            if self.health > 0:
                                time.sleep(2)
                                if "Mute button" in self.items:
                                    print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                else:
                                    print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                            else:
                                self.dead = True
                                time.sleep(1)
                                if "Mute button" in self.items:
                                    print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                else:
                                    print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                Player.revive(self)
                    if not self.dead and shaman <= 0:
                        self.points += 700
                        print("\n\nYou have defeated the goblin shaman! Well played!")
                        time.sleep(2)
                    elif self.dead and shaman <= 0:
                        self.points += 600
                        print(
                            "\nBoth of you somehow end up dying and it ends as a draw.\nYou get the points, so if you "
                            "wanted them that's good, but no win for you.")
        else:
            time.sleep(2)
            input("This will be a tricky fight as the shaman has only 90 hp but has some tricks up his sleeve.(x) ")
            if self.health < 200 and self.potion1 > 0:
                Player.ask_potion(self)
            shaman = 75
            time.sleep(1)
            print("There goes the shaman with his shaman-igans (pun added after update"
                  ") as he starts powering up a spell...\n")
            time.sleep(3)
            action_if = False
            while not action_if:
                try:
                    action = int(
                        input("Smoke begins appearing around him, he might become invisible for you.\n(1)rush him"
                              "\n(2)keep your distance "))
                    assert (action in range(1, 3))
                    if action in range(1, 3):
                        action_if = True
                except:
                    print("\nDidn't type a number properly, try again.")
            if action == 1:
                if self.weapon == 0:
                    time.sleep(1)
                    input("You rush the goblins shaman and he laughs as the smoke was actually bait.\n"
                          "He swipes his hand and tries to erase your weapon but misses as you had no weapon equipped!"
                          "\n(x) ")
                    time.sleep(1)
                    shaman -= self.attack
                    print(f"His mishit allow you to get a hit back for {self.attack} damage as you laugh back!")
                    Player.ask_weapon(self)
                elif self.weapon > 0:
                    self.weapon = 0
                    self.weapon_hp = 0
                    self.health -= 5
                    if self.health > 0:
                        time.sleep(1)
                        input("You rush the goblins shaman and he laughs as the smoke was actually bait.\n"
                              "What he accomplishes is he swipes with his now glowing (goblin) hand and "
                              "erases your weapon and that also results in -5 health for you!\n(x) ")
                        Player.ask_weapon(self)
                    else:
                        time.sleep(1)
                        print("You rush the goblins shaman and he laughs as the smoke was actually bait.\n"
                              "What he accomplishes is he swipes with his now glowing (goblin) hand and\n"
                              "erases you from existence. Bit unfair that.")
            elif action == 2:
                time.sleep(1)
                attacks = ["ice", "fire", "poison"]
                attack = random.choice(attacks)
                if attack == "fire":
                    self.health -= 39
                    print("The shaman completely disappears in the smoke and you are left standing near the door.")
                    time.sleep(3)
                    if self.health > 0:
                        print("Suddenly you get hit by some sort of fire spell and you get you of the way as soon\n"
                              "as you can but it's not fast enough as you lose 39 health!")
                    else:
                        self.dead = True
                        print("The shaman burns you with a fire attack that you can't handle. Sorry.")
                        Player.revive(self)
                elif attack == "ice":
                    self.health -= 17
                    print("The shaman completely disappears in the smoke and you are left standing near the door.")
                    time.sleep(3)
                    if self.health > 0:
                        if "Time stone" in self.items or "Shiny necklace" in self.items:
                            print("Suddenly you get hit by some sort of ice spell and it hits you for 17 health as well"
                                  "\nas nearly freeze you. Now you have the slow effect on you... Wait, you don't, "
                                  "your\n"
                                  "item protects you from that.")
                        else:
                            print("Suddenly you get hit by some sort of ice spell and it hits you for 17 health as well"
                                  "\nas nearly freeze you. Now you have the slow effect on you so basically take it as "
                                  "if your attack is cut in half\n since that the most damage you'll be doing slowed "
                                  "down.")
                            self.slowed = True
                            if self.slowed:
                                self.attack = self.attack // 2 + 1
                                if self.weapon > 0:
                                    self.weapon = self.weapon // 2 + 1
                                if self.weapon2 > 0:
                                    self.weapon2 = self.weapon2 // 2 + 1
                    else:
                        self.dead = True
                        print("The shaman uses an ice attack and freezes you to death.")
                        Player.revive(self)
                elif attack == "poison":
                    self.poisoned = True
                    self.health -= 9
                    print("The shaman completely disappears in the smoke and you are left standing near the door.")
                    time.sleep(3)
                    if self.health > 0:
                        print("Suddenly you get hit by some sort of a... poison spell and it hits you "
                              "for only 3 health but this feels like a powerful poison, it will hurt"
                              "\n you for the duration of this fight as well.")
                        if "Shiny necklace" in self.items:
                            self.poisoned = False
                            time.sleep(1)
                            print("Shiny necklace says no to the poison!")
                    else:
                        self.dead = True
                        print("The shaman uses a poison to kill you. Not great.")
                        Player.revive(self)
            time.sleep(2)
            turn = "y"
            while shaman > 0 and not self.dead:
                if turn == "y":
                    atk_if = False
                    while not atk_if:
                        try:
                            atk = int(input("\nThe shaman feels a bit tired from his last attack and you might have an "
                                            "opening\n"
                                            f"here. (You have {self.health} hp and he has {shaman})\n(1)attack for "
                                            f"{self.attack + self.weapon}\n(2)play safe an wait it out.\n(3)drink "
                                            f"potion"
                                            f" if you have one "))
                            assert (atk in range(1, 4))
                            if atk in range(1, 4):
                                atk_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    tired = [False, True, False, False, True, False, True]
                    shaman_tired = random.choice(tired)
                    if atk == 1:
                        if shaman_tired:
                            shaman -= self.attack + self.weapon
                            print(f"\nYou hit him for {self.attack + self.weapon} but some sort of auto-teleport "
                                  f"activates and he is now at the other side of the room.")
                        elif not shaman_tired:
                            dmg = random.randint(8, 13)
                            self.health -= dmg
                            print("\nYou try to hit him but he regains his powers back just in time to teleport himself"
                                  f"\naway before dealing {dmg} damage to you.")
                            if self.health <= 0:
                                self.dead = True
                                print("\nYou have lost the fight.")
                                Player.revive(self)
                    elif atk == 2:
                        if shaman_tired:
                            print(f"\nHe did not regain his powers fast enough. Maybe should have attacked after all.")
                        elif not shaman_tired:
                            print(
                                "\nHe quickly comes back to his best. Had you attacked you might have been in trouble.")
                    elif atk == 3:
                        Player.ask_potion(self)
                        if shaman_tired:
                            print(f"\nHe did not regain his powers fast enough. Maybe should have attacked after all.")
                        elif not shaman_tired:
                            print(
                                "\nHe quickly comes back to his best. Had you attacked you might have been in trouble.")
                elif turn == "s":
                    moves = ["melee", "ranged", "clones"]
                    move = random.choice(moves)
                    if move == "melee" or move == "ranged":
                        df_if = False
                        while not df_if:
                            try:
                                df = int(input(f"\nYou have {self.health} health and the shaman has {shaman}."
                                               f"\nHe drops some more smoke and you expect an attack."
                                               f"\n(1)try to counter his attack\n(2)focus on dodging "))
                                assert (df in range(1, 3))
                                if df in range(1, 3):
                                    df_if = True
                            except:
                                print("\nDidn't type a number properly, try again.")
                        if df == 1:
                            if move == "melee":
                                self.health -= 20
                                if self.health > 0:
                                    dmg = (self.attack + self.weapon)
                                    shaman -= dmg
                                    print("The shaman went for a close range spell and he hits you for 20"
                                          f"\nbut you quickly reply and hit him back for {dmg}!")
                                else:
                                    self.dead = True
                                    print("The shaman hits you with a close range spell and you can't handle it.")
                                    Player.revive(self)
                            elif move == "ranged":
                                self.health -= 25
                                if self.health > 0:
                                    print("The shaman went for a ranged spell and he hits you for 25"
                                          " and you didn't really dodge it and couldn't hit back. :(")
                                else:
                                    self.dead = True
                                    print("The shaman hits you with a long range spell and you can't handle it.")
                                    Player.revive(self)
                        elif df == 2:
                            if move == "melee":
                                self.health -= 10
                                if self.health > 0:
                                    print("The shaman went for a close range spell and he hits you for 10"
                                          f"\nbut it could have been more if you hadn't dodged some of his attacks.")
                                else:
                                    self.dead = True
                                    print("The shaman hits you with a close range spell and you can't handle it.")
                                    Player.revive(self)
                            elif move == "ranged":
                                self.health -= 5
                                if self.health > 0:
                                    print("The shaman went for a ranged spell and he nicks only 5 hp from you as"
                                          " you dodged most of his attacks comfortably.")
                                else:
                                    self.dead = True
                                    print("The shaman hits you with a long range spell and you can't handle it.")
                                    Player.revive(self)
                    elif move == "clones":
                        df_if = False
                        while not df_if:
                            try:
                                df = int(input(f"\nYou have {self.health} health and the shaman has {shaman}."
                                               f"\nHe drops some more smoke and as it goes away you are attacked by..."
                                               f"3 shaman goblins rushing at you.\nYou gotta"
                                               f" hit one of them and hope you don't"
                                               f" hit a clone but the shaman himself.\n"
                                               f"\n(1)go for the left one\n(2)go for the middle\n(3)go for the "
                                               f"right one "))
                                assert (df in range(1, 4))
                                if df in range(1, 4):
                                    df_if = True
                            except:
                                print("\nDidn't type a number properly, try again.")
                        clones = [1, 2, 3]
                        clone = random.choice(clones)
                        if df == clone:
                            shaman -= self.attack + self.weapon
                            print(f"\nYou make your choice and it was correct as you hit him for "
                                  f"{self.attack + self.weapon} but some sort of auto-teleport\n"
                                  f"activates and he is now at the other side of the room.")
                        elif df != clone:
                            self.health -= 26
                            if self.health > 0:
                                print("\nYou make your choice and swing but the shaman you hit was the clone "
                                      "and turns to dust as the\nother two slam you for 26 hp.")
                            else:
                                self.dead = True
                                print("\nYou make your choice and swing but the shaman you hit was the clone "
                                      "and turns to dust as the\nother two straight up murder you.")
                                Player.revive(self)
                time.sleep(3)
                turn = "s" if turn == "y" else "y"
                if "Blessed flower" in self.items:
                    if "Strong juice" in self.items:
                        if not self.dead and self.health < 200:
                            time.sleep(1)
                            self.health += 1
                            if self.health > 200:
                                self.health = 200
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ...... 1 ..!")
                            else:
                                print("\nYou have been healed 1 hp!")
                    else:
                        if not self.dead and self.health < 100:
                            time.sleep(1)
                            self.health += 1
                            if self.health > 100:
                                self.health = 100
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ...... 1 ..!")
                            else:
                                print("\nYou have been healed 1 hp!")
                if self.poisoned and not self.dead:
                    self.health -= 3
                    if self.health > 0:
                        time.sleep(2)
                        if "Mute button" in self.items:
                            print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                        else:
                            print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                    else:
                        self.dead = True
                        time.sleep(1)
                        if "Mute button" in self.items:
                            print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                        else:
                            print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                        Player.revive(self)
            if not self.dead and shaman <= 0:
                self.points += 700
                print("\n\nYou have defeated the goblin shaman! Well played!")
                time.sleep(2)
            elif self.dead and shaman <= 0:
                self.points += 600
                print("\nBoth of you somehow end up dying and it ends as a draw.\nYou get the points, so if you "
                      "wanted them that's good, but no win for you.")

    def cold_play(self):
        print("Your enemy is...")
        time.sleep(2)
        input("Cold Play! Just a guy who casts a simple yet effective ice/freeze spell.\n(x) ")
        if "Portable black hole" in self.items and self.black_hole:
            if self.black_hole:
                time.sleep(1)
                hole_if = False
                while not hole_if:
                    try:
                        hole = int(
                            input("You can use your black hole to insta-kill Cold Play\n(1)do it\n(2)save it "))
                        assert (hole in range(1, 3))
                        if hole in range(1, 3):
                            hole_if = True
                    except:
                        print("Didn't type a number properly.")
                if hole == 1:
                    self.black_hole = False
                    input(
                        "\nYou throw the black hole as it sucks Cold Play in it and it disappears right after. (x) ")
                    self.points += 600
                    time.sleep(3)
                    print("\n\nYou have successfully defeated Cold Play, congratulations, my friend!")
                else:
                    print("\nOkay, moving on.")
                    time.sleep(0.8)
                    input("\nSo the special thing about this fight is that if you get hit a certain amount of times\n"
                          "you will be frozen to death. He is slow so you will be attacking but carefully."
                          " His health is 150.\n"
                          "Also no option for throwing a bomb since he can freeze it."
                          "\n(x) ")
                    Player.ask_weapon(self)
                    time.sleep(1)
                    freeze = random.randint(4, 6)
                    attacked = 0
                    enemy = 140
                    print("\nGood luck!")
                    while not self.dead and enemy > 0:
                        time.sleep(2)
                        attack_if = False
                        while not attack_if:
                            try:
                                attack = int(input(f"\nYou can attack him as he is not fast. You are on {self.health} "
                                                   f"hp and he is on"
                                                   f" {enemy}. You can even take a potion. There is the "
                                                   "chance of him hitting back though. \n(1)attack\n(2)take "
                                                   "potion\n(3)just defend"
                                                   " it out in case he attacks back. "))
                                assert (attack in range(1, 5))
                                if attack in range(1, 5):
                                    attack_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        counter = random.randint(1, 8)
                        time.sleep(2)
                        if attack == 1:
                            dmg = self.attack + self.weapon
                            enemy -= dmg
                            print(f"\nYou hit your enemy for {dmg} damage.")
                            time.sleep(1)
                            if enemy > 0:
                                if counter in range(4, 9):
                                    print("\nThe enemy did not react in time.")
                                elif counter == 1 or counter == 2 or counter == 3:
                                    attacked += 1
                                    self.health -= 12
                                    print("\nYour enemy hits you for 12.")
                                    time.sleep(1)
                                    if self.health > 0:
                                        if attacked == 1:
                                            if self.slowed:
                                                print("\nThis attack is supposed to slow you but you "
                                                      "are already slowed down, can't say if that is good or bad.")
                                            elif not self.slowed:
                                                if "Time stone" in self.items or "Shiny necklace" in self.items:
                                                    print(
                                                        "You should have been slowed down here but your "
                                                        "item protects you!")
                                                else:
                                                    self.slowed = True
                                                    if self.slowed:
                                                        self.attack = self.attack // 2 + 1
                                                        if self.weapon > 0:
                                                            self.weapon = self.weapon // 2 + 1
                                                        if self.weapon2 > 0:
                                                            self.weapon2 = self.weapon2 // 2 + 1
                                                    print("\nHe also applies the slow effect on you.")
                                            if "Mirror stand" in self.items:
                                                self.attack = (self.attack // 2)
                                                print(
                                                    "Your stand is frozen from the attack and you have to finish"
                                                    " the fight\n"
                                                    "with your normal attack.")
                                        elif attacked > 1:
                                            if attacked == freeze:
                                                time.sleep(2)
                                                print(
                                                    "\nYou have been frozen by Cold Play's spell. No resurrections"
                                                    " can help you"
                                                    "\nout here since you are still kinda alive but also stuck.")
                                                self.dead = True
                                                self.frozen = True
                                                Player.revive(self)
                                    else:
                                        self.dead = True
                                        print("\nYou don't have the health and have been defeated by Cold Play.")
                        elif attack == 2:
                            Player.ask_potion(self)
                            if counter in range(4, 9):
                                print("\nThe enemy did not strike back.")
                            elif counter == 1 or counter == 2 or counter == 3:
                                attacked += 1
                                self.health -= 12
                                print("\nYour enemy hits you for 12.")
                                time.sleep(1)
                                if self.health > 0:
                                    if attacked == 1:
                                        if self.slowed:
                                            print("\nThis attack is supposed to slow you but you "
                                                  "are already slowed down, can't say if that is good or bad.")
                                        elif not self.slowed:
                                            self.slowed = True
                                            if self.slowed:
                                                self.attack = self.attack // 2 + 1
                                                if self.weapon > 0:
                                                    self.weapon = self.weapon // 2 + 1
                                                if self.weapon2 > 0:
                                                    self.weapon2 = self.weapon2 // 2 + 1
                                            print("\nHe also applies the slow effect on you.")
                                    elif attacked > 1:
                                        if attacked == freeze:
                                            time.sleep(2)
                                            print(
                                                "\nYou have been frozen by Cold Play's spell. No resurrections "
                                                "can help you"
                                                "\nout here since you are still kinda alive but also stuck.")
                                            self.dead = True
                                            self.frozen = True
                                else:
                                    self.dead = True
                                    print("\nYou don't have the health and have been defeated by Cold Play.")
                        elif attack == 3:
                            time.sleep(1)
                            if counter in range(4, 9):
                                print("\nThe enemy decided not to attack so that was wrong I guess.")
                            elif counter == 1 or counter == 2 or counter == 3:
                                print(
                                    "\nThe enemy shoots a spell at you but you were aware and defend brilliantly! Yes.")
                        if "Blessed flower" in self.items:
                            if "Strong juice" in self.items:
                                if not self.dead and self.health < 200:
                                    time.sleep(1)
                                    self.health += 1
                                    if self.health > 200:
                                        self.health = 200
                                    if "Mute button" in self.items:
                                        print(f"\n... .... .... ...... 1 ..!")
                                    else:
                                        print("\nYou have been healed 1 hp!")
                            else:
                                if not self.dead and self.health < 100:
                                    time.sleep(1)
                                    self.health += 1
                                    if self.health > 100:
                                        self.health = 100
                                    if "Mute button" in self.items:
                                        print(f"\n... .... .... ...... 1 ..!")
                                    else:
                                        print("\nYou have been healed 1 hp!")
                        if self.poisoned and not self.dead:
                            self.health -= 3
                            if self.health > 0:
                                time.sleep(2)
                                if "Mute button" in self.items:
                                    print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                else:
                                    print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                            else:
                                self.dead = True
                                time.sleep(1)
                                if "Mute button" in self.items:
                                    print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                else:
                                    print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                Player.revive(self)
                    if not self.dead and enemy <= 0:
                        self.points += 600
                        time.sleep(3)
                        print("\n\nYou have successfully defeated Cold Play, congratulations, my friend!")
                        if "Mirror stand" in self.items:
                            self.attack = self.attack * 2
                            print("Your stand is free again.")
        else:
            input("\nSo the special thing about this fight is that if you get hit a certain amount of times\n"
                  "you will be frozen to death. He is slow so you will be attacking but carefully. His health is 150.\n"
                  "Also no option for throwing a bomb since he can freeze it."
                  "\n(x) ")
            Player.ask_weapon(self)
            time.sleep(1)
            freeze = random.randint(4, 6)
            attacked = 0
            enemy = 140
            print("\nGood luck!")
            while not self.dead and enemy > 0:
                time.sleep(2)
                attack_if = False
                while not attack_if:
                    try:
                        attack = int(input(f"\nYou can attack him as he is not fast. You are on {self.health} "
                                           f"hp and he is on"
                                           f" {enemy}. You can even take a potion. There is the "
                                           "chance of him hitting back though. \n(1)attack\n(2)take potion\n(3)just "
                                           "defend"
                                           " it out in case he attacks back. "))
                        assert (attack in range(1, 5))
                        if attack in range(1, 5):
                            attack_if = True
                    except:
                        print("\nDidn't type a proper number.")
                counter = random.randint(1, 8)
                time.sleep(2)
                if attack == 1:
                    dmg = self.attack + self.weapon
                    enemy -= dmg
                    print(f"\nYou hit your enemy for {dmg} damage.")
                    time.sleep(1)
                    if enemy > 0:
                        if counter in range(4, 9):
                            print("\nThe enemy did not react in time.")
                        elif counter == 1 or counter == 2 or counter == 3:
                            attacked += 1
                            self.health -= 12
                            print("\nYour enemy hits you for 12.")
                            time.sleep(1)
                            if self.health > 0:
                                if attacked == 1:
                                    if self.slowed:
                                        print("\nThis attack is supposed to slow you but you "
                                              "are already slowed down, can't say if that is good or bad.")
                                    elif not self.slowed:
                                        if "Time stone" in self.items or "Shiny necklace" in self.items:
                                            print("You should have been slowed down here but your item protects you!")
                                        else:
                                            self.slowed = True
                                            if self.slowed:
                                                self.attack = self.attack // 2 + 1
                                                if self.weapon > 0:
                                                    self.weapon = self.weapon // 2 + 1
                                                if self.weapon2 > 0:
                                                    self.weapon2 = self.weapon2 // 2 + 1
                                            print("\nHe also applies the slow effect on you.")
                                    if "Mirror stand" in self.items:
                                        self.attack = (self.attack // 2)
                                        print("Your stand is frozen from the attack and you have to finish the fight\n"
                                              "with your normal attack.")
                                elif attacked > 1:
                                    if attacked == freeze:
                                        time.sleep(2)
                                        print(
                                            "\nYou have been frozen by Cold Play's spell. No resurrections can help"
                                            " you"
                                            "\nout here since you are still kinda alive but also stuck.")
                                        self.dead = True
                                        self.frozen = True
                                        Player.revive(self)
                            else:
                                self.dead = True
                                print("\nYou don't have the health and have been defeated by Cold Play.")
                elif attack == 2:
                    Player.ask_potion(self)
                    if counter in range(4, 9):
                        print("\nThe enemy did not strike back.")
                    elif counter == 1 or counter == 2 or counter == 3:
                        attacked += 1
                        self.health -= 12
                        print("\nYour enemy hits you for 12.")
                        time.sleep(1)
                        if self.health > 0:
                            if attacked == 1:
                                if self.slowed:
                                    print("\nThis attack is supposed to slow you but you "
                                          "are already slowed down, can't say if that is good or bad.")
                                elif not self.slowed:
                                    self.slowed = True
                                    if self.slowed:
                                        self.attack = self.attack // 2 + 1
                                        if self.weapon > 0:
                                            self.weapon = self.weapon // 2 + 1
                                        if self.weapon2 > 0:
                                            self.weapon2 = self.weapon2 // 2 + 1
                                    print("\nHe also applies the slow effect on you.")
                            elif attacked > 1:
                                if attacked == freeze:
                                    time.sleep(2)
                                    print("\nYou have been frozen by Cold Play's spell. No resurrections can help you"
                                          "\nout here since you are still kinda alive but also stuck.")
                                    self.dead = True
                                    self.frozen = True
                        else:
                            self.dead = True
                            print("\nYou don't have the health and have been defeated by Cold Play.")
                elif attack == 3:
                    time.sleep(1)
                    if counter in range(4, 9):
                        print("\nThe enemy decided not to attack so that was wrong I guess.")
                    elif counter == 1 or counter == 2 or counter == 3:
                        print("\nThe enemy shoots a spell at you but you were aware and defend brilliantly! Yes.")
                if "Blessed flower" in self.items:
                    if "Strong juice" in self.items:
                        if not self.dead and self.health < 200:
                            time.sleep(1)
                            self.health += 1
                            if self.health > 200:
                                self.health = 200
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ...... 1 ..!")
                            else:
                                print("\nYou have been healed 1 hp!")
                    else:
                        if not self.dead and self.health < 100:
                            time.sleep(1)
                            self.health += 1
                            if self.health > 100:
                                self.health = 100
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ...... 1 ..!")
                            else:
                                print("\nYou have been healed 1 hp!")
                if self.poisoned and not self.dead:
                    self.health -= 3
                    if self.health > 0:
                        time.sleep(2)
                        if "Mute button" in self.items:
                            print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                        else:
                            print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                    else:
                        self.dead = True
                        time.sleep(1)
                        if "Mute button" in self.items:
                            print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                        else:
                            print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                        Player.revive(self)
            if not self.dead and enemy <= 0:
                self.points += 600
                time.sleep(3)
                print("\n\nYou have successfully defeated Cold Play, congratulations, my friend!")
                if "Mirror stand" in self.items:
                    self.attack = self.attack * 2
                    print("Your stand is free again.")

    def gladiator(self):
        if "Portable black hole" in self.items and self.black_hole:
            if self.black_hole:
                time.sleep(1)
                hole_if = False
                while not hole_if:
                    try:
                        hole = int(
                            input("You can use your black hole to destroy the arena and skip the fight."
                                  "\n(1)do it\n(2)save it "))
                        assert (hole in range(1, 3))
                        if hole in range(1, 3):
                            hole_if = True
                    except:
                        print("Didn't type a number properly.")
                if hole == 1:
                    self.black_hole = False
                    input(
                        "\nYou throw the black hole as it sucks everyone in it including the gladiator "
                        "and it disappears right after. (x) ")
                    self.points += 600
                    print("You have defeated the Gladiator, well played.")
                else:
                    print("\nOkay, moving on.")
                    time.sleep(0.7)
                    if "Mirror stand" in self.items:
                        self.attack = (self.attack // 2)
                    gladiator_atk = (self.attack + self.weapon) + 1
                    gladiator_hp = 70
                    print("You step into an arena. How did they build that in here.")
                    time.sleep(1)
                    skip_if = False
                    while not skip_if:
                        try:
                            skip = int(
                                input("A lot of text before the fight, if you've seen it already you can skip it."
                                      "\n(1)skip\n(2)display the text "))
                            assert (skip in range(1, 3))
                            if skip in range(1, 3):
                                skip_if = True
                        except:
                            print("\nDidn't type a proper number.")
                    if skip != 1:
                        time.sleep(2)
                        print("It's just like in the movies (because I lack creativity).")
                        time.sleep(2)
                        print("\n-Welcome, fellow adventurers. Welcome, dear spectators!")
                        time.sleep(2)
                        print("...Today we are here to witness the duel between these two brave gladiators!")
                        time.sleep(2)
                        print("...They will fight to death. The winner shall receive freedom.")
                        time.sleep(2)
                        print("\nYour opponent turns to you.")
                        time.sleep(2)
                        print("\n-Don't think we are trapped here or something. We fight for the win here.")
                        time.sleep(2)
                        print("...I will show you no mercy and I expect no mercy from you. "
                              "I believe our battle will be one for the ages.")
                        time.sleep(4)
                        print("...Good luck my friend.")
                        time.sleep(1)
                        print(
                            "Announcer again:\n-Before we begin the match, you have to know that you will be "
                            "allowed only"
                            " one weapon.")
                        time.sleep(2)
                        print("...This is your last chance to pick your weapon. Choose wisely.")
                        if "Mirror stand" in self.items:
                            time.sleep(2)
                            print("...And no stands. (Meaning you lose your 3x attack boost just for this fight.")
                    swap = random.randint(1, 2)
                    if swap == 1 and self.weapon2 > 0:
                        gladiator_atk = (self.weapon2 + self.attack) + 10
                        print("Your opponent has changed his weapon.")
                        time.sleep(2)
                    Player.ask_weapon(self)
                    Player.ask_potion(self)
                    time.sleep(1)
                    turn = "y"
                    time.sleep(1)
                    print(
                        "The duel shall now begin. It will be turn based, because I lack creativity. Your opponent's "
                        "attack is"
                        f" {gladiator_atk} and his health is 70.")
                    time.sleep(2)
                    while not self.dead and gladiator_hp > 0:
                        if turn == "y":
                            atk_if = False
                            while not atk_if:
                                try:
                                    atk = int(
                                        input(
                                            f"\nYou are on the attack now. (Your health is {self.health} and your "
                                            f"opponent has"
                                            f" {gladiator_hp})\n(1)attack from the left\n(2)attack from the right"
                                            f"\n(3)attack from the middle "))
                                    assert (atk in range(1, 4))
                                    if atk in range(1, 4):
                                        atk_if = True
                                except:
                                    print("\nDidn't type a number properly, try again.")
                            weak_side = random.randint(1, 3)
                            if atk == weak_side:
                                chance = random.randint(1, 2)
                                if chance == 1:
                                    dmg = (self.attack + self.weapon)
                                    gladiator_hp -= dmg
                                    print("Your opponent does a terrible job defending and you get the full damage in"
                                          f" ({dmg}). He is now on {gladiator_hp} hp.")
                                elif chance == 2:
                                    dmg = (self.attack + self.weapon) // 2
                                    gladiator_hp -= dmg
                                    print("Your opponent barely defends. You get half your damage in"
                                          f" ({dmg}) He is now on {gladiator_hp} hp.")
                            elif atk != weak_side:
                                counter = random.randint(1, 3)
                                if counter == 1:
                                    dmg = (self.attack + self.weapon) // 4
                                    reflect = gladiator_atk // 2
                                    gladiator_hp -= dmg
                                    if gladiator_hp > 0:
                                        self.health -= reflect
                                    if self.health > 0:
                                        print(f"You attack and get {dmg} damage in but your opponent simultaneously"
                                              f" attacks you and you lose {reflect}.\n(You are now on {self.health} "
                                              f"and he"
                                              f" is on {gladiator_hp})")
                                    else:
                                        self.dead = True
                                        print("Your opponent counters your attack and finishes you.")
                                        Player.revive(self)
                                elif counter == 2 or counter == 3:
                                    dmg = random.randint(1, 3)
                                    gladiator_hp -= dmg
                                    print(f"You attack and get only {dmg} damage because you opponent defends expertly."
                                          f" (He is now on {gladiator_hp} hp).")
                        elif turn == "g":
                            df_if = False
                            while not df_if:
                                try:
                                    df = int(input(
                                        f"\nYour turn to defend! What is the plan? (You have {self.health} hp "
                                        f"and your opponent "
                                        f"has {gladiator_hp})"
                                        "\n(1)counter\n(2)just focus on the defense "))
                                    assert (df in range(1, 3))
                                    if df in range(1, 3):
                                        df_if = True
                                except:
                                    print("\nDidn't type a number properly, try again.")
                            if df == 1:
                                chance = random.randint(1, 3)
                                if chance == 1:
                                    reflect = (self.attack + self.weapon) // 2
                                    dmg = gladiator_atk // 4
                                    self.health -= dmg
                                    if self.health > 0:
                                        gladiator_hp -= reflect
                                        print(f"He attacks and gets {dmg} damage in but you counter him successfully "
                                              f"and get {reflect} damage on him.\n(You are now on {self.health} and he"
                                              f" is on {gladiator_hp})")
                                    else:
                                        self.dead = True
                                        print("Your opponent finishes you off.")
                                else:
                                    dmg = gladiator_atk
                                    self.health -= dmg
                                    if self.health > 0:
                                        print(f"You fail to counter him and take the full {dmg} damage. Ouch.\n"
                                              f"(You are now on {self.health} hp)")
                                    else:
                                        self.dead = True
                                        print("Your opponent finishes you off.")
                                        Player.revive(self)
                            elif df == 2:
                                chance = random.randint(1, 3)
                                if chance == 1:
                                    dmg = gladiator_atk // 2
                                    self.health -= dmg
                                    if self.health > 0:
                                        print(f"You don't defend very well and take {dmg} damage.\n"
                                              f"(You are now on {self.health} hp)")
                                    else:
                                        self.dead = True
                                        print("Your opponent finishes you off.")
                                        Player.revive(self)
                                else:
                                    dmg = random.randint(1, 3)
                                    self.health -= dmg
                                    if self.health > 0:
                                        print(f"You defend neatly and take only {dmg} damage.\n"
                                              f"(You are now on {self.health} hp)")
                                    else:
                                        self.dead = True
                                        print("Your opponent finishes you off.")
                                        Player.revive(self)
                        if "Blessed flower" in self.items:
                            if "Strong juice" in self.items:
                                if not self.dead and self.health < 200:
                                    time.sleep(1)
                                    self.health += 1
                                    if self.health > 200:
                                        self.health = 200
                                    if "Mute button" in self.items:
                                        print(f"\n... .... .... ...... 1 ..!")
                                    else:
                                        print("\nYou have been healed 1 hp!")
                            else:
                                if not self.dead and self.health < 100:
                                    time.sleep(1)
                                    self.health += 1
                                    if self.health > 100:
                                        self.health = 100
                                    if "Mute button" in self.items:
                                        print(f"\n... .... .... ...... 1 ..!")
                                    else:
                                        print("\nYou have been healed 1 hp!")
                        if self.poisoned and not self.dead:
                            self.health -= 3
                            if self.health > 0:
                                time.sleep(2)
                                if "Mute button" in self.items:
                                    print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                                else:
                                    print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                            else:
                                self.dead = True
                                time.sleep(1)
                                if "Mute button" in self.items:
                                    print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                                else:
                                    print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                                Player.revive(self)
                        time.sleep(3)
                        turn = "g" if turn == "y" else "y"
                    if gladiator_hp <= 0:
                        time.sleep(2)
                        print("Your opponent falls. Before you get a chance to kill him or spare him"
                              " he just stabs himself in the chest.\nAnyway... Congratulations on your victory, "
                              "your are free"
                              " from the arena!")
                        self.points += 600
                        if "Mirror stand" in self.items:
                            self.attack = self.attack * 2
                            time.sleep(0.7)
                            print("\nYou get your stand back.")
        else:
            if "Mirror stand" in self.items:
                self.attack = (self.attack // 2)
            gladiator_atk = (self.attack + self.weapon) + 1
            gladiator_hp = 70
            print("You step into an arena. How did they build that in here.")
            time.sleep(1)
            skip_if = False
            while not skip_if:
                try:
                    skip = int(input("A lot of text before the fight, if you've seen it already you can skip it."
                                     "\n(1)skip\n(2)display the text "))
                    assert (skip in range(1, 3))
                    if skip in range(1, 3):
                        skip_if = True
                except:
                    print("\nDidn't type a proper number.")
            if skip != 1:
                time.sleep(2)
                print("It's just like in the movies (because I lack creativity).")
                time.sleep(2)
                print("\n-Welcome, fellow adventurers. Welcome, dear spectators!")
                time.sleep(2)
                print("...Today we are here to witness the duel between these two brave gladiators!")
                time.sleep(2)
                print("...They will fight to death. The winner shall receive freedom.")
                time.sleep(2)
                print("\nYour opponent turns to you.")
                time.sleep(2)
                print("\n-Don't think we are trapped here or something. We fight for the win here.")
                time.sleep(2)
                print("...I will show you no mercy and I expect no mercy from you. "
                      "I believe our battle will be one for the ages.")
                time.sleep(4)
                print("...Good luck my friend.")
                time.sleep(1)
                print("Announcer again:\n-Before we begin the match, you have to know that you will be allowed only"
                      " one weapon.")
                time.sleep(2)
                print("...This is your last chance to pick your weapon. Choose wisely.")
                if "Mirror stand" in self.items:
                    time.sleep(2)
                    print("...And no stands. (Meaning you lose your 3x attack boost just for this fight.")
            swap = random.randint(1, 2)
            if swap == 1 and self.weapon2 > 0:
                gladiator_atk = (self.weapon2 + self.attack) + 10
                print("Your opponent has changed his weapon.")
                time.sleep(2)
            Player.ask_weapon(self)
            Player.ask_potion(self)
            time.sleep(1)
            turn = "y"
            time.sleep(1)
            print(
                "The duel shall now begin. It will be turn based, because I lack creativity. Your opponent's attack is"
                f" {gladiator_atk} and his health is 70.")
            time.sleep(2)
            while not self.dead and gladiator_hp > 0:
                if turn == "y":
                    atk_if = False
                    while not atk_if:
                        try:
                            atk = int(
                                input(
                                    f"\nYou are on the attack now. (Your health is {self.health} and your opponent has"
                                    f" {gladiator_hp})\n(1)attack from the left\n(2)attack from the right"
                                    f"\n(3)attack from the middle "))
                            assert (atk in range(1, 4))
                            if atk in range(1, 4):
                                atk_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    weak_side = random.randint(1, 3)
                    if atk == weak_side:
                        chance = random.randint(1, 2)
                        if chance == 1:
                            dmg = (self.attack + self.weapon)
                            gladiator_hp -= dmg
                            print("Your opponent does a terrible job defending and you get the full damage in"
                                  f" ({dmg}). He is now on {gladiator_hp} hp.")
                        elif chance == 2:
                            dmg = (self.attack + self.weapon) // 2
                            gladiator_hp -= dmg
                            print("Your opponent barely defends. You get half your damage in"
                                  f" ({dmg}) He is now on {gladiator_hp} hp.")
                    elif atk != weak_side:
                        counter = random.randint(1, 3)
                        if counter == 1:
                            dmg = (self.attack + self.weapon) // 4
                            reflect = gladiator_atk // 2
                            gladiator_hp -= dmg
                            if gladiator_hp > 0:
                                self.health -= reflect
                            if self.health > 0:
                                print(f"You attack and get {dmg} damage in but your opponent simultaneously"
                                      f" attacks you and you lose {reflect}.\n(You are now on {self.health} and he"
                                      f" is on {gladiator_hp})")
                            else:
                                self.dead = True
                                print("Your opponent counters your attack and finishes you.")
                                Player.revive(self)
                        elif counter == 2 or counter == 3:
                            dmg = random.randint(1, 3)
                            gladiator_hp -= dmg
                            print(f"You attack and get only {dmg} damage because you opponent defends expertly."
                                  f" (He is now on {gladiator_hp} hp).")
                elif turn == "g":
                    df_if = False
                    while not df_if:
                        try:
                            df = int(input(
                                f"\nYour turn to defend! What is the plan? (You have {self.health} hp and your"
                                f" opponent "
                                f"has {gladiator_hp})"
                                "\n(1)counter\n(2)just focus on the defense "))
                            assert (df in range(1, 3))
                            if df in range(1, 3):
                                df_if = True
                        except:
                            print("\nDidn't type a number properly, try again.")
                    if df == 1:
                        chance = random.randint(1, 3)
                        if chance == 1:
                            reflect = (self.attack + self.weapon) // 2
                            dmg = gladiator_atk // 4
                            self.health -= dmg
                            if self.health > 0:
                                gladiator_hp -= reflect
                                print(f"He attacks and gets {dmg} damage in but you counter him successfully "
                                      f"and get {reflect} damage on him.\n(You are now on {self.health} and he"
                                      f" is on {gladiator_hp})")
                            else:
                                self.dead = True
                                print("Your opponent finishes you off.")
                        else:
                            dmg = gladiator_atk
                            self.health -= dmg
                            if self.health > 0:
                                print(f"You fail to counter him and take the full {dmg} damage. Ouch.\n"
                                      f"(You are now on {self.health} hp)")
                            else:
                                self.dead = True
                                print("Your opponent finishes you off.")
                                Player.revive(self)
                    elif df == 2:
                        chance = random.randint(1, 3)
                        if chance == 1:
                            dmg = gladiator_atk // 2
                            self.health -= dmg
                            if self.health > 0:
                                print(f"You don't defend very well and take {dmg} damage.\n"
                                      f"(You are now on {self.health} hp)")
                            else:
                                self.dead = True
                                print("Your opponent finishes you off.")
                                Player.revive(self)
                        else:
                            dmg = random.randint(1, 3)
                            self.health -= dmg
                            if self.health > 0:
                                print(f"You defend neatly and take only {dmg} damage.\n"
                                      f"(You are now on {self.health} hp)")
                            else:
                                self.dead = True
                                print("Your opponent finishes you off.")
                                Player.revive(self)
                if "Blessed flower" in self.items:
                    if "Strong juice" in self.items:
                        if not self.dead and self.health < 200:
                            time.sleep(1)
                            self.health += 1
                            if self.health > 200:
                                self.health = 200
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ...... 1 ..!")
                            else:
                                print("\nYou have been healed 1 hp!")
                    else:
                        if not self.dead and self.health < 100:
                            time.sleep(1)
                            self.health += 1
                            if self.health > 100:
                                self.health = 100
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ...... 1 ..!")
                            else:
                                print("\nYou have been healed 1 hp!")
                if self.poisoned and not self.dead:
                    self.health -= 3
                    if self.health > 0:
                        time.sleep(2)
                        if "Mute button" in self.items:
                            print(f"\n... ...... .... ... .. ... .... 3 .. ... ... ... .... .. {self.health}")
                        else:
                            print(f"\nThe poison hits you as you lose 3 hp and you are down to {self.health}")
                    else:
                        self.dead = True
                        time.sleep(1)
                        if "Mute button" in self.items:
                            print(f"\n. .... .. ...... ..... 3 .. .... ... ... ....'. ...... .. .... ....")
                        else:
                            print("\nA tick of poison takes 3 hp from you and that's enough to kill you.")
                        Player.revive(self)
                time.sleep(3)
                turn = "g" if turn == "y" else "y"
            if gladiator_hp <= 0:
                time.sleep(2)
                print("Your opponent falls. Before you get a chance to kill him or spare him"
                      " he just stabs himself in the chest.\nAnyway... Congratulations on your victory, your are free"
                      " from the arena!")
                self.points += 600
                if "Mirror stand" in self.items:
                    self.attack = self.attack * 2
                    time.sleep(1)
                    print("\nYou get your stand back")

    def fight(self, action, i, u):
        if action == 1:
            Player.attack(self, i, u)
        elif action == 2:
            if i == "Sonic the hedgehog":
                self.dead = True
            elif i == "creator":
                self.dead = True
                self.frozen = True
                print("No.")
                Player.revive(self)
            else:
                Player.ram(self, i, u)
        elif action == 3:
            if i == "Sonic the hedgehog":
                self.dead = True
            elif i == "creator":
                self.dead = True
                self.frozen = True
                print("No.")
                Player.revive(self)
            else:
                Player.run_away(self)
                self.skipped = True
        elif action == 4:
            if "Portable black hole" in self.items:
                self.black_hole = False
            self.dead = True
            self.given_up = True
            self.points -= 100
            if "Mute button" in self.items:
                print(f"...., ...'.. ...... .. ... .... .. ....... ... . ... .. ......, ..")
            else:
                print("Okay, you're giving up but that is costing you a ton of points, gg")

    def attack(self, i, u):
        if self.bombs > 0:
            bomb_if = False
            while not bomb_if:
                try:
                    bomb = int(input("You can use a bomb if you want (clears all enemies)\n(1)yes\n(2)no "))
                    assert (bomb in range(1, 3))
                    if bomb in range(1, 3):
                        bomb_if = True
                except:
                    print("Didn't type a number properly.")
            if bomb == 1:
                if i != "Subaru":
                    self.bombs -= 1
                self.points += math.floor(u * 1.5)
                print(f"You used a bomb, the {i} couldn't make it. That was easy.")
            elif bomb == 2:
                if self.weapon2 > 0:
                    equip_if = False
                    while not equip_if:
                        try:
                            equip = int(input("Do you want to equip your second weapon?\n(1)yes\n(2)no "))
                            assert (equip in range(1, 3))
                            if equip in range(1, 3):
                                equip_if = True
                        except:
                            print("Didn't type a number properly.")
                    if equip == 1:
                        if i != "Subaru":
                            Player.equip_weapon(self)
                if self.attack + self.weapon < u:
                    self.dead = True
                    print(f"Your attack is not strong enough, you have died to the {i}")
                else:
                    v = math.floor(math.pow(u, 0.5) - math.pow((self.attack + self.weapon), 0.25))
                    if "Belt" in self.items:
                        v = 0
                    if v > 0:
                        if i != "Subaru":
                            self.health -= v
                        if "Mute button" in self.items:
                            print(f"... .... ...... ... {i}, ... ... .... {v} ...... .. ... ........")
                        else:
                            print(f"You have killed the {i}, but you lost {v} health in the process.")
                        if i == "snakes":
                            poison = random.randint(1, 2)
                            if poison == 1:
                                self.poisoned = True
                                print("You have been poisoned by one of the snakes.")
                                if "Shiny necklace" in self.items:
                                    self.poisoned = False
                                    time.sleep(1)
                                    print("Shiny necklace says no to the poison!")
                        if i == "zombies":
                            self.cursed = True
                            print("You have been cursed by the zombies.")
                            if "Shiny necklace" in self.items:
                                self.cursed = False
                                time.sleep(1)
                                print("Shiny necklace says no to the curse!")
                    elif v <= 0:
                        if "Mute button" in self.items:
                            print(f".... ...... .. .... ......, ... .... ... {i} ...........")
                        else:
                            print(f"Your attack is good enough, you kill the {i} flawlessly.")
                    if i == "sonic the hedgehog":
                        self.points += 420
                    else:
                        if i != "Subaru":
                            self.points += math.floor(u * 1.5)
                    if self.health <= 0:
                        self.dead = True
                        print("Your health is too low even for attacking, you have died :/")
                        if self.dead:
                            Player.revive(self)
                    else:
                        if self.weapon_hp > 0:
                            if i != "Subaru":
                                self.weapon_hp -= 1
                                if self.weapon_hp == 0:
                                    self.weapon = 0
                                    time.sleep(1)
                                    print("\nYou have exhausted your weapon.\n")
                                    Player.ask_weapon(self)
                                    time.sleep(1)
                        time.sleep(1)
        else:
            if self.weapon2 > 0:
                equip_if = False
                while not equip_if:
                    try:
                        equip = int(input("Do you want to equip your second weapon?\n(1)yes\n(2)no "))
                        assert (equip in range(1, 3))
                        if equip in range(1, 3):
                            equip_if = True
                    except:
                        print("Didn't type a number properly.")
                if equip == 1:
                    if i != "Subaru":
                        Player.equip_weapon(self)
            if self.attack + self.weapon < u:
                self.dead = True
                print(f"Your attack is not strong enough, you have died to {i}")
            else:
                v = math.floor(math.pow(u, 0.5) - math.pow((self.attack + self.weapon), 0.25))
                if "Belt" in self.items:
                    v = 0
                if v > 0:
                    if i != "Subaru":
                        self.health -= v
                    if "Mute button" in self.items:
                        print(f"... .... ...... ... {i}, ... ... .... {v} ...... .. ... ........")
                    else:
                        print(f"You have killed the {i}, but you lost {v} health in the process.")
                    if i == "snakes":
                        poison = random.randint(1, 2)
                        if poison == 1:
                            self.poisoned = True
                            print("You have been poisoned by one of the snakes.")
                            if "Shiny necklace" in self.items:
                                self.poisoned = False
                                time.sleep(1)
                                print("Shiny necklace says no to the poison!")
                    if i == "zombies":
                        self.cursed = True
                        print("You have been cursed by the zombies.")
                        if "Shiny necklace" in self.items:
                            self.cursed = False
                            time.sleep(1)
                            print("Shiny necklace says no to the curse!")
                elif v <= 0:
                    if "Mute button" in self.items:
                        print(f".... ...... .. .... ......, ... .... ... {i} ...........")
                    else:
                        print(f"Your attack is good enough, you kill the {i} flawlessly.")
                if i == "sonic the hedgehog":
                    self.points += 420
                else:
                    if i != "Subaru":
                        self.points += (u * 2)
                if self.health <= 0:
                    self.dead = True
                    print("Your health is too low even for attacking, you have died :/")
                    if self.dead:
                        Player.revive(self)
                else:
                    if self.weapon_hp > 0:
                        if i != "Subaru":
                            self.weapon_hp -= 1
                            if self.weapon_hp == 0:
                                self.weapon = 0
                                time.sleep(1)
                                print("\nYou have exhausted your weapon.\n")
                                Player.ask_weapon(self)
                                time.sleep(1)
                    time.sleep(1)
        rand_loot = random.randint(1, 12)
        time.sleep(2)
        if not self.dead and not self.trap:
            if i != "Subaru" and i != "creator":
                if rand_loot in range(5, 10):
                    coins = random.randint(1, u // 2)
                    self.coins += coins
                    if "Mute button" in self.items:
                        print(f"... {i} ....... {coins} ....(.).")
                    else:
                        print(f"The {i} dropped {coins} coin(s).")
                elif rand_loot == 10:
                    potion = random.randint(10, 25)
                    if "Mute button" in self.items:
                        print(f"... {i} ....... . ...... .... ..... {potion}.")
                    else:
                        print(f"The {i} dropped a potion that heals {potion}.")
                    Player.take_potion(self, potion)
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        Player.ask_potion(self)
                elif rand_loot == 11:
                    if "Mute button" in self.items:
                        print(f"... {i} ....... . ...... .....! ...'. ... .... .. ....")
                    else:
                        print(f"The {i} dropped a wooden chest! Let's see what it has.")
                    Player.open_chest(self, 0)
                elif rand_loot == 12:
                    chest = random.randint(0, 1)
                    if chest == 0:
                        open_if = False
                        while not open_if:
                            try:
                                open_chest = int(
                                    input(
                                        f"You kill the {i} and find a silver chest!\n(1)open it - 1 key\n(2)leave it "))
                                assert (open_chest in range(1, 3))
                                if open_chest in range(1, 3):
                                    open_if = True
                            except:
                                print("Didn't type a number properly.")
                        if open_chest == 1:
                            Player.open_chest(self, 1)
                    elif chest == 1:
                        open_if = False
                        while not open_if:
                            try:
                                open_chest = int(
                                    input(
                                        f"You kill the {i} and find a golden chest!\n(1)open it "
                                        f"- 2 keys\n(2)leave it "))
                                assert (open_chest in range(1, 3))
                                if open_chest in range(1, 3):
                                    open_if = True
                            except:
                                print("Didn't type a number properly.")
                        if open_chest == 1:
                            Player.open_chest(self, 2)

    def ram(self, i, u):
        if "Light trainers" in self.items:
            v = 0
        else:
            v = math.floor(math.pow(u, 0.5) * 2.5)
        self.health -= v
        if self.health <= 0:
            self.dead = True
            print("\n*sobbing\nWe don have da capaciti.")
        else:
            if "Light trainers" in self.items:
                if "Mute button" in self.items:
                    print("... .... .. ...... :D")
                else:
                    print("You lost no health :D")
            else:
                if "Mute button" in self.items:
                    print(f"... ....... .. ... ....... ... {i}, ... ... .... {v} ...... .. ..... ...")
                else:
                    print(f"You managed to run through the {i}, but you lost {v} health in doing so.")
            time.sleep(1)
            if self.double:
                self.double_enemy.append(i)
                self.double_enemy.append(v)
                print("\nIf you try to run away from the second room you'll lose the same amount of health as now\n"
                      f"because you'd have to run past the {i} again.")

    def run_away(self):
        if "Light trainers" not in self.items:
            self.health -= 3
        if self.health <= 0:
            self.dead = True
            print("Why did you try running when you are pretty much a corpse fam, what did you expect?")
        else:
            self.skipped = True
            self.points -= 50
            if "Mute button" in self.items:
                print("... .... ....... .. ... ...., ... .... .......")
            else:
                print("You have managed to run away, but lost points.")
            if len(self.double_enemy) == 2:
                self.health -= self.double_enemy[-1]
                if self.health <= 0:
                    self.dead = True
                    print(f"\nBack in the first room {self.double_enemy[0]} waited for you at the door\n"
                          f"and killed you. Dang these double rooms.")
                else:
                    if "Light trainers" in self.items:
                        print("No health lost for running around :D")
                    else:
                        print(f"\nYou also lose health for running past {self.double_enemy[0]} again.")
                    self.double_enemy.clear()

    def play(self):
        print("\n")
        time.sleep(1)
        while not self.dead:
            Player.print_stats(self)
            input("(x)")
            max_hp = 100
            if "Strong juice" in self.items:
                max_hp = 200
            if self.health < max_hp:
                if self.potion1 > 0:
                    Player.ask_potion(self)
            time.sleep(1)
            if "Mute button" in self.items:
                print(f"\n.... ....: {self.rooms_cleared + 1}")
            else:
                print(f"\nNext room: {self.rooms_cleared + 1}")
            if self.rooms_cleared % 5 == 4:
                if self.rooms_cleared % 10 == 9:
                    boss = random.randint(1, 4)
                    if boss in range(3, 5) and self.rooms_cleared >= 19:
                        valid = False
                        while not valid:
                            try:
                                if "Mute button" in self.items:
                                    command = int(input("\n..'. . .... .. . .... ....!! .. ... ...... ... ... .. ..?"
                                                        " (.. ....... ...., .. ...... ..!)"
                                                        "\n(1)..., ..... \n(2).. "))
                                else:
                                    command = int(input("\nIt's a door to a boss room!! Do you reckon you can do it"
                                                        "? (No running away, no giving up!)"
                                                        "\n(1)yes, enter \n(2)no "))
                                if command == 1:
                                    print("\nHere we go then.\n")
                                    Player.boss_room(self)
                                    time.sleep(3)
                                    valid = True
                                elif command == 2:
                                    print("You skip it, but I don't blame you.")
                                    self.skipped = True
                                    valid = True
                                if not valid:
                                    print("Didn't type 1 or 2 or sth went wrong, try again")
                            except ValueError:
                                print("Didn't type 1 or 2 or sth went wrong, try again")
                    else:
                        safe = random.randint(1, 4)
                        if safe == 1:
                            use_if = False
                            while not use_if:
                                try:
                                    use_key = int(input("You see a door to a safe room but it's locked."
                                                        "\n(1)Unlock with a key\n(2)skip "))
                                    assert (use_key in range(1, 3))
                                    if use_key in range(1, 3):
                                        use_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if use_key == 1:
                                if self.keys > 0:
                                    self.keys -= 1
                                    safe_random = random.randint(1, 3)
                                    if safe_random == 1:
                                        Player.item_room(self)
                                    elif safe_random == 2:
                                        Player.shop(self)
                                    elif safe_random == 3:
                                        Player.empty_room(self)
                                elif self.keys == 0:
                                    self.safe_skipped = True
                                    print("Not counting safe rooms as skipped!")
                            elif use_key == 2:
                                self.safe_skipped = True
                                if self.keys == 0:
                                    print("I won't count the room as skipped since you had no choice really")
                                if self.keys > 0:
                                    print("I will not take points since you skipped a safe room, but you miss out on\n"
                                          "whatever was in there.")
                        else:
                            if "Shiny necklace" in self.items:
                                rand = random.randint(0, 299)
                            else:
                                rand = random.randint(0, 300)
                            if 0 <= rand <= 240:
                                valid = False
                                while not valid:
                                    try:
                                        command = int(input("\nYou see a door, do you want to enter?\nyes(1)\nno(2) "))
                                        if command == 1:
                                            print("\nYou enter the room.")
                                            Player.enter_room(self)
                                            time.sleep(3)
                                            valid = True
                                        elif command == 2:
                                            print("You skipped it, you coward, less points for you.")
                                            self.points -= 20
                                            self.skipped = True
                                            valid = True
                                        if not valid:
                                            print("Didn't type 1 or 2 or sth went wrong, try again")
                                    except ValueError:
                                        print("Didn't type 1 or 2 or sth went wrong, try again")
                            elif rand == 300:
                                if "Mute button" in self.items:
                                    print("... .... ......... . ...... .... .. ... ....... ... ......... .... .... ...."
                                          ", ... ........ . .... ....... ....'. ... .....?")
                                else:
                                    print("You have triggered a secret trap in the hallway and instantly die. Well done"
                                          ", you unlocked a rare ending. Aren't you happy?")
                                self.points = -420
                                self.dead = True
                            elif rand in range(241, 300):
                                Player.double_room(self)
                else:
                    use_if = False
                    while not use_if:
                        try:
                            use_key = int(input("You see a door to a safe room but it's locked."
                                                "\n(1)Unlock with a key\n(2)skip "))
                            assert (use_key in range(1, 3))
                            if use_key in range(1, 3):
                                use_if = True
                        except:
                            print("Didn't type a number properly.")
                    if use_key == 1:
                        if self.keys > 0:
                            self.keys -= 1
                            safe_random = random.randint(1, 5)
                            if safe_random == 1 or safe_random == 2:
                                Player.item_room(self)
                            elif safe_random == 4 or safe_random == 5:
                                Player.shop(self)
                            elif safe_random == 3:
                                Player.empty_room(self)
                        elif self.keys == 0:
                            self.safe_skipped = True
                            print("Why did you click 1, you have no keys, we are skipping it anyway."
                                  "\n(Why did I ask the question then?)")
                    elif use_key == 2:
                        self.safe_skipped = True
                        if self.keys == 0:
                            print("I won't count the room as skipped since you had no choice really")
                        if self.keys > 0:
                            print("I will not take points since you skipped a safe room, but you miss out on\n"
                                  "whatever was in there.")
            else:
                if "Shiny necklace" in self.items:
                    rand = random.randint(0, 299)
                else:
                    rand = random.randint(0, 300)
                if 0 <= rand <= 234:
                    valid = False
                    while not valid:
                        try:
                            if "Mute button" in self.items:
                                command = int(input("\n... ... . ...., .. ... .... .. .....?\n...(1)\n..(2) "))
                            else:
                                command = int(input("\nYou see a door, do you want to enter?\nyes(1)\nno(2) "))
                            if command == 1:
                                print("\nYou enter the room.")
                                Player.enter_room(self)
                                time.sleep(3)
                                valid = True
                            elif command == 2:
                                if "Mute button" in self.items:
                                    print("... ....... .., ... ......, .... ...... ... ....")
                                else:
                                    print("You skipped it, you coward, less points for you.")
                                self.points -= 20
                                self.skipped = True
                                valid = True
                            if not valid:
                                print("Didn't type 1 or 2 or sth went wrong, try again")
                        except ValueError:
                            print("Didn't type 1 or 2 or sth went wrong, try again")
                elif rand in range(235, 240):
                    valid = False
                    while not valid:
                        try:
                            if "Mute button" in self.items:
                                command = int(input("\n..'. . .... .. . .... ....!! .. ... ...... ... ... .. ..?"
                                                    " (.. ....... ...., .. ...... ..!)"
                                                    "\n(1)..., ..... \n(2).. "))
                            else:
                                command = int(input("\nIt's a door to a boss room!! Do you reckon you can do it"
                                                    "? (No running away, no giving up!)"
                                                    "\n(1)yes, enter \n(2)no "))
                            if command == 1:
                                print("\nHere we go then.\n")
                                Player.boss_room(self)
                                time.sleep(3)
                                valid = True
                            elif command == 2:
                                print("You skip it, but I don't blame you.")
                                self.skipped = True
                                valid = True
                            if not valid:
                                print("Didn't type 1 or 2 or sth went wrong, try again")
                        except ValueError:
                            print("Didn't type 1 or 2 or sth went wrong, try again")
                elif rand == 300:
                    if "Mute button" in self.items:
                        print("... .... ......... . ...... .... .. ... ....... ... ......... .... .... ...."
                              ", ... ........ . .... ....... ....'. ... .....?")
                    else:
                        print("You have triggered a secret trap in the hallway and instantly die. Well done"
                              ", you unlocked a rare ending. Aren't you happy?")
                    self.points = -420
                    self.dead = True
                elif rand in range(240, 300):
                    Player.double_room(self)
            if self.frozen:
                break
            if self.restart:
                break
            if self.winner:
                break
            if not self.dead:
                if not self.skipped and not self.safe_skipped:
                    time.sleep(1)
                    pray = random.randint(1, 100)
                    if "Detector" in self.items:
                        rand_loot = random.randint(4, 24)
                    else:
                        rand_loot = random.randint(1, 24)
                    if "Lucky 13" in self.items:
                        rand_loot = random.randint(15, 24)
                    if rand_loot in range(0, 15):
                        if pray == 100 and self.pray:
                            self.coins += 100
                            self.pray = False
                            if "Mute button" in self.items:
                                print("... .... ....... ..... ....... ... .....")
                                time.sleep(3)
                                print("\n... ....!\n")
                                time.sleep(2)
                                print("... ...... ....... .. ... .... .... .........! ... ... 100 .....!")
                            else:
                                print("You find nothing after leaving the room.")
                                time.sleep(3)
                                print("\nBut wait!\n")
                                time.sleep(2)
                                print("You prayed earlier so the gods have responded! You get 100 coins!")
                        else:
                            if "Mute button" in self.items:
                                print("... .... ....... ..... ....... ... .....")
                            else:
                                print("\nYou find nothing after leaving the room.")
                    elif rand_loot in range(15, 20):
                        coins = random.randint(3, 6)
                        self.coins += coins
                        if "Mute button" in self.items:
                            print(f"\n....... ... .... ... .... {coins} ......")
                        else:
                            print(f"\nLeaving the room you find {coins} coins.")
                    elif rand_loot == 20:
                        self.keys += 1
                        if "Mute button" in self.items:
                            print("\n... ..... . ... ....... ... ....!")
                        else:
                            print("\nYou found a key leaving the room!")
                    elif rand_loot == 21:
                        self.bombs += 1
                        if "Mute button" in self.items:
                            print("\n... .... . ..... ..... ....... ... ....!")
                        else:
                            print("\nYou find a random bomba leaving the room!")
                    elif rand_loot == 22:
                        discounts = [10, 20, 25]
                        disc = random.choice(discounts)
                        if self.discount == 0:
                            self.discount = disc
                            if "Mute button" in self.items:
                                print(f"\n... .... . {disc}% ........ ...... .. ... ... .. ... ..... .... .....")
                            else:
                                print(f"\nYou find a {disc}% discount coupon at the end of the room. Very cool.")
                        elif self.discount > 0:
                            if disc > self.discount:
                                self.discount = disc
                                if "Mute button" in self.items:
                                    print(f"\n... .... . ...... ........({disc}%) .. ... ... .. ... .... "
                                          f"... .. ........ ....\n"
                                          f"........ ... (.... ...'. ....., .....)")
                                else:
                                    print(f"\nYou find a better discount({disc}%) at the end of the room "
                                        f"and it replaces your\n"
                                        f"previous one (they don't stack, sorry)")
                            elif disc <= self.discount:
                                if "Mute button" in self.items:
                                    print(f"\n... .... . ........ ({disc}%) .. ... ... .. ... ...., "
                                          f"... ..'. ... ...... .... .... "
                                          f"....... ...,\n.. ... ..... .. .... .... ..... ........")
                                else:
                                    print(f"\nYou find a discount ({disc}%) at the end of the room, "
                                          f"but it's not better than your "
                                          f"current one,\nso you might as well have found nothing.")
                    elif rand_loot == 23:
                        chest = random.randint(1, 10)
                        if chest in range(1, 6):
                            if "Mute button" in self.items:
                                print("\n... ..... . ...... ..... .. ... ... .. ... ....! ...'. ... .... .. ....")
                            else:
                                print("\nYou found a wooden chest at the end of the room! Let's see what it has.")
                            Player.open_chest(self, 0)
                        elif chest in range(6, 9):
                            open_if = False
                            while not open_if:
                                try:
                                    if "Mute button" in self.items:
                                        open_chest = int(input("\n... ..... . ...... ..... .. ... ... .. ... ....! "
                                                               ".. ... .... .. ...... ..?"
                                                               "\n(1)... - 1 ... ........\n(2).. "))
                                    else:
                                        open_chest = int(input("\nYou found a silver chest at the end of the room! "
                                                               "Do you want to unlock it?"
                                                               "\n(1)yes - 1 key required\n(2)no "))
                                    assert (open_chest in range(1, 3))
                                    if open_chest in range(1, 3):
                                        open_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if open_chest == 1:
                                Player.open_chest(self, 1)
                        elif chest in range(9, 11):
                            open_if = False
                            while not open_if:
                                try:
                                    if "Mute button" in self.items:
                                        open_chest = int(input("\n... ..... . ...... ..... .. ... ... .. ... ....! "
                                                               ".. ... .... .. ...... ..?"
                                                               "\n(1)... - 2 .... ........\n(2).. "))
                                    else:
                                        open_chest = int(input("\nYou found a golden chest at the end of the room! "
                                                               "Do you want to unlock it?"
                                                               "\n(1)yes - 2 keys required\n(2)no "))
                                    assert (open_chest in range(1, 3))
                                    if open_chest in range(1, 3):
                                        open_if = True
                                except:
                                    print("Didn't type a number properly.")
                            if open_chest == 1:
                                Player.open_chest(self, 2)
                    elif rand_loot == 24:
                        drink_if = False
                        while not drink_if:
                            try:
                                if "Mute button" in self.items:
                                    drink = int(input("\n... .... . ......... ..... .. ... ... .. ... ..... "
                                                      ".. ... .... .. ..... ..?"
                                                      "\n(1)...\n(2).. "))
                                else:
                                    drink = int(input("\nYou find a mysterious drink at the end of the room. "
                                                      "Do you want to drink it?"
                                                      "\n(1)yes\n(2)no "))
                                assert (drink in range(1, 3))
                                if drink in range(1, 3):
                                    drink_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if drink == 1:
                            Player.myst_drink(self)
                elif self.skipped:
                    self.rooms_skipped += 1
                    self.points -= 30
                time.sleep(2)
                self.rooms_cleared += 1
                self.points += 5
                if self.skipped or self.safe_skipped:
                    if "Mute button" in self.items:
                        print(f"\n\n.... {self.rooms_cleared} ........!!\n")
                    else:
                        print(f"\n\nRoom {self.rooms_cleared} \"passed\"!!\n")
                elif not self.skipped and not self.safe_skipped:
                    if "Mute button" in self.items:
                        print(f"\n.... {self.rooms_cleared} ......!!\n")
                    else:
                        print(f"\nRoom {self.rooms_cleared} passed!!\n")
                if "Reality stone" in self.items:
                    if self.stone < 3:
                        self.stone += 1
                        if self.stone == 3:
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n....... ..... .........\n")
                            else:
                                print("\nReality stone recharged!\n")
                                time.sleep(0.8)
                if "Restart button" in self.items:
                    if self.button:
                        restart_if = False
                        while not restart_if:
                            try:
                                restart = int(
                                    input("Do you want to restart your run (with your current items, score and"
                                          " attack)?\n(1)yes\n(2)no "))
                                assert (restart in range(1, 3))
                                if restart in range(1, 3):
                                    restart_if = True
                            except:
                                print("\nDidn't type a proper number.")
                        if restart == 1:
                            self.button = False
                            self.restart = True
                            if "Mute button" in self.items:
                                print(f".... .... .. ..")
                            else:
                                print("Okay here we go.")
                            if self.restart:
                                break
                    else:
                        restart = random.randint(1, 13)
                        if restart == 13:
                            time.sleep(1)
                            self.restart = True
                            if "Mute button" in self.items:
                                print(f".. ... ....... ...... ... ........., .. ... ........ ... .... .....!")
                            else:
                                print("Uh oh. Restart button has activated, we are starting all over again!")
                        if self.restart:
                            break
                if self.restart:
                    break
                if "Brochure" in self.items:
                    print("\n")
                    rand = random.randint(1, 110)
                    if rand == 1:
                        input("The brochure can give you a tip about not yet unlocked items! Too bad it just wasted\n"
                              "a tip on the brochure itself... (x) ")
                    elif rand == 2:
                        input("The mega bomb and golden key give you one bomb or key every 3 rooms. The giant coin\n"
                              "gives you a coin every room instead! (x) ")
                    elif rand == 3:
                        input("The time stone only protects from slow effect and the room with a watch. Actual time\n"
                              "travel is impossible (for me) to code. (x) ")
                    elif rand == 4:
                        input("Blessed flower gives 2 hp after room and 1 hp per turn at boss fights. But did you know"
                              "\nit heals you 2 hp upon picking it up? (x)")
                    elif rand == 5:
                        input("The item score gambler has 10% chance to double your score and 5% chance to make it half"
                              "\nIt also makes playing games with Brad safe and lotteries are 50% off! (x) ")
                    elif rand == 6:
                        input("The item light trainers was initially called speed shoes but that sounded stupid. (x) ")
                    elif rand == 7:
                        input("Since blessed flower heals you every turn if you can stall one certain boss fight you\n"
                              "can get infinite heals! (x) ")
                    elif rand == 8:
                        input("Broken glasses double the damage of the next weapons you pick up. You also get a\n"
                              "choice between 2 items in a box. The unpicked item stays in the item pool. (x)")
                    elif rand == 9:
                        input("Breath of air is the only item that can save you from a freeze! Also it has a 50%\n"
                              "chance to revive you a second time, both times are full heals as well, "
                              "what an item! (x) ")
                    elif rand == 10:
                        input("Detector has a hidden effect apart from telling you about secrets in walls and holes."
                              "\nIt also increases the chance of a reward after a room. (x) ")
                    elif rand == 11:
                        input("Brave juice will revive you only if you give up. Basically a situational extra life. "
                              "(x) ")
                    elif rand == 12:
                        input("Shiny necklace prevents all negative effects. But it also removes random traps in the\n"
                              "hallway and bad mysterious drink effects! Pretty versatile for an item. (x) ")
                    elif rand == 13:
                        input("The item belt makes killing enemies flawless every time. Not the best but saves\n"
                              "health in the long run. Oh and it gives you +5 attack upon picking up. (x) ")
                    elif rand == 14:
                        input("The restart button breaks after being used and will have a 1/13 chance to restart "
                              "the run \nafter a room. But its surprise "
                              "function is that it has a chance to restart even if you die. \nPotential lifeline. (x) ")
                    elif rand == 15:
                        input("Russian roulette looks like a bad item when you pick it up but it's not completely a\n"
                              "troll item. It reduces the chance of encountering a fight! (x) ")
                    elif rand == 16:
                        input("Metal and a dream is in my opinion the most boring item. It gives 2 weapons\n"
                              "and increases your base attack by 7. Not useless but boring. (x) ")
                    elif rand == 17:
                        input("Red wig looks like a troll item but it actually multiplies your final score in the end\n"
                              "by 1.3, now that is a hidden function. Hang on I just revealed it... (x) ")
                    elif rand == 18:
                        input("The item Lucky 13 is actually the 19th item on the list. It has no hidden functions,\n"
                              "100% chance of a reward after a room is good enough I even think it's too op. (x) ")
                    elif rand == 19:
                        input("The strong juice item is the "
                              "only thing that breaks the 100 health cap. I have not written\n"
                              "its code yet so please pray that I've done it properly since it will be a nightmare. "
                              "(x) ")
                    elif rand == 20:
                        input("The mute button is the real troll item. Pick it up if you want to kill your run for a"
                              " laugh. (x) ")
                    elif rand == 21:
                        input("Portable black hole kills a boss in 1 shot, it even skips the waves in a certain fight."
                              "\nThe only item with a hidden bad function. Giving up sacrifices the item. (x) ")
                    elif rand == 22:
                        input("Reality stone gives you a reroll of an item box and a reroll of a room layout, yes, a"
                              "room layout!\nIt has a 3 room cooldown though. Best item for me. (x) ")
                    elif rand == 23:
                        input("Mirror stand doubles the damage of your character (not the weapons). The item is turned"
                              "\noff for 2 certain boss fights. (x) ")
                    elif rand == 24:
                        input("Killing yourself with the cursed staff item gives a lot of points and I mean a lot.\n"
                              "The sacrifice room is even better because it does the same if you die there. (x) ")
                    elif rand == 25:
                        input("The Gladiator copies your weapon. If he switches his weapon it means he copies your\n"
                              "second weapon. You get a change of weapons after that so use it to your advantage. (x) ")
                    elif rand == 26:
                        input("The Giant Crab fight is actually very easy with any damage  a few bombs. There is a\n"
                              "small chance there is no weak spot at all so you can just hope there.")
                    elif rand == 27:
                        input("Defending against Cold Play can stall the battle for infinite turns. Bad with a poison,"
                              "\nop with a certain item ;). (x) ")
                    elif rand == 28:
                        input("Yes, the Goblin Shaman is annoying. The only advice is attack at the start if you don't"
                              "\nhave a weapon and don't attack with a weapon. Your second weapon is not erased though."
                              " (x) ")
                    elif rand == 29:
                        input("The lucky charm used to increase chance of rewards after a room but this effect is now "
                              "removed\n since a few items do it now. (x) ")
                    elif rand == 30:
                        input("If you meet the creator you can escape only by giving up or just killing him with your"
                              "\nactual attack. He freezes you like Cold Play so only one item can get you out. (x) ")
                    elif rand == 31:
                        input("If you've prayed at a temple you actually get a small chance to get revived. Also a tiny"
                              "\nchance to replace a blank reward after a room with a lot of coins! (x) ")
                    elif rand == 32:
                        input("Don't say no to Parry. (x) ")
                    elif rand == 33:
                        input("Brad can play 3 different mini games with you. You can actually make the bet with more "
                              "\nresources than you actually have! Just don't lose the game after that... (x) ")
                    elif rand == 34:
                        input("5 items are unlocked by default and 20 by getting wins. Only wins when you are not\n"
                              "playing for points count. Play for points after you unlock everything I guess. (x) ")
                    elif rand == 35:
                        input("If you see a titan go for the back of the neck. (x) ")
                    elif rand == 36:
                        input("The tips for the brochure take about 300 lines of my code I hate this item. (x) ")
                    elif rand == 37:
                        input("Always carry a bomb for the poison room. (x) ")
                    elif rand == 38:
                        input("The chance of finding an item box in a hole is 33.3% and the chance of finding a secret"
                              "\nroom behind a wall is 50%. The detector does not increase the chances, but it tells "
                              "the outcome. (x) ")
                    elif rand == 39:
                        input("Praying at a church can hurt you. Don't trust me? Try it. (x) ")
                    elif rand == 40:
                        input("The lottery is the only place where you can type any instead of the required number "
                              "and\ncontinue the game (except for \"(x)\" messages like this one of course). (x) ")
                    elif rand == 41:
                        input("You need 45 coins to escape from a corrupt politician. (x) ")
                    elif rand == 42:
                        input("If you get slowed down and then remove the slow effect you will actually get more damage"
                              "\nthan before. This was initially a mistake but I decided to leave it at that. (x) ")
                    elif rand == 43:
                        input("Extra lives revive you in the hallway if you can't kill an enemy.\nThey will try to"
                              " respawn you inside a poison room unfortunately for you to die again. (x) ")
                    elif rand == 44:
                        input("Lucky charms will try to revive you in the hallway before extra lives try to do it\n"
                              "there. Lucky charms last infinitely so this can save you a life. (x) ")
                    elif rand == 45:
                        input("If a lucky charm fails to revive you and an extra life does it instead, the lucky\n"
                              "charm remains active and will try again on the next death. (x) ")
                    elif rand == 46:
                        input("Lucky charms remove poisons and curses but not slows. They also revive you with 19 hp."
                              "\nExtra lives on the other hand revive you with 75 and remove nothing. (x) ")
                    elif rand == 47:
                        input("If you pray at a temple and then kill a cat the effect is removed. Most useless shit"
                              "\nI've ever coded. (x) ")
                    elif rand == 48:
                        input("If you have the Light Trainers the messages will still tell you that you will lose"
                              " health\nafter running. I would have to change the message literally everywhere in"
                              " the game, no thanks. (x) ")
                    elif rand == 49:
                        input("Restarting a run resets literally everything except your items, damage and points. (x) ")
                    elif rand == 50:
                        input("Your Lie in April is the only anime to make me cry. Others got close but this one, \n"
                              "bloody hell... (x) ")
                    elif rand == 51:
                        input("Do you want to look for a romcom but find pain instead? Bunny girl senpai is the anime"
                              " for you. (x) ")
                    elif rand == 52:
                        input("Do you want to look for a romcom but find existential crisis instead? Oregairu is the "
                              "anime for you. (x) ")
                    elif rand == 53:
                        input("Mushoku Tensei is a better isekai than Re:Zero, but Re:Zero is the better anime. (x) ")
                    elif rand == 54:
                        input("Your Name is a better movie than A silent voice I am ready to die on this hill. (x) ")
                    elif rand == 55:
                        input("If you haven't watched Attack on Titan yet what are you waiting for? (x) ")
                    elif rand == 56:
                        input("Bunny Girl Senpai didn't make me cry but it's the only anime that made me "
                              "violently\nsmack a pillow against a wall. Watch the series first then the movie. (x) ")
                    elif rand == 57:
                        input("I have not left the apartment in 2 weeks; help. (x) ")
                    elif rand == 58:
                        input("Mysterious drinks can do 11 different things, 6 of them good. You do the math. (x) ")
                    elif rand == 59:
                        input("If you want balance changes then too bad, I don't care anymore. (x) ")
                    elif rand == 60:
                        input("There is a 25% chance to find Parry's stick in any type of chest. (x) ")
                    elif rand == 61:
                        input("There is a chance to find a cure for your poison in chests! 20% for a silver and\n"
                              "50% for a golden. (x) ")
                    elif rand == 62:
                        input("There are 2 specific room layouts with a normal and a large box. They do not work like"
                              "\nitem boxes but rather like silver and golden chests that require bombs instead of keys"
                              " to open. (x) ")
                    elif rand == 63:
                        input("Try to save your potions because sometimes there are random heals, there are not many"
                              "\nworse feelings than getting a full heal right after drinking a potion. (x) ")
                    elif rand == 64:
                        input("There are 15 different special room layouts. 2 of them are trolls and 13 are good so"
                              " how\n am I getting troll rooms on every test run then??? aaaaaaaaaaaaaaaaaaaaaa (x) ")
                    elif rand == 65:
                        input("If you get special room layout 13 there is a 1/8 chance to get the biggest secret in\n"
                              "the game. Alternatively it gives you a lucky charm. (x) ")
                    elif rand == 66:
                        input("There are only 5 different scenarios where you can get slowed down. I haven't counted\n"
                              "poisons and curses but I think they are more common. (x) ")
                    elif rand == 67:
                        input("Your potions are automatically moved to the left if there are empty slots (like right "
                              "after\ndrinking one). (x) ")
                    elif rand == 68:
                        input("There is literally nothing difficult in the code for this game. Except for the time it\n"
                              "takes me to write it.")
                    elif rand == 69:
                        input("Score gambler makes lottery attemps cost 5 coins. If you guess one number right, you"
                              " get 6 back.\nYou see where I'm going with this? (x) ")
                    elif rand == 70:
                        input("If you take damage from snakes they have a 50% chance to poison you. The funny thing\n"
                              "is they do it even if you die (I think). (x) ")
                    elif rand == 71:
                        input("If you take damage from zombies they are guaranteed to curse you. (x) ")
                    elif rand == 72:
                        input("If you kill MrBeast he drops you a lot of money. (x) ")
                    elif rand == 73:
                        input("If you kill a samurai he drops a sword. (x)")
                    elif rand == 74:
                        input("The room with a watch in the middle freezes the run for 33 minutes and 20 seconds.\n"
                              "The only counter for this is the item Time Stone. (x) ")
                    elif rand == 75:
                        input("There is a 50% chance to get an enemy added from the first version of the game and 50%\n"
                              "chance to get one from the update. My favourite brochure tip. (x) ")
                    elif rand == 76:
                        input("Do not speedrun a manga if you don't need to. Read only 1-3 chapters a day please "
                              "trust me. (x) ")
                    elif rand == 77:
                        input("I am not watching Demon Slayer fuck you. (x) ")
                    elif rand == 78:
                        input("First half of Sword Art Online season 1 is peak anime. Season 3 is fine as well I\n"
                              "suppose but the rest is garbage. (x) ")
                    elif rand == 79:
                        input("Real men watch K-ON. (x) ")
                    elif rand == 80:
                        input("Noucome might be the most underrated romcom in all of anime. (x) ")
                    elif rand == 81:
                        input("Subaru is the most powerful anime character and there is literally no way to"
                              " argue with this. (x)")
                    elif rand == 82:
                        input("There are a lot of brochure tips about anime, what am I, a weeb? Maybe. (x)")
                    elif rand == 83:
                        input("There is a small chance of encountering a boss room, treasure room or a shop randomly."
                              " (x) ")
                    elif rand == 84:
                        input("The chance of dying from a random trap in the hallway is 0.25%. It was higher before and"
                              "\nit's one of the only things I regret about this game. With Shiny necklace the chance"
                              " is 0% though. (x) ")
                    elif rand == 85:
                        input("The game is inspired by The BInding of Isaac.")
                    elif rand == 86:
                        input("Cold Play is the 4th boss, added after the update. The unique thing about him is not the"
                              "\ndamage he deals (he deals a bit though) but the fact he can instantly kill you after"
                              " 4-6 attacks. (x) ")
                    elif rand == 87:
                        input("If you don't have the attack or a bomb, you will die if you try to attack enemies. (x) ")
                    elif rand == 88:
                        input("I set up a formula that tells you the health drained when running through an enemy.\n"
                              "I am not happy about it but it's too late to change it now. (x) ")
                    elif rand == 89:
                        input("Special tip! No tip here, but a reward, item box! Congrats on the luck hehehe. (x) ")
                        Player.item_box(self)
                    elif rand == 90:
                        input("If you see Subaru you can escape by not killing him. After the update there are no \n"
                              "consequences after attacking him but just in case leave the room. (x) ")
                    elif rand == 91:
                        input("(At least) 2 different rooms that can instantly kill you exist. Tip for the poison room:"
                              "\nIf you escape behind you, you are safe, but if you bomb the other door you get "
                              "poisoned. (x) ")
                    elif rand == 92:
                        input("Confess your feelings to your crush, even if you get rejected it doesn't feel too bad\n"
                              "because you at least tried. Only advice is maybe wait a bit longer but confess "
                              "eventually. (x) ")
                    elif rand == 93:
                        input("If you run through goblins they will steal your coins. (x) ")
                    elif rand == 94:
                        input("The manga Mieruko-chan is better than the anime, but both are worth it. "
                              "Nice series, 8.5/10. (x) ")
                    elif rand == 95:
                        input("Playing in \"custom\" game mode counts for the wins and unlocks so if you are tired\n"
                              "of the game like me just give yourself 30 damage and an item. (x) ")
                    elif rand == 96:
                        input("Playing in \"random\" game mode shuffles your stats but also gives you a small\n"
                              "chance to start with a slow, curse, poison, lucky charm or an item. (x) ")
                    elif rand == 97:
                        input("Shops only appear when you have no money and vice versa. (x) ")
                    elif rand == 98:
                        input("Special rooms are usually good but be careful. One of the layouts will restart your run"
                              ". (x) ")
                    elif rand == 99:
                        input("Giving Parry his lost stick will pay out with a very strong weapon. (x) ")
                    elif rand == 100:
                        input("Breath of air tries to revive you before your extra lives do. (x) ")
                    elif rand == 101:
                        input("Lucky charms could theoretically give you infinite lives. But it's not reliable. "
                              "\nThe only reliable thing with this ability is the item Brave juice. (x) ")
                    elif rand == 102:
                        input("There is a random chance the brochure can give you an item box instead of an item!"
                              "\nDon't sleep on it. (x) ")
                    elif rand == 103:
                        input("Shiny necklace does not literally make you immune to being cursed or poisoned. It\n"
                              "actually removes the effects right after they are applied to you. (x) ")
                    elif rand == 104:
                        input("Restarting a run is helpful for already used items: Portable black hole is available"
                              "\nagain, Reality stone cooldown is reset, but best of all, Breath of air is recharged"
                              " too! (x) ")
                    elif rand == 105:
                        input("If you reroll something with the reality stone there is the small chance of rerolling"
                              "\ninto the exact same item or room. (x) ")
                    elif rand == 106:
                        input("Mute button was supposed to turn literally every text in the game into dots but even\n"
                              "I don't have the time for that. (x) ")
                    elif rand == 107:
                        input("Score gambler gives you 100 points upon picking up, even if you start the run with it."
                              " (x) ")
                    elif rand == 108:
                        input("If you give up with brave juice you only lose 50 points, instead of the usual 100. (x) ")
                    elif rand == 109:
                        input("If you start with items that would give you stats or consumables when picked up, you'd"
                              "\nstill get that effect (most noticable with Metal and a dream or Giant coin). (x) ")
                    elif rand == 110:
                        input("The mirror stand doubles only your current damage. Any boosts you get after that do not"
                              "\nget a multiplier.")
                    print("\n")
                if "Score gambler" in self.items:
                    change = random.randint(1, 20)
                    if change in range(1, 3):
                        time.sleep(1)
                        self.points = self.points * 2
                        if "Mute button" in self.items:
                            print(f"... ..... ....... ... ....... .... ......!")
                        else:
                            print("The score gambler has doubled your points!")
                    if change == 3:
                        time.sleep(1)
                        self.points = self.points // 2
                        if "Mute button" in self.items:
                            print(f"... ..... ....... ... ...... .... ......!")
                        else:
                            print("The score gambler has halved your points!")
                self.skipped = False
                self.safe_skipped = False
                if "Giant coin" in self.items:
                    time.sleep(0.7)
                    self.coins += 1
                    if "Mute button" in self.items:
                        print(f".... ..... .... ..... ... . .... :)")
                    else:
                        print("Your giant coin gives you a coin :)")
                    time.sleep(0.7)
                if "Mega bomb" in self.items:
                    if self.rooms_cleared % 3 == 0:
                        time.sleep(1)
                        self.bombs += 1
                        if "Mute button" in self.items:
                            print(f"... .... .... ..... ... . .....")
                        else:
                            print("The mega bomb gives you a bomb.")
                        time.sleep(0.7)
                if "Golden key" in self.items:
                    if self.rooms_cleared % 3 == 1:
                        time.sleep(1)
                        self.keys += 1
                        if "Mute button" in self.items:
                            print(f"... ...... ... ..... . ... ... ....")
                        else:
                            print("The golden key drops a key for you.")
                        time.sleep(0.7)
                if self.parry:
                    parry = random.randint(1, 5)
                    if parry == 1:
                        if self.parry_item:
                            input(f"-Oh hey, {self.name}, it's Parry. You found the stick?\n(x)")
                            if "Mute button" in self.items:
                                print(f"\n... .... .. .. ....\n-....... .. .... ...... ....... ... ... . .........."
                                      f"\n\n.. ..... ... ..... ... ...........")
                            else:
                                print("\nYou hand it to him.\n-Yoooooo so cool thanks exactly the one I described."
                                      "\n\nHe waves his stick and disappears.")
                            time.sleep(7)
                            self.parry = False
                            self.parry_dead = True
                            self.points += 100
                            if "Mute button" in self.items:
                                print(f".... .. .. .. .... ....... ..... .. ... ...... .. .........??")
                            else:
                                print("Hang on is he just leaving where is the reward or something??")
                            time.sleep(5)
                            slot_if = False
                            while not slot_if:
                                try:
                                    slot = int(input("You are about to continue as you hear that voice again."
                                                     "\n\n-Oh yeah you probably want something. Have this, it "
                                                     "should carry you for a while."
                                                     "\nAn axe materializes out of thin air. "
                                                     "What? Why an axe? It looks powerful though - "
                                                     "60 damage, lasts 9 rooms.\n"
                                                     f"Don't scroll I will show you your current weapons:"
                                                     f"\nequipped: +{self.weapon} attack, {self.weapon_hp} rooms left"
                                                     f"\nslot 2: +{self.weapon2} attack, {self.weapon2_hp} rooms left"
                                                     "\n(1)equip in slot 1\n(2)slot 2"
                                                     "\n(3)leave it like a moron "))
                                    assert (slot in range(1, 4))
                                    if slot in range(1, 4):
                                        slot_if = True
                                except:
                                    print("\nDidn't type a proper number.")
                            if slot != 3:
                                Player.take_weapon(self, slot, 60, 9)
                        elif not self.parry_item:
                            if "Mute button" in self.items:
                                print(f"... ...... ..... ... ... .... .... . ..... .. .. ... .... ..... ...")
                            else:
                                print("You notice Parry but you don't have a stick rn so you just avoid him. "
                                      "Good call.")
                if "Blessed flower" in self.items:
                    max_hp = 100
                    if "Strong juice" in self.items:
                        max_hp = 200
                    if self.health < max_hp:
                        time.sleep(1)
                        self.health += 2
                        if self.health > max_hp:
                            self.health = max_hp
                        if "Mute button" in self.items:
                            print(f"\n... .... ...... 2 ..!")
                        else:
                            print("\nYou have been healed 2 hp!")
            if self.restart:
                break
            if self.poisoned and not self.dead:
                self.health -= 7
                time.sleep(1)
                if "Mute button" in self.items:
                    print(f"... ... ........ ........, .. ... ... 7 .......")
                else:
                    print("You are currently poisoned, so bye bye 7 health.")
                if self.health <= 0:
                    self.dead = True
                    if "Mute button" in self.items:
                        print(f"... ...'. ...... ... ......, ....")
                    else:
                        print("You can't handle the poison, rip.")
                if self.cursed:
                    if not self.dead:
                        kill = random.randint(1, 15)
                        if kill in range(1, 3):
                            self.dead = True
                            time.sleep(3)
                            if "Mute button" in self.items:
                                print(f"...'.. ...... ... .... ... ...... .... ......")
                            else:
                                print("You're cursed and that has killed you. Yikes.")
                time.sleep(3)
            if self.dead:
                if self.charm:
                    revive = random.randint(1, 2)
                    if revive == 1:
                        self.dead = False
                        self.health = 19
                        time.sleep(3)
                        if "Mute button" in self.items:
                            print(f"\n... .... .... ....... .. ... ....... .. .... ..... ...... ..... ... . ......!"
                                  f"\n(.. ... .... ...... ... ........ .... ......, .. ...'. "
                                  f"..... .. ....... ... ... .... ....\n.... .. ... .... ......)")
                        else:
                            print("\nYou have been revived in the hallway by your lucky charm. Lucky for a reason!"
                                  "\n(If you died inside the previous room itself, it won't "
                                  "count as cleared and the next room"
                                  "\nwill be the same number)")
                        if self.cursed:
                            self.cursed = False
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n.... .. . ... .... .. .... ..... .. ....... ......!")
                            else:
                                print("\nThis is a new life so your curse is lifted. Cheers!")
                        if self.poisoned:
                            self.poisoned = False
                            time.sleep(1)
                            if "Mute button" in self.items:
                                print(f"\n.... ... .... ....... .... ......!")
                            else:
                                print("\nYour new life cancels your poison!")
                        time.sleep(2)
                if self.dead and self.pray:
                    life = random.randint(1, 20)
                    if life == 20:
                        max_hp = 100
                        if "Strong juice" in self.items:
                            max_hp = 200
                        self.dead = False
                        self.health = max_hp
                        self.pray = False
                        if "Mute button" in self.items:
                            print(f"... ...... .. . ...... ... ... .... .... ..... ... .... ....! ...........")
                        else:
                            print("You prayed at a temple and the gods have given you life back! Unbelievable.")
            if "Brave juice" in self.items and self.given_up:
                self.points += 50
                self.dead = False
                self.given_up = False
                self.health = 50
                time.sleep(1)
                if "Mute button" in self.items:
                    print(f"\n... .... .... ....... ....... .. .... ..... .....,"
                          f". ...'. ....... ...'.. ........ ........ .... ...."
                          f"\n... .... 50 ...... .... ... ... ...... .... .......? .......")
                else:
                    print("\nYou have been revived outside by your brave juice, "
                          "I can't believe you've actually utilized this item"
                          ".\nYou have 50 health now. Can you repeat this process? Hmm...")
            if self.dead:
                if "Breath of air" in self.items:
                    time.sleep(1)
                    if self.breath == 1:
                        revive = random.randint(1, 2)
                        if revive == 1:
                            max_hp = 100
                            if "Strong juice" in self.items:
                                max_hp = 200
                            self.health = max_hp
                            self.breath -= 1
                            self.dead = False
                            if self.frozen:
                                self.frozen = False
                            if "Mute button" in self.items:
                                print(f"\n... .... .... ....... .. ... ....... .. .... ...... .. ...! .... .. ... "
                                      f".... ... .. ... ...\n.. .. ........\n")
                            else:
                                print("\nYou have been revived in the hallway by your Breath of air! This is the "
                                      "last one of the run\n"
                                      "so be careful.\n")
                    elif self.breath == 2:
                        max_hp = 100
                        if "Strong juice" in self.items:
                            max_hp = 200
                        self.health = max_hp
                        self.breath -= 1
                        self.dead = False
                        if self.frozen:
                            self.frozen = False
                        if "Mute button" in self.items:
                            print(f"\n... .... .... ....... .. ... ....... .. .... ...... .. ...! "
                                  f".... .. .... ....... .... . ......\n.. ...... ......\n")
                        else:
                            print(
                                "\nYou have been revived in the hallway by your Breath of air! "
                                "Back to full health with a chance"
                                "\nto happen again.\n")
                time.sleep(1.5)
                if self.extra_lives > 0 and not self.frozen:
                    time.sleep(2)
                    self.dead = False
                    self.health = 75
                    self.extra_lives -= 1
                    if "Mute button" in self.items:
                        print(f"\n... ........ ...... ... ..... ... ... .. ..... .... .. ... "
                              f".... .... ....... ... .... ... ........ ....... ... ..... ... ... .... 75..."
                              f"\n.... ..... ..... ... ... {self.extra_lives}")
                    else:
                        print(
                            "\nFor whatever reason you died. You had an extra live so you "
                            "have been revived but this has happened outside the room. You now have 75hp."
                            f"\nYour extra lives are now {self.extra_lives}")
            if self.dead and "Restart button" in self.items:
                restart = random.randint(1, 13)
                if restart == 13:
                    time.sleep(3)
                    self.restart = True
                    if "Mute button" in self.items:
                        print(f".. .... .... ... ...... .... ..... ..... ... ....... ...... ... .........,\n"
                              f".. ... ........ ... .... .....!")
                    else:
                        print("Oh wow. Your run should have ended here, but restart button has activated,\n"
                              "we are starting all over again!")
                if self.restart:
                    break
            if self.restart:
                break

    def the_game(self):
        msg_if = False
        while not msg_if:
            try:
                msg = int(input("Print out starting message?\n(1)yes\n(2)no "))
                assert (msg in range(1, 3))
                if msg == 1:
                    msg_if = True
                    time.sleep(2)
                    input(f"Hello there, {self.name}! You are stuck in a dungeon and you have to make your way "
                          "through rooms! \nImagine you are walking through a narrow hallway "
                          "and you see the rooms. \nWhen you clear/skip one you keep walking through "
                          "the hallway. (the rooms are not connected)."
                          "\nJust type the number required for the actions (the game will instruct you, no worries)\n"
                          "Try to escape or just survive as long as possible to get more points."
                          "\nType anything to get started! (quick note: if you "
                          "see a \"(x)\" at the end of text, type anything to move "
                          "on, like right now)\n(x) ")
                elif msg == 2:
                    msg_if = True
            except:
                print("Didn't type a proper number.")
        game_mode_if = False
        while not game_mode_if:
            try:
                game_mode = int(input("What will be your goal?\n(1)to win\n(2)play for points "))
                assert (game_mode in range(1, 3))
                if game_mode in range(1, 3):
                    game_mode_if = True
            except:
                print("Didn't type a proper number.")
        if game_mode == 2:
            self.score = True
        condition_if = False
        while not condition_if:
            try:
                condition = int(input("Choose a difficulty.\n(1)easy - start off with better base "
                                      "attack and a key\n(2)normal - base stats"
                                      "\n(3)hard - poor attack and start with half health\n(4)random\n(5)custom "))
                if condition in range(1, 6):
                    condition_if = True
                assert (condition in range(1, 6))
            except:
                print("Didn't type a proper number.")
        if condition == 1:
            self.attack = 15
            self.keys = 1
        elif condition == 3:
            self.health = 50
            self.attack = 7
        elif condition == 4:
            self.health = random.randint(65, 100)
            self.attack = random.randint(6, 20)
            curse = random.randint(1, 9)
            if curse == 1:
                self.cursed = True
            poison = random.randint(1, 9)
            if poison == 1:
                self.poisoned = True
            charm = random.randint(1, 8)
            if charm == 1:
                self.charm = True
            key = random.randint(1, 3)
            if key == 1:
                self.keys = 1
            bomb = random.randint(1, 3)
            if bomb == 1:
                self.keys = 1
            self.coins = random.randint(0, 5)
            discount = random.randint(1, 10)
            if discount == 15:
                self.discount = 20
            item = random.randint(1, 5)
            if item == 1:
                the_item = random.choice(item_pool)
                while the_item == "Russian roulette" or the_item == "Cursed staff":
                    the_item = random.choice(item_pool)
                self.items.append(the_item)
                item_pool.remove(the_item)
        elif condition == 5:
            health = int(input("\nChoose starting health. (1 - 100) "))
            if health in range(1, 101):
                self.health = health
            else:
                self.health = 50
                print("Wrong number, I'm starting you with 50.")
            attack = int(input("\nChoose starting base attack. (1 - 30) "))
            if attack in range(1, 31):
                self.attack = attack
            else:
                self.attack = 10
                print("You don't follow orders huh, enjoy the default attack.")
            curse_if = False
            while not curse_if:
                try:
                    curse = int(input("\nStart off with a curse?\n(1)yes\n(2)no "))
                    assert (curse in range(1, 3))
                    if curse in range(1, 3):
                        curse_if = True
                except:
                    print("Didn't type a proper number.")
            if curse == 1:
                self.cursed = True
            poison_if = False
            while not poison_if:
                try:
                    poison = int(input("Start off with a poison?\n(1)yes\n(2)no "))
                    assert (poison in range(1, 3))
                    if poison in range(1, 3):
                        poison_if = True
                except:
                    print("Didn't type a proper number.")
            if poison == 1:
                self.poisoned = True
            charm_if = False
            while not charm_if:
                try:
                    charm = int(input("Start off with a lucky charm?\n(1)yes\n(2)no "))
                    assert (curse in range(1, 3))
                    if charm in range(1, 3):
                        charm_if = True
                except:
                    print("Didn't type a proper number.")
            if charm == 1:
                self.charm = True
            key_if = False
            while not key_if:
                try:
                    key = int(input("Start off with a key?\n(1)yes\n(2)no "))
                    assert (key in range(1, 3))
                    if key in range(1, 3):
                        key_if = True
                except:
                    print("Didn't type a proper number.")
            if key == 1:
                self.keys = 1
            bomb_if = False
            while not bomb_if:
                try:
                    bomb = int(input("Start off with a bomb?\n(1)yes\n(2)no "))
                    assert (bomb in range(1, 3))
                    if bomb in range(1, 3):
                        bomb_if = True
                except:
                    print("Didn't type a proper number.")
            if bomb == 1:
                self.bombs = 1
            item_if = False
            while not item_if:
                try:
                    item = int(input("Start off with an item?\n(1)yes\n(2)no "))
                    assert (item in range(1, 3))
                    if item in range(1, 3):
                        item_if = True
                except:
                    print("Didn't type a proper number.")
            if item == 1:
                the_item = random.choice(item_pool)
                while the_item == "Russian roulette" or the_item == "Cursed staff":
                    the_item = random.choice(item_pool)
                self.items.append(the_item)
                item_pool.remove(the_item)
        print("Lucky Dungeon!")
        if "Belt" in self.items:
            self.attack += 5
        if "Giant coin" in self.items:
            self.coins += 25
        if "Metal and a dream" in self.items:
            self.attack += 7
            print("Your starting item is Metal and a dream so please claim your weapons.")
            time.sleep(2)
            weapon1 = random.randint(18, 60)
            weapon1_hp = random.randint(3, 7)
            take_if = False
            while not take_if:
                try:
                    take = int(input(f"If you take the first weapon you will have {weapon1} "
                                     f"attack +{self.attack} (your base attack), and it will last for "
                                     f"{weapon1_hp} rooms. "
                                     "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                     "\nyes(2) - put it in slot 2(not equipping it)\n"
                                     "Recommended to click 1 if you have no weapons "
                                     "and click 2 if you have 1 weapon.\n"
                                     "If you have 2 weapons it will replace the one you have in the slot you chose."
                                     "\nno(3) "))
                    assert (take in range(1, 4))
                    if take in range(1, 4):
                        take_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take != 3:
                Player.take_weapon(self, take, weapon1, weapon1_hp)
            weapon2 = random.randint(18, 60)
            weapon2_hp = random.randint(3, 7)
            print("\n")
            take2_if = False
            while not take2_if:
                try:
                    take2 = int(input(f"If you take the second weapon you will have {weapon2} "
                                      f"attack +{self.attack} (your base attack), and it will last for "
                                      f"{weapon2_hp} rooms. "
                                      "Do you want to take it?\nyes(1) - put it in slot 1(equip it)"
                                      "\nyes(2) - put it in slot 2(not equipping it)\n"
                                      "Recommended to click 1 if you have no weapons "
                                      "and click 2 if you have 1 weapon.\n"
                                      "If you have 2 weapons it will replace the one you have in the slot you chose."
                                      "\nno(3) "))
                    assert (take2 in range(1, 4))
                    if take2 in range(1, 4):
                        take2_if = True
                except:
                    print("\nDidn't type a proper number.")
            if take2 != 3:
                Player.take_weapon(self, take2, weapon2, weapon2_hp)
        if "Mirror stand" in self.items:
            self.attack = self.attack * 2
        if "Shiny necklace" in self.items:
            if self.cursed:
                self.cursed = False
            if self.poisoned:
                self.poisoned = False
        if "Score gambler" in self.items:
            self.points += 100
        Player.play(self)
        while self.restart:
            self.health = 100
            self.slowed = False
            self.frozen = False
            self.poisoned = False
            self.cursed = False
            self.charm = False
            self.winner = False
            self.dead = False
            self.given_up = False
            self.rooms_cleared = 0
            self.skipped = False
            self.safe_skipped = False
            self.rooms_skipped = 0
            self.coins = 0
            self.bombs = 0
            self.keys = 0
            self.discount = 0
            self.weapon = 0
            self.weapon_hp = 0
            self.weapon2 = 0
            self.weapon2_hp = 0
            self.potion1 = 0
            self.potion2 = 0
            self.potion3 = 0
            self.parry = False
            self.parry_item = False
            self.parry_enemy = False
            self.parry_dead = False
            self.brad_enemy = False
            self.brad_dead = False
            self.cat = False
            self.pray = False
            self.trap = False
            self.restart = False
            self.double = False
            self.double_enemy = []
            self.extra_lives = 0
            self.breath = 2
            self.black_hole = True
            self.stone = 3
            Player.play(self)
        time.sleep(1)
        self.points += math.floor(self.coins * 0.3)
        self.points += self.bombs * 3
        self.points += self.keys * 3
        self.points += (self.potion1 + self.potion2 + self.potion3)
        self.points += self.discount
        self.points += (len(self.items) * 75)
        if "Mute button" in self.items:
            input("\n\n\n\n\n\n... ... ... ......\n(x) ")
        else:
            input("\n\n\n\n\n\nThe run has ended.\n(x) ")
        if game_mode == 2:
            if not self.dead and self.winner:
                self.points += 100
                print(f"You won the game with {self.health} health left")
                self.points += self.health * 5
                if self.cat:
                    time.sleep(1)
                    print("You find the cat outside and you adopt it!!! Everyone loves a happy ending. ^-^ ")
            else:
                print("You died/gave up, so you obviously have 0 health left")
            time.sleep(2)
            if condition == 2:
                self.points = math.floor(self.points + (self.points * (20 / 100)))
            if condition == 3:
                self.points = math.floor(self.points + (self.points * (50 / 100)))
            if self.points < 0:
                self.points = 0
            print("\nThe important one, your score."
                  "\nYour leftover health, resources, selected difficulty"
                  "\nand actions are taken into account when calculating your score.")
            time.sleep(2)
            if "Red wig" in self.items:
                self.points = math.ceil(self.points * 1.3)
            print(f"\n\nAnd your final score is {self.points}")
            file = open('current.txt', 'w')
            data = f"{self.points}"
            file.write(data)
            file.close()
            f = open('current.txt', 'r')
            content = f.readlines()[0]
            a = 0
            digits = 0
            for i in content:
                digits += 1
            for i in content:
                if i.isdigit():
                    a += int(i) * math.pow(10, (digits - 1))
                    digits -= 1
            time.sleep(1)
            print(f"\nCurrent score           {self.name}: {int(a)}")
            # saved the current result, next up the high score
            h = open('highest.txt', 'r')
            content = h.readlines()[0]
            size = len(content)
            # Slice string to remove last 2 characters from string
            c = content[:size - 2]
            digits = 0
            b = 0
            for i in c:
                digits += 1
            for i in c:
                b += int(i) * math.pow(10, (digits - 1))
                digits -= 1
            hn = open('highest_name.txt', 'r')
            highest_name = hn.readlines()[0]
            print(f"Previous highest score  {highest_name}: {int(b)}")
            if int(a) > int(b):
                rewrite = open('highest.txt', 'w')
                data = str(a)
                rewrite.write(data)
                rewrite_name = open('highest_name.txt', "w")
                rewrite_name.write(self.name)
                rewrite.close()
                rewrite_name.close()
            h.close()
            hn.close()
        if game_mode == 1:
            if self.winner:
                input("You beat the game! Absolutely incredible. I am genuinely happy that you decided to play,"
                      f"\nnevermind win the whole thing. You did it in {self.rooms_cleared + 1} rooms with "
                      f"{self.health} health to spare. \nI admire you for this and I hope that you jump in "
                      "the dungeon once again, you're very welcome in here.\n(x) ")
                if self.cat:
                    time.sleep(1)
                    print("You find the cat outside and you adopt it!!! Everyone loves a happy ending. ^-^ ")
                h = open('wins.txt', 'r')
                content = h.readlines()[0]
                size = len(content)
                # Slice string to remove last 2 characters from string
                cont = content[:size - 2]
                digits = 0
                wins = 0
                for i in cont:
                    digits += 1
                for i in cont:
                    if i.isdigit():
                        wins += int(i) * math.pow(10, (digits - 1))
                        digits -= 1
                wins += 1
                h = open('wins.txt', 'w')
                h.write(str(wins))
                time.sleep(3)
                if wins == 1:
                    items = open('items.txt', 'a')
                    item_1 = "Score gambler"
                    item_2 = "Light trainers"
                    item_3 = "Broken glasses"
                    items.write("\n")
                    items.write(item_1)
                    items.write("\n")
                    items.write(item_2)
                    items.write("\n")
                    items.write(item_3)
                    print("You have unlocked some new items! Score gambler, Light trainers and Broken Glasses")
                    items.close()
                elif wins == 2:
                    items = open('items.txt', 'a')
                    item = "Giant coin"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Giant coin")
                    items.close()
                elif wins == 3:
                    items = open('items.txt', 'a')
                    item_1 = "Breath of air"
                    item_2 = "Detector"
                    items.write("\n")
                    items.write(item_1)
                    items.write("\n")
                    items.write(item_2)
                    print("You have unlocked more new items! Detector and Breath of air")
                    items.close()
                elif wins == 4:
                    items = open('items.txt', 'a')
                    item = "Brave juice"
                    item_2 = "Shiny necklace"
                    item_3 = "Belt"
                    items.write("\n")
                    items.write(item)
                    items.write("\n")
                    items.write(item_2)
                    items.write("\n")
                    items.write(item_3)
                    print("You have unlocked 3 new items! Brave juice, Shiny necklace and Belt")
                    items.close()
                elif wins == 5:
                    items = open('items.txt', 'a')
                    item = "Restart button"
                    item2 = "Russian roulette"
                    item3 = "Metal and a dream"
                    items.write("\n")
                    items.write(item)
                    items.write("\n")
                    items.write(item2)
                    items.write("\n")
                    items.write(item3)
                    print("You have unlocked yet more new items! Russian roulette, Restart button and Metal and "
                          "a dream.")
                    items.close()
                elif wins == 6:
                    items = open('items.txt', 'a')
                    item = "Red wig"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Red wig")
                    items.close()
                elif wins == 7:
                    items = open('items.txt', 'a')
                    item = "Lucky 13"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Lucky 13 (the name of the item)")
                    items.close()
                elif wins == 8:
                    items = open('items.txt', 'a')
                    item = "Strong juice"
                    item2 = "Mute button"
                    items.write("\n")
                    items.write(item)
                    items.write("\n")
                    items.write(item2)
                    print("You have unlocked a new items! Strong juice and Mute button")
                    items.close()
                elif wins == 9:
                    items = open('items.txt', 'a')
                    item = "Portable black hole"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Portable black hole")
                    items.close()
                elif wins == 10:
                    items = open('items.txt', 'a')
                    item = "Reality stone"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Reality stone")
                    items.close()
                elif wins == 11:
                    items = open('items.txt', 'a')
                    item = "Mirror stand"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Mirror stand")
                    items.close()
                elif wins == 13:
                    items = open('items.txt', 'a')
                    item = "Cursed staff"
                    items.write("\n")
                    items.write(item)
                    print("You have unlocked a new item! Cursed staff")
                    items.close()
                h.close()
            else:
                print("You lost but the fact that you tried in the first place makes me truly happy! You cleared\n"
                      f"{self.rooms_cleared} rooms.")
        time.sleep(2)
        print(f"\nThank you for playing, {self.name} <3")


print("\n\n\n\n\n--------------\nNew run!\n--------------")
p1 = Player(input("\n\n\n\n\nWhat is your name? "))
p1.the_game()
