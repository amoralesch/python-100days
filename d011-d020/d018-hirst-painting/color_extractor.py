# Color Extractor

# Small tool to take any image present in the current directory, and
# extract the N most used colors from it.
#
# Shown in the course, and used to find the colors to use in our own
# Hirst painting.

import colorgram

colors = colorgram.extract('image.jpg', 20)

rgb_colors = []

for color in colors:
    rgb = color.rgb
    rgb_colors.append((rgb.r, rgb.g, rgb.b))

print(rgb_colors)
