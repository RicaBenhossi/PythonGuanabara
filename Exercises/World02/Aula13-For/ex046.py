from time import sleep
from emoji import emojize
for x in range(10, 0, -1):
    print(str(x) + ('.' * 3))
    sleep(1)
print(emojize('YEY seus FDP! :unamused: :fireworks:', use_aliases=True))
