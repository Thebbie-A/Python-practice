
# read the volume from the user
radius = float(input('Enter radius: '))
height = float(input('Enter height : '))

volume = 3.14 * (radius ** 2) * height
rounded_volume = round(volume,1)

# display the results in 1 decimal place
print(rounded_volume)


