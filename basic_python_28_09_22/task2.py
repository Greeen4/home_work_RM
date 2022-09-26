def triplets_number(arr, a, b, c):
    triplets = list()

    for k in range(len(arr)):
        for j in range(k):
            for i in range(j):

                if abs(arr[i]-arr[j]) <=a and abs(arr[j]-arr[k]) <= b \
                        and abs(arr[i]-arr[k]) <= c:
                    triplets.append((arr[i], arr[j], arr[k]))

    if triplets:
        print("There are ", len(triplets), "triplets: ", triplets)
    else:
        print("No triplets")

    return len(triplets)
                

if __name__ == '__main__':
    arr = list(map(int, input("Input a sequense separated by spaces: ").split()))
    a, b, c = [int(x) for x in input("Input a, b, c separated by spaces: ").split()]
    t_number = triplets_number(arr, a, b, c)
