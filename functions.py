from math import factorial
from sympy import primerange


def calc_factorial(number):
    if number < 0:
        return "Não há fatorial de números negativos."

    return factorial(number)


def calc_primorial(number):
    if number < 0:
        return "Não há primorial de números negativos."

    primes = list(primerange(1, number + 1))
    result = 1

    for prime in primes:
        result *= prime

    return result


def convert_temperature(temperature, scale):
    match scale:
        case "Celsius":
            return (temperature * 9 / 5) + 32
        case "Fahrenheit":
            return (temperature - 32) * 5 / 9
