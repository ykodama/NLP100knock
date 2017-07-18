def ngram(seq, n, type):
    if type == 'word':
        seq_list = seq.split(" ")
    elif type == 'char':
        seq = seq.replace(' ', '')
        seq_list = list(seq)

    lst = []
    n_phrase = len(seq_list) - n + 1
    for i in range(n_phrase):
        phrase = seq_list[i:i+n]
        lst.append(phrase)
    return lst

s = 'I am an NLPer'
print(ngram(s, 2, 'word'))
print(ngram(s, 2, 'char'))
