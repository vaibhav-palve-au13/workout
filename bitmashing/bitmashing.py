from BitMashing.addition import Addition

from BitMashing.substraction import Substraction

from BitMashing.multiplection import Multiplection

from BitMashing.division import Division


if __name__ == "__main__":
    add = Addition(1, 5)

    print( f" Addition of {add.number1} and {add.number2} no. = {add.addition()}")

    sub = Substraction(4, 3)

    print( f" Substraction of {sub.number1} and {sub.number2} no. = {sub.substraction()}")

    mul = Multiplection(2)

    print( f" Multiplication of {mul.number1} of 2  no. = {mul.multiplection()}")

    div = Division(6)

    print(f" Division of {div.number1} 2 no.  = {div.division()}")