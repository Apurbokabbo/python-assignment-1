def vowelCounter(sentence):
    vowels = ['a','e','i','o','u']
    count=0
    for word in sentence:
        if(word[0] in vowels):
            count+=1

    return count

sentence = input("Enter a sentence: ")
print("Vowel in your sentence :",vowelCounter(sentence))