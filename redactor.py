import sys

if __name__ == "__main__":
    #Declare some variable based on system arguments
    filename = sys.argv[1];
    file = open(filename, "rU")
    toRemove = sys.argv[2:]
    
    #Read the file into a string
    text = ""
    for line in file:
        text += line
    
    #Now search through the string to remove all substrings in toRemove
    for stringToRemove in toRemove:
        while text.find(stringToRemove) != -1:
            index = text.find(stringToRemove)
            text = text[:index] + "[Redacted]" + text[(index+len(stringToRemove)):]
    
    #Write to the file
    file = open(filename, "w");
    file.write(text)
    
    #Good times!
    sys.exit(0)