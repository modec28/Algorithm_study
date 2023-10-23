def solution():
    first_angle = int(input())
    second_angle = int(input())
    third_angle = int(input())

    if first_angle==60 and second_angle==60 and third_angle ==60:
        return "Equilateral"
    
    if sum([first_angle, second_angle, third_angle]) == 180:
        if first_angle == second_angle or second_angle == third_angle or first_angle == third_angle:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Error"

print(solution())
