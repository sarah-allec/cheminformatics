import pubchempy as pcp
import pandas as pd
import numpy as np

def make_xyz(coords,fname):
    with open(fname,'w') as new:
        new.write( str(len(coords)) +'\n\n' )
    pd.DataFrame(coords).to_csv(fname, sep='\t', header=False, index=False, mode='a')

quinones = [ 'p-benzoquinone', 'tetramethyl-p-benzoquinone', '2,6-di-tert-butyl-p-benzoquinone', 
        '2,6-dichloro-p-benzoquinone', 'tetrachloro-p-benzoquinone', 'p-naphthoquinone', 
        '2,3-dimethyl-1,4-naphthoquinone', '2,3-dichloro-1,4-naphthoquinone', '9,10-anthraquinone', 
        '2-chloro-9,10-anthraquinone', 'o-naphthoquinone', '9,10-phenanthraquinone', 
        '2-iodophenanthrene-9,10-dione', '2,7-diiodophenanthrene-9,10-dione' ]

for quinone in quinones:
    my_record = pcp.get_compounds(quinone,'name',record_type='3d')[0].to_dict(properties=['atoms'])
    my_atoms = my_record['atoms']
    coords = [ [ a['element'], a['x'], a['y'], a['z']] for a in my_atoms ]
    make_xyz(coords, quinone+'.xyz')
