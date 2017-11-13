def spiralmatrix(twodarr):
    rstart =0
    rend = len( twodarr )
    cstart = 0
    cend =  len(twodarr[0]) 
    while rstart < rend and cstart < cend:
            i = cstart
            while i < cend:
                print(twodarr[rstart][i])
                i += 1
            rstart += 1
            j = rstart
            while j < rend:
                print(twodarr[j][cend-1])
                j +=1
            cend -= 1
           
            if rend > rstart+1:
                k = cend 
                while k >= cstart:
                    print (twodarr[rend-1][k])
                    k -= 1 
                rend -=1
            if cend > cstart+1:
                m = rend 
                while m > rstart:
                    print (twodarr[m][cstart])
                    m -= 1
                cstart += 1

spiralmatrix([[1,  2,  3,  4,  5,  6],[7,  8,  9,  10, 11, 12],[13, 14, 15, 16, 17, 18]])            
               
                
        
      
    