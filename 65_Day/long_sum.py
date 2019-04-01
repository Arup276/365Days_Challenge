def lone_sum(a, b, c):

	if a == b and b == c:
    
		return 0
  
	if a == b:
    
		return c
  
	if a == c:
    
		return b
  
	if b == c:
    
		return a
  
	else:
    
		return a+b+c
    
