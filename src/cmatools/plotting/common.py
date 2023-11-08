"""Defaults for plot creation."""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def plot_defaults(num):
    """Return plotting default setup."""
    # Set output figure size
    fig = plt.figure(figsize=(16, 8), num=num)
    # Instantiate and set map projection
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()  # Ensure map has global extent coverage
    ax.coastlines()  # Add coastline vector dataset to map
    # Use text to add lat, lon labels s gridlines overrides use of x,y labels
    ax.text(
        -0.05,
        0.55,
        "latitude",
        va="bottom",
        ha="center",
        rotation="vertical",
        rotation_mode="anchor",
        transform=ax.transAxes,
    )
    ax.text(
        0.5,
        -0.1,
        "longitude",
        va="bottom",
        ha="center",
        rotation="horizontal",
        rotation_mode="anchor",
        transform=ax.transAxes,
    )
    # Add gridlines and labels
    gridlines = ax.gridlines(
        draw_labels=True, linewidth=0.4, color="gray", alpha=0.4, linestyle="--"
    )
    # Remove top and right labels
    gridlines.top_labels = False
    gridlines.right_labels = False
    return fig, plt, ax
