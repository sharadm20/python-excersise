#!/usr/bin/env python3

import bcrypt
print('Enter passcode to be hashed:')
passwd = str(input())
passwd = passwd.encode('utf-8')
# passwd = 'b'+rawpass

# print(passwd)
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

# print(salt)
print(hashed)
