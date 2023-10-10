import json
import numpy

bankingdatabase=numpy.zeros((7,401))
print(bankingdatabase)



numpy.savetxt('bankingdatabase.csv', bankingdatabase, delimiter=',')
