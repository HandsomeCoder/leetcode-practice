def main():

    total = int(input())
    for t in range(total):
        m, n, p = map(int, input().split())
        
        john_steps = None
        max_steps = [0 for  _ in range(n)]
        for i in range(m):
            steps = list(map(int, input().split()))

            for j in range(n):
                max_steps[j] = max(max_steps[j], steps[j])

            if (i+1) == p:
                john_steps = steps


        for i in range(n):
            max_steps[i] = abs(max_steps[i] - john_steps[i])


        print(f"Case #{t+1}: {sum(max_steps)}")

main()