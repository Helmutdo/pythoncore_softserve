def solution(number):
    """
    Return sum of all multiples of 3 or 5 below number.
    Multiples of both counted once. Negative input returns 0.
    """
    if number <= 0:
        return 0
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)
