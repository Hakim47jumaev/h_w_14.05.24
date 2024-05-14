oll_numbers = int(input())
bum = oll_numbers
number = 0
odd=0
while oll_numbers>0:
    number = oll_numbers%10
    if number%2!=0:
        odd+=1
    number=0
    oll_numbers//=10
if odd==len(str(bum)):
    print(True)
else:
    print(False)