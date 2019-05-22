N = [[1,11.-5,3],[3,22,-2,4],[5,10,-6,8],[5,16,-1,3]]
suma = 0
for i in range (4):
    suma = suma + N[i][2-i]
print ("la suma es: ",suma)
