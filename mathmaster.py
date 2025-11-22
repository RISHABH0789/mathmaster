import math 

#all functions
def add(a,b):
    sum = a+b
    print(f"Answer: {sum}")

def sub(a,b):
    difference = a-b
    print(f"Answer: {difference}")

def multiply(a,b):
    product = a*b
    print(f"Answer: {product}")

def divide(a,b):
    if b == 0:
        print(f"Cannot divide {a} with 0")
    else:
        quotient = a/b
        remainder = a%b
        print(f"Quotient: {quotient}\nRemainder: {remainder}")

def table(num):
    i = 1
    while i<11:
        print(f"{num} X {i} = {num*i}")
        i += 1

def square(num):
    sq = num**2
    print(f"Answer: {sq}")

def square_root(num):
    squareRoot = math.sqrt(num)
    print(f"Answer: {squareRoot}")

def cube(num):
    cb = num**3
    print(f"Answer: {cb}")

def cube_root(num):
    cubeRoot = math.cbrt(num)
    print(f"Answer: {cubeRoot}")

def exponent(num,power):
    expo = num**power
    print(f"Answer: {expo}")

def perimeter_triangle(s1,s2,s3):
    triangle = s1+s2+s3
    print(f"Answer: {triangle}")

def perimeter_square(side):
    square = 4*side
    print(f"Answer: {square}")

def perimeter_rectangle(length,breadth):
    rect = 2*(length+breadth)
    print(f"Answer: {rect}")

def circumference(radius):
    circle = 2*22/7*radius
    print(f"Answer: {circle}")

def area_triangle(base,height):
    t_area = 1/2*base*height
    print(f"Answer: {t_area}")

def area_square(side):
    s_area = side**2
    print(f"Answer: {s_area}")

def area_rectangle(length,breadth):
    r_area = length*breadth
    print(f"Answer: {r_area}")

def area_circle(radius):
    c_area = 22/7*radius**2
    print(f"Answer: {c_area}")

def area_trapezium(s1,s2,height):
    tra_area = 1/2*(s1+s2)*height
    print(f"Answer: {tra_area}")

def volume_cube(length):
    cb_volume = length**3
    print(f"Answer: {cb_volume}")

def volume_cuboid(length,width,height):
    cbd_volume = length*width*height
    print(f"Answer: {cbd_volume}")

def volume_cylinder(radius,height):
    cy_volume = 22/7*radius**2*height
    print(f"Answer: {cy_volume}")
    
def simple_interest(principal,rate,time):
    amount = int((principal*rate*time)/100)
    si = int(amount-principal)
   
    needed = True
   
    while needed:

       amount_also = input("Do you want Amount also?[Y/N]").lower()

       if amount_also == "yes" or amount_also == "y":
             print(f"Amount: {amount}\nSimple Interest: {si}")
             needed = False
   

       elif amount_also == "no" or amount_also == "n": 
            print(f"Simple Interest: {si}")
            needed = False
           
       else:
          print("Tell me only yes or no")

def compound_interest(principal,rate,time):
   amount = int(principal*(rate/100+1)**time)
   ci = int(amount-principal)
   
   needed = True
   
   while needed:

      amount_also = input("Do you want Amount also?[Y/N]").lower()

      if amount_also == "yes" or amount_also == "y":
            print(f"Amount: {amount}\nCompound Interest: {ci}")
            needed = False
   

      elif amount_also == "no" or amount_also == "n": 
           print(f"Compound Interest: {ci}")
           needed = False
           
      else:
         print("Tell me only yes or no")

def help():#created to let user know in what scenario they can use it
    i = 0
    num = 1
    cmd = ["Finding Sum","Finding Difference","Finding Product","Finding Quotient and Remainder","Making Table of given number","Finding Square","Finding Square root","Finding Cube","Finding Cube root","Finding Exponent","Finding Perimeter of Square","Finding Perimeter of Rectangle","Finding Perimeter of Triangle","Finding Circumference of Circle","Finding Area of Square","Finding Area of Rectangle","Finding Area of Triangle","Finding Area of Circle","Finding Area of Trapezium","Finding Volume of Cube","Finding Volume of Cuboid","Finding Volume of Cylinder"]
    length = len(cmd)
    print("I can assist in these:")
    while i != length:
        print(f"{num}:{cmd[i]}")
        num += 1
        i += 1

