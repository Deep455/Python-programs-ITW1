string=""
for row in range(1,8,1):
	string=string+"*"
	temp_for_star=0
	temp_for_spaces=0
	if (row==1) or (row==4):
		temp_for_star=2               
	if (row==2) or (row==3):
		temp_for_spaces=2
	else:
		temp_for_spaces=row-4
	for k in range(temp_for_star):
		string=string+"*"
	for k in range(temp_for_spaces):
		string=string+" "
	string=string+"*"
	string=string+"\n"
print(string)
