def ngram(seq, n, type):
    if type == 'word':
        seq = seq.split(" ")
    elif type == 'char':
        seq = seq.replace(' ', '')

    lst = []
    n_phrase = len(seq) - n + 1
    for i in range(n_phrase):
        phrase = seq[i:i+n]
        lst.append(phrase)
    return lst

if __name__ == "__main__":
    s1 = "paraparaparadise"
    s2 = "paragraph"
    X = set(ngram(s1, 2, 'char'))
    Y = set(ngram(s2, 2, 'char'))
    print(X)
    print(Y)
    sum_XY = X&Y
    prod_XY = X|Y
    diff_XY = X-Y
    print(sum_XY)
    print(prod_XY)
    print(diff_XY)

    print("'se' in X: {0}".format('se' in X))
    print("'se' in Y: {0}".format('se' in Y))
