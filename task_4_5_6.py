class WareHouse:
    info = {
        'goods': [],
        'items': 0
    }
    capacity = 10

    @classmethod
    def acceptance(cls, product):
        checked_list = []
        if cls.info['items'] <= cls.capacity:
            try:
                if len(cls.info['goods']) > 0:
                    for item in cls.info['goods']:
                        if item[0] == product.name:
                            item[1] += 1
                        checked_list.append(item[0])
                    if product.name not in checked_list:
                        cls.info['goods'].append([product.name, 1])
                else:
                    cls.info['goods'].append([product.name, 1])
                cls.info['items'] += 1
            except ValueError:
                print('Введены некорректные данные, повнимательнее:)')
        else:
            print('Склад полностью заполнен! Попробуйте выполнить списание.')

    @classmethod
    def write_off(cls, product):
        checked_list = []
        if cls.info['items'] != 0:
            try:
                for item in cls.info['goods']:
                    if item[0] == product.name:
                        item[1] -= 1
                        cls.info['items'] -= 1
                        if item[1] <= 0:
                            cls.info['goods'].remove(item)
                    checked_list.append(item[0])
                if product.name not in checked_list:
                    print('Данного товара нет на складе!')
            except ValueError:
                print('Введены некоректные данные! Попробуйте чуть внимательнее)')
        else:
            print('Склад пуст! Списывать нечего!:)')


class Equipment:
    def __init__(self, colour, brand, multitask=False):
        self.colour = colour
        self.brand = brand
        self.multitask = multitask


class Printer(Equipment):
    name = 'Printer'

    def __init__(self, colour, brand, multitask, color_print, print_speed, cartridge_volume):
        super().__init__(colour, brand, multitask)
        self.print_speed = print_speed
        self.color_print = color_print
        self.cartridge_volume = cartridge_volume


class Scanner(Equipment):
    name = 'Scanner'

    def __init__(self, colour, brand, scan_speed, scan_quality, multitask):
        super().__init__(colour, brand, multitask)
        self.scan_speed = scan_speed
        self.scan_quality = scan_quality


class Xerox(Equipment):
    name = 'Xeroxу'

    def __init__(self, colour, brand, xerox_speed, multitask, color_print=False):
        super().__init__(colour, brand, multitask)
        self.xerox_speed = xerox_speed
        self.color_print = color_print


if __name__ == '__main__':
    s_1 = Scanner('black', 'Samsung', 1200, 'high', multitask=True)
    s_2 = Scanner('white', 'Lenovo', 1250, 'medium', multitask=True)
    print(s_1.colour, s_1.brand, s_1.scan_quality, s_1.scan_speed, s_1.multitask)
    p_1 = Printer('white', 'Asus', False, True, 150, 23)
    print(p_1.colour, p_1.print_speed, p_1.color_print)
    x_1 = Xerox('blue', 'Xerox', 1150, multitask=False, color_print=True)
    print(x_1.color_print, x_1.xerox_speed, x_1.brand)
    print()
    WareHouse.acceptance(s_1)
    WareHouse.acceptance(p_1)
    WareHouse.acceptance(s_2)
    WareHouse.acceptance(x_1)
    print(WareHouse.info)
    WareHouse.write_off(s_1)
    WareHouse.write_off(x_1)
    WareHouse.write_off(x_1)
    print(WareHouse.info)
