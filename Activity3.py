class pair_elements:
   def twoSums(self,Nums,target):
      lookup = {}
      for i, num in enumerate(Nums):
        if target - num in lookup:
         return(lookup[target - num], i)
      lookup[num]= i
value= int(input("Enter the number for which u wanna make this research : "))
print("index1=%d, index2=%d" % pair_elements().twoSums((10,20,30,40,50,60,70),value))