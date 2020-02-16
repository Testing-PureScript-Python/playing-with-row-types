from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block("No document", assign("exports", record()))
res = module_code(res)
