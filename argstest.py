import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--gpiooff")
args = parser.parse_args()
if args.gpiooff:
    print("Arguments: " , args.gpiooff)
else:
    print("no args")
    
