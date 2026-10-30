def is_even(number: int) -> bool:
    """
Return True if number is even and False if it is odd.

:param number: Integer being checked.
:return: True if even, False if odd.
    """
    if number % 2 == 0:
        return True
    else:
        return False

def count_vowels(text: str) -> int:
    """
Count how many vowels are in text.
Uppercase and lowercase vowels both count.

:param text: String being checked.
:return: Total number of vowels.
    """
    count = 0

    for letter in text:
        if letter.lower() in "aeiou":
            count += 1

    return count

def celsius_to_fahrenheit(celsius: float) -> float:
    """
Convert a Celsius temperature to Fahrenheit.

:param celsius: Temperature in Celsius.
:return: Temperature in Fahrenheit.
    """
    processed_calculated_value = (celsius * 9 / 5) + 32
    return processed_calculated_value

def reverse_text(text: str) -> str:
    """
Return the characters in text in reverse order.

:param text: Text being reversed.
:return: Reversed text.
    """
    return text[::-1]

def larger_number(a: int, b: int) -> int:
    """
Return whichever of the two integers is larger.
If they are equal, return either value.

:param a: first integer.
:param b: second integer.
:return: larger integer.
    """
    if a > b:
        return a
    else:
        return b

def average_two(a: int, b: int) -> float:
    """
Calculate and return the average of two integers.

:param a: first integer.
:param b: second integer.
:return: average of both integers.
    """
    return (a + b) / 2

def can_afford(balance: float, cost: float) -> bool:
    """
Return True if balance is greater than or equal to cost.
Otherwise, return False.

:param balance: amount of money available.
:param cost: cost of the item.
:return: True if affordable, otherwise False.
    """
    if balance >= cost:
        return True
    else:
        return False

def repeat_text(text: str, times: int) -> str:
    """
Return one string containing text repeated the given number of times.

:param text: Text to repeat.
:param times: Number of repetitions.
:return: Repeated text.
    """
    return text * times

def contains_word(sentence: str, word: str) -> bool:
    """
Return True if word appears somewhere inside sentence.

Otherwise, return False.

:param sentence: Sentence being checked.
:param word: Word being searched for.
:return: True if found, otherwise False.
    """
    if word in sentence:
        return True
    else:
        return False

def calculate_tip(cost: float, percent: float) -> float:
    """
Calculate and return the amount of tip.

:param cost: Original cost.
:param percent: Tip percentage.
:return: Calculated tip amount.
    """
    return cost * percent / 100

def make_initials(first_name: str, last_name: str) -> str:
    """
Return the uppercase first letters of the two names.

:param first_name: Person's first name.
:param last_name: Person's last name.
:return: Uppercase initials.
    """
    return first_name[0].upper() + last_name[0].upper()

def percent_score(points: float, possible: float) -> float | None:
    """
Calculate what percentage of the possible points were earned.

Return None if possible is less than 1.

:param points: Points earned.
:param possible: Total possible points.
:return: Percentage earned or none if possible is less than 1.
    """
    if possible < 1:
        return None
    else:
        return (points / possible) * 100

def is_between(number: int, minimum: int, maximum: int) -> bool:
    """
Return True if number is between minimum and maximum,
including both limits.

:param number: Number being checked.
:param minimum: Lowest allowed number.
:param maximum: highest allowed number.
:return: True if inside the range, otherwise False.
    """
    if minimum <= number <= maximum:
        return True
    else:
        return False

def all_different(a: str, b: str, c: str) -> bool:
    """
Check if three strings are different.

:param a: First string.
:param b: Second string.
:param c: Third string.
:return: True if all three strings are different.
    """
    if a != b and a != c and b != c:
        return True
    else:
        return False

def average_three(a: int, b: int, c: int) -> float:
    """
Calculate and return the average of three integers.

:param a: First integer.
:param b: Second integer.
:param c: Third integer.
:return: Average of the three integers.
    """
    return (a + b + c) / 3

