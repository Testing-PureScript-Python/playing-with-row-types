module Main where


data IO a
data Unit

foreign import println :: forall a. a -> IO {}
foreign import discard :: forall a b. IO a -> (a -> IO b) -> IO b

getFoo :: forall a r. {foo :: a | r} -> a
getFoo {foo} = foo


main :: IO {}
main = do println (getFoo {foo: 1, bar: "2"}) 
          println (getFoo {foo: "3", bar: 4})
          println (getFoo {foo: {}})
          println (getFoo {foo: {foo_nested: 5, bar_nested: 6}, bar: 7})
  