totalclass=int(input('enter total class held'))
attendence=int(input('enter class attended by a student'))
percentofclassattended=attendence/totalclass*100
if(percentofclassattended>75):
    print('eligible',percentofclassattended)
else:
    print('not eligible',percentofclassattended)