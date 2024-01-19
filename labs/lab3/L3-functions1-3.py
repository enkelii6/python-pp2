def solve(numheads, numlegs):
    x = numlegs - numheads * 2
    print("Chickens:", x/2, "Rabbits:", numheads - x/2)

solve(int(input("Heads:")), int(input("Legs:")))
