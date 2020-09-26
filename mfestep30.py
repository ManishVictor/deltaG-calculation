import math as m
from seqfold import dg, dg_cache, fold, Struct#download seqfold by JJ Timons from github
from typing import List
header=num=''
count=add=0

with open("input1.txt","r") as file1:#single line fasta file required
    read=file1.read()
    data=read.split("\n")
    #print(data)# Check your process
    for each in data:
        if(">" in each):
            header=each
            #print(each)#check your process
        else:
            for i in range(0,len(each)-30,30):#window of 30 nucleotides because ribosmes shadow those many nucleotides
                str=each[i:i+42:]#this will input the step size. you can change 42 to any value depending upon your requirement
                #print(str)#check your process
                dg(str, temp = 37.0)
                structs: List[Struct] = fold(str)
                num=sum(s.e for s in structs)
                #print(num)#check your process
                if(m.isinf(num)):
                    pass
                else:
                    add+=num
                    #print(add)#check your process
                    count=count+1
            if (count!=0):
                str=format(float((add/count)),'.2f')
                print(str)
                add=count=0
                with open("deltaG.txt","a") as file2:#output filename
                    file2.write(header+":"+str+"\n")#output style
            else:
                pass