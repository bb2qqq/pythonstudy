### Formula of permutation
    The number of permutations of n distinct objects is n factorial usually written as n!, which means the product of all positive integers less than or equal to n.  
    对于一个独特元素数为n的集合上，求它的permutations时，在第一个位置上，我们有n个选择，第二个位置n-1个阶乘，到最后一个位置时，我们还剩下1种选择。  
    所以总的可能性是n!

### Formula of combination
    combanation就是从一个有n个不同元素的集合中取出k个作为子集合，问有多少个不同的k个元素的子集。
    在选择子集的第一个元素时，我们有n种选择，第二个元素有n-1种选择，第k个元素时有n-k+1种选择。
    所以combination的公式是：n!/(n-k)!
    我看了下wikipedia上的公式，和我的不同，我想大概有问题，于是拿set([3, 2, 1])做下试验，取两个元素做组合
    嗯，第一个元素有3种可能，1，2，3，第二个元素有两种可能，可是，是1，2，还是2，3还是1，3呢。。。
    好，我先选1，还剩下2，3，共有(1, 2), (1, 3)两种组合。我先选2，共有(2, 3), (2, 1)两种选择。。
    等等，貌似重复了。不对！
    让我们以集合的角度来思考这一点。
    我们要从n人中选k人。让我们用电影院排队来做一个比喻。n人排队，我们只取排在前面的k人。当我们选定一个特定的k人组合。
    这k人组合内部有k!种排队方式，在他们身后的没被选中的n-k人有(n-k)!种排队方式。
    这特定的k人组合被选中的时候，他们的排队状态共有k!(n-k)!种可能。
    而所有人共有n!种排队方式。
    所以，所有不同的k人组合数等于   n!/k!(n-k)!
