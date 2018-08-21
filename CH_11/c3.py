def curve_pre():
    a = 25
    def curve(x):
        return a * (x ** 2)
    return curve

f = curve_pre()
print(f(2))
