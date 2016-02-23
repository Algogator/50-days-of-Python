cost = float(raw_input("Cost of item: "))
given = float(raw_input("Amount paid: "))
change = int(given - cost)
paisa = given - cost - change
print "Change: ", change
paisa = int(paisa * 100)
print "Paisa: ", paisa
print "=" * 30


def changecalc(change, dn, no):
    change = change - (dn * no)
    print "'%d' : %d" % (dn, no)
    return change


def calc(change):
    if change >= 1000:
        t = change / 1000
        if t != 0:
            change = changecalc(change, 1000, t)
            calc(change)
        else:
            return
    elif change >= 500:
        f = change / 500
        if f != 0:
            change = changecalc(change, 500, f)
            calc(change)
        else:
            return
    elif change >= 100:
        h = change / 100
        if h != 0:
            change = changecalc(change, 100, h)
            calc(change)
        else:
            return
    elif change >= 50:
        fv = change / 50
        if fv != 0:
            change = changecalc(change, 50, fv)
            calc(change)
        else:
            return
    elif change >= 20:
        tw = change / 20
        if tw != 0:
            change = changecalc(change, 20, tw)
            calc(change)
        else:
            return
    elif change >= 10:
        tn = change / 10
        if tn != 0:
            change = changecalc(change, 10, tn)
            calc(change)
        else:
            return
    elif change >= 5:
        five = change / 5
        if five != 0:
            change = changecalc(change, 5, five)
            calc(change)
        else:
            return
    elif change >= 2:
        two = change / 2
        if two != 0:
            change = changecalc(change, 2, two)
            calc(change)
        else:
            return
    elif change >= 1:
        o = change / 1
        if o != 0:
            change = changecalc(change, 1, o)
            calc(change)
        else:
            return
    else:
        return

print "Rupee: "
calc(change)

if paisa != 0:
    print "Paisa: "
    calc(paisa)
