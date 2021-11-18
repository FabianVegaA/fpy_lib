# Fpylib

This is a library to do functional programming in Python.

## Index

- [Fpylib](#fpylib)
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
# Range finite with step 1
list(irange(1, ..., 10))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(irange(1.1, ..., 5.2))  # Output: [1.1, 2.1, 3.1, 4.1, 5.1]
list(irange("a", ..., "l"))  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
list(irange("A", ..., "M", final_include=True))  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

# Range finite with step custom
list(irange(0, 2, 12))  # Output: [0, 2, 4, 6, 8, 10]
list(irange(0.1, 0.5, 2.5))  # Output: [0.1, 0.5, 0.9, 1.3, 1.7000000000000002, 2.1]
list(irange("a", "c", "l"))  # Output: ['a', 'c', 'e', 'g', 'i', 'k']

# Range infinite with step custom
list(irange(0, 5))  # Output: [0, 1, 2, 3, 4, 5 ...] An infinite range.
list(irange(0.1, 0.6))  # Output: [0.1, 0.7, 1.2999999999999998 ...] An infinite range.
list(irange("a"))  # Output: ['a', 'b', ..., 'z', 'aa', 'ab', ...] An infinite range.

```

### Lazyness to functions

Inspired by Haskell, this library provides a function `lazy_eval` that can be used to make a function lazy. This function is a decorator that can be used to make a function lazy, and `lazy_class` also a decorator to classes that can be used to make all methods lazy.

For example, the following code:

```python
@lazy_eval
def sum3(x, y, z):
    return x + y + z

sum3(1)       # Output: A functions that receive 2 arguments.
sum3(1, 2)    # Output: A functions that receive one arguments.
sum3(1, 2, 3) # Output: 6
```

And to make the class `Foo` lazy, the following code:

```python
@lazy_class
class Foo:
  def __init__(self, x):
    self.x = x

  def sum3(self, y, z):
    return self.x + y + z

foo = Foo(1)
sum1 = foo.sum3(2, 3) # Output: A functions that receive one arguments.
sum1(4) # Output: 9
```

This is a very useful feature to make a function lazy, and do not use the function `partial` to do not evaluate directly the function.

### Compose and paralelize functions
