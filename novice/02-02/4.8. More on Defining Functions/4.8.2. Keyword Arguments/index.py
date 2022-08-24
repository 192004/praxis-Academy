# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")

# parrot(1000)                                          
# parrot(voltage=1000)                                 
# parrot(voltage=1000000, action='VOOOOOM')             
# parrot(action='VOOOOOM', voltage=1000000)             
# parrot('a million', 'bereft of life', 'jump')         
# parrot('a thousand', state='pushing up the daisies') 

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     
# parrot(actor='John Cleese')

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print (kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")