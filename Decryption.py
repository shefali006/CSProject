#Importing Important Libraries
import cv2
import os
import string

img = cv2.imread("originalImage.jpg") #Reading the Original Image

msg = input("Enter the Secret Message: ") #Enter the Message to be Hidden
password = input("Enter the Passcode: ") #Enter the Password to Secure Data

a = {} #Dictionary for Storing the ASCII Value
d = {} #Dictionary for Storing Data

for i in range(255):
    a[chr(i)] = i
    d[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = a[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

message = ""
n = 0
m = 0
z = 0

pwd = input("Enter the Passcode for Decryption: ")
if password == pwd:
    for i in range(len(msg)):
        message = message + d[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("The Decrypted Message is: ", message)
else:
    print("You are not 'auth'")
