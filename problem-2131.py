# 2131 - Longest Palindrome by Concatenating Two Letter Words

def longestPalindrome(words):
    uniquePairs = {}
    for word in words:
        if word in uniquePairs:
            uniquePairs[word] += 1
        else:
            uniquePairs[word] = 1

    count = 0
    hasCentre = False
    for word in uniquePairs:
        revWord = word[1] + word[0]
        if revWord != word:
            if revWord in uniquePairs:
                count += min(uniquePairs[revWord], uniquePairs[word]) * 2
        else:
            n = uniquePairs[word]
            if n % 2 == 0:
                count += n * 2
            else:
                count += (n - 1) * 2
                hasCentre = True
    if hasCentre:
        count += 2
    return count