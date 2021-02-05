numbers = []

def isPrime(n) : #pasted from geeksforgeeks

    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        print(n)
        return True

    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False

    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    print(n)
    return True

interval1 = int(input("What is the lower threshold of the interval?:\t"))
interval2 = int(input("what is the upper threshold of the interval?:\t"))
while interval1 < interval2+1: 
    numbers.append(interval1)
    interval1 += 1
#print(numbers)
for i in range(len(numbers)):
    isPrime(numbers[i])
    
