sentence = "Now I need a drink, alcoholic of course, after the heavy lectures\
            involving quantum mechanics."
sentence = sentence.replace('.', '')
sentence = sentence.replace(',', '')
sentence = sentence.split()

n_char_list = []

for wi in sentence:
    n_char_list.append(len(wi))

print (n_char_list)
