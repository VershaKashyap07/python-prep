r ,c = 3, 2
def variation1B(r,c):
    r =r-1
    c =c-1
    n_r = r-c
    
    r_fact= findfact(r)
    c_fact= findfact(c)
    n_r_fact= findfact(n_r)
    
    return int((r_fact/c_fact)/n_r_fact)
    
        
    
def findfact(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact
    
#print(variation1B(r,c))
#print(findfact(4))

def variation1_better(r,c):
    element  = ncr(r-1,c-1)
    return element

def ncr(n,r):
    res = 1
    for i in range(r):
        res =  res*(n-i)
        res= res//(i+1)
    return res
    
print(variation1_better(r,c))

n=5


def variation2B(n):
    for c in range(1, n+1):
        print(ncr(n-1,c-1), end =" ")
    print()

def ncr(n,r):
    res = 1
    for i in range(r):
        res =  res*(n-i)
        res= res//(i+1)
    return res
    
print(variation2B(n))

def pascalTriangleVariation2(n):
    ans = 1
    print(ans, end=" ") # printing 1st element

    #Printing the rest of the part:
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end=" ")
    print()

print(pascalTriangleVariation2(n))

def generateRow(row):
    ans = 1
    ansRow = [1] #inserting the 1st element
    
    #calculate the rest of the elements:
    for col in range(1, row):
        ans *= (row - col)
        ans //= col
        ansRow.append(ans)
    return ansRow

def pascalTriangle(n):
    ans = []
    
    #store the entire pascal's triangle:
    for row in range(1, n+1):
        ans.append(generateRow(row))
    return ans

if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()