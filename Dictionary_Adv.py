nobel_prize_winners = { #creating a dictionairy
    (1979, "physics"):["Glashow","Salam","Weinberg"],
    (1962, "chemistry"):["Hodgkin"],
    (1984, "biology"):("McClintock"),
}

nobel_prize_winners.update({(1922, "Physics"):"Einstein"}) #adding an element in our dictionairy
print(nobel_prize_winners)

del nobel_prize_winners[1962, "chemistry"]
print("List after deletion: \n")
print(nobel_prize_winners)