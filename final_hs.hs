sumCube n = sum [y ** 3 | y <- [1, 2..n]]

main = print(sumCube 10)