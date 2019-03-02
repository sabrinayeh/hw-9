
destinations = [
"Space Needle",
"Crater Lake",
"Golden Gate Bridge",
"Yosemite National Park",
"Las Vegas, Nevada",
"Grand Canyon National Park",
"Aspen, Colorado",
"Mount Rushmore",
"Yellowstone National Park",
"Sandpoint, Idaho",
"Banff National Park",
"Capilano Suspension Bridge",
]


import geocoder

# Declare destinations list here.

# Loop through each destination.
for point in destinations:
	g = geocoder.arcgis(point)
	print(point, " is located at ", g.latlng)
#   Get the lat-long coordinates from `geocoder.arcgis`.
#   Print out the place name and the coordinates.