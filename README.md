# Collatz Conjecture

A Python implementation for exploring the **Collatz conjecture**, a famous unsolved problem in mathematics involving simple operations on positive integers.

## Overview

The Collatz conjecture proposes that every positive integer eventually reaches 1 when repeatedly transformed according to two rules:

- If the current number is even, divide it by 2.
- If the current number is odd, multiply it by 3 and add 1.

Once the sequence reaches 1, it enters the cycle:

`1 → 4 → 2 → 1`

Despite the simplicity of these rules, the conjecture remains unproven for all positive integers.

This project implements the transformation process in Python and generates the sequence for a user-specified starting integer.

## Mathematical Definition

For a positive integer \(n\), define the Collatz function:

\[
T(n)=
\begin{cases}
n/2 & \text{if } n \equiv 0 \pmod{2}\\
3n+1 & \text{if } n \equiv 1 \pmod{2}
\end{cases}
\]

Repeated application of \(T\) generates the Collatz sequence.

## Implementation

```python
def collatz(number):
    """Return and print the next Collatz sequence value."""
    if number % 2 == 0:
        num_process = number // 2
    else:
        num_process = 3 * number + 1

    print(num_process, end=' ')
    return num_process


def main():
    number = int(input("Enter a positive integer: "))

    while number != 1:
        number = collatz(number)


if __name__ == "__main__":
    main()
```

## Example

Starting integer: `3`

Generated sequence:

```text
10 5 16 8 4 2 1
```

The sequence reaches 1 after seven transformations.

## How to Run

1. Install Python 3.
2. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/collatz-conjecture.git
   ```

3. Navigate to the project directory:

   ```bash
   cd collatz-conjecture
   ```

4. Run the program:

   ```bash
   python collatz.py
   ```

   On some systems, use `python3 collatz.py`.

5. Enter a positive integer when prompted.

## Mathematical and Computational Concepts

- Integer sequences and iterative functions
- Parity and modular arithmetic
- Conditional logic
- Iteration and termination conditions
- Computational exploration of a mathematical conjecture

## Scope and Limitations

This implementation generates a Collatz sequence for a single positive integer. It does not prove the conjecture, test all positive integers, or provide advanced statistical analysis.

The program currently assumes valid integer input and does not include input validation.

## Future Improvements

- Calculate the number of steps required to reach 1.
- Track the maximum value reached in a sequence.
- Compare sequences generated from different starting integers.
- Test a range of starting values and summarize the results.
- Visualize sequence lengths and maximum values.
- Add input validation and automated tests.

## About the Conjecture

The Collatz conjecture is an open problem in number theory. Although computational experiments have verified the behavior for very large ranges of starting values, these observations do not constitute a general mathematical proof.

This project provides a starting point for exploring the conjecture computationally.

## License

Released under the MIT License, if adopted. See the `LICENSE` file for the terms of use.
