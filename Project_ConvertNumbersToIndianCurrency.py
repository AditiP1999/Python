#2. Accept digit number from user and print it into word.
#Input: 9
#Output: Nine
#Input: -3
#Output Three

def performOperation(iNum):
    str = ''
    li = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    li_tens = ['','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
    li_el = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']

    if iNum < 0:
        iNum = iNum * -1

    #Handle the number in lakhs
    if iNum>99999 and iNum<10000000:
        iths = iNum // 100000
        if iths>0 and iths<9:
            str = str + ' '  + li[iths]
        elif iths>9 and iths<20:
            digit = iths // 10
            iths = iths % 10
            str = str + ' ' + li_el[digit]
        else:
            digit = iths // 10
            iths = iths % 10
            str = str + ' ' + li_tens[digit]
            str = str + ' '  + li[iths]

        str = str + " Lakhs "
        iNum = iNum % 100000

    #Handle the number in thousands
    if iNum>999 and iNum<100000:
        iths = iNum // 1000
        if iths>0 and iths<9:
            str = str + ' '  + li[iths]
        elif iths>9 and iths<20:
            digit = iths // 10
            iths = iths % 10
            str = str + ' ' + li_el[digit]
        else:
            digit = iths // 10
            iths = iths % 10
            str = str + ' ' + li_tens[digit]
            str = str + ' '  + li[iths]

        str = str + " Thousand "
        iNum = iNum % 1000

    #Handle the number in hundred
    if iNum>99 and iNum<1000:
        digit = iNum // 100
        iNum = iNum % 100
        str = str + li[digit] + ' Hundred'

    #Handle the number in tens
    if iNum>9 and iNum<100:
        digit = iNum // 10
        iNum = iNum % 10
        str = str + ' ' + li_tens[digit] 

    #Handle the single numbers
    if (iNum > len(li)-1) or (iNum < 0):
        str = 'Input is more than 10000000 Rupees'
    else:
        str = str + ' '  + li[iNum]

    return str
        
def main():
    iVal = input("Enter the number = ")
    iVal = int(iVal)
    output = performOperation(iVal)
    print(output.strip(),"Rupees Only")

if __name__ == "__main__":
    main()