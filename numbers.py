def sum_of_list(numbers):
    """Calculate the sum of numbers in a list."""
    return sum(numbers)


def average(numbers):
    """Calculate the average (mean) of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median_and_mode(numbers):
    """Calculate the median and mode of a list."""
    if not numbers:
        return None, None

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    # Calculate median
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]

    # Calculate mode
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    highest = max(frequency.values())
    mode = [key for key, value in frequency.items()
            if value == highest]

    return median, mode