sal = int(input('Enter your salary: '))
if sal<10000:
    hra = 0.67*sal
    da = 0.73*sal
elif sal<=20000:
    hra = 0.69*sal
    da = 0.76*sal
else:
    hra = 0.73*sal
    da = 0.8*sal
gs = hra + da +sal
print("Gross Sal: ",gs)

# hra,da = (0.67*sal,0.73*sal) if sal<10000 else (0.69*sal,0.76*sal) if sal<20000 else (0.73*sal,0.8*sal)

x = "Teja" if True else "Vorsu"
print(x)

