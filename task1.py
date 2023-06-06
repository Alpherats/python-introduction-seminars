def check_rythm(song):
    phraze = song.split()

    for i in range(len(phraze)):
        words = phraze[i].split('-')
        prev_of_vowels = None
        for j in range(len(words)):
            amount_of_vowels = words[j].count('а') + words[j].count('е') + words[j].count('ё') + \
                                 words[j].count('и') + words[j].count('о') + words[j].count('у') + \
                                 words[j].count('ы') + words[j].count('э') + words[j].count('ю') + \
                                 words[j].count('я')

            if prev_of_vowels is not None and amount_of_vowels!= prev_of_vowels:
                return "Пам парам"
            prev_of_vowels = amount_of_vowels

    return "Парам пам-пам"

song = input("Введите: ")
res = check_rythm(song)
print(res)
