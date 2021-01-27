findSmallestPositive :: (Num a, Ord a) => [a] -> a
findSmallestPositive [] = error "maximum of empty list"  
findSmallestPositive [x] = x  
findSmallestPositive (x:xs) 
    | x < 0 = minTail
    | x < minTail = x
    | otherwise = minTail  
    where minTail = findSmallestPositive xs

main = print (findSmallestPositive [8, 3, -1, 2, -5, 7])