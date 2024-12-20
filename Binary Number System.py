#Conversion from decimal number to binary number
dec_num=int(input("Enter the number: "))
ans=0
power=1
while(dec_num>0):
    rem=dec_num%2
    dec_num=dec_num//2
    ans+=rem*power
    power*=10
print("Conversion from decimal number to binary number: ",ans)