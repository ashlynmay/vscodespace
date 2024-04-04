import re


def main():
    text = gettext()
    wordc = (words(text))
    mult = wordc/100
    letterc = letters(text, mult)
    sentencec = sentences(text, mult)
    grade = round(0.0588 * letterc - 0.296 * sentencec - 15.8)
    output(grade)

# Get text
def gettext():
    text = input("Text: ")
    return text

# Calculate words
def words(text):
    return len(text.split())


# Calculate letters per 100 words
def letters(text, mult):
    count = 0
    for i in range(len(text)):
        if (text[i].isalpha()):
            count += 1
    letterc = count / mult
    return letterc


# Calculate sentences per 100 words
def sentences(text, mult):
    total = (len(re.split('[.!?]', text))-1)
    sentencec = total / mult
    return sentencec


# Print grade
def output(grade):
    if grade < 16 and grade > 1:
        print("Grade " + str(grade))
    elif grade == 16 or grade > 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print("Invalid Grade")
        return 1


main()
