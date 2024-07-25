nums=input()
nums=eval(nums)
max_sum=nums[0]
current_sum=nums[0]
start=0
end=0
for i in range(1,len(nums)):
    if nums[i]>current_sum+nums[i]:
        current_sum=nums[i]
        start=i
    else:
        current_sum=current_sum+nums[i]
        
    if current_sum>max_sum:
        max_sum=current_sum
        end=i
    
print(max_sum,nums[start:end+1])
