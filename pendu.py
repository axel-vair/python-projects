import random 

with open("dico_france.txt", "r", encoding="ISO-8859-1") as f:
    word = f.read().split()
    word = random.choice(word)



# *** Initiation variables *** #

letters = ""
underscores = []
sizeWord = len(word)
listWord = list(word)

## ** Underscore map ** ## 
for letters in word:
    underscores += "-"
    
# *** Choose difficulty then assign number of lives *** # 

def difficulty():
    stringDifficulty = str(input("Choisir la difficulté: 'facile' 'intermédiaire' 'difficile'"))
    if stringDifficulty == "facile": 
        lives = 10
        print(f"You have {lives} lives")
        return lives
    elif stringDifficulty == "intermédiaire":
        lives = 5
        print(f"You have {lives} lives")
        return lives
    elif stringDifficulty == "difficile":
        lives = 3
        return lives
    elif stringDifficulty != "facile" or "intermédiaire" or "difficile":
        print("Erreur, choisissez une difficulté.")
        difficulty()
lives = int(difficulty())


# *** Verify letters put and random word *** # 
print(f"Le mot est composé de {sizeWord} lettres. \n")
print(' '.join(underscores))


while lives != 0 and underscores != listWord:
    inputLetter = str(input("Entrer une lettre: > "))
    if inputLetter in word: 
        for x in range(sizeWord):
            if listWord[x] == inputLetter: 
                underscores[x] = inputLetter
                letters = letters + inputLetter
                print(f"The {inputLetter} is in the word !")
                print(' '.join(underscores))
               
    else: 
        lives -= 1
        print(f"{inputLetter} ne fait pas partie du mot, vous perdez 1 vie. Il vous reste {lives} vie(s)")


# *** Win and lose conditions *** #

if lives == 0:
    print("Vous n'avez plus de vies. Vous avez perdu !")
elif underscores == listWord: 
    print("Bien joué ! Vous avez trouvé le mot !") 
