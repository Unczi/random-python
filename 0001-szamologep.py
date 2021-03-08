print("Szia! Én vagyok a számológép.")
print("Milyen műveletet szeretnél elvégezni? A következő karakterek valamelyike beírásával válaszolj.")
print("+\n-\n*\n/\n")
muvelet = input()
elsotag = input("Oké. Mi a műveleted első tagja/tényezője? (a műveletednek 2 tagja lehet)\n")
masodiktag = input("Mi a második?\n")
if muvelet == "+":
    print("Az eredmény:",int(elsotag)+int(masodiktag))
elif muvelet == "-":
    print("Az eredmény:",int(elsotag)-int(masodiktag))
elif muvelet == "*":
    print("Az eredmény:",int(elsotag)*int(masodiktag))
elif muvelet == "/":
    if masodiktag == "0":
        print("Hé, nem figyeltél matek órán?\nNEM lehet 0-val osztani! :P")
    else:
        print("Az eredmény:",int(elsotag)/int(masodiktag))
else:
    print("Valószínűleg rossz műveleti jelet adtál meg, kérlek próbáld újra!")
