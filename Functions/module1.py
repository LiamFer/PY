def make_car(
        manufacturer:str,
        model:str,
        **plus_info):
    '''This function returns a dictionary with informations about a car.'''
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in plus_info.items():
        car[key] = value
    print(car)
    return car
