import random
karakterek = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
hossz = input("Hány karakterből álljon a jelszó? ")
holtartok = 0
print("A jelszavad:", end=" ")
while holtartok != int(hossz):
    print(karakterek[random.randint(0, len(karakterek)-1)], end="")
    holtartok += 1
