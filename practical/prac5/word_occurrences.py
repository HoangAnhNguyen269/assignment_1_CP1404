text = input('Text: ')
text=text.split(' ')
word_to_num={}
for word in text:
    frequency = word_to_num.get(word, 0)
    word_to_num[word]= frequency +1
word_keys = list(word_to_num.keys())
word_keys.sort()
for word in word_keys:
    print('{:<12s} {}'.format(str(word +' :'), word_to_num[word]))

