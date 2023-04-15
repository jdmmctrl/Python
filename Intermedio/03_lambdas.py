
### Lambdas ###

# Las lambdas son funciones anónimas, es decir, funciones sin nombre.

# Las lambdas son funciones que se pueden usar en cualquier lugar donde se necesite una función.

def sum_two_values(
    first_value, second_value): return first_value + second_value


print(sum_two_values(2, 4))


def multiply_values(
    first_value, second_value): return first_value * second_value - 3


print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))
