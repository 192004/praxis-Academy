# def http_eror(status):
#         match status:
#             case 400:
#                 return "Bad request"
#             case 404:
#                 return "Not found"
#             case 418:
#                 return "I'm a teapot"
#             case _:
#                 return "Something's wrong with the internet"

# print(http_eror())

match ():
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

def where_is(point):
    match point:
        case point (x=0, y=0):
            print("Origin")
        case point (x=0, y=y):
            print(f"Y={y}")
        case point (x=x, y=0):
            print(f"X={x}")
        case point ():
            print("Somewhere else")
        case _:
            print("Not a point")