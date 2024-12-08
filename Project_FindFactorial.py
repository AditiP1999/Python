#Write a program to find factorial of given number.
#Input: 5
#Output: 120 (5*4*3*2* 1)
#Input: -5
#Output: 120 (5*4*3*2*1)
#Input: 4 
#Output: 24 (4*3*2*1)

def performOperation(iNum):
    if iNum < 0:
        iNum = iNum * -1

    result = 1
    for i in range(1,iNum+1):
        result = result * i
    return result
        
def main():
    iVal = input("Enter the number = ")
    iVal = int(iVal)
    output = performOperation(iVal)
    print(output)

if __name__ == "__main__":
    main()