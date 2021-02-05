recommendClothing :: (RealFloat a) => a -> String  
recommendClothing degreesCelsius
    | degreesFahrenheit >= 80 = "You should wear a shortsleeved shirt today."  
    | degreesFahrenheit > 65 = "You should wear a longsleeved shirt today."
    | degreesFahrenheit > 50 = "You should wear a sweater today."   
    | otherwise = "You should wear a jacket today."
    where degreesFahrenheit = degreesCelsius * 9 / 5 + 32

main = print (recommendClothing 15)