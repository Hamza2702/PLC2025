-- create inpFunc
inpFunc a b = [a..b]

-- Define applicatorFunc
applicatorFunc inpFunc a b =
    fromIntegral (sum (inpFunc a b))

main = do
    putStrLn "Enter the starting integer (a):"
    a <- readLn
    putStrLn "Enter the ending integer (b):"
    b <- readLn
    let result = applicatorFunc inpFunc a b
    putStrLn ("Result = " ++ show result)
