
import numpy
bankingdatabase=numpy.load("bankingdatabase2player.npy")


#print(numpy.unique(bankingdatabase,return_counts=True))

print(bankingdatabase[0,16,5,0]+bankingdatabase[0,15,5,0])
