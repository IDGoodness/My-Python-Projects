def generate():
    from operator import length_hint
    import random

    lowerCase = "qwertyuiopasdfghjklzxcvbnm"
    upperCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
    number = "0123456789"
    symbols = '''`~!@#$%^&*()_+-=|\"'{}[]:;?/>.<,'''

    UseFor = lowerCase + upperCase + number + symbols
    length_for_pass = 8

    password = "".join(random.sample(UseFor, length_for_pass))

    print("Your generated password: "+password)
    result.element.text = generate()



