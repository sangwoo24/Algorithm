def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        line = ''
        bin_a = bin(arr1[i])[2:] #str
        bin_b = bin(arr2[i])[2:]

        bin_a = '0' * (n-len(bin_a)) + bin_a
        bin_b = '0' * (n-len(bin_b)) + bin_b
        for j in range(n):
            if bin_a[j] == '0' and bin_b[j] == '0':
                line += " "
            else:
                line += "#"
        ans.append(line)
    return ans
            

            