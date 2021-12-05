#
# for temporaray_secret in secreto:
#     if
secret = input("type a word: ")
temporaray_secret = ""

typed = ['P', 'p', 'y', 'Y', 'T', 't', 'o', 'O', 'h', 'H', 'N', 'n']

attempt = 3

for secret_letter in secret:

    print(f"interaction for letter {secret_letter}")
    if attempt <= 0:

        print(temporaray_secret)

    elif secret_letter in typed:
        print(f"Good, a letter lyrics i wanted {secret_letter} ")
        temporaray_secret += secret_letter
        print(temporaray_secret)
    elif temporaray_secret != typed:
        attempt -= 1
        print(f"você so tem mais {attempt} tentativa!".upper())
        secret = input("jo: ")
        print(temporaray_secret)
    else:
        print(f"Good, a letter lyrics i wanted {secret_letter} ")
        temporaray_secret += "*"
        print(temporaray_secret)

print(temporaray_secret)


print(temporaray_secret)
if secret == temporaray_secret:
    print("você ganhou!")
