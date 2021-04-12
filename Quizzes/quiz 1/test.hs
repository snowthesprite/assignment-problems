factor a b = if a `mod` b == 0 then b else 0

sumFactors n = sum [factor n y | y <- [1, 2..n]]

main = print(sumFactors 10) -- should come out to 1+2+5+10 = 18