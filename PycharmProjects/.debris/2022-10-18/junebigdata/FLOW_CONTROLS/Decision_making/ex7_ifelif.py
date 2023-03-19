#sub1,2,3,4/50
#total marks
#180+ grade a+
#160-170 grade a
#140-159 grade b+
#120-139 b
#100-119 c+
#80-99 c
#<80 fail
subject1=int(input('enter mark'))
subject2=int(input('enter mark'))
subject3=int(input('enter mark'))
subject4=int(input('enter mark'))
totalmarks=subject4+subject3+subject2+subject1
if(totalmarks>180):
    print('Your grade is A+',totalmarks)
elif(totalmarks>160)&(totalmarks<180):
    print('Your grade is A',totalmarks)
elif(totalmarks>140)&(totalmarks<159):
    print('Your grade is B+',totalmarks)
elif(totalmarks>120)&(totalmarks<139):
    print('your grade is B',totalmarks)
elif(totalmarks>100)&(totalmarks<119):
    print('Your grade is C+',totalmarks)
elif(totalmarks<99)&(totalmarks>80):
    print('Your grade is C')
else:
    print('FAILED')