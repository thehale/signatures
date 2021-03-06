# Copyright (c) 2022 Joseph Hale
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

__version__ = "0.3.1"

from typing import *
import inspect


def equal(function: Callable[..., Any], otherFunction: Callable[..., Any]) -> bool:
    """Determines if two functions have equal signatures.

    Args:
        function (Callable[..., Any]): The first function to compare
        otherFunction (Callable[..., Any]): The second function to compare

    Returns:
        bool: True if both function signatures are equal. False otherwise.
    """
    return inspect.signature(function) == inspect.signature(otherFunction)


def compatible(function: Callable[..., Any], otherFunction: Callable[..., Any]) -> bool:
    signature = inspect.signature(function)
    otherSignature = inspect.signature(otherFunction)
    are_compatible_params = __are_parameters_compatible(signature, otherSignature)
    are_compatible_returns = __are_return_types_compatible(signature, otherSignature)
    return are_compatible_params and are_compatible_returns


def __are_parameters_compatible(
    signature: inspect.Signature, otherSignature: inspect.Signature
) -> bool:
    are_compatible = True
    for key in signature.parameters.keys():
        if key in otherSignature.parameters.keys():
            paramType = signature.parameters[key].annotation
            otherParamType = otherSignature.parameters[key].annotation
            equivalent = __are_types_compatible(paramType, otherParamType)
            are_compatible = are_compatible and equivalent
        else:
            are_compatible = False
    return are_compatible


def __are_return_types_compatible(
    signature: inspect.Signature, otherSignature: inspect.Signature
) -> bool:
    return __are_types_compatible(
        signature.return_annotation, otherSignature.return_annotation
    )


def __are_types_compatible(subtype: Type[Any], supertype: Type[Any]) -> bool:
    equal = __are_types_equal(subtype, supertype)
    subclass = __issubtype(subtype, supertype)
    return equal or subclass


def __are_types_equal(subtype: Type[Any], supertype: Type[Any]) -> bool:
    return str(subtype) == str(supertype)


def __issubtype(subtype: Type[Any], supertype: Type[Any]) -> bool:
    if supertype is None:
        return subtype is None
    elif __is_generic(supertype):
        return (
            __issubtype(subtype.__bound__, supertype.__bound__)
            if __is_generic(subtype)
            else __issubtype(subtype, supertype.__bound__)
        )
    else:  # supertype is not directly a Generic
        if all(__is_parameterized_generic(a) for a in [subtype, supertype]):
            return __same_base_type(subtype, supertype) and __generic_args_are_subtypes(
                subtype, supertype
            )
        elif all(not __is_parameterized_generic(a) for a in [subtype, supertype]):
            return issubclass(subtype, supertype)
        else:  # any(not is_parameterized_generic(a) for a in [subtype, supertype]):
            return False


def __generic_args_are_subtypes(subtype: Type[Any], supertype: Type[Any]) -> bool:
    return all(
        __issubtype(key, value)
        for key, value in dict(zip(subtype.__args__, supertype.__args__)).items()
    )


def __same_base_type(subtype: Type[Any], supertype: Type[Any]) -> bool:
    return issubclass(subtype.__origin__, supertype.__origin__)


def __is_generic(arg: Type[Any]) -> bool:
    """Returns whether the `arg` is a `Generic` types."""
    return isinstance(arg, TypeVar)


def __is_parameterized_generic(arg: Type[Any]) -> bool:
    """
    Returns whether all `args` are concrete types with one or more `Generic` parameters.
    """
    return hasattr(arg, "__args__")
