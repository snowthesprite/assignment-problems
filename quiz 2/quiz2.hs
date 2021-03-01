calcPoints :: Char -> Int
calcPoints n  
    | n == 'A'  =  4
    | n == 'B'  =  3
    | n == 'C'  =  2
    | n == 'D'  =  1
    | n == 'F'  =  0

calcTotalPoints l = sum([calcPoints x | x <- l])

calcGPA list = (calcTotalPoints list) / (length list)

main = print( calcGPA ['A', 'B', 'B', 'C', 'C', 'C', 'D', 'F'] )