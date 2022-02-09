import math

def shortest_distance(x1, y1, x2, y2):  # this function finds the distance between two points (x1,y1) and (x2,y2)
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 4)


def process_input(x1, y1, x2, y2):
    try:
        x1 = float(x1)
    except ValueError:
    	  print ("Wrong x1")
    	  return
    try:
        y1 = float(y1)
    except ValueError:
        print ("Wrong y1")
        return
    try:
        x2 = float(x2)
    except ValueError:
        print ("Wrong X2")
        return
    try:
        y2 = float(y2)
    except ValueError:
        print ("Wrong y2")
        return
    
    distance = shortest_distance(x1, y1, x2, y2)
    
    print(distance)	

def main(): 
    
    x1 = input("Enter x1")
    y1 = input("Enter y1")
    x2 = input("Enter x2")
    y2 = input("Enter y2")
    process_input(x1,y1,x2,y2)
        
    
if __name__ == '__main__':
    main()
 