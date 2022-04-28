'''
công thức chuyển đổi độ C --> F
F = C * 9/5 +32
'''
def convert_to_f():
    n = 0
    while True:
        c = input('please enter C degree: ')
        if c:
            c = float(c)
            f = round(c * 9/5 + 32, 1)
            print(f'{c} C degree has F degree is: {f}')
            break
        else:
            print('nhap lai')
            n += 1
            if n>2:
                print('ban da nhap sai qua nhieu lan')
                break


def main():
    convert_to_f()


if __name__ == '__main__':
    main()

