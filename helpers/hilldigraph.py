import numpy as np


#Data cleaning
    #must be divisble into pairs, along with removing all other forms of data cleaning

def datacleaning_digraph(inputtext):
    output = ''
    #Text should be lower
    inputtext = inputtext.lower()
    count_unrecognizedchar = 0
    for s in inputtext:
        if ord(s) in range(97,123):
            output += s
        else:
            count_unrecognizedchar += 1
    if len(output)%2==1:
        output = output + 'x'
    return output



def valid_key_hilldigraph(a,b,c,d):
    det = a*d - b*c
    key = np.array([[a,b],[c,d]])
   

    if det%2!=0 and det%13!=0:
        return True, key
    else:
        return False,0
    


def hilldigraph_encrypt(ip, key):
    #Converting it into desired array, and into mod 26 integers YEAHHHH not as complicated as it looks!
    input_array = np.array([[(ord(i)-96)%26 for i in ip[::2]], [(ord(i)-96)%26 for i in ip[1::2]]])

    #Taking product of arrays
    output_array = np.dot(key, input_array)

    #Converting them backkk to letters!
    output_str = ''
    for j in range(len(ip)//2):
        for i in range(2):
            output_str += chr(output_array[i][j]%26 + 96)

    return output_str
