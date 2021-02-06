def say(s, n = 2, m = 1):
    for i in range(1, n + 1):
        print(s * m)

say("Ha!")
print()

say("Ha!", 3)
print()

say("Ha!", m = 3)
print()

say( m = 3, s = "SSSSS!")
print()
