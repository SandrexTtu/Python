def read_int(prompt, min, max):
    ok = False
    while not ok:
	    try:
		    value = int(input(prompt))
		    ok = True
	    except ValueError:
		    print("error:wrong input")
	    if ok:
		    ok = value >= min and value <= max
	    if not ok:
		    print("Error:the value is not within permitted range (" + str(min)+ "..." + str(max)+")")
    return value;



v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
