#Monosubstitution
#multiplicative

#check if key is valid.
#as we know key inverse lies in 1 to 25, so we check... acc to ciphering manual

def valid_key_multiplicative(key):
    
    key_inverse_exist = 0
    for key_inverse in [1,3,5,7,9,11,15,17,19,21,23,25]:
        if (key*key_inverse)%26==1:
            key_inverse_exist += 1
    
    if key_inverse_exist>0:
        return True
    else:
        return False

   

#DATA CLEANING - Dont forget


def multiplicative_encrypt(ip, key):
    output = ''
    for i in ip:
        output += chr((((ord(i)-96)*key)%26 + 96))
    return output


def multiplicative_decrypt(ip):
    dec = {}
    for keyi in [3,5,7,9,11,15,17,19,21,23,25]:
        output = ''
        for i in ip:
            output += chr(((ord(i)-96)*keyi)%26 + 96)
            
        dec[keyi] = output
    return dec
