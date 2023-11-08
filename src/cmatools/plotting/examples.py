"""Example map plots."""

import cartopy.crs as ccrs

from cmatools.data_creation.downloads import natural_earth_points
from cmatools.data_creation.simple import (
    example_data_lat_lon_series,
    example_data_single_lat_lon,
)
from cmatools.data_creation.tabular import example_csv_data, generate_synthetic_stations
from cmatools.plotting.common import plot_defaults

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

# Example 1


def plot_example_map_1():
    """Plot example map 1."""
    # Load plot defaults
    fig, plt, ax = plot_defaults(1)
    # Set titles
    fig.suptitle("Example map 1 - title", fontsize=16)
    ax.set_title("Example 1 ax title")
    # Load input data
    lat, lon = example_data_single_lat_lon()
    # x, y: float or array-like, shape (n, )
    # long , lat
    ax.scatter(lon, lat, s=40, c="r", alpha=0.9, transform=ccrs.PlateCarree())
    # plt.savefig('map.png')
    plt.show()


# -------------------------------------------------------------------------------------


def plot_example_map_2():
    """Plot example amp 2."""
    fig, plt, ax = plot_defaults(2)
    # Set titles
    fig.suptitle("Example map 2 - title", fontsize=16)
    ax.set_title("Example 2 ax title")
    # Load input data
    lat, lon, ID = example_data_lat_lon_series()
    ax.scatter(
        lon,
        lat,
        s=50,
        c="r",
        edgecolor="black",
        alpha=0.75,
        transform=ccrs.PlateCarree(),
    )
    for count, station in enumerate(ID):
        ax.text(
            lon[count],
            lat[count],
            station,
            horizontalalignment="left",
            transform=ccrs.PlateCarree(),
            fontsize=11,
        )
    plt.show()


# -------------------------------------------------------------------------------------


def plot_example_map_3():
    """Plot example map 3."""
    fig, plt, ax = plot_defaults(3)
    # Set titles
    fig.suptitle("Example map 3 - title", fontsize=16)
    ax.set_title("Example 3 ax title")
    # Load input data
    stations = example_csv_data()
    # Map points as lon, lat values
    ax.scatter(
        stations.lon,
        stations.lat,
        s=50,
        c="r",
        edgecolor="black",
        alpha=0.75,
        transform=ccrs.PlateCarree(),
    )
    # plt.savefig('map.png')
    plt.show()


# -------------------------------------------------------------------------------------


def plot_example_map_4():
    """Plot example map 4."""
    fig, plt, ax = plot_defaults(4)
    # Set titles
    fig.suptitle("Example map 4 - title", fontsize=16)
    ax.set_title("Example 4 ax: Populated locations")
    # Load data
    points = natural_earth_points()
    # Map points as lon, lat values
    ax.scatter(
        [point.x for point in points],
        [point.y for point in points],
        transform=ccrs.PlateCarree(),
    )
    plt.show()


# -------------------------------------------------------------------------------------


def plot_example_map_5(sample):
    """Plot example map 5."""
    # Apply map defaults
    fig, plt, ax = plot_defaults(5)
    # Set titles
    fig.suptitle("Example map 5 - title", fontsize=16)
    ax.set_title("Example 5 ax title")
    # Load input data
    stations = generate_synthetic_stations(sample)
    # Map points on the map as lon, lat values
    ax.scatter(
        stations.longitudes,
        stations.latitudes,
        s=50,
        c="r",
        edgecolor="black",
        alpha=0.75,
        transform=ccrs.PlateCarree(),
    )
    plt.show()


# -------------------------------------------------------------------------------------


def plot_example_map_6(sample):
    """Plot example map 6."""
    # Apply map defaults
    fig, plt, ax = plot_defaults(6)
    # Set titles
    fig.suptitle("Example map 6 - title", fontsize=16)
    ax.set_title("Example 6 ax title")
    # Load input data - 1st
    lat, lon, ID = example_data_lat_lon_series()
    ax.scatter(
        lon,
        lat,
        s=100,
        c="b",
        edgecolor="black",
        alpha=0.75,
        transform=ccrs.PlateCarree(),
    )
    for count, station in enumerate(ID):
        ax.text(
            lon[count],
            lat[count],
            station,
            horizontalalignment="left",
            transform=ccrs.PlateCarree(),
            fontsize=11,
        )
    # Load input data - 2nd
    stations = generate_synthetic_stations(sample)
    # Map points on the map as lon, lat values
    ax.scatter(
        stations.longitudes,
        stations.latitudes,
        s=15,
        c="r",
        edgecolor="black",
        alpha=0.75,
        transform=ccrs.PlateCarree(),
    )
    plt.show()
