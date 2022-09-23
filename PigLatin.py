def findFirstVowel(word):
    for index, letter in enumerate(word):
        print("checking:", index, letter, sep="\t")
        if letter in "aeiou":
            return index
    return len(word) - 1


def convertToPigLatin(word):
    index = findFirstVowel(word)
    if index == 0:
        return word[1:] + word[0] + "way"
    else:
        return word[index:] + word[:index] + "ay"


def main():
    finished = False
    while not finished:
        word = input()
        word = word.lower()
        if word == "done":
            finished = True
        else:
            pig = convertToPigLatin(word)
            print(pig)


main()
