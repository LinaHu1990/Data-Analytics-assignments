# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#part1 
#define function greet w. arg name, greeting template

def greet(name, greeting_template="Hello, <name>!"):
    return greeting_template.replace("<name>",name)

print(greet("Bob"))

#part2 
def force(mass, body = "earth"):       
    body_dictionary = {
        "sun":274.0,
        "jupiter":24.9,
        "neptune":11.2,
        "saturn": 10.4,
        "earth":9.8,
        "uranus":8.9,
        "venus":8.9,
        "mars":3.7,
        "mercury":3.7,
        "moon":1.6,
        "pluto":0.6,}    
    return round(body_dictionary[body] * mass, 1)
    
print(force(3, "sun"))
 
#part3
def pull(m1, m2, d):
    G = 6.674 * 10**-11
    return (m1 * m2 / (d**2)) * G
   
print(pull(0.1, 1500, 3))