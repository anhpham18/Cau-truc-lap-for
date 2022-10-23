i = 0
socuoi = 0
sodau = 0

num = input ("Nhập 2 số bất kỳ, cách nhau bằng 1 khoảng trắng: ")

haiso = num.split()
for so in haiso:
    i += 1
    soint = int(so)
    if i == 1:
        sodau += soint
    if i == 2:
        socuoi += soint

if socuoi < sodau:
    print ("số cuối cần lớn hơn số đầu!")
else:
    for j in range (sodau, socuoi +1):
        if j % 3 == 0 and j % 5 == 0:
            print ("FizzBuzz")
        elif j % 3 == 0:
            print ("Fizz")
        elif j % 5 == 0:
            print ("Buzz")
        else:
            print (j)