# Copyright (c) 2022 Joseph Hale
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from typing import *

import signatures


def test_version() -> None:
    assert signatures.__version__ == "0.2.0"


class Test__FunctionSignatureEquality:
    class Test__EqualWhen:
        def test__a_function_is_compared_with_itself(self) -> None:
            def func(foo: Any) -> None:
                pass

            assert signatures.equal(func, func)

        def test__two_functions_differ_only_by_name(self) -> None:
            def foo(thing: Any) -> None:
                pass

            def bar(thing: Any) -> None:
                pass

            assert signatures.equal(foo, bar)

        def test__they_use_the_same_generic(self) -> None:
            T = TypeVar("T")

            def foo(thing: T) -> None:
                pass

            def bar(thing: T) -> None:
                pass

            assert signatures.equal(foo, bar)

    class Test__UnequalWhen:
        def test__they_have_different_return_types(self) -> None:
            def foo(foo: Any) -> None:
                pass

            def bar(bar: Any) -> int:
                pass

            assert not signatures.equal(foo, bar)

        def test__they_have_a_different_parameter_name(self) -> None:
            def foo(thing1: Any) -> None:
                pass

            def bar(thing2: Any) -> None:
                pass

            assert not signatures.equal(foo, bar)

        def test__they_have_a_different_number_of_parameters(self) -> None:
            def foo(thing1: Any) -> None:
                pass

            def bar(thing1: Any, thing2: Any) -> None:
                pass

            assert not signatures.equal(foo, bar)

        def test__they_use_different_generics(self) -> None:
            T = TypeVar("T")
            V = TypeVar("V")

            def foo(thing: T) -> None:
                pass

            def bar(thing: V) -> None:
                pass

            assert not signatures.equal(foo, bar)


class Test__FunctionSignatureCompatibility:
    class Test__CompatibleGiven:
        def test__the_same_generic(self) -> None:
            T = TypeVar("T")

            def foo(thing: T) -> None:
                pass

            def bar(thing: T) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__a_subclass_of_another_parameters_type(self) -> None:
            def foo(thing: int) -> None:
                pass

            def bar(thing: bool) -> None:
                pass

            assert signatures.compatible(bar, foo)

        def test__an_instance_of_another_parameters_generic(self) -> None:
            T = TypeVar("T", bound=int)

            def foo(thing: bool) -> None:
                pass

            def bar(thing: T) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__a_stricter_generic_then_another_parameter(self) -> None:
            V = TypeVar("V", bound=bool)
            T = TypeVar("T", bound=int)

            def foo(thing: V) -> None:
                pass

            def bar(thing: T) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__multiple_identical_parameters(self) -> None:
            def foo(thing: int, stuff: int) -> None:
                pass

            def bar(thing: int, stuff: int) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__parameters_using_generic_classes(self) -> None:
            def foo(thing: List[int]) -> None:
                pass

            def bar(thing: List[int]) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__parameters_using_generic_classes_with_subtype(self) -> None:
            def foo(thing: List[bool]) -> None:
                pass

            def bar(thing: List[int]) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__parameters_using_generic_classes_with_multiple_subtypes(self) -> None:
            def foo(thing: Tuple[bool, str]) -> None:
                pass

            def bar(thing: Tuple[int, str]) -> None:
                pass

            assert signatures.compatible(foo, bar)

        def test__parameters_using_nested_generic_classes(self) -> None:
            def foo(thing: List[Tuple[bool, str]]) -> None:
                pass

            def bar(thing: List[Tuple[int, str]]) -> None:
                pass

            assert signatures.compatible(foo, bar)

    class Test__IncompatibleGiven:
        def test__different_parameter_names(self) -> None:
            def foo(thing1: int) -> None:
                pass

            def bar(thing2: int) -> None:
                pass

            assert not signatures.compatible(foo, bar)

        def test__at_least_one_parameter_with_a_different_name(self) -> None:
            def foo(thing: int, stuff1: int) -> None:
                pass

            def bar(thing: int, stuff2: int) -> None:
                pass

            assert not signatures.compatible(foo, bar)

        def test__different_parameter_types(self) -> None:
            def foo(thing: int) -> None:
                pass

            def bar(thing: str) -> None:
                pass

            assert not signatures.compatible(foo, bar)

        def test__an_noninstance_of_a_generic(self) -> None:
            T = TypeVar("T", bound=int)

            def foo(thing: T) -> None:
                pass

            def bar(thing: str) -> None:
                pass

            assert not signatures.compatible(bar, foo)

        def test__parameters_using_different_generic_subtypes(self) -> None:
            def foo(thing: List[int]) -> None:
                pass

            def bar(thing: List[Tuple[int, str]]) -> None:
                pass

            assert not signatures.compatible(foo, bar)

        def test__parameters_using_different_nested_generic_classes(self) -> None:
            def foo(thing: List[Tuple[int, bool]]) -> None:
                pass

            def bar(thing: List[Tuple[int, str]]) -> None:
                pass

            assert not signatures.compatible(foo, bar)
