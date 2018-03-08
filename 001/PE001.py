
def series_sum(x):
    k=(x+1)*x/2
    return k

P=int(input("Enter the range : "))-1

p3=P//3
p5=P//5
p15=P//15

Sum=series_sum(p3)*3 + series_sum(p5)*5 - series_sum(p15)*15
print(int(Sum))
