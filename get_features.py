from cinfony import pybel, rdk

xyz_fname = "xyz.txt"
xyz_f = open(xyz_fname)
xyz_names = [ line.rstrip() for line in xyz_f.readlines() ]

data_list = []
for i, xyz in enumerate(xyz_names):
    pybel_mol = next(pybel.readfile("xyz", xyz))
    smiles = pybel_mol.write("smi")
    rdk_mol = rdk.Chem.MolFromSmiles(smiles)
    natoms = rdk_mol.GetNumAtoms()
    nbonds = rdk_mol.GetNumBonds()
    mw = rdk.Chem.Descriptors.ExactMolWt(rdk_mol)
    heavymw = rdk.Chem.Descriptors.HeavyAtomMolWt(rdk_mol)
    nvalence = rdk.Chem.Descriptors.NumValenceElectrons(rdk_mol)
    morganfp1 = rdk.Chem.Descriptors.FpDensityMorgan1(rdk_mol)
    morganfp2 = rdk.Chem.Descriptors.FpDensityMorgan2(rdk_mol)
    morganfp3 = rdk.Chem.Descriptors.FpDensityMorgan3(rdk_mol)
    data_list.append( [natoms, nbonds, mw, heavymw, nvalence, morganfp1, morganfp2, morganfp3] )
