# converting height from feet to meter using function 
user_height_ft = int(input('Enter your height : '))
user_height_inch =int(input('Enter your height : '))


def feet_to_meters( height_ft = 0 , height_inch = 0):
    return (height_ft * 12 + height_inch)  * 0.0254


print(f"{user_height_ft} feet and {user_height_inch} inches is equal to {feet_to_meters(user_height_ft, user_height_inch):.2f} meters")