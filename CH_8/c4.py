def city_temp(**param):
    for key, value in param.items():
        print(key + ' : ' + value)

a = {'bj':'32c', 'sh':'31c'}
city_temp(bj = '32c', xm = '23c', sh = '31c')
city_temp(**a)