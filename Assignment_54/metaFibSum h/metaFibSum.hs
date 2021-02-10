fib :: (Integral a) => a -> a  
fib 0 = 0  
fib 1 = 1  
fib n = fib (n - 1) + fib (n - 2)

partialSumEntries n = [fib (x) | x <- [0, 1..n]]

partialSum n = sum (partialSumEntries n)

metaSumEntries n = [partialSum x | x <- [0..fib (n)]]

metaSum n = sum [ metaSumEntries (n) !! x | x <- partialSumEntries (n)]

main = print (metaSum 6)