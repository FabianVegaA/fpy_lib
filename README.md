# Fpylib

This is a library to do functional programming in Python.

[![Build Status](https://app.travis-ci.com/FabianVegaA/fpy_lib.svg?branch=main)](https://app.travis-ci.com/FabianVegaA/fpy_lib)
## Index

- [Fpylib](#fpylib)
  - [Index](#index)
  - [Features](#features)
    - [Intelligents Ranges with `irange`](#intelligents-ranges-with-irange)
    - [Lazyness to functions](#lazyness-to-functions)
    - [Compose and paralelize functions](#compose-and-paralelize-functions)
  - [Functional Programming in Python?](#functional-programming-in-python)
    - [Functor](#functor)
      - [Fmap](#fmap)
    - [Applicative](#applicative)
    - [Monad](#monad)
      - [Bind (>>)](#bind-)
      - [Unit](#unit)
    - [Maybe](#maybe)
    - [FList](#flist)

## Features

### Intelligents Ranges with `irange`

This library provides a function `irange` that behaves like `range` but is capable to understand the range that is needed with first, second and the final values. It is receive a Number or a String and return a generator.

To use it, you can use the following syntax:

```python
from fpylib.irange import irange

# Range finite with step 1
list(irange(1, ..., 10))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(irange(1.1, ..., 5.2))  # Output: [1.1, 2.1, 3.1, 4.1, 5.1]
list(irange("a", ..., "l"))  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
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
from fpylib.lazyness import lazy_eval

@lazy_eval
def sum3(x, y, z):
    return x + y + z

sum3(1)       # Output: A functions that receive 2 arguments.
sum3(1, 2)    # Output: A functions that receive one arguments.
sum3(1, 2, 3) # Output: 6
```

And to make the class `Foo` lazy, the following code:

```python
from fpylib.lazyness import lazy_class

@lazy_class
class Foo:
  def __init__(self, x):
    self.x = x

  def sum3(self, y, z):
    return self.x + y + z

foo = Foo(1)
sum_five = foo.sum3(2, 3) # Output: A functions that receive one arguments.
sum_five(4)               # Output: 9
```

This is a very useful feature to make a function lazy, and do not use the function `partial` to do not evaluate directly the function.

### Compose and paralelize functions

Into this library, there is a function `compose` that can be used to compose two or more functions, to make pipelines to process data. Also, there is a function `parallelize` that can be used to paralelize a function.

For example, the following code:

```python
from fpylib.composer import compose

decendent_pair_numbers = compose(
  lambda x: list(range(x)),
  lambda x: x[::-1],
  lambda x: x[::2]
)

decendent_pair_numbers(5) # Output: [4, 2, 0]

```

And the following code:

```python
from fpylib.composer import parallelize

def median(*xs):
    if len(xs) % 2 == 0:
        return (xs[len(xs) // 2 - 1] + xs[len(xs) // 2]) / 2
    return xs[len(xs) // 2 + 1]


describe = parallelize(
    lambda *xs: sum(xs) / len(xs),
    median,
    max,
    min,
)

describe(1, 2, 3, 4, 5, 6) # Output: (3.5, 3.5, 6, 1)

```

In this case, the functions into parallelize receive the same arguments, but it can receive a agument different to each function with the parameter `uniqui_intput`. For example:

```python
from fpylib.composer import parallelize

func_parallelized = parallelize(
    sorted,
    sum,
    max,
    min,
)

list_1 = [1, 4, 2, 3, 4, 1, 2, 3, 4, 10]
list_2 = [5, 6, 7, 8, 9, 10]
list_3 = [-1, -5, 100, 19, 99]

func_parallelized(
  list_1, list_2, list_3, list_3, uniqui_intput=False
) # Output: ([1, 1, 2, 2, 3, 3, 4, 4, 4, 10], 45, 100, -5)

```

## Functional Programming in Python?

### Functor

The Functors are a mathematical concept that is used to describe a value wrapped in a context.

In Fpylib, the functor is implemented by the class `Functor`, that inherits from `Generic[T]` where `T` is the type of the value. It also is an immutable class. This class would be used to build new functors for that is need to implement the `fmap` function.

#### Fmap

This function is a general `fmap` function, that used to map a function over a functor. For example:

```python
from fpylib.functors import fmap

fmap(lambda x: x + 1, Functor(1)) # Output: Functor 2
```

### Applicative

The usefull of this module is that it provide of `apply`, this is used to apply a wrapped function over a wrapped value.

For example:

```python
from fpylib.functors import apply

apply(Functor(lambda x: x + 1), Functor(1)) # Output: Functor 2
```

Other functions that can be used with this module is:

```python
from fpylib.functors import lift_a2

lift_a2(lambda x, y: x * y, Functor(5), Functor(3)) # Output: Functor 15
```

This is the same to do:

```python
from fpylib.functors import apply

apply(fmap(func, f1), f2)
```

> Yes this is copy from `liftA2` in Haskell.

### Monad

I think that the best way to explain this concept is:

> "In short, a monad is a way to structure computations in terms of values and sequences of computations using typed values" [All About Monads](https://wiki.haskell.org/All_About_Monads)

#### Bind (>>)

This function to bind a function over a monoid value. For example:

```python
Monad(1) >> (lambda x: x + 1) # Output: Monad 2
```

Or even:

```python
example = (
  Monad(1)
  >> (lambda x: x + 1)
  >> (lambda x: x ** 2)
  >> (lambda x: x // 3)
  >> (lambda x: x * 10)
  >> str

) # Output: Monad "10"
```

#### Unit

This is a function to wrap a value in a monad. For example:

```python
from fpylib.functors import unit

m = unit(SomeMonad, 1) # Output: SomeMonad 1
```

> This will be more interesting later when we will use the [FList](#flist) and [Maybe](#maybe) monads.

### Maybe

This is Functor, Applicative and Monad. It is used to keep a information flow without errors.

For example:

```python
from fpylib.functors import Maybe, Just, Nothing

def div(x: Number, y: Number) -> Maybe[Number]:
    if y == 0:
        return Nothing()
    return Just(x / y)

div(1, 0) # Output: Nothing
div(1, 2) # Output: Just 0.5
```

Or better:

```python
from fpylib.functors import Maybe, Just, Nothing, unit

def div(x: Number, y: Number) -> Maybe[Number]:
  return unit(Maybe, x / y)

div(1, 0) # Output: Nothing
div(1, 2) # Output: Just 0.5
```

Of this way, the function `div` can be used to divide two numbers without errors, and build pipelines to process data in a safe way.

> Observe that if the second argument of the function `div` causes an error this function will return `Nothing`.

Like the next example:

```python
from fpylib.functors import unit

def email_process(email: str) -> Maybe[str]:
    return (
        unit(Maybe, email)
        >> (lambda s: s.strip())
        >> (lambda s: s.lower())
        >> (lambda s: None if "@" not in s else s)
        >> (lambda s: None if any(c in s for c in "!#$%&*+-/=?^_`{|}~") else s)
    )

email_process("  Fpylib@email.com   ") # Output: Just fpylib@email.com
email_process("  This is not a email   ") # Output: Nothing
```

### FList

This is other implemention of the Applicative and Functor. It would be used as a list of values.

Some of its features are:

- It does not store None values.
- It is a immutable list.
- It have its own implementation of the `fmap` and `apply` functions.

```python
fl = unit(FList, irange(1, ..., 4)) # Output: FList [1,2,3]

# How to use the fmap function
fmap(lambda x: x + 1, fl) # Output: FList [2,3,4]

# And to use the apply function
fl_funcs = unit(FList,[(lambda x: x * 2),(lambda x: x + 3)])

apply(fl_funcs, fl) # Output: FList [2,4,6,4,5,6]
```

To the case of be an empty list obtain a `EmptyFList`. For example:

```python
empty_fl = unit(FList, []) # Output: EmptyFList
```

This also have a lot of functions to manipulate Flist's.

| Name      | Description                                                 | signature                                                       |
| --------- | ----------------------------------------------------------- | --------------------------------------------------------------- |
| concat    | Concatenate two or more FList.                              | `(function) concat: (*ls: FList[T]) -> FList[T]`                |
| head      | Get the first element of a FList.                           | `(function) head: (l: FList[T]) -> T`                           |
| last      | Get the last element of a FList.                            | `(function) last: (l: FList[T]) -> T`                           |
| tail      | Get the all elements of a FList except the first one.       | `(function) tail: (l: FList[T]) -> FList[T]`                    |
| init      | Get all elements of a FList except the last one.            | `(function) init: (l: FList[T]) -> FList[T]`                    |
| uncons    | Get the first element of a FList and the rest of the FList. | `(function) uncons: (l: FList[T]) -> Maybe[Tuple[T, FList[T]]]` |
| singleton | Create a FList with a single element.                       | `(function) singleton: (x: T) -> FList[T]`                      |
| null      | Verify if a FList is empty.                                 | `(function) null: (l: FList[T]) -> bool`                        |
| length    | Get the length of a FList.                                  | `(function) length: (l: FList[T]) -> int`                       |
| reverse   | Reverse a FList.                                            | `(function) reverse: (l: FList[T]) -> FList[T]`                 |
