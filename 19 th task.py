class PowerCalculator:
    def calculate_power(self, x, n):
        # Check if n is a non-negative integer
        if not isinstance(n, int) or n < 0:
            raise ValueError("Exponent (n) must be a non-negative integer")

        result = 1
        base = x

        while n > 0:
            # If n is odd, multiply the result by the current base
            if n % 2 == 1:
                result *= base

            # Square the base for the next iteration
            base *= base

            # Divide n by 2 to move to the next bit
            n //= 2

        return result


# Example usage:
if __name__ == "__main__":
    calculator = PowerCalculator()

    try:
        # Take user input for base (x) and exponent (n)
        base_input = float(input("Enter the base (x): "))
        exponent_input = int(input("Enter the exponent (n): "))

        # Calculate the power using the class method
        result = calculator.calculate_power(base_input, exponent_input)

        # Display the result
        print(f"{base_input} raised to the power of {exponent_input} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
