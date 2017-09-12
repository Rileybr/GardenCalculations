import math

# get parameters of the garden
side_length = float(input("How long is one of the sides of the garden in feet? :"))
distance_between_plants = float(input("How much room between plants in feet? :"))
soil_depth = float(input("How deep is the garden soil in feet? :"))
fill_depth = float(input("How deep is the garden fill in feet? :"))

# calculate the area of circles
radius = side_length / 4
circle_area = radius**2 * math.pi
area_of_circles = circle_area * 3

# calculates how many plants needed
total_plants = area_of_circles / distance_between_plants**2
total_plants_in_circle = total_plants / 3
total_plants_in_semi_circle = total_plants_in_circle / 2

# calculate the fill for the garden
garden_area = side_length * side_length
fill_surface_area = garden_area - area_of_circles
fill_area = (fill_surface_area * fill_depth) * 0.037037  # multiplying to get data in cubic yards

# calculate the soil for the garden
soil_area = (area_of_circles * soil_depth) * 0.037037  # multiplying to get data in cubic yards
circle_soil_area = soil_area / 3
semi_circle_soil_area = circle_soil_area / 2

# prints the requirements of the garden
print("------------------------------------------------------------------------------------------------------------")
print("Plants for each semi-circle garden:", int(total_plants_in_semi_circle))
print("Plants for the circle garden:", int(total_plants_in_circle))
print("Total plants for garden:", int(total_plants))
print("Soil for each semicircle garden:", "{:.1f}".format(semi_circle_soil_area), "cubic yards")
print("Soil for the circle garden:", "{:.1f}".format(circle_soil_area), "cubic yards")
print("Total soil for the garden:", "{:.1f}".format(soil_area), "cubic yards")
print("Total fil for the garden:", "{:.1f}".format(fill_area), "cubic yards")
