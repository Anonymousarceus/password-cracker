import random

import pyautogui
chars="abcdefghijklmnopqrstuvwxyz@1234567890"
allchars=list(chars)
pwd=pyautogui.password("enter a password")
sample_pwd=""
while(sample_pwd!=pwd):
    sample_pwd=random.choices(allchars, k=len(pwd))
    print("<="+str(sample_pwd)+"=>")
    if sample_pwd== list(pwd):
        print("the pass is "+"".join(sample_pwd))
        break
