from math import ceil, sqrt

def get_distance(x, y):
    return ceil(sqrt((x * x) + (y * y)))

def main():

    total = int(input())
    for t in range(total):
        rs, rh = map(int, input().split())
        
        m = int(input())
        
        distances = []
        for _ in range(m):
            x, y = list(map(int, input().split()))
            d = get_distance(x, y)
            if d <= (rh + rs):
                distances.append((d, "R"))

        n = int(input())
        for _ in range(n):
            x, y = list(map(int, input().split()))
            d = get_distance(x, y)
            if d <= (rh + rs):
                distances.append((d, "Y"))


        score = 0
        prev_team = None
        distances.sort()
        for _, team in distances:
            if prev_team == None:
                prev_team = team

            if prev_team == team:
                score += 1
            else:
                break

        R = Y = 0
        if prev_team == "R":
            R = score
        else:
            Y = score 
            
        print("Case #{}: {} {}".format(t+1, R, Y))

main()