a = "rice"
b = "garri"
c = "beans"
d = "sugar"
e = "meat"
f = "bread"
ab  = ("rice and garri")
ac  = ("rice and beans")
bc  = ("garri and beans")
abc = ("rice, garri and beans")
order = input('''Which of these items do you have? (garri/rice/beans): ''')
if order == a :
    print(f"I will buy {a} and {e} ")
if order == b :
    print(f"I will buy {b} and {d} ")
if order == c :
    print(f"I will buy {c} and {f} ")
if order == ab:
    pa = float(input("what is the price of rice? "))
    pb = float(input("what is the price of garri? "))
    if pa > pb:
        print(f"I will buy {b}")
    elif pb > pa :
        print(f"I will buy {a}")
    elif pb == pa :
        wa = float(input("what is the weight of rice? "))
        wb = float(input("what is the weight of garri? "))
        if wa > wb:
            print(f"I will buy {b}")
        elif wb > wa:
            print(f"I will buy {a}")
        else:
            print(f"I will buy {a} and {b}")
if order == ac :
    pa = float(input("what is the price of rice? "))
    pc = float(input("what is the price of beans? "))
    if pa > pc:
        print(f"I will buy {c}")
    elif pc > pa:
        print(f"I will buy {a}")
    elif pc == pa:
        wa = float(input("what is the weight of rice? "))
        wc = float(input("what is the weight of beans ? "))
        if wa > wc:
            print(f"I will buy {c}")
        elif wc > wa:
            print(f"I will buy {a}")
        else:
            print(f"I will buy {a} and {c}")
if order == bc :
    pc = float(input("what is the price of beans? "))
    pb = float(input("what is the price of garri? "))
    if pc > pb:
        print(f"I will buy {b}")
    elif pb > pc:
        print(f"I will buy {c}")
    elif pc == pb:
        wb = float(input("what is the weight of garri? "))
        wc = float(input("what is the weight of beans ? "))
        if wb > wc:
            print(f"I will buy {c}")
        elif wc > wb:
            print(f"I will buy {c}")
        else:
            print(f"I will buy {b} and {c}")
if order == abc:
    print(f"I will buy {abc} ")





