def  num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
    d =createones(grid_width, grid_height)
    d[start_x][start_y]=0
    f=[[start_x,start_y]]
    while(len(f)>0):
        new=[]
        for x in f:
            if(0<=x[0]+conn_x1<grid_height and 0<=x[1]+conn_y1<grid_width):
                d=offit( x[0]+conn_x1, x[1]+conn_y1,d)
                if([x[0]+conn_x1, x[1]+conn_y1]):
                    new.append([x[0]+conn_x1, x[1]+conn_y1])
            if(0<=x[0]+conn_x2<grid_height and 0<=x[1]+conn_y2<grid_width):
                d=offit( x[0]+conn_x2, x[1]+conn_y2,d)
                if( [x[0]+conn_x2, x[1]+conn_y2] not in f):
                    new.append( [x[0]+conn_x2, x[1]+conn_y2])
        f=new
    return d
def offlights(grid_width, grid_height,conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y,ans):
    if(0<=start_x+conn_x1<grid_height and 0<=start_y+conn_y1<grid_width):
        ans=offit( start_x+conn_x1, start_y+conn_y1,ans)
    if(0<=start_x+conn_x2<grid_height and 0<=start_y+conn_y2<grid_width):
        ans=offit( start_x+conn_x2, start_y+conn_y2,ans)
    return ans
def offit(x,y,ans):
   
    ans[x][y]=0
    return ans
    


def createones(grid_width, grid_height):
    ans=[]
    for i in range(grid_height):
        ans.append([])
        for  x in range(grid_width):
            ans[i].append(1)
    return ans
print(num_illuminated(10,5,1,1,0,-1,1,1))