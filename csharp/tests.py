# from django.contrib.auth.models import User
# from django.test import TestCase
#
#
# class UsersTests(TestCase):
#
#     def test_wrong_password(self):
#         user = User.objects.create(username="test2", password='jopa')
#         self.assertTrue(user.check_password("jopa"), True)


import re

password = "R@m@_f0rtu9e$"
flag = 0
while True:
    if len(password) < 8:
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Not a Valid Password")

