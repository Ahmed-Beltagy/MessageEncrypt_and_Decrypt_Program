def Encrypt():
    import random
    temp = []
    n = random.randint(1, 20) * 10 - 10
    print()
    message = input("Please enter your message ")
    for i in message:
        x = ord(i)
        y = x + n
        b = chr(y)
        z = temp.append(b)
    EncryptedMessage = "".join(temp)
    print("*********************** The Encrypted Message Is: ********************")
    print()
    print(EncryptedMessage)
    print()
    print("### The Key to decrypt this message is: ", n, "....Please don't share this key with anyone, Except the person you want to decrypt your message.")
    print()
    re_write = input("Do you want to write again...(yes/no) ").lower()
    if re_write == "yes":
        Encrypt()
    else:
        print()
        back_to_hompage = input("Do you want to go back to homepage?....(yes/no) ").lower()
        if back_to_hompage == "yes":
            Introduction()
            Choice()
        else:
            exit()
def Decrypt():
    print()
    message = input("Please enter the message you want to decrypt.... ")
    print()
    key = int(input("please enter the key..... "))
    temp = []
    for i in message:
        x = ord(i)
        y = x - key
        z = chr(y)
        List = temp.append(z)
    DecryptedMessage = "".join(temp)
    print("********************** The Decrypted Message Is: **************************")
    print()
    print(DecryptedMessage)
    print()
    re_enter_message = input("Do you want to Re-enter the message....(yes/no) ").lower()
    if re_enter_message == "yes":
        Decrypt()
    else:
        print()
        back_to_homepage = input("Do you want to go back to homepage?...(yes/no) ").lower()
        if back_to_homepage == "yes":
            Introduction()
            Choice()
        else:
            exit()
def Introduction():
    print()
    print("This is an app to encrypt and decrypt your messages to keep it safe. ")
    print()
    print("The person that you are going to send him the encrypted message should have the app to be able to decrypt the message. ")
    print()
    print("1- Encrypt")
    print("2- Decrypt")
    print()
def Choice():
    print()
    choice = input("Please select which one do you want to do....(1/2) ")
    print()
    if choice == "1":
        Encrypt()
    if choice == "2":
        Decrypt()

Introduction()
Choice()
