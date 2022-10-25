#!/usr/bin/python3
if __name__ == "__main__":
    import inspect, collections
    if len(inspect.signature(collection.args)) == 0:
        print("Number of argument:")
    elif len(inspect.signature(collection.args)) > 0:
        print("Number of arguments:")
    for i in range(len(inspect.signature(collection.args))):
        print(args(i))
    
