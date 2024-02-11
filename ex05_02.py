import re

def generator_numbers(text):
   
    pattern = r"\b\d+\b"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text, func):
   
    numbers = func(text)

   
    total = sum(numbers)

    return total




text = """
The company's revenue in January was $10,000.
In February, it was $15,000.
In March, it was $20,000.
"""

total_profit = sum_profit(text, generator_numbers)


print(total_profit)  # Output: 45000.0