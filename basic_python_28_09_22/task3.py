from collections import Counter
import heapq


if __name__ == "__main__":
    arr = list(map(int, input("Input a sequense separated by spaces: ").split()))
    k = int(input("Please input k: "))

    if k == len(arr):
        print(arr)
        raise(0)
   
    count = Counter(arr)   

    print(heapq.nlargest(k, count.keys(), key=count.get))