def describe_temperature(temperature: float, cold_limit: float, hot_limit: float) -> str:
    """
Return a string describing the temperature.

:param temperature: Temperature being checked.
:param cold_limit: Temperature below which it is cold.
:param hot_limit: Temperature above which it is hot.
:return: cold, hot, or comfortable.
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


def temperature_in_safe_range(celsius: float, minimum_f: float, maximum_f: float) -> bool:
    """
Convert Celsius to Fahrenheit and check if it is inside the safe range.

:param celsius: Temperature in Celsius.
:param minimum_f: Minimum safe temperature in Fahrenheit.
:param maximum_f: Maximum safe temperature in Fahrenheit.
:return: True if inside the range, otherwise False.
    """
    fahrenheit = celsius_to_fahrenheit(celsius)

    if minimum_f <= fahrenheit <= maximum_f:
        return True
    else:
        return False

def can_afford_with_tip(balance: float, cost: float, tip_percent: float) -> bool:
    """
Check if someone can afford a purchase including the tip.

:param balance: Amount of money available.
:param cost: Original cost of the purchase.
:param tip_percent: Tip percentage.
:return: True if affordable, otherwise False.
    """
    tip = calculate_tip(cost, tip_percent)
    total_cost = cost + tip

    if balance >= total_cost:
        return True
    else:
        return False

def meets_average(score1: float, score2: float, score3: float, required_average: float) -> bool:
    """
Check if three scores meet the required average.

:param score1: First score.
:param score2: Second score.
:param score3: Third score.
:param required_average: Average needed.
:return: True if the average is high enough, otherwise False.
    """
    average = average_three(score1, score2, score3)

    if average >= required_average:
        return True
    else:
        return False

def initials_match(first_name: str, last_name: str, expected_initials: str) -> bool:
    """
Check if someone's initials match the expected initials.

:param first_name: Person's first name.
:param last_name: Person's last name.
:param expected_initials: Initials being compared.
:return: True if the initials match, otherwise False.
    """
    initials = make_initials(first_name, last_name)

    if initials.upper() == expected_initials.upper():
        return True
    else:
        return False

if __name__ == "__main__":
    # Testing if the Basic functions work

    print(is_even(8))
    print(is_even(7))
    print(count_vowels("Hello World"))
    print(count_vowels("PYTHON"))
    print(celsius_to_fahrenheit(25))
    print(celsius_to_fahrenheit(0))
    print(reverse_text("robot"))
    print(reverse_text("Python"))
    print(larger_number(10, 20))
    print(larger_number(50, 30))
    print(average_two(10, 20))
    print(average_two(5, 15))
    print(can_afford(100, 75))
    print(can_afford(20, 50))
    print(repeat_text("Go!", 3))
    print(repeat_text("Hi", 2))
    print(contains_word("I like Python", "Python"))
    print(contains_word("Hello World", "Java"))
    print(calculate_tip(20.0, 15))
    print(calculate_tip(50.0, 20))
    print(make_initials("Leon", "Kennedy"))
    print(make_initials("Jai", "Rangray"))
    print(percent_score(18, 20))
    print(percent_score(5, 0))
    print(is_between(5, 1, 10))
    print(is_between(15, 1, 10))
    print(all_different("apple", "banana", "orange"))
    print(all_different("apple", "apple", "orange"))
    print(average_three(70, 80, 90))
    print(average_three(50, 60, 70))
    print(describe_temperature(10, 15, 25))
    print(describe_temperature(20, 15, 25))
    print(describe_temperature(30, 15, 25))

# Testing the Advanced functions
print(temperature_in_safe_range(0, 32, 100))
print(temperature_in_safe_range(30, 50, 80))
print(can_afford_with_tip(100, 80, 10))
print(can_afford_with_tip(50, 80, 15))
print(meets_average(80, 90, 100, 90))
print(meets_average(50, 60, 70, 80))
print(initials_match("Leon", "Kennedy", "LK"))
print(initials_match("leon", "kennedy", "lk"))
