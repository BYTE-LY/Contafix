#!/bin/env python3
import vobject
import os

find_pos=lambda File:[i for i in range(len(File)) if File[i].startswith('BEGIN')]
numbers_list=lambda vcard:[str(str(i.value).replace(' ','')).replace('-','') for i in vcard.contents['tel']]

def num_conv(number):
    new='DONT'
    if number.startswith('091'): 
        new=['+218'+number[1:],'madar']
    elif number.startswith('092'):
        new=['+218'+number[1:],'libyana']
    elif number.startswith('095'):
        new=['+218'+number[1:],'libyana']
    elif number.startswith('094'):
        new=['+218'+number[1:],'libyana']

    elif number.startswith('00218'):
        if number[5:].startswith('91'):
            new=['0'+number[5:],'madar']
        elif number[5:].startswith('92'):
            new=['0'+number[5:],'libyana']
        elif number[5:].startswith('95'):
            new=['0'+number[5:],'libyana']
        elif number[5:].startswith('94'):
            new=['0'+number[5:],'libyana']

    elif number.startswith('+218'):
        if number[4:].startswith('91'):
            new=['0'+number[4:],'madar']
        elif number[4:].startswith('92'):
            new=['0'+number[4:],'libyana']
        elif number[4:].startswith('95'):
            new=['0'+number[4:],'libyana']
        elif number[4:].startswith('94'):
            new=['0'+number[4:],'libyana']
    else:
        print('skipping',number)
    return new

def check_numbers(numbers):
    for u in numbers:
        if num_conv(u)!='DONT':
            U=num_conv(u)
            if not (U[0] in numbers):
                yield(U)


def main(input_file):
    if __name__=='__main__':
    
        with open(input_file,'r') as i:
            contacts=(i.readlines())
        
        with open('newfile.vcf','w') as file:
            for i in find_pos(contacts):
                vcard=vobject.readOne(''.join(contacts[i:]))
                for i in (check_numbers(numbers_list(vcard))):
                    print('adding',i[0] )
                    vcard.add('tel').value=i[0]
                file.write(vcard.serialize())
            
if os.name == 'nt': 
    os.system('cls') 
else: 
    os.system('clear') 

print('This script resolves the issue of the phone numbers in Libya (AppleOSs)')
print('Source Code at https://github.com/BYTE-LY/Contafix/')
print('Made by @BYTE-LY\n')

while True:
    input_file=input('drag your contacts file and drop it here/write the full path(.vcf) ')
    if os.path.isfile:
        main(input_file)
        break
    else:
        print('file does not exist')
