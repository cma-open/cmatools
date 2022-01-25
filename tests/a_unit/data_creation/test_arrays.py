"""Tests for data creation arrays module."""

import numpy as np

from cmatools.data_creation.arrays import (
    data_array,
    data_array_sample,
    data_locations_and_values_array,
    data_locations_and_values_array_other,
)

# TODO update valid air temp range in K

DEBUG = True


def print_details(array):
    """Print out details of the data array."""
    print("---")
    print(f"Type: {type(array)}")
    print(f"Data values: {array}")
    print(f"Number of dimensions: {array.ndim}")
    print(f"Shape, length of each dimension: {array.shape}")
    print(f"Total number of elements: {array.size}")


def test_data_array():
    """Test simple data array."""
    data = data_array()
    assert isinstance(data, np.ndarray)
    assert data.ndim == 1  # Verify only 1 dimension
    assert data.shape == (3,)  # Verify shape, length of dimensions
    assert data.size == 3  # Verify number of elements
    if DEBUG:
        print_details(data)


def test_data_array_sample():
    """Test data array with optional sample size setting."""
    data50 = data_array_sample()
    assert isinstance(data50, np.ndarray)
    assert data50.ndim == 1  # Verify only 1 dimension
    assert data50.shape == (50,)  # Verify shape, length of dimensions
    assert data50.size == 50  # Verify number of elements
    data150 = data_array_sample(sample=150)
    assert isinstance(data150, np.ndarray)
    assert data150.ndim == 1  # Verify only 1 dimension
    assert data150.shape == (150,)  # Verify shape, length of dimensions
    assert data150.size == 150  # Verify number of elements
    if DEBUG:
        print_details(data50)
        print_details(data150)


def test_data_locations_and_values_array():
    """Test data array with both locations and data values."""
    output = data_locations_and_values_array()
    assert isinstance(output, tuple)
    locations, values = data_locations_and_values_array()
    # Verify locations (expect array)
    assert isinstance(locations, np.ndarray)
    assert locations.ndim == 2  # Verify only 1 dimension
    assert locations.shape == (2, 8)  # Verify shape, length of dimensions
    assert locations.size == 16  # Verify number of elements
    # Verify data values (expect array)
    assert isinstance(values, np.ndarray)
    assert values.ndim == 1  # Verify only 1 dimension
    assert values.shape == (8,)  # Verify shape, length of dimensions
    assert values.size == 8  # Verify number of elements
    if DEBUG:
        print_details(locations)
        print_details(values)


def test_data_locations_and_values_array_other():
    """Test data array with both locations and data values."""
    output = data_locations_and_values_array_other()
    assert isinstance(output, tuple)
    locations, values = data_locations_and_values_array_other()
    # Verify locations (expect array)
    assert isinstance(locations, np.ndarray)
    assert locations.ndim == 2  # Verify only 1 dimension
    assert locations.shape == (2, 4)  # Verify shape, length of dimensions
    assert locations.size == 8  # Verify number of elements
    # Verify data values (expect array)
    assert isinstance(values, np.ndarray)
    assert values.ndim == 1  # Verify only 1 dimension
    assert values.shape == (4,)  # Verify shape, length of dimensions
    assert values.size == 4  # Verify number of elements
    if DEBUG:
        print_details(locations)
        print_details(values)
