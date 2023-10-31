<!--
 Copyright (c) 2022 Joseph Hale
 
 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
-->

# Signatures

Utilities for assessing Python function signature equality and compatibility,
with the latter accounting for subtypes (including Generics!)

<!-- BADGES -->
[![](https://badgen.net/github/license/thehale/signatures)](https://github.com/thehale/signatures/blob/master/LICENSE)
[![](https://badgen.net/badge/icon/Sponsor/pink?icon=github&label)](https://github.com/sponsors/thehale)
[![](https://img.shields.io/badge/LinkedIn-thehale-0A66C2?logo=linkedin)](https://linkedin.com/in/thehale)

## Examples
See the [test suite](/tests/test_signatures.py) for a full set of examples.

### Equality
```python
# Identical function signatures are equal.
import signatures

def foo(thing: Any) -> None:
    pass

def bar(thing: Any) -> None:
    pass

assert signatures.equal(foo, bar)
```
```python
# Different function signatures are not equal.
import signatures

def foo(eggs: Any) -> None:
    pass

def bar(cheese: Any) -> None:
    pass

assert not signatures.equal(foo, bar)
```

### Compatibility
```python
# A function signature is compatible with a more
# generic function signature.
from typing import TypeVar

import signatures

T = TypeVar("T", bound=int)

def foo(thing: bool) -> None:
    pass

def bar(thing: T) -> None:
    pass

assert signatures.compatible(foo, bar)
```
```python
# Compatibility checks support nested Generic types.
import signatures

def foo(thing: List[Tuple[bool, str]]) -> None:
    pass

def bar(thing: List[Tuple[int, str]]) -> None:
    pass

assert signatures.compatible(foo, bar)
```
```python
# A function signature is not compatible when
# Generic types are not compatible.
import signatures

def foo(thing: List[int]) -> None:
    pass

def bar(thing: List[Tuple[int, str]]) -> None:
    pass

assert not signatures.compatible(foo, bar)
```

## [License](/LICENSE)
Mozilla Public License v2.0
