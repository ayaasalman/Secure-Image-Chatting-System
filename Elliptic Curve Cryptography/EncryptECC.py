import Elliptic
import math
import os
import random
import imgToDat
import numpy as np

def encrypt_to_disk(name):
    p = 487
    # p = 997
    a = 0
    b = 3

    document = "inverse_ppp" + str(p) + ".txt"
    if not os.path.exists(document):
        Elliptic.calc_inverse(p, document)
    ECC = Elliptic.Elliptic(p, a, b, document)

    ECC.get_key()
    # name = input("enter the file path and name: ")
    
    plain = imgToDat.compressedImg(name)
    return ECC.encrypt2(plain), plain


