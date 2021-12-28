# # import pyotp
# import time
# # from pyotp import TOTP
# import pyotp
# totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
# print("Current OTP:", totp.now())
# print(totp)
# print(totp.now())

# # # OTP verified for current time
# # var = input('Enter Your otp here :')

# # totp.verify(var) # => True

# # time.sleep(30)
# # totp.verify(var) # => False

# while True:
#    var = input('Enter Your otp here :')
#    a = totp.verify(var) # => True
#    print(a)
   
#    totp.verify(var)
#    if a == True:
#        break

# Generate the secrert key:-------------------------
import pyotp  
import base64
class generateKey:
    @staticmethod
    def returnValue(email):
        return 'JBSWY3DPEHPK3PXP'+str(email)


# Generate the OTP :---------------------------------
email = "v@gmail.com"
keygen = generateKey()
                
key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
print(key)
# interval = 300 means after 300 seconds, otp will expire
totp = pyotp.TOTP(key,interval=300)  # TOTP Model for OTP is created
otp = totp.now()
                
print(otp)

# Verify the OTP :----------------------------------
keygen = generateKey()
key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
print(key)
totp = pyotp.TOTP(key,interval=300)
verify = totp.verify(542978)
print(verify)
