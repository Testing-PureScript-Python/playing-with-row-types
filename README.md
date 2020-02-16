# Playing With Row Types of PureScript-Python

A reason why PureScript is appealing is its row polymorphisms,
which gives us the capability of expressing extensible records.

## Requisite

The same as [Hello World of PureScript-Python](https://github.com/Testing-PureScript-Python/hello-world).

## Notes

Our example is presented in the Main module, at `src/Main.purs`:

```purescript
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
```

Run `spago run` you get

```
1
3
{}
{'foo_nested': 5, 'bar_nested': 6}
```

Check out `src/Main.py` to get the implementation of `println` and `discard`.

## An Examplar Use Case of Extensible Records

The compiler of Python is untyped, things like Mypy needs manual annotations and not expressive enough for quite a few use cases.

For instance, when designing a object for configuration, you might not know the whole fields of your configuration object:

```python
def f(x: Configure):
    use(x.a, x.b, x.c)


def g(x: Configure):
    use(x.x, x.y, x.z)
```

When you didn't finish making your configure functions, you won't know the concrete definition of `Configure` because it changes correspondingly with the demands.

You might make some abstract types to support interface-oriented programming,
but it's verbose when implementing the concrete `Configure` type, or even using it in each configure function.

A rudimentary solution is using `typing_extensions.Protocol`, see [PEP0544](https://www.python.org/dev/peps/pep-0544/),
which gives more expressive examples about the reason why we needs things like extensible records.


Unfortunately, `typing_extensions.Protocol` is still be incapable of expressing safer and more composable code,
that is because `Mypy`(of course, including PyCharm) doesn't support higher rank types or higher kinded types(PureScript does!).

We give an example to show Mypy's weakness about higher kinded types,


<details>

<summary>following code cannot be typed by any python static type checker so far.</summary>

```python
class Linq(Protocol):
  def map(...): ... # cannot type in Mypy
  # its type is: `(a -> b) -> M[a] -> M[b]`, where `M` is Mappable


def f(x: int) -> float
    ...

mappable1 = [1, 2, 3] # type: List[int]
mappable2 = None      # type: Optional[int]
mappable3 = 3         # type: Optional[int]

mappable4 = BinaryTree.make_leaf(1) # type: BinaryTree[int]

Linq.map(f, [1, 2])    # want List[float]
Linq.map(f, mappable2) # want Optiinal[float]
Linq.map(f, mappable3) # want Optiinal[float]
Linq.map(f, mappable4) # want BinaryTree[float]
```

</details>



<details>

<summary> However in purescript, it's simple. </summary>

```purescript
-- | This module is to show the type checker,
--   and cannot run without giving proproriate implementations in Example.py
module Example where

-- polymorphic map with virtual calls
type LinqType = forall r f. {map :: forall a b. (a -> b) -> f a -> f b | r}

data PyList a
data PyOptional a


foreign import mkPyList :: forall a. Array a -> PyList a
foreign import mkPyOption :: forall a. a -> PyOptional a
foreign import mkPyNone :: forall a. PyOptional a
foreign import f :: Int -> Number
foreign import linq :: LinqType

list1 =  mkPyList [1, 2]
opt1 =  mkPyOption 1
opt2 :: PyOptional Int
opt2 = mkPyNone

test3 :: PyList Number
test1 = linq.map f list1

test3 :: PyOptional Number
test2 = linq.map f opt1

test3 :: PyOptional Number
test3 = linq.map f opt2
```

</details>

