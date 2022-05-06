import numpy as np
from random import randint

Encode_List = np.array(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '+', "/"])
Last_Output = ""


def get_rand_str(length=10, output=''):
    Length = length
    if Length > 0:
        chr_num = randint(0, 63)
        Output = output + Encode_List[chr_num]
        return get_rand_str(Length - 1, Output)
    else:
        return output