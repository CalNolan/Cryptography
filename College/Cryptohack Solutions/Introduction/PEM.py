from Crypto.PublicKey import RSA

f = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')

key = str(RSA.import_key(f.read()))
print(key)

keyhex = key.split('at ')[1]
print(keyhex)

ans = int(keyhex, 16)
print(ans)

f.close()