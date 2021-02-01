squareSingleDigitNumbers list = map (^2) (filter (<10) list)

main = print (squareSingleDigitNumbers [2, 7, 15, 11, 5])