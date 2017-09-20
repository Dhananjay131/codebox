#!usr/bin/python3
#MxN matrix


def nullifyRow(rowNum):
	j=0
	while j<n:
		a[rowNum][j]=0
		j+=1
def nullifyCol(colNum):
	i=0
        while i<m:
                a[i][colNum]=0
                i+=1

a=[[1,2,3,4],[5,6,0,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]	
i,m=0,5
j,n=0,4
row,col=0,0

while row<m:
	while col<n:
		if a[row][col]==0 :
			print("Rows and columns to be deleted: ",row," ",col)
			nullifyRow(row)
			nullifyCol(col)
			print a
			exit(0)
		col+=1
	row+=1
	col=0


