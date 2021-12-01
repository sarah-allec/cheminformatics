proc my_render {} {
  display projection orthographic
  display depthcue off
  color Display Background white
  set files { "p-benzoquinone" "tetramethyl-p-benzoquinone" "2,6-di-tert-butyl-p-benzoquinone" "2,6-dichloro-p-benzoquinone" "tetrachloro-p-benzoquinone" "p-naphthoquinone" "2,3-dimethyl-1,4-naphthoquinone" "2,3-dichloro-1,4-naphthoquinone" "9,10-anthraquinone" "2-chloro-9,10-anthraquinone" "o-naphthoquinone" "9,10-phenanthraquinone" "2-iodophenanthrene-9,10-dione" "2,7-diiodophenanthrene-9,10-dione" } 
   foreach f $files {
	  set filename ${f}.xyz
          puts $filename
          mol new $filename type xyz
          mol color Element
          mol representation VDW 0.3 15.0
          mol selection all
          mol material EdgyShiny
          mol addrep top
          mol selection all
          mol representation DynamicBonds 2.0 0.2 6.0
          mol color ColorID 2
          mol material BrushedMetal
          mol addrep top
          render TachyonInternal ${f}.png
          mol delete top
   } 
}
