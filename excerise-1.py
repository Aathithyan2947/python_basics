print("String Functions")
print("1.Upper")
print("2.Lower")
print("3.Capitalize the word")
print("4.Split")
print("5.Swap the case")
print("6.Replace a string in a sentence")
print("7.Find the string is alphabet or not")
print("8.Count the length of the string")
print("9.Title case")
print("10.Zero fill")

run=True

while run:
    word=input("Enter the string : ")
    opt=int(input("Enter the operation to be performed : "))
    if opt==1:
        print("The selected function : Upper")
        print("Answer : "+" "*2+word.upper())
    elif opt==2:
        print("The selected function : Lower")
        print("Answer : "+" "*2+word.lower())
    elif opt==3:
        print("The selected function :Capitalize the word ")
        print("Answer : "+" "*2+word.capitalize())
    elif opt==4:
        li=word.split()
        print("The selected function :Split function")
        print("Answer : "+" "*2+str(li))
    elif opt==5:
        print("The selected function :Swap the case")
        print("Answer : "+" "*2+word.swapcase())
    elif opt==6:
        word_to_replace=input("Enter the word to be replaced: ")
        replace_word=input("Enter the replacable word : ")
        print("The selected function : replace the word")
        print("Answer : "+" "*2+word.replace(word_to_replace,replace_word))
    elif opt==7:
        print("The selected function : Find the string is alphabet or not")
        print("Answer : "+" "*2+str(word.isalpha()))
    elif opt==8:
        print("The selected function : Count the length of the string")
        print("Answer : "+" "*2+str(len(word)))    
    elif opt==9:
        print("The selected function : Title case")
        print("Answer : "+" "*2+str(word.title()))
    elif opt==10:
        print("The selected function : Zero fill")
        print("Answer : "+" "*2+word.zfill(len(word)+4))
    else:
        print("Please Select the correct option ")
    choice=input("Do you want to continue or not , press Y or N : ")
    if choice=="N":
        run=False
