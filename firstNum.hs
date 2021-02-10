chain :: (Integral a) => a -> [a]  
chain 1 = [1]  
chain n  
    | even n =  n:chain (n `div` 2)  
    | odd n  =  n:chain (n*3 + 1)

firstNumberWithChainLengthAtLeast :: Int -> Int
firstNumberWithChainLengthAtLeast n = length (takeWhile (notLong) (map chain [1..n])) + 1
    where notLong xs = length xs < n

main = print (firstNumberWithChainLengthAtLeast 15)