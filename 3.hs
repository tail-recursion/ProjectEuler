

{-
while n > 1:
    while n % d == 0:
        n = n / d
        factors.append(d)
    d = d + 1
-}

-- n > 0
prime_factors :: Integer -> Integer -> [Integer] -> [Integer]
prime_factors n d factors = case n of
    1 -> return factors
    _ | n `mod` d == 0 && (n/d) `mod` d != 0 -> prime_factors (n/d) (d+1) (d:factors)
      | n `mod` d == 0 -> prime_factors (n/d) d factors
      | otherwise -> prime_factors n d



-- largest = max prime_factors 600851475143 2 [[]
