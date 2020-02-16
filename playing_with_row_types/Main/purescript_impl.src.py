from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
res = block( "No document"
           , assign( "$foreign"
                   , call( var('import_module')
                         , "playing_with_row_types.Main.purescript_foreign" ) )
           , assign( "ps_getFoo"
                   , define( None
                           , ["ps_v"]
                           , block(ret(get_item(var("ps_v"), "foo"))) ) )
           , assign( "ps_main"
                   , call( call( get_attr(var("$foreign"), "discard")
                               , call( get_attr(var("$foreign"), "println")
                                     , call( var("ps_getFoo")
                                           , metadata( 15
                                                     , 27
                                                     , "src\Main.purs"
                                                     , record( ( "foo"
                                                               , metadata( 15
                                                                         , 33
                                                                         , "src\Main.purs"
                                                                         , 1 ) )
                                                             , ( "bar"
                                                               , metadata( 15
                                                                         , 41
                                                                         , "src\Main.purs"
                                                                         , "2" ) ) ) ) ) ) )
                         , define( None
                                 , ["ps_$__unused"]
                                 , block( ret( call( call( get_attr( var( "$foreign" )
                                                                   , "discard" )
                                                         , call( get_attr( var( "$foreign" )
                                                                         , "println" )
                                                               , call( var( "ps_getFoo" )
                                                                     , metadata( 16
                                                                               , 27
                                                                               , "src\Main.purs"
                                                                               , record( ( "foo"
                                                                                         , metadata( 16
                                                                                                   , 33
                                                                                                   , "src\Main.purs"
                                                                                                   , "3" ) )
                                                                                       , ( "bar"
                                                                                         , metadata( 16
                                                                                                   , 43
                                                                                                   , "src\Main.purs"
                                                                                                   , 4 ) ) ) ) ) ) )
                                                   , define( None
                                                           , ["ps_$__unused"]
                                                           , block( ret( call( call( get_attr( var( "$foreign" )
                                                                                             , "discard" )
                                                                                   , call( get_attr( var( "$foreign" )
                                                                                                   , "println" )
                                                                                         , call( var( "ps_getFoo" )
                                                                                               , metadata( 17
                                                                                                         , 27
                                                                                                         , "src\Main.purs"
                                                                                                         , record( ( "foo"
                                                                                                                   , metadata( 17
                                                                                                                             , 33
                                                                                                                             , "src\Main.purs"
                                                                                                                             , record(  ) ) ) ) ) ) ) )
                                                                             , define( None
                                                                                     , [ "ps_$__unused" ]
                                                                                     , block( ret( call( get_attr( var( "$foreign" )
                                                                                                                 , "println" )
                                                                                                       , call( var( "ps_getFoo" )
                                                                                                             , metadata( 18
                                                                                                                       , 27
                                                                                                                       , "src\Main.purs"
                                                                                                                       , record( ( "foo"
                                                                                                                                 , metadata( 18
                                                                                                                                           , 33
                                                                                                                                           , "src\Main.purs"
                                                                                                                                           , record( ( "foo_nested"
                                                                                                                                                     , metadata( 18
                                                                                                                                                               , 46
                                                                                                                                                               , "src\Main.purs"
                                                                                                                                                               , 5 ) )
                                                                                                                                                   , ( "bar_nested"
                                                                                                                                                     , metadata( 18
                                                                                                                                                               , 61
                                                                                                                                                               , "src\Main.purs"
                                                                                                                                                               , 6 ) ) ) ) )
                                                                                                                               , ( "bar"
                                                                                                                                 , metadata( 18
                                                                                                                                           , 70
                                                                                                                                           , "src\Main.purs"
                                                                                                                                           , 7 ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("getFoo", var("ps_getFoo"))
                           , ("main", var("ps_main"))
                           , ("println", get_attr(var("$foreign"), "println"))
                           , ( "discard"
                             , get_attr(var("$foreign"), "discard") ) ) ) )
res = module_code(res)
