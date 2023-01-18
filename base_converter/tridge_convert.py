class Transformer(object):
    """Convert numbers from base 10 integers to base N strings and back again.
        Sample usage:
        # >>> base20 = Transformer('0123456789abcdefghij')
        # >>> base20.from_decimal(1234)  # '31e'
        # >>> base20.to_decimal('31e')  # 1234
    """
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        if isinstance(number, str):
            n = 0
            for digit in number:
                n = n * len(fromdigits) + fromdigits.index(digit)
            return n
        else:
            if number == 0:
                return todigits[0]
            digits = []
            while number:
                digits.append(todigits[number % len(todigits)])
                number //= len(todigits)
            return ''.join(digits[::-1])


binary_transformer = Transformer('01')
print(f"binary_transformer from decimal result is: {binary_transformer.from_decimal(1234)}")
print(f"binary_transformer to decimal result is: {binary_transformer.to_decimal('10011010010')}")
hex_transformer = Transformer('0123456789ABCDEF')
print(f"hex_transformer from decimal result is: {hex_transformer.from_decimal(1234)}")
print(f"hex_transformer to decimal result is: {hex_transformer.to_decimal('4D2')}")
base62_transformer = Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
print(f"base62_transformer from decimal result is: {base62_transformer.from_decimal(1234)}")
print(f"base62_transformer to decimal result is: {base62_transformer.to_decimal('Tu')}")
