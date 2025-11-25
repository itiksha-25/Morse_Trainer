#app i made to help learn morse code
import random

# main function to input and show menu buttons
def main():

    while True:
        print()
        print(" 📚 === Morse Code Learning App ===📚")

        print(" 1️⃣   Text to Morse")

        print("   2.Morse to Text")
        print(" 3Quiz on Morse Code")
        print("4.  Exit")
        choice = input("✔️   choose option ✔️    ")


        if choice == '1':
            tomorse()
        elif choice == '2':
            totext()
        elif choice == '3':
            quiz()
        elif choice == '4':
            print("Goodbye. Come study again soon  👋")
            break
        else:
            print("Please enter choice correctly")

#list of morse code for everything needed
MORSE = {'0': '-----',        '1': '.----',   '2': '..---',   '3': '...--',   '4': '....-',
    '5': '.....',   '6': '-....',   '7': '--...',   '8': '---..','9': '----.', 'A': '.-','B': '-...',   'C': '-.-.',     'D': '-..', 'E': '.',   'F': '..-.','G': '--.', 'H': '....',
    'I': '..','J': '.---',    'K': '-.-', 'L': '.-..',    'M': '--',  'N': '-.',  'O': '---', 'P': '.--.',
    'Q': '--.-',    'R': '.-.', 'S': '...','T': '-',  'U': '..-',  'V': '...-',    'W': '.--', 'X': '-..-',
    'Y': '-.--',  'Z': '--..',}
#for input morse code to convert to text
rev = {v: k for k, v in MORSE.items()}




#takestext and converting -> morse code
def tomorse():
    print()
    text = input("Enter text to convert to morse code!: ")
    text= text.upper()
    words = text.split()   # split into words because of spaces they have in between
    m_words = []

    for w in words:
        m_letters = []
        for c in w:
            if c in MORSE:
                code = MORSE[c]
                m_letters.append(code)
        m_words.append(" ".join(m_letters))

       # / after each word for morse code
    morse = " / ".join(m_words)

    print("\nMorse Code:")
    print(morse)


  #converts text -> morse code
def totext():
    print()
    print("Enter morse code [words with . and - and separate alphabets with spaces and words with '/']")
    morse = input("morse Code: ")
    words = morse.split('/')   
    #split words for convertion
    converted_words = []


    for w in words:
        alphabets = w.strip().split()
        converted_letters = []
        for mcode in alphabets:
            if mcode in rev:
                converted_letters.append(rev[mcode])
            else:
                converted_letters.append('?')
        converted_words.append("".join(converted_letters))
    text = " ".join(converted_words)
    print()
    print("Text:",text)




def quiz():             #quiz on morse code
    print()
    print("⏳  --- Morse Code Quiz ---⌛  ")
    alphabets = list(MORSE.keys())
    while True:
        alphabet = random.choice(alphabets)
        morse = MORSE[alphabet]
        print()
        print("What is this in morse code? ", morse)
        answer = input("Give your answer (or write 'QUIT' to quit the quiz): ")
        if answer.upper() == 'QUIT':
            break
        elif answer.lower() == alphabet:
            print("✔️Right!✔️    ", morse, "is",alphabet)
        else:
            print("❌  Wrong  " ,morse, "is",alphabet)


if __name__ == "__main__":
    main()
