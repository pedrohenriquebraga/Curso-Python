def ValidaOp(msg, vop=False):
    while True:
        try:
            num = int(input(msg))
        except:
            print("\033[1;31mERRO!!DIGITE UM NÚMERO VALIDO!!\033[m")
            continue
        else:
            if vop is True:
                if num > 3 or num < 0:
                    print("\033[1;31mERRO!!DIGITE UMA OPÇÃO VÁLIDA\033[m")
                else:
                    return num
            else:
                return num
