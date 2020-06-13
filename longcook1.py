# n=int(input())
# beg=1
# end=n
# num=(beg+end)//2
# while(beg<=end):
#     print(n)
#     c=input()
#     if(c=='E'):
#         break
#     elif(c=='G'):
#         # will say truth now
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
#         elif(c=='G'):
#             beg=num+1    
#         else:
#             end=num-1
#         num=(beg+end)//2
#     else:
#         # may say anythin
#         print(num)
#         c1=input()
#         if(c1=='E'):
#             break
#         print(num)
#         c2=input()
#         if(c2=='E'):
#             break
        
#         if(c1==c2):
#             # is telling truth
#             if(c1=='E'):
#                 break
#             elif(c1=='G'):
#                 beg=num+1
#             else:
#                 end=num-1
#             num=(beg+end)//2

#         else:
#             print(n)
#             c=input()
#             if(c=='E'):
#                 break
#             elif(c=='G'):
#                 # prev one was truth 
#                 if(c2=='G'):
#                     beg=num+1
#                 else:
#                     end=num-1
#                 num=(beg+end)//2
#             else:
#                 # prev one was lie
#                 if(c1=='G'):
#                     beg=num+1
#                 else:
#                     end=num-1
#                 num=(beg+end)//2

# n=int(input())
# beg=1
# end=n
# num=(beg+end)//2
# print(n)
# c=input()
# if(c=='E'):
#     pass    
# elif(c=='G'):
#     # now truth
#     while(1):
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
#         elif(c=='G'):
#             beg=num+1
#         else:
#             end=num-1
#         num=(beg+end)//2
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
# else:
#     while(1):
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
#         elif(c=='G'):
#             beg=num+1
#         else:
#             end=num-1
#         num=(beg+end)//2
# for z in range(int(input())):
#     n,k=map(int,input())
    
# n=int(input())
# beg=1
# end=n
# num=(beg+end)//2
# while(1):
#     print(n)
#     c=input()
#     if(c=='E'):
#         break
#     elif(c=='L'):
#         pass
#     else:
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
#         elif(c=='G'):
#             beg=num+1
#         else:
#             end=num-1
#         num=(beg+end)//2

# n=int(input())
# 
# beg=1
# end=n
# num=(beg+end)//2
# while(1):
#     print(n)
#     c=input()
#     if(c=='E'):
#         break
#     elif(c=='L'):
#         print(num)
#         c1=input()
#         if(c1=='E'):
#             break
#         f=0
#         while(1):
#             print(num)
#             c2=input()
#             if(c2=='E'):
#                 f=1
#                 break
#             if(c1==c2):   
#                 # if(c1=='E'):
#                 #     f=1
#                 #     break
#                 if(c1=='G'):
#                     beg=num+1
#                 else:
#                     end=num-1
#                 num=(beg+end)//2   
#                 break
#             else:
#                 c1=c2      
#         if(f==1):
#             break
#     else:
#         print(num)
#         c=input()
#         if(c=='E'):
#             break
#         elif(c=='G'):
#             beg=num+1
#         else:
#             end=num-1
#         num=(beg+end)//2

# #final--
# elif(n<=100000):

n=int(input())
# l=[i for i in range(1,n+1)]
# def fun(beg,end,l):
#     if(beg<=end):
#         num=(beg+end)//2   
#         if(beg==end):
#             print(l[num])
#             c=input()
#             if(c=='E'):
#                 return -1
#         else:    
#             print(l[num])
#             c=input()
#             if(c=='E'):
#                 return -1
#             elif(c=='L'):
#                 print(l[(num+end)//2])
#                 c1=input()
#                 if(c1=='E'):
#                     return -1
#                 elif(c1=='L'):
#                     end=(num+end)//2-1
#                     return fun(beg,end,l)
#                 else:
#                     print(l[(num+beg)//2])
#                     c2=input()
#                     if(c2=='E'):
#                         return -1
#                     elif(c2=='G'):
#                         beg=(num+end)//2 + 1
#                         return fun(beg,end,l)
#                     else:
#                         del l[(num+beg)//2:(num+end)//2 + 1]
#                         return fun(beg,len(l)-1,l)
#             else:
#                 print(l[(num+beg)//2])
#                 c1=input()
#                 if(c1=='E'):long int l[n]
#                     return -1
#                 elif(c1=='G'):
#                     beg=(num+beg)//2 + 1
#                     return fun(beg,end,l)
#                 else:
#                     print(l[(num+end)//2])
#                     c2=input()
#                     if(c2=='E'):
#                         return -1
#                     elif(c2=='L'):
#                         end=(num+beg)//2 - 1
#                         return fun(beg,end,l)
#                     else:
#                         del l[(num+beg)//2:(num+end)//2 + 1]
#                         return fun(beg,len(l)-1,l)
# fun(0,n-1,l)


def function(beg1,end1,beg2,end2):
    # print("ANDAR AYA",beg1,end1,beg2,end2)
    if(beg1<=end1 and beg2<=end2):
        mid=(beg1+end2)//2
        print(mid)
        c=input()
        if(c=='E'):
            return -1
        if(c=='G'):
            count=0
            prev='L'
            while(beg1<=end1 and beg2<=end2):
                mid1=(beg1+end1)//2
                mid2=(beg2+end2)//2
                print(mid1)
                #+=1
                c1=input()
                if(c1=='E'):
                    return -1
                elif(c1=='G' and count==0):
                    return function(mid1+1,end1,beg2,end2)
                count=1
                if(c1=='L' and prev=='G'):
                    end1=mid1-1
                    # print("Prev wala kiya",beg1,end1,beg2,end2)
                if(c1==prev and c1=='G'):
                    beg1=mid1+1
                    return function(beg1,end1,beg2,end2)

                print(mid2)
                #+=1
                c2=input()
                prev=c2
                if(c2=='E'):
                    return -1
                elif(c1==c2):
                    if(c1=='L'):
                        end2=mid2-1 
                    else:
                        beg1=mid1+1
                    return function(beg1,end1,beg2,end2)
                elif(c1=='L' and c2=='G'):
                    end1=mid1-1
                    beg2=mid2+1
                

        else:
            count=0
            prev='G'
            while(beg1<=end1 and beg2<=end2):
                mid1=(beg1+end1)//2
                mid2=(beg2+end2)//2
                print(mid2)
                #+=1
                c1=input()
                if(c1=='E'):
                    return -1
                elif(c1=='L' and count==0):
                    return function(beg1,end1,beg2,mid2-1)
                count=1
                if(c1=='G' and prev=='L'):
                    beg2=mid2+1
                    
                if(c1==prev and c1=='L'):
                    end2=mid2-1
                    return function(beg1,end1,beg2,end2)


                print(mid1)
                #+=1
                c2=input()
                prev=c2
                if(c2=='E'):
                    return -1
                elif(c1==c2):
                    if(c1=='G'):
                        beg1=mid1+1
                    else:
                        end2=mid2-1
                    return function(beg1,end1,beg2,end2)
                elif(c1=='G' and c2=='L'):
                    end1=mid1-1
                    beg2=mid2+1

    # print("After everythin",beg1,end1,beg2,end2)
    if(beg1>end1 and beg2<=end2):
        function(beg2,(beg2+end2)//2,(beg2+end2)//2,end2)
    elif(beg2>end2 and beg1<=end1):
        function(beg1,(beg1+end1)//2,(beg1+end1)//2,end1)

function(1,n//2,n//2,n) 






