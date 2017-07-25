import random


def random_order(s):
    s = s.split(" ")
    s2 = []
    for w in s:
        if len(w) > 4:
            body = list(w[1:-1])
            body_rand_list = random.sample(body, len(body))
            body_rand = "".join(body_rand_list)
            w = w[0] + body_rand + w[-1]

        s2.append(w)
    s2 = " ".join(s2)
    return s2


if __name__ == "__main__":
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(random_order(s))