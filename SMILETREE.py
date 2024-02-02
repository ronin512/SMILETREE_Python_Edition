# Ζητάμε από τον χρήστη το επιθυμητό ύψος του δέντρου
print("THE TREE OF SMILES (version 1) BY CV. ")
a = int(input("Enter desired height of tree: "))

# Ελέγχουμε ότι το ύψος είναι μεγαλύτερο από 1 και μικρότερο από 23
while a > 23 or a < 1:
    print("Invalid height. Please enter a height between 1 and 23.")
    a = int(input("Enter desired height of tree: "))

# Εκτυπώνουμε το δέντρο
f = 0
for i in range(a):
    # Εκτυπώνουμε κενά πριν από τα ":)"
    for k in range(a, 0, -1):
        print(" ", end="")
    
    f += 1
    # Εκτυπώνουμε τα ":)" με βάση την τρέχουσα τιμή του 'f'
    for y in range(f):
        print(":)", end="")
    
    # Αλλάζουμε γραμμή και μειώνουμε το ύψος
    print()
    a -= 1
