"""Tests for the example_numpy module.

Tests have been added to cover the code provided by the module used to illustrate
codestyle examples.

"""

import types

import pytest

from cmatools.examplesubpackage.example_numpy import (
    ExampleClass,
    ExampleError,
    example_generator,
    function_with_pep484_type_annotations,
    function_with_types_in_docstring,
    module_level_function,
)


def test_function_with_types_in_docstring():
    """Test function_with_types_in_docstring."""
    # Expect return True if param1 is > param2
    assert function_with_types_in_docstring(12, "10") is True
    # Expect return False if param1 < param2
    assert function_with_types_in_docstring(2, "100") is False


def test_function_with_types_in_docstring_raises_error():
    """Test raises error: function_with_types_in_docstring."""
    # Expect error raised if param2 is a word not digits
    with pytest.raises(ValueError):
        function_with_types_in_docstring(12, "ten")
    # Expect error raised if param1 is not an integer
    with pytest.raises(TypeError):
        function_with_types_in_docstring("fifteen", "10")


def test_function_with_pep484_type_annotations():
    """Test function_with_pep484_type_annotations."""
    # Expect return True if param1 is > param2
    assert function_with_pep484_type_annotations(12, "10") is True
    # Expect return False if param1 < param2
    assert function_with_pep484_type_annotations(2, "100") is False


def test_function_with_pep484_type_annotations_raises_error():
    """Test raises error: function_with_pep484_type_annotations."""
    # Expect error raised if param2 is a word not digits
    with pytest.raises(ValueError):
        function_with_pep484_type_annotations(12, "ten")
    # Expect error raised if param1 is not an integer
    with pytest.raises(TypeError):
        function_with_pep484_type_annotations("fifteen", "10")


def test_module_level_function_positional():
    """Test module_level_function with positional arguments."""
    # Expect returns False, as value is less than target(100)
    assert module_level_function(5) is False
    # Expect returns False, as value is less than target(100)
    assert module_level_function(5, "1") is False
    # Expect return True, as value greater than target(100)
    assert module_level_function(500, "1") is True
    # Expect return True, as value greater than target(100)
    assert module_level_function(500) is True


def test_module_level_function_positional_and_args():
    """Test module_level_function with positional arguments and *args list."""
    # Expect returns False, as value is less than target(100)
    assert module_level_function(5, "15", 5, 7, 8, 9) is False
    # Expect returns False, as value is less than target(100)
    assert module_level_function(5, "1", 5, 12, 78) is False

    # Expect return True, as value greater than target(100)
    assert module_level_function(500, "1", 45, 67, 888) is True
    # Expect return True, as value greater than target(100)
    assert module_level_function(500, "111", 12, 24, 35, 777) is True


def test_module_level_function_positional_args_and_kwargs():
    """Test module_level_function with positional arguments, *args and **kwargs."""
    # Expect returns False, as value is less than target(100)
    assert (
        module_level_function(5, "15", 5, 7, 8, 9, QC="High", source="HadObs", CF=1.7)
        is False
    )
    # Expect returns False, as value is less than target(100)
    assert module_level_function(5, "1", 5, 12, 78, QC="Low") is False
    # Expect return True, as value greater than target(100)
    assert module_level_function(500, "1", 45, 67, 888, source="CEDA") is True
    # Expect return True, as value greater than target(100)
    assert (
        module_level_function(500, "111", 12, 24, 35, 777, CF=1.6, source="CEDA")
        is True
    )
    # Expect return True, as value greater than target(100)
    # optional verbose param triggers verbose output
    assert (
        module_level_function(
            500, "111", 12, 24, 35, 777, CF=1.6, source="CEDA", verbose=True
        )
        is True
    )


def test_module_level_function_raises_error():
    """Test module_level_function raises error."""
    # Expect raises error as param1 and param2 cannot be equal
    with pytest.raises(ValueError):
        module_level_function(1, 1)
    # Expect raises error as param 2 is not a string
    with pytest.raises(ValueError):
        module_level_function(5, 1)


def test_example_generator():
    """Test example_generator function."""
    # Confirm instance type
    assert isinstance(example_generator(7), types.GeneratorType)
    # Confirm expected output from use of generator in list comprehension
    assert [i for i in example_generator(4)] == [0, 1, 2, 3]
    # Confirm yield next values from generator
    example_generator_value = example_generator(4)
    assert next(example_generator_value) == 0
    assert next(example_generator_value) == 1
    assert next(example_generator_value) == 2


def test_example_generator_raises_error():
    """Test example_generator function raises error."""
    # Confirm raises error if n is a string
    with pytest.raises(TypeError):
        result = [i for i in example_generator("12")]
        print(result)


def test_example_error():
    """Test example_error class."""
    # Confirm error message is raised correctly
    with pytest.raises(ExampleError, match="must be 0 or None"):
        raise ExampleError("value must be 0 or None")
    # Confirm error message is raised correctly, when called with message and err code
    with pytest.raises(ExampleError, match="must be 0 or None"):
        raise ExampleError("value must be 0 or None", 24)


def test_example_class():
    """Test for example_class."""
    # Instantiate class instance object
    example = ExampleClass("12", ["10", "20", "30"], 8888)
    assert isinstance(example, ExampleClass)


def test_example_class_properties():
    """Test example_class properties."""
    # ExampleClass('1', ['10', '29'], 3).attribute_string.func(11)
    # Create a valid ExampleClass object
    example = ExampleClass("1", ["10", "29"], 3)
    # test readonly attribute
    assert example.readonly_property == "readonly_property"


# TODO - check here - integration vs unit test?
def test_example_class_raises_error():
    """Test example_class errors."""
    # Check error is raised if param1 is not a string
    with pytest.raises(TypeError, match="must be a string"):
        ExampleClass(1, ["10", "29"], 3)
    # Check error is raised if param2 is not a list of strings
    with pytest.raises(TypeError, match="must be a list of strings"):
        ExampleClass("1", "param2", "param3")
    # Check error is raised if param2 is not list of strings
    with pytest.raises(TypeError, match="must be a list of strings"):
        ExampleClass("1", [12, 13, 4], 3)
    # Check error is raised if param3 is not an integer
    with pytest.raises(TypeError, match="must be an integer"):
        ExampleClass("1", ["12", "23", "345"], "param3")
    # Check that error is raised if a valid attribute is re-assigned an invalid value
    example = ExampleClass("12", ["10", "20", "30"], 8888)  # Initiated as valid
    example.attribute_integer = 9999  # Valid re-assignment
    with pytest.raises(TypeError, match="must be an integer"):
        example.attribute_integer = "8888"  # Invalid, as is string, not integer


def test_example_class_example_method():
    """Test example_class.example_method."""
    # Create a valid ExampleClass object
    example = ExampleClass("1", ["10", "29"], 3)
    # Test class method, expect return True
    assert example.example_method("param1", "param2") is True
