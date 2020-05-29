#mono substitution
#additive cypher


#data cleaning
def datacleaning(inputtext):
    output = ''
    #Text should be lower
    inputtext = inputtext.lower()
    count_unrecognizedchar = 0
    for s in inputtext:
        if ord(s) in range(97,123):
            output += s
        else:
            count_unrecognizedchar += 1
        if count_unrecognizedchar>0:
            print('Input text contained unrecognized characters, such as spaces and numbers, which have been ignored in the output')
    return output

def additive_encrypt(ip,key):
    output = ''
    for i in ip:
        output += chr(((ord(i)-97+key)%26 + 97))
    return output

def additive_decrypt(ip):
    dec = {}
    for key in range(0,26):
        output = ''
        for i in ip:
            output += chr(((ord(i)-97+key)%26 + 97))
            
        dec[26-key] = output
            
            
    return dec
