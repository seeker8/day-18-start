import colorgram

colors = colorgram.extract('spot.png', 10)
normalized_colors = []

for color in colors:
    r,g,b = color.rgb
    normalized_colors.append((r,g,b))

print(normalized_colors)