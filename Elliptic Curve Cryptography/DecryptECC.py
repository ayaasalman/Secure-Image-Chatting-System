import Elliptic
import math
import os
import random
import imgToDat
import numpy as np

def decrypt_to_pic(c):
    p = 487
    # p = 997
    a = 0
    b = 3

    document = "inverse_ppp" + str(p) + ".txt"
    if not os.path.exists(document):
        calc_inverse(p, document)
    ECC = Elliptic.Elliptic(p, a, b, document)

    ECC.get_key()
    de = ECC.decrypt2(c)
    return de


