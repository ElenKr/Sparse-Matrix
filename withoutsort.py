import random
import time


############################################Αρχικοποίηση
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



    #print(data)

#########################################Πολ/σμός με διάνυσμα
def multivector(data,iloc,x,j,nextj):
    
    b=100*[0]
    k=0
    summ=0
    
    for i in range(0,len(iloc)):
        summ=0
        if iloc[i]==-1:
            b[i]=0
        else:
            line=iloc[i]
            while nextj[line]!=-1:
                
                summ=data[line][2]*x[data[line][1]]+summ
        
                line=nextj[line]
            summ=data[line][2]*x[data[line][1]]+summ
        b[i]=summ
        

    #print("b=",b)

    
#########################################Εμφάνιση κατά γραμμές
def elements(iloc,j,data,nextj):
    for i in range(0,4):
        k=0
        row=5*[0]
        if iloc[i]!=-1:               
            line=iloc[i]
                       
            while nextj[line]!=-1:
                k=j[line]
                row[k]=data[line][2]        
                line=nextj[line]

            k=j[line]
            row[k]=data[line][2]
            
        print(i,':',end=' ')    
        print(row)
    
        
##########################################Προσθήκη νέου στοιχείου
        
def addElement(data,iloc,el,nextj):
    k=0
    found=False
    if iloc[el[0]]==-1: #poy h grammh einai adeia
        iloc[el[0]]=len(data)-1
        data.append(el)
        nextj.append(-1)
    else: 
              
        for i,x in enumerate(data):
            if el[0]==x[0] and el[1]==x[1]:
                found=True
                k=i
                
        if found==True:           
            data[k]=el      
        else: #poy den einai adeia alla den yparxei idio j
            data.append(el)
            nextj.append(-1) 
            line=iloc[el[0]]
            
            while nextj[line]!=-1:        
                line=nextj[line]
                
            nextj[line]=len(data)-1 
    
##########################################Πολ/σμός Α με ΑΤ
            
def multi_anastrofos(data,iloc,j,nextj):
    gin=10000*[-1]
    jj=0
    k=0
    summ=0   
   

    for i in range(0,len(iloc)):
        summ=0
        for jj in range(0,len(iloc)):
             

             line=iloc[i]
             line2=iloc[jj]
             
             if line==-1 or line2==-1:
                summ=0
                
             else :
                while nextj[line]!=-1:
                    line2=iloc[jj]
                    while nextj[line2]!=-1:
                        if data[line][1]==data[line2][1]:
                            summ=summ+data[line][2]*data[line2][2]
                        
                        line2=nextj[line2]
                    
                    if data[line][1]==data[line2][1]:
                        summ=summ+data[line][2]*data[line2][2]
                    line=nextj[line]
                if data[line][1]==data[line2][1]:
                        summ=summ+data[line][2]*data[line2][2]
             gin[k]=summ
             k=k+1
             summ=0
    #print("gin=",gin)   
           
                
    


##########################################
def main():
    data=[]
    
    makedata(data)
    
   
    nz=len(data)
    j=nz*[-1]
    xx=10000*[1]
    
    for i,x in enumerate(data):    
        j[i]=x[1]
        
    iloc=100*[-1]
    nextj=len(data)*[-1]
    #el=(1,2,3)

    for aa,x in enumerate(data):
        if iloc[x[0]]==-1:
            iloc[x[0]]=aa
        else:
            nxt=iloc[x[0]]
            while nextj[nxt]!=-1:
                nxt=nextj[nxt]
               
            nextj[nxt]=aa
    #print(data)
    #print("j=",j)        
    #print("iloc=",iloc)
    #print("nextj=",nextj)
    #elements(iloc,j,data,nextj)
    #multi_anastrofos(data,iloc,j,nextj)
            
    to=time.time()    
    multi_anastrofos(data,iloc,j,nextj)
    to=time.time()-to
    print("the multiplication Α*ΑΤ took ",to,"sec")
     #multivector(data,iloc,xx,j,nextj)
    #addElement(data,iloc,el,nextj)
    #print(data)
    #multi_anastrofos(data,iloc,j,nextj)
    #print("j",j)        
    #print("iloc",iloc)
    #print("nextj",nextj)


if __name__=="__main__":
    main()
