from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as joinpath
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\playing-with-row-types"
res = block("No document", assign("exports", record()))
res = module_code(res)
