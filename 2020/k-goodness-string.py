def get_goodness(S):
    score = 0
    for i in range(0,int(len(S)/2)):
        if(S[i] != S[len(S)-i-1]):
            score+=1
    return score

def ans(N, K, S):
    return abs(get_goodness(S)-K)


for t in range(int(input())):
    N, K = input().split(" ")
    S = input()
    print(f"Case #{t+1}: {ans(int(N), int(K), S)}")


