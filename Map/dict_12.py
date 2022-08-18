students = {
	'Aex':{
		'class':'V',
		'rolld_id':2
	},
    'Puja':{
    	'class':'V',
        'roll_id':3
    }
}

# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 


for i in students:
	print(i)
	for z in students[i]:
		print(z, students[i][z])