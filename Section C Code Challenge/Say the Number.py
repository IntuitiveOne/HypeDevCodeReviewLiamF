from num2words import num2words


def num_word(numtoword):

    numinwords = num2words(numtoword) #calling the num2words function which takes the digits of users input assuming said digits make a singular number and provides a string that would be as if the number was written in words

    print(numinwords.capitalize()+".")
    
##################################################################################################

### assumming i didn't know the num2words module existed this is how I would code the function ###

##################################################################################################    

def num_wordwithoutmodule(numtoword):

    singles = ['','one','two','three','four','five','six','seven','eight','nine']                                   #creating lists to be used in if statements and printing out of word
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    decades = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    triplepowersoften = ['','thousand','million','billion','trillion','quadrillion']                                #we could keep going but that is out of scope for what the exercise asked for

    words = [] #creating list to append appropiate words from the above lists into
    
    if numtoword==0: 
        words.append('zero') #if number is 0 we can skip all the statements and proceed to print immediately
    else:
        numStr = str(numtoword)
        numStrLen = len(numStr) #need to figure out length of number, to do this we must change the number into a string
        groups = int((numStrLen + 2)/3) #slicing number into groupings of 3 digits
        numStr = numStr.zfill(groups*3)

        for i in range(0,groups*3,3):
            hundreds = int(numStr[i]) #how many hundreds, units, tens and groupings using a for loop
            tens = int(numStr[i+1])
            units = int(numStr[i+2])
            g = int(groups-(i/3+1))
                                      #if statements appending to the words list based on the placement of each substring in each unit category list
            if hundreds >= 1:
                words.append(singles[hundreds])                
                words.append("hundred") #solution to the "hundreds" issue significantly reducing needed code
                
            if tens > 1:
                words.append(decades[tens])
                if units >= 1:
                    words.append(singles[units])
            elif tens == 1:
                if units >= 1:
                    words.append(teens[units])
                else:
                    words.append(decades[tens])
            else:
                if units >= 1:
                    words.append(singles[units])
            
            if g >= 1 and (hundreds + tens + units) > 0:
                words.append(triplepowersoften[g])

    #print(words) still have to figure out how to add ands and commas and hypens to the printed out string, run out of time for assignment to complete that aspect    

    wordsasstring = ' '.join(words)
    wordsasstring = wordsasstring.capitalize()
    print(wordsasstring+".")
    


numtoword = input("What is the number you want to convert?\n\n")

numtowordlist = list(numtoword) #converted to a list for easier string manipulations

if "," in numtowordlist: #removing commas from the given input

    numtoword = numtoword.replace(",", "")


while numtoword.isnumeric() == False: #simple while loop that asks user to repeatedly put in an input until an appropiate one is given (Only numbers or numbers with commas "," are acceptable)

    numtoword = input("Bad input, try again and only put numbers as your input.\n\nWhat is the number you want to convert?\n")
    numtowordlist = list(numtoword)
    if "," in numtowordlist:
            numtoword = numtoword.replace(",", "")

#testing both functions(with module, without module)

num_word(numtoword) 
num_wordwithoutmodule(int(numtoword))    
