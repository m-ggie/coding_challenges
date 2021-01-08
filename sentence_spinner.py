def spin_words(sentence):
    sentence = sentence.split()
    spun_list = [""]
    for word in sentence:
        if len(word) >= 5:
            spun_string=''.join(reversed(word))
            spun_list.append(spun_string)
        else:
            spun_list.append(word)
    spun_string = " ".join(spun_list)
    print(spun_string[1:])
    return spun_string[1:]

inputsentence = "Stop spinning my sentences"

spin_words(inputsentence)
