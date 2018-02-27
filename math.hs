


factors n i list = case i of
    n -> n:list
    _
        | n `mod` i == 0 -> factors n (i+1) i:list
        | otherwise      -> factors n (i+1) list
