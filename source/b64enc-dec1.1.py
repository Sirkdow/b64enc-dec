import base64


print    (" _       __ _  _                         __ _           ") 
print    ("| |     / /| || |                       / /| |          ") 
print    ("| |__  / /_| || |_    ___ _ __   ___   / /_| | ___  ___ ") 
print    ("| '_ \| '_ \__   _|  / _ \ '_ \ / __| / / _` |/ _ \/ __|")
print    ("| |_) | (_) | | |   |  __/ | | | (__ / / (_| |  __/ (__ ")
print    ("|_.__/ \___/  |_|    \___|_| |_|\___/_/ \__,_|\___|\___|")
print    ("")
print    ("               Developed by Sirkdow                     ")
print    ("               (Fabrizio D'Onofrio)                     ")
print    ("                       v1.1                             ")
print    ("")                                                              


def encode():
    b = raw_input("Type Something to encode: ")
    e = base64.b64encode(b)
    print("")
    print("Success:")
    print("")
    print(e)
    print("")

def decode():
    b = raw_input("Type Something to decode: ")
    try:
        d = base64.b64decode(b)
    except:
        print("Syntax Error")
    print("")
    print(d)


s = raw_input("Type e to encode or d to decode: ")
print("")
       
if s == 'e':
        encode()
elif s == 'd':
        decode()        
else:
    print("%s is not valid. Restart." % (s))
    print("")