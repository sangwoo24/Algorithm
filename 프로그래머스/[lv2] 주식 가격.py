def solution(prices):
    ans = [len(prices)-i-1 for i in range(len(prices))]
    
    for i in range(len(prices)- 1):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                ans[i] = j - i
                break
    return ans