# pip install colorgram.py

import colorgram


def get_colors(image): 
  colors = colorgram.extract(image, 15)
  rgb_colors = []

  for color in colors:
    dec_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(dec_color)
    
  return rgb_colors