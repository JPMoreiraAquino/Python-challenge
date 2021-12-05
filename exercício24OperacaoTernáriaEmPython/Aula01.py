logged_user = True
# we can use this method
# if logged_user:
#     msg = 'logged in user'
# else:
#     msg = 'user needs to login'

# or we can use this method with shortcuts
msg = 'logged in user' if logged_user else 'user needs to login '
print(msg)
