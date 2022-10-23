import os
val = 0
files = os.listdir('pictures')
for f in files:
    os.rename('pictures/' + str(f), 'pictures/test_' + str(val) + '.png')
    val +=1