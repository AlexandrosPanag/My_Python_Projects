nobel_prize_winners = { #creating a dictionary
    (1979, "physics"):["Glashow","Salam","Weinberg"],
    (1962, "chemistry"):["Hodgkin"],
    (1984, "biology"):("McClintock"),
}

nobel_prize_winners.update({(1922, "Physics"):"Einstein"}) #adding an element in our dictionary
print(nobel_prize_winners) #print the list with added element

del nobel_prize_winners[1962, "chemistry"] #removing an element from out dictionary
print("List after deletion: \n")
print(nobel_prize_winners) #print the list with the removed element