#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:04:44 2024

@author: ethan
"""

import random

class Character:
    def __init__(self, name="", hitPoints=20, hitChance=50, maxDamage=5, armor=0):
        self.name = name
        self.hitPoints = hitPoints 
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property   
    def hitPoints(self):
        return self.__hitPoints
        
    @hitPoints.setter  
    def hitPoints(self, value):
        self.__hitPoints = value
    
    def printStats(self):
        print(f"""
{self.name}
    Hit Points: {self.hitPoints}
    Hit Chance: {self.hitChance}
    Max Damage: {self.maxDamage}
    Armor:      {self.armor}       
    """ )
   
    def hit(self, enemy):
        if random.randint(1,100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}..." )
            damage = random.randint(1, self.maxDamage)
            print(f" for {damage} points of damage... ")
            damage -= enemy.armor
            if damage < 0 :
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name}'s armor absorbs {enemy.armor} points")
            enemy.hitPoints -= damage
        else:
            print(f"{self.name} misses {enemy.name}")

def basicFight(character1, character2):
    print(f"--- Basic Fight between {character1.name} and {character2.name} ---")
    while character1.hitPoints > 0 and character2.hitPoints > 0:
        character1.hit(character2)
        if character2.hitPoints <= 0:
            print(f"{character2.name} has been defeated!")
            break
        character2.hit(character1)
        if character1.hitPoints <= 0:
            print(f"{character1.name} has been defeated!")
            break
    print("--- End of Fight ---")       

def main():
    c = Character()
    c.name = "George"
    c.hitPoints = -157
    c.printStats()    
    e = Character()
    e.name = "Jerry"
    e.hitPoints = -157
    e.printStats()
    
if __name__ == "__main__":
    main()