if __name__ == "__main__":

    chatbot = True
    
    print("Hi,How can I help you?\n")
    
    while chatbot:
        prompt = input().lower()
        #for add
        if "add" in prompt:
            num1 = float(input("First Num: "))
            num2 = float(input("Second Num: "))
            add(num1,num2)
    
        #for subtract
        elif "sub" in prompt:
            num1 = int(input("First Num: "))
            num2 = float(input("Second Num: "))        
            sub(num1,num2)
    
        #for multiplication
        elif "multiply" in prompt:
            num1 = float(input("First Num: "))
            num2 = float(input("Second Num: "))        
            multiply(num1,num2)
    
        #for division
        elif "divide" in prompt:
            num1 = float(input("First Num: "))
            num2 = float(input("Second Num: "))        
            divide(num1,num2)
        
        #for printing table of any number
        elif "table" in prompt:
           num= int(input("Number For Table: "))
           table(num)
           
       #for getting square root 
        elif "square root" in prompt:
           num = float(input("Number: "))
           
           square_root(num)
        
        #for getting square
        elif "square" in prompt:
           num = float(input("Number: "))
           
           square(num)
        
        #for getting cube root
        elif "cube root" in prompt:
           num = float(input("Number: "))
           
           cube_root(num)
        
        #for getting cube
        elif "cube" in prompt:
           num = float(input("Number: "))
           
           cube(num)
        
        #checking for root first because conditions are checked line by line, so if first condition will satisfy the squre and cube will be given every time, to prevent this checking root first is necessary
        
        #for exponent
        elif "exponent" in prompt:
           num = float(input("Number: "))
           power = int(input("Power: "))
           
           exponent(num,power)

        #for circumference
        elif "circumference" in prompt:
           radius = float(input("Radius of Circle: "))
           
           circumference(radius)
        
        #here all things are divided into parts for better reading and understanding
        elif "perimeter" in prompt:
           
           #for square
           if "square" in prompt:
              side = float(input("Length of Side of Square: "))
              perimeter_square(side)
           
          #for rectangle
           elif "rectangle" in prompt:
              length = float(input("Length of Rectangle: "))
              breadth = float(input("Breadth of Rectangle: "))
              perimeter_rectangle(length,breadth)

                      
           #for triangle
           elif "triangle" in prompt:
              s1 = float(input("Length of First Side: "))
              s2 = float(input("Length of Second Side: "))
              s3 = float(input("Length of Third Side: "))
              perimeter_triangle(s1,s2,s3)

           
           #to check if only perimeter is written           
           elif "" in prompt:
              print("Give Shape Name for calculating its Perimeter")


           #when no condition satisfy
           else:
              print("\t\tFor Now I can only deal with Perimeter of Square,Rectangle and Triangle\n")

        #same thing is here also but for area
        elif "area" in prompt:
           
           #for square
           if "square" in prompt:
              side = float(input("Length of Side of Square: "))
              
              area_square(side)

                      
           #for rectangle
           elif "rectangle" in prompt:
              length = float(input("Length of Rectangle: "))
              breadth = float(input("Breadth of Rectangle: "))
              
              area_rectangle(length,breadth)

           
           #for triangle         
           elif "triangle" in prompt:
              base = float(input("Base of Triangle: "))
              height = float(input("Height of Triangle: "))
              
              area_triangle(base,height)

           
           #for circle           
           elif "circle" in prompt:
              radius = float(input("Radius of Circle: "))
              
              area_circle(radius)


           #for trapezium
           elif "trapezium" in prompt:
              s1 = float(input("First Side of Trapezium: "))
              s2 = float(input("Second Side of Trapezium: "))
              height = float(input("Height of Trapezium: "))
              
              area_trapezium(s1,s2,height)

                      
           #to check if only area is written
           elif "" in prompt:
              print("Give Shape Name for calculating its Perimeter")


           #when no condition satisfy
           else:
              print("\t\tFor Now I can only deal with Area of Square, Rectangle, Triangle, Circle and Trapezium\n")

        #again for better reading and understanding
        elif "volume" in prompt:
           #for cube
           if "cube" in prompt:
              length = float(input("Length of Each Side of Cube: "))
              
              volume_cube(length)
           
           
           #for cuboid
           elif "cuboid" in prompt:
              length = float(input("Length of Side of Cuboid: "))
              breadth = float(input("Breadth of Side of Cuboid: "))
              height = float(input("Height of side of Cuboid: "))
              
              volume_cuboid(length,breadth,height)
           
           
           #for cylinder
           elif "cylinder" in prompt:
              radius = float(input("Radius at Bottom and Top: "))
              height = float(input("Height of Cylinder: "))
              
              volume_cylinder(radius,height)
           
           
           #to check if only volume is written
           elif "" in prompt:
              print("Give Shape Name for calculating its Perimeter")


           #when no condition satisy
           else:
              print("\t\tFor Now I can only deal with Volume of Cube, Cuboid and Cylinder\n")

        #for SI
        elif "simple interest" in prompt:
           principal = float(input("Principal: "))
           rate = float(input("Rate Of Interest: "))
           time = float(input("Time: "))
           
           simple_interest(principal,rate,time)

        #for CI
        elif "compound interest" in prompt:
           principal = float(input("Principal: "))
           rate = float(input("Rate Of Interest: "))
           time = float(input("Time: "))
           
           compound_interest(principal,rate,time)
        
        elif "help" in prompt:
           help()

elif __name__ != "__main__":
   print("Thank You For Using MasterMath By Rishabh Raj")
