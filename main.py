import random

p1_value_1 = random.randint(1, 6)
p1_value_2 = random.randint(1, 6)

p2_value_1 = random.randint(1, 6)
p2_value_2 = random.randint(1, 6)

p1_sum = p1_value_1 + p1_value_2
p2_sum = p2_value_1 + p2_value_2

if p1_sum > p2_sum:
    print("Player 1 won")
elif p1_sum < p2_sum:
    print("Player 2 won")
else:
    print("AMAZING! It is DRAW!")
    