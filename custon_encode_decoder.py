#ENCODER
def input_():
    global a, word, number, BOLD, END
    END = '\033[0m'
    BOLD = '\033[1m'
    while True:
        print("Type 'encode' to encrypt, 'decode' to decrypt:")
        a=input("")
        if a.lower()=='encode' or a.lower()=='decode':
            break
        else:
            print("Type correctly.")
            
    word=input("Type your word. ")
    number=int(input("Type your shift number. "))



def decoder(word, number):
    pwe='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alphabets=pwe.split(" ")
    
    for i in range(number):

        alpha=alphabets[25]
        alphabets.remove(alpha)
        alphabets.insert(0, alpha)
  
    return alphabets
        
    
def  encoder(word, number):
    pwe='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alphabets=pwe.split(" ")

    for i in range(number):
        alpha=alphabets[0]
        alphabets.remove(alpha)
        alphabets.insert(25, alpha)
    return alphabets


def new_word(alphabets):
    word2=word.upper()
    pwe='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alphaR=pwe.split(" ")
    new_wordd=''
    for i in word2:
        if i.isalpha()==False:
            new_wordd+=i
        else:
            k=alphaR.index(i)
            new_wordd+=alphabets[k]
    if a.lower()=='encode':       
        print(f"Your encoded result is:{BOLD} {new_wordd.lower()}{END}")
    else:
        print(f"Your decoded result is: {BOLD}{new_wordd.lower()}{END}")
        
        
while True:        
    input_()

    if a=='encode':
        new_word(encoder(word, number))
    else:
        new_word(decoder(word, number))
    print("")
    while True:
        q=input("Type 'yes' if you want to encode again or 'no' to quit. ")
        if q=='yes'or q=='no':
            break
        else:
            print("Type correctly.")
 
    if q=='no':
        print("Thank you!")
        break
    print("")
        
