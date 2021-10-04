#Create a function called hasL() that returns true/false if a given word w contains at least once instance of the letter "l"
def hasL(w):
    for i in range(0, len(w)):
        if w[i] == "l":
            return True
    else:
        return False

print(hasL("hello"))

