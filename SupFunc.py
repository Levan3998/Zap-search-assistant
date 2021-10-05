def add_spaces(l):
    s= ""
    for i in l:
        s = s + str(i) + " "
    return s


def get_numeric_vals(s):
    flag = False
    cur_num = ""
    l = []
    for i in s:
        if i.isnumeric():
            cur_num = cur_num + i
        else:
            if(cur_num != ""):
                l.append(cur_num)
                cur_num = ""
    return l


def find_best(l):
    five_stars = []
    four_stars = []
    for i in l:
        if(i["rating"] != None):
            if(i["rating"] >= 4.5):
                if(i["rating"] == 5):
                    five_stars.append(i)
                else:
                    four_stars.append(i)
    five_stars.sort(key = lambda tup: float(tup["rates"]))
    four_stars.sort(key = lambda tup: float(tup["rates"]))
    return (five_stars,four_stars)


import matplotlib.pyplot as plt

def plot_price_rates(l):
    lp, lr = [], []
    for i in l:
        if(i is not None):
            lp.append(i["price"])
            lr.append(i["rates"])
    plt.plot(lp, lr, 'ro')
    plt.axis([0,max(lp),0,max(lr)])
    plt.show()


def find_best_offers(l):
    l.reverse()
    last_price = 100000
    new_l = []
    for i in l:
        if(float(get_numeric_vals(i["price"])[0]) > last_price):
            last_price = 0
        else:
            last_price = float(get_numeric_vals(i["price"])[0])
            new_l.append(i)
    return new_l
