
#  rate of painting per square meter is 20 rs

area = float(input("Enter the area in square meters (one wall): "))
interior_cost = float(input("Enter the cost of painting interior wall per square meter: "))
exterior_cost = float(input("Enter the cost of painting exterior wall per square meter: "))

#interior walls + exterior walls of two rooms

interior_walls = 8 
exterior_walls = 7 # (exterior walls of two rooms minus the common wall)

interior_area = area * interior_walls
exterior_area = area * exterior_walls

interior_cost = interior_area * interior_cost
exterior_cost = exterior_area * exterior_cost
total_area = interior_area + exterior_area
painting_cost = interior_cost + exterior_cost

print("Total area to be painted:", total_area)
print("Total cost of painting:", painting_cost)


"""Calculate the cost of painting the following building’s walls (both interior and 
exterior). You need to accept area (one wall) and cost of both interior and 
exterior wall.  
(Note: 1. Below diagram is of two joint rooms. 
    2. It is upper view of building.) """


