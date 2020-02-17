from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as joinpath
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\playing-with-row-types"
res = block( " | This module is to show the type checker,   and cannot run without giving proproriate implementations in Example.py"
           , assign( "$foreign"
                   , call( var('import_module')
                         , "playing_with_row_types.Example.purescript_foreign" ) )
           , assign("ps_opt2", get_attr(var("$foreign"), "mkPyNone"))
           , assign( "ps_test3"
                   , call( call( get_item( get_attr(var("$foreign"), "linq")
                                         , "map" )
                               , get_attr(var("$foreign"), "f") )
                         , var("ps_opt2") ) )
           , assign( "ps_opt1"
                   , call( get_attr(var("$foreign"), "mkPyOption")
                         , metadata( 17
                                   , 20
                                   , joinpath(project_path, "src\\Example.purs")
                                   , 1 ) ) )
           , assign( "ps_test2"
                   , call( call( get_item( get_attr(var("$foreign"), "linq")
                                         , "map" )
                               , get_attr(var("$foreign"), "f") )
                         , var("ps_opt1") ) )
           , assign( "ps_list1"
                   , call( get_attr(var("$foreign"), "mkPyList")
                         , metadata( 16
                                   , 19
                                   , joinpath(project_path, "src\\Example.purs")
                                   , mktuple( metadata( 16
                                                      , 20
                                                      , joinpath( project_path
                                                      , "src\\Example.purs" )
                                                      , 1 )
                                            , metadata( 16
                                                      , 23
                                                      , joinpath( project_path
                                                      , "src\\Example.purs" )
                                                      , 2 ) ) ) ) )
           , assign( "ps_test1"
                   , call( call( get_item( get_attr(var("$foreign"), "linq")
                                         , "map" )
                               , get_attr(var("$foreign"), "f") )
                         , var("ps_list1") ) )
           , assign( "exports"
                   , record( ("list1", var("ps_list1"))
                           , ("opt1", var("ps_opt1"))
                           , ("opt2", var("ps_opt2"))
                           , ("test1", var("ps_test1"))
                           , ("test2", var("ps_test2"))
                           , ("test3", var("ps_test3"))
                           , ("mkPyList", get_attr(var("$foreign"), "mkPyList"))
                           , ( "mkPyOption"
                             , get_attr(var("$foreign"), "mkPyOption") )
                           , ("mkPyNone", get_attr(var("$foreign"), "mkPyNone"))
                           , ("f", get_attr(var("$foreign"), "f"))
                           , ("linq", get_attr(var("$foreign"), "linq")) ) ) )
res = module_code(res)
