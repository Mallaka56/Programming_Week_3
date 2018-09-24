
def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        print('True')
    else:
        if oldpassword == newpassword or len(newpassword) <6:
            print('False')

