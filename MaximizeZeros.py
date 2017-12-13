def setZeroes( A ):
        i = 0
        jo = []
        flag = False
        while i < len(A):
            j = 0
            while j < len(A[i]):
                print("loop", j)
                if A[i][j] == 0:
                    print("came", i, j)
                    jo.append(j)
                    flag = True
                    break
                else:
                    print("loop1", j)
                    print("came1", i, j)
                    if j in jo:
                        print("came2", i, j)
                        A[i][j] = 0
                j += 1
            print(jo)
            if flag:
                A[i] = [0]*len( A[i] )
                flag = False
            i += 1
        return A
print(setZeroes([
  [0, 0],
  [1, 1]
]))