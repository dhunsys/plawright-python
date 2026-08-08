from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/place_order.feature")


class Calculator:
    def add(self, a, b):
        return a + b


@given("I have a calculator", target_fixture="calculator")
def calculator():
    return Calculator()


@when(
    parsers.parse("I add {first_number} and {second_number}"),
    target_fixture="result",
)
def add_numbers(calculator, first_number, second_number):
    return calculator.add(float(first_number), float(second_number))


@then(parsers.parse("the result should be {sum}"))
def verify_result(result, sum):
    assert result == float(sum)