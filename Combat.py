#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 13:18:59 2024

@author: ethan
"""
import tbc

def main():
    us = tbc.Character()
    us.name = "Us"
    us.hitPoints = 10
    us.hitChance = 60
    us.maxDamage = 5
    us.armor = 2

    them = tbc.Character("Them", 50, 20, 5, 0)

    us.printStats()
    them.printStats()

    tbc.basicFight(us, them)

    us = tbc.Character(name="Us")
    them = tbc.Character(name="Them")
    us.printStats()
    them.printStats()

    tbc.userFight(us, them)

if __name__ == "__main__":
    main()
