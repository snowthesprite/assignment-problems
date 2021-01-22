bmiTell :: (RealFloat a) => a -> String  
bmiTell degreesCelsius
    | bmi <= underweightThreshold = "The patient may be underweight. If this is the case, the patient should be recommended a higher-calorie diet."  
    | bmi <= normalThreshold = "The patient may be at a normal weight."   
    | otherwise = "The patient may be overweight. If this is the case, the patient should be recommended exercise and a lower-calorie diet."  
    where bmi = degreesCelsius * 9 / 2 + 32
          underweightThreshold = 18.5  
          normalThreshold = 25.0

main = print (bmiTell 15)