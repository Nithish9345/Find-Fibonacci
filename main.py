def fibnocci_series(f):
    if f == 0:
        return 0
    if f == 1:
        return 1

    return fibnocci_series(f-1) + fibnocci_series(f-2)

print(fibnocci_series(6))

"""Find Fibonacci
The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

Given a number A, find and return the Ath Fibonacci Number using recursion.

Given that F0 = 0 and F1 = 1.

Example Input

Input 1:
A = 2

Input 2:
A = 9

Example Output

Output 1:
1

Output 2:
34"""