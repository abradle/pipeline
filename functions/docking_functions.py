import db_functions as dbf

def get_comp_chem_ready():
    bound_list = []
    run_list = []
    conn, c = dbf.connectDB()
    c.execute("SELECT bound_conf FROM proasis_hits WHERE strucid != ''")
    rows = c.fetchall()
    for row in rows:
        bound_list.append(str(row[0]))
    c.execute('SELECT bound_conf FROM refinement WHERE bound_conf IN %s AND outcome SIMILAR TO %s', (tuple(bound_list), '(%4%|%5%)'))
    results = c.fetchall()
    for result in results:
        if len(result) > 0:
            run_list.append(str(result[0]))

    return run_list

def get_strucids(run_list):
    out_dict = {'strucid':[], 'crystal':[], 'directory':[], 'ligands':[]}
    conn, c = dbf.connectDB()
    for struc in run_list:
        c.execute("SELECT strucid, crystal_name, ligand_list FROM proasis_hits WHERE bound_conf=%s AND ligand_list != 'None'", (struc,))
        rows = c.fetchall()
        for row in rows:
            out_dict['strucid'].append(str(row[0]))
            out_dict['crystal'].append(str(row[1]))
            out_dict['ligands'].append(str(row[2]))

            if 'Refine' in struc.split('/')[-2]:
                pdb = str(struc.split('/')[-2] + '/' + struc.split('/')[-1])
            else:
                pdb = struc.split('/')[-1]

            directory = struc.replace(pdb, '')
            out_dict['directory'].append(directory)

    return out_dict
