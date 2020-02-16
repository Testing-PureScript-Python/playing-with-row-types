-- | This module is to show the type checker,
--   and cannot run without giving proproriate implementations in Example.py
module Example where

type LinqType = forall r f. {map :: forall a b. (a -> b) -> f a -> f b | r}

data PyList a
data PyOptional a


foreign import mkPyList :: forall a. Array a -> PyList a
foreign import mkPyOption :: forall a. a -> PyOptional a
foreign import mkPyNone :: forall a. PyOptional a
foreign import f :: Int -> Number

list1 =  mkPyList [1, 2]
opt1 =  mkPyOption 1
opt2 :: PyOptional Int
opt2 = mkPyNone

foreign import linq :: LinqType
test1 :: PyList Number
test1 = linq.map f list1

test2 :: PyOptional Number
test2 = linq.map f opt1

test3 :: PyOptional Number
test3 = linq.map f opt2

