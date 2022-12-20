#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = int(my_list_1)
            b = int(my_list_2)
            result.append(a / b)
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except (TypeError, ValueError):
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")

        finally:
            pass
    return result
