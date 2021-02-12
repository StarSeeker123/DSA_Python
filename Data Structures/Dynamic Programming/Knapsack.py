#Knapsack

def knapsack(wt, val, W, n):

    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n-1] <= W:
        t[n][W] = max(
            val[n-1] + knapsack(
                wt, val, W-wt[n-1], n-1),
            knapsack(wt, val, W, n-1))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1)
        return t[n][W]


# driver code
val = [10, 20, 30]#[10,20,30]
wt = [1, 1, 1]#[1,1,1]
W = 2#2
n = len(val)

t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
print(knapsack(wt, val, W, n))
