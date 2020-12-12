"""
CP1404/CP5632 Practical
State colors in a dictionary
"""

NAME_TO_CODE={'aliceblue':'#f0f8ff','antiquewhite1':'#ffefdb','antiquewhite':'#faebd7','antiquewhite2':'#eedfcc','antiquewhite3':'#cdc0b0','antiquewhite4':'#8b8378','aquamarine1':'#7fffd4',
              'aquamarine2':'#76eec6','aquamarine4':'#458b74','azure1':'#f0ffff'}

color_name = input('Enter the color name: ')
color_name = color_name.lower()
while color_name != '':
    if color_name in NAME_TO_CODE:
        print(NAME_TO_CODE[color_name])
    else:
        print('Invalid input')
    color_name = input('Enter the color name: ')
    color_name = color_name.lower()
