#two.py
import one

print("TOP LEVEL IN TWO.PY")	

one.func()

if __name__ == '__main__': # RUN THE SCRIPT 
	print("TWO.PY is being run directly")

else:
	print("TWO.PY has been imported")
