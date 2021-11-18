# fpy_lib

This is a library to do functional programming in Python.

## Index

- [fpy_lib](#fpy_lib)
  - [Index](#index)
  - [Features](#features)
    - [Intelligents Ranges with `irange`](#intelligents-ranges-with-irange)
    - [Lazyness to functions](#lazyness-to-functions)
    - [Compose and paralelize functions](#compose-and-paralelize-functions)

## Features

### Intelligents Ranges with `irange`

This library provides a function `irange` that behaves like `range` but is capable to understand the range that is needed with first, second and the final values. It is receive a Number or a String and return a generator.

To use it, you can use the following syntax:

```python
# # Range finite with step 1
list(irange(1, ..., 10))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(irange(1.1, ..., 5.2))  # Output: [1.1, 2.1, 3.1, 4.1, 5.1]
list(irange("a", ..., "l"))  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
list(irange("A", ..., "M", final_include=True))  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

# # Range finite with step custom
list(irange(0, 2, 12))  # Output: [0, 2, 4, 6, 8, 10]
list(irange(0.1, 0.5, 2.5))  # Output: [0.1, 0.5, 0.9, 1.3, 1.7000000000000002, 2.1]
list(irange("a", "c", "l"))  # Output: ['a', 'c', 'e', 'g', 'i', 'k']

# # Range infinite with step custom
list(irange(0, 5))  # Output: [0, 1, 2, 3, 4, 5 ...] An infinite range.
list(irange(0.1, 0.6))  # Output: [0.1, 0.7, 1.2999999999999998 ...] An infinite range.
list(irange("a"))  # Output: ['a', 'b', ..., 'z', 'aa', 'ab', ...] An infinite range.

```

### Lazyness to functions

### Compose and paralelize functions
