"""
Game Time with Minutes
Read the start time and end time of a game, in hours and minutes (initial hour, initial minute, final hour, final minute). Then print the duration of the game, knowing that the game can begin in a day and finish in another day,

Obs.: With a maximum game time of 24 hours and the minimum game time of 1 minute.

Input
Four integer numbers representing the start and end time of the game.

Output
Print the duration of the game in hours and minutes, in this format: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” . Which means: the game lasted XXX hour(s) and YYY minutes.
"""

a,b,c,d = map(int, input().split())

if a<=c:
    if b<=d:
        print(f"O JOGO DUROU {c-a} HORA(S) E {d-b} MINUTO(S)")
    else:
       print(f"O JOGO DUROU {c-a} HORA(S) E {(b+58)-d} MINUTO(S)")
else:
    if b<=d:
        print(f"O JOGO DUROU {(a+24)-c} HORA(S) E {d-b} MINUTO(S)") 
    else:
       print(f"O JOGO DUROU {(a+24)-c} HORA(S) E {(b+58)-d} MINUTO(S)") 
