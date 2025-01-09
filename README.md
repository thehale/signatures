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
[![Joseph Hale's software engineering blog](https://jhale.dev/badges/website.svg)](https://jhale.dev)
[![](https://jhale.dev/badges/follow.svg)](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=thehale)

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
Copyright (c) 2022 - 2024, Joseph Hale. All Rights Reserved.

```
signatures by Joseph Hale is licensed under the terms of the Mozilla
Public License, v 2.0, which are available at https://mozilla.org/MPL/2.0/.

You can download the source code for signatures for free from
https://github.com/thehale/signatures.
```
<details>

<summary><b>What does the MPL-2.0 license allow/require?</b></summary>

### TL;DR

You can use files from this project in both open source and proprietary
applications, provided you include the above attribution. However, if
you modify any code in this project, or copy blocks of it into your own
code, you must publicly share the resulting files (note, not your whole
program) under the MPL-2.0. The best way to do this is via a Pull
Request back into this project.

If you have any other questions, you may also find Mozilla's [official
FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) for the MPL-2.0 license
insightful.

If you dislike this license, you can contact me about negotiating a paid
contract with different terms.

**Disclaimer:** This TL;DR is just a summary. All legal questions
regarding usage of this project must be handled according to the
official terms specified in the `LICENSE` file.

### Why the MPL-2.0 license?

I believe that an open-source software license should ensure that code
can be used everywhere.

Strict copyleft licenses, like the GPL family of licenses, fail to
fulfill that vision because they only permit code to be used in other
GPL-licensed projects. Permissive licenses, like the MIT and Apache
licenses, allow code to be used everywhere but fail to prevent
proprietary or GPL-licensed projects from limiting access to any
improvements they make.

In contrast, the MPL-2.0 license allows code to be used in any software
project, while ensuring that any improvements remain available for
everyone.

</details>

