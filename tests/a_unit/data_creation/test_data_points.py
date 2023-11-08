"""Tests for data_points module."""

from cmatools.data_creation.data_points import generate_synthetic_stations

# generate_random_lat_lon,; plot_example_1_map,;
# plot_example_2_map,; plot_example_3_map,;
# plot_example_4_map,; plot_example_5_map,


DEBUG = True


def test_generate_synthetic_stations():
    """Test generate synthetic stations."""
    df = generate_synthetic_stations(5)
    if DEBUG:
        print("-")
        print(df)


# def test_generate_ranom_lat_lon():
#     lat, lon = generate_random_lat_lon(50)
#     assert isinstance(lat, list)
#     assert isinstance(lon, list)
#     # Check values for latitudes (-90 to 90)
#     assert max(lat) <= 90
#     assert min(lat) >= -90
#     # Check vals for longitudes (-180 to 180)
#     assert max(lon) <= 180
#     assert min(lon) >= -180
#     if DEBUG:
#         counts = len(lat), len(lon)
#         print("-")
#         print(f"Sample counts: {counts}")
#         for (lat, lon) in zip(lat, lon):
#             print(f"Lat: {lat}, Lon: {lon}")
