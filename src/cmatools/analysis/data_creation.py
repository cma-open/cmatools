
""" Example data analysis module - creating output data in netcdf format """

# import stand library imports
from pathlib import Path

# import third party imports
import iris

# import local app / lib imports
from cmatools.definitions import ROOT_DIR

sea_temp = "tos_O1_2001-2002.nc"
sea_temp_file = Path(ROOT_DIR) / "data" / "inputs" / sea_temp
output_file = Path(ROOT_DIR) / "data" / "outputs" / "tos_ouput.nc"

print(sea_temp_file.exists())
#sea_temp_file="/home/h02/jwinn/github-repos/cmatools/cmatools/data/inputs/tos_O1_2001-2002.nc"

print(iris.__version__)

print(sea_temp_file)
# need to use string as iris cant deal with PosixPath
cubes = iris.load_cubes(str(sea_temp_file))
print(cubes)

print(cubes[0])

cube = cubes[0]

#src = cube.attributes.pop('source')
#all = cube.attributes
#hist = cube.attributes.pop('history')

#print(src)
#print(all)
#print(hist)
print("vvvvvvvvvvvvvvvvvvv")
#cube.attributes

metadata = cube.metadata
print(metadata)
print("///////////////////////////////")
print(cube.attributes)
print(cube.attributes['history'])

for key, value in metadata.attributes.items():
    print(key, value)
    #metadata.attributes[key] = value

print("///////////////////////////////")

cube.attributes['history'] = 'updated'


for coord in cube.coords():
    print(coord.name())

print("------------")

# amend the attributes - history


#iris.cube.Cube.attributes["history":"changed"]


# run the analysis
# 1. initially just set a named CF standards version an ensure that is kept in the output file
# 2. run analysis that take a user set year date range setting to customise output

iris.config.netcdf.conventions_override = True

# Save just the sea_surface_temperature to a netcdf file
iris.save(cubes[0], str(output_file))

print("------------------------------------------------------")

# re load and view the output file
cubes_out = iris.load_cubes(str(output_file))
print(cubes_out)

print("")
print("----------------------- output file -------------------------------")
print("")

print(cubes_out[0])

# TODO developer notes
# initially as a simple script
# then move to use the config scripts for data dir output
# then change to use input at a for the analysis

# in the above example, the input data is in CF-1.0,
# when saved out to a new netcdf and checked, the CF of the file then matches the version used by Iris
# in order to retain original update, or set the Cf in the current system, need to use iris config setting

# Q
# why is there so little info in the iris docs on setting and accessing the cube metadata, very difficult to google
# these sorts of details
# ideally have a section next to the main metadata reference
#
# raise Pr about posixpath use as input to loads?

