def main():
    total = int(input())
    for t in range(total):
        _ = int(input())
        total = 0
        prefix_sum = []
        for num in map(int, input().split()):
            if num >= 0:
                pln = len(prefix_sum)
                for idx in range(pln):
                    prefix_sum[idx] += num
                    total += prefix_sum[idx]
                
                total += num
                prefix_sum.append(num)
            else:
                new_prefix_sum = []
                for prefix in prefix_sum:
                    lsum = prefix + num
                    if lsum < 0:
                        continue

                    total += lsum
                    new_prefix_sum.append(lsum)    
                prefix_sum = new_prefix_sum

        print(f"Case #{t+1}: {total}")
           
main()