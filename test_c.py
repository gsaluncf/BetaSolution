from c import Car


def test_accelerate_from_0():
    my_car = Car()
    my_car.accelerate()
    my_car.goto_mechanic()
    assert my_car.speed == 5


def test_accelerate_and_break():
    my_car = Car()
    my_car.accelerate()
    my_car.brake()
    assert my_car.speed == 0
