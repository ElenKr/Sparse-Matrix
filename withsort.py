import random
import time



def makedata(data):
    k=0
    
    element=()
    i=40000*[-1]
    j=40000*[-1]
    val=40000*[0]
    random.seed(1059438)
    
    while k<40000:        
        found=False
        val[k]=random.randint(1,99)
        i[k]=random.randint(0,99)
        j[k]=random.randint(0,9999)

        if k!=0:
            for x in data:
                if i[k]==x[0] and j[k]==x[1]:
                    found=True
                
                
        if found==False:           
            element=(i[k],j[k],val[k])
            data.append(element)
            k=k+1

            
######################################## πολ/σμος με διάνυσμα χ
            
def multivector(data,iloc,j,x):
    b=100*[0]
    k=0    
    for i in range(0,len(iloc)):
        summ=0
        
        if iloc[i]==-1: #an h grammh einai adeia
            b[i]=0
        else:
            
            k=iloc[i]#arxh grammhs

            
            #gia thn teleytaia grammh
            if i+1==len(iloc):
                mm=len(data)
            
            #gia thn thn perpythsh poy iloc[i+1]==-1
            else:
                z=i
                while iloc[z+1]==-1:
                    z=z+1
                mm=z+1
                mm=iloc[mm]   
            for k in range(iloc[i],mm):
                
                summ=data[k][2]*x[j[k]]+summ
            
            b[i]=summ
            
            
    #print("b=",b)
        

########################################για να βρω πόσα είναι τα στοιχεία της κάθε γραμμής

def elements(iloc,j,data):
    row=5*[0]
    for i in range(0,4):
        
        ll=True
        if iloc[i]==-1:
            print(i,':',end=' ')
            print(row)
            
        else:   
            if i+1==len(iloc):
                number=len(data)-iloc[i]

            else:
                k=i+1
                while ll==True:
                    if iloc[k]!=-1:
                        ll=False
                    else:
                        k=k+1          
                number=iloc[k]-iloc[i]
                  
            k=iloc[i]
            print(i,':',end=' ')
            
            
                
            for aa in range(number):
                row[j[k]]=data[k][2]
                k=k+1
            print(row)
        row=5*[0]
        
        

            
##############################################
def addElement(data,iloc,j,el):
    found=False
    l=0

        
    if iloc[el[0]]==-1:#adeia h grammh
        data.append(-1)
        nz=len(data) 
        for jj in range(nz-1,iloc[el[0]+1],-1):
            data[jj]=data[jj-1]
            
        data[iloc[el[0]+1]]=el
       
        for x in range(el[0]+1,len(iloc)):
           iloc[x]=iloc[x]+1 
        iloc[el[0]]=iloc[el[0]+1]-1
        j.append(-1)
        for i in range(nz):
           j[i]=data[i][1]

    else:
        for ii,xx in enumerate(data):
            
            if el[0]==xx[0] and el[1]==xx[1]:
                found=True
                l=ii
                
                
        if found==True: #uparxei idio kai antikathista          
            data[l]=el
            
        else:
            data.append(-1)
            nz=len(data)
    
            k=iloc[el[0]]
            x=data[iloc[el[0]]][1]

            while x<el[1]:
                k=k+1
                x=data[k][1]  
            
            for jj in range(nz-1,k-1,-1):   
                data[jj]=data[jj-1]
            
            data[k]=el     
            for x in range(el[0]+1,len(iloc)):
                if iloc[x]!=-1:
                    iloc[x]=iloc[x]+1
                    
            j.append(-1)
            for i in range(nz):
                j[i]=data[i][1]
            print("data=",data)

##############################################πολ/σμος με αναστροφο
def multix(data,iloc,pl):
    summ=10000*[0]
    pl=len(iloc)*[0]
    number=0
    
    ############# i elements gia na metra  ta stoixeia ana grammi
    for i in range(0,len(iloc)):
        
        ll=True
        if iloc[i]==-1:
            #print(i,':',end=' ')
            #print(row)
            continue
            
        else:   
            if i+1==len(iloc):
                number=len(data)-iloc[i]

            else:
                k=i+1
                while ll==True:
                    if iloc[k]!=-1:
                        ll=False
                    else:
                        k=k+1          
                number=iloc[k]-iloc[i]
                  
            k=iloc[i]
          
            
            
            pl[i]=number
     #######      
    
    k=0
    aaa=0
    
    for gr in range(0,4):

        for st in range(0,4):

            nw=iloc[gr]
            y=iloc[st]
            k=aaa
           
            
            while nw<(iloc[gr]+pl[gr]):
              
                for y in range(iloc[st],iloc[st]+pl[st]):
                    if data[nw][1]==data[y][1]:
                        summ[k]=data[nw][2]*data[y][2]+summ[k]
                nw= nw+1
               
                y=y+1
                               
            
            aaa=aaa+1
   # print("sum=",sum0)

        
            
###############################################

def main():
    
    data=[]
    ve=10000*[1]
    
    makedata(data)
    data.sort()
    #print("data=",data) 
    nz=len(data)
    iloc=100*[-1]
    j=nz*[-1]
    
    pll=len(iloc)*[0] 
    for i in range(nz):
        j[i]=data[i][1]
    
    for aa,x in enumerate(data):
        if iloc[x[0]]==-1:
            iloc[x[0]]=aa
            
    #print("iloc=",iloc)
    #el=(2,1,10)
    #addElement(data,iloc,j,el)    
    #to=time.time()
    #multivector(data,iloc,j,ve)
    #to=time.time()-to
    #print("multiplication with vector took:",to,"sec")
            
    #me anastrofo
    to=time.time()
    multix(data,iloc,pll)
    to=time.time()-to
    print("multiplication A AT took:",to,"sec")
    
    #εκτύπωση κατά γραμμές
    #elements(iloc,j,data)
    #multi(data,iloc,j)

if __name__=="__main__":
    main()
                  
