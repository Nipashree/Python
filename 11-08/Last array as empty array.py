a=np.array([[1, 2, 3], [4, 5, 6]])
a=np.append(a,np.empty((1, 3),dtype=int),axis=0)
print(a)
