# -*- coding: cp1252 -*-
import winsound
import math
import random
dict = {}

#initialize dict with factors for deriving all 22 shrutis in an octave
def init_22():
    global dict
    dict["s"] = 1.0
    dict["r1"] = 32.0/31.0
    dict["r2"]= 16.0/15.0
    dict["r3"]= 10.0/9.0 
    dict["r4"]= 9.0/8.0
    dict["g1"]= 32.0/27.0 
    dict["g2"]= 6.0/5.0
    dict["g3"]= 5.0/4.0
    dict["g4"]= 81.0/64.0
    dict["m1"]= 4.0/3.0
    dict["m2"]= 27.0/20.0
    dict["m3"]= 45.0/32.0
    dict["m4"] =64.0/45.0
    dict["p"]= 3.0/2.0
    dict["d1"]= 128.0/81.0
    dict["d2"]=8.0/5.0
    dict["d3"]= 5.0/3.0
    dict["d4"]= 27.0/16.0
    dict["n1"]=16.0/9.0
    dict["n2"]= 9.0/5.0
    dict["n3"]= 115.0/80.0
    dict["n4"]= 31.0/16.0
    dict["S"]=  2.0

def init_equi():
    global dict
    dict["s"]  = 1.000000
    dict["r1"] = 1.059463
    dict["r2"] = 1.122462
    dict["r3"] = 1.189207 
    dict["g1"] = 1.189207
    dict["g2"] = 1.259921
    dict["g3"] = 1.259921 
    dict["m1"] = 1.334840
    dict["m2"] = 1.414214
    dict["p"] =  1.498307
    dict["d1"] = 1.587401
    dict["d2"] = 1.681793
    dict["d3"] = 1.781797
    dict["n1"] = 1.781797
    dict["n2"] = 1.887749
    dict["n3"] = 1.887749
    dict["S"]  = 2.000000

def getFrequencies(swaraList,baseFreq):
    freqList=[]
    for swara in swaraList:
        freqList.append(int(dict[swara]*baseFreq))
    return freqList
        
    
#Return all the swaras for DheeraShakarabharanam 
def getDheeraShankarabharanamSwaras():
    theSwaras = []
    theSwaras.append("s")
    theSwaras.append("r2")
    theSwaras.append("g2")
    theSwaras.append("m1")
    theSwaras.append("p")
    theSwaras.append("d2")
    theSwaras.append("n2")
    theSwaras.append("S")
    return theSwaras

#Return all the frequencies for DheeraShakarabharanam, given the frequency of aadhaara shadjamam
def getDheeraShankarabharanamFrequencies(baseFrequency):
    return getFrequencies(getDheeraShankarabharanamSwaras(), baseFrequency)

def getMadhyama(melaNumber):
    if (melaNumber>36):
        return "m2"
    else:
        return "m1"


def getDhaNi(melaNumber):
    if(melaNumber%6==1):
        return ["d1","n1"]
    elif(melaNumber%6==2):
        return ["d1","n2"]
    elif(melaNumber%6==3):
        return ["d1","n3"]
    elif(melaNumber%6==4):
        return ["d2","n2"]
    elif(melaNumber%6==5):
        return ["d2","n3"]
    else:
        return ["d3","n3"]

def getRiGa(melaNumber):
    if(math.ceil((melaNumber%36)/6.0)==1):
        return ["r1","g1"]
    elif(math.ceil((melaNumber%36)/6.0)==2):
        return ["r1","g2"]
    elif(math.ceil((melaNumber%36)/6.0)==3):
        return ["r1","g3"]
    elif(math.ceil((melaNumber%36)/6.0)==4):
        return ["r2","g2"]
    elif(math.ceil((melaNumber%36)/6.0)==5):
        return ["r2","g3"]
    else:
        return ["r3","g3"]
    

#Return all the swaras for a given Melakartha (number according to Katapayadi)
def getMelaSwaras(melaNumber):
    #To do given melakarta number get frequencies
    '''if(melaNumber<1 or melaNumber>72):
        raise Error()'''
    
    MelaSwaraList=[]
    RiGa = getRiGa(melaNumber)
    DhaNi = getDhaNi(melaNumber)
    Ma = getMadhyama(melaNumber)
    
    MelaSwaraList.append("s")
    MelaSwaraList.append(RiGa[0])
    MelaSwaraList.append(RiGa[1])
    MelaSwaraList.append(Ma)
    MelaSwaraList.append("p")
    MelaSwaraList.append(DhaNi[0])
    MelaSwaraList.append(DhaNi[1])
    MelaSwaraList.append("S") 
    return MelaSwaraList

def playScale(ragaFrequencies, duration):
    for x in ragaFrequencies:
        print x
        winsound.Beep(x, duration)
    for x in reversed(ragaFrequencies):
        print x
        winsound.Beep(x, duration)

def playPhrase(ragaFrequencies, duration):
    for x in ragaFrequencies:
        print x
        winsound.Beep(x, duration)
    

def insertionSort(alist):
    playPhrase(alist,700)
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
        playPhrase(alist,700)
        playPhrase(phrase2Frequencies,700)


def selectionsort(aList):
    playPhrase(aList,700)
    for i in range( len( aList ) ):
        least = i
        for k in range( i + 1 , len( aList ) ):
            if aList[k] < aList[least]:
                least = k
        swap( aList, least, i )
        playPhrase(aList,700)
        playPhrase(phrase2Frequencies,700)

def bubblesort(a):
    playPhrase(a,700)
    update=True
    n=len(a)
    while(update==True and n>1):
        update = False
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                update = True
        playPhrase(a,700)
        playPhrase(phrase2Frequencies,700)

        n-=1
        
    return a

 
 
def swap( A, x, y ):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp
    
base = 400
init_equi()
#raga = getDheeraShankarabharanamFrequencies(base)
#playScale(raga, 1000)
#print getMelaSwaras(56)
'''mela= input("enter mela number(1-72) >> ")
melaFrequencies = getFrequencies(getMelaSwaras(mela), base)
playScale(melaFrequencies, 1000)
'''
'''
mela=random.randint(1,72)
phrase2=["m2","r2","g2","m2","p","n2","p","d2","n2","S"]
print ("this is melakarta number ",mela)
melaSwaras=getMelaSwaras(mela)
print melaSwaras
melaFrequencies=getFrequencies(melaSwaras, base)
playScale(melaFrequencies, 1000)
random.shuffle(melaSwaras)
print melaSwaras
phraseFrequencies=getFrequencies(melaSwaras,400)
print("this is the shuffled phrase",phraseFrequencies)
insertionSort(phraseFrequencies)
'''
phrase=["S","p","g2","m2","d1","n2","s","r1"]
phrase2=["m2","r2","g2","m2","p","n2","p","d2","n2","S"]
phraseFrequencies=getFrequencies(phrase,400)
phrase2Frequencies=getFrequencies(phrase2,400)
insertionSort(phraseFrequencies)
#selectionsort(phraseFrequencies)
#bubblesort(phraseFrequencies)





    







    
