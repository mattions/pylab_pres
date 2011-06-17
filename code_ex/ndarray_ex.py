# ndarray_ex.py 
# This use the console style.
# Do not use this stile on a program.

# Creating an array
x = array([1, 2, 3])
print x*3
# [3 6 9]
print x-1
# [0 1 2]
y = array([10, 20, 30, 40])
print x*y
# [10 40 90]

# Multidimension

z = array([ [1, 2, 3], [10, 20, 30]])
# Can apply the math to the multidimensional
res = z*x + y
print res
#[[ 11,  24,  39],
#[ 20,  60, 120]]

# Indexing 
# Row 0:
z[0,:]
# Row 1:
z[1,:]

# Column 0
z[:,0]
# Column 1
z[:,1]
