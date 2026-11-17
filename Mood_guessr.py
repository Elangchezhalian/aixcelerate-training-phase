sentence = input("Enter a sentence: ")
happy_words = ["happy", "good", "great", "love"]
sad_words = ["sad", "bad", "cry", "upset"]
if any(word in sentence for word in happy_words):
    print("Happy")
elif any(word in sentence for word in sad_words):
    print("Sad")
else:
    print("Not sure")
