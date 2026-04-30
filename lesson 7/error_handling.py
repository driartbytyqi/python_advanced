

numri1 = 10

numri2 = 0

try:
    rezultati = numri1/numri2

except ZeroDivisionError:
    print("hejj nuk mundem me pjestu me 000")



numri3 = 20

numri4 = 2

try:
    rezultati = numri3/numri4

except ZeroDivisionError:
    print("hejj nuk mundem me pjestu me 000")
else:
    print("pjestimi eshte i pranushem")


mesazhi = "hello"
try:
    textToInt = int(mesazhi)
except Exception as e:
    print("ka ndodh nje error",e)

def divide_numbers(a,b):
    try:
        rezultat = a/b
        print("rezultati eshte : ",rezultat)

    except ZeroDivisionError:
        print("hej ke tentu me pjestu me 0")

    except TypeError:
        print("invalid type for division")
    except Exception as a:
        print("ka ndhodhe nje error",a)
        
divide_numbers(10,2)