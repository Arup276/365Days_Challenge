def make_bricks(small, big, goal):

 	sums = small + 5*big
 
	req_small = goal % 5
  
	if sums >= goal and small >= req_small:
    
		return True
  
	else:
	
	return False