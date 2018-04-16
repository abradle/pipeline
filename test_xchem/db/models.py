# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Crystal(models.Model):
    crystal_name = models.TextField(blank=False, null=False)


class Target(models.Model):
    target_name = models.TextField(blank=False, null=False)

class SoakdbFiles(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    filename = models.TextField(blank=True, null=True)
    modification_date = models.BigIntegerField(blank=True, null=True)
    proposal = models.TextField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soakdb_files'


class DataProcessing(models.Model):
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    alert = models.TextField(blank=True, null=True)
    auto_assigned = models.TextField(blank=True, null=True)
    cchalf_high = models.TextField(blank=True, null=True)
    cchalf_low = models.TextField(blank=True, null=True)
    cchalf_overall = models.TextField(blank=True, null=True)
    completeness_high = models.TextField(blank=True, null=True)
    completeness_low = models.TextField(blank=True, null=True)
    completeness_overall = models.TextField(blank=True, null=True)
    crystal_name = models.ForeignKey(Crystal, on_delete=models.CASCADE) # changed to foreign key
    dimple_mtz_path = models.TextField(blank=True, null=True)
    dimple_pdb_path = models.TextField(blank=True, null=True)
    dimple_status = models.TextField(blank=True, null=True)
    file_id = models.ForeignKey(SoakdbFiles, on_delete=models.CASCADE) # changed to use soakdb file
    image_path = models.TextField(blank=True, null=True)
    isig_high = models.TextField(blank=True, null=True)
    isig_low = models.TextField(blank=True, null=True)
    isig_overall = models.TextField(blank=True, null=True)
    lattice = models.TextField(blank=True, null=True)
    log_name = models.TextField(blank=True, null=True)
    logfile_path = models.TextField(blank=True, null=True)
    mtz_name = models.TextField(blank=True, null=True)
    mtz_path = models.TextField(blank=True, null=True)
    multiplicity_high = models.TextField(blank=True, null=True)
    multiplicity_low = models.TextField(blank=True, null=True)
    multiplicity_overall = models.TextField(blank=True, null=True)
    original_directory = models.TextField(blank=True, null=True)
    point_group = models.TextField(blank=True, null=True)
    program = models.TextField(blank=True, null=True)
    protein = models.ForeignKey(Target, on_delete=models.CASCADE) # added as foreign key
    r_cryst = models.TextField(blank=True, null=True)
    r_free = models.TextField(blank=True, null=True)
    r_merge_high = models.TextField(blank=True, null=True)
    r_merge_low = models.TextField(blank=True, null=True)
    r_merge_overall = models.TextField(blank=True, null=True)
    res_high = models.TextField(blank=True, null=True)
    res_high_15_sigma = models.TextField(blank=True, null=True)
    res_high_outer_shell = models.TextField(blank=True, null=True)
    res_low = models.TextField(blank=True, null=True)
    res_low_inner_shell = models.TextField(blank=True, null=True)
    res_overall = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    spacegroup = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    unique_ref_overall = models.TextField(blank=True, null=True)
    unit_cell = models.TextField(blank=True, null=True)
    unit_cell_vol = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_processing'


class Dimple(models.Model):
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    crystal_name = models.ForeignKey(Crystal, on_delete=models.CASCADE)  # changed to foreign key
    file_id = models.ForeignKey(SoakdbFiles, on_delete=models.CASCADE)  # changed to use soakdb file
    mtz_path = models.TextField(blank=True, null=True)
    pandda_hit = models.TextField(blank=True, null=True)
    pandda_path = models.TextField(blank=True, null=True)
    pandda_reject = models.TextField(blank=True, null=True)
    pandda_run = models.TextField(blank=True, null=True)
    pdb_path = models.TextField(blank=True, null=True)
    protein = models.ForeignKey(Target, on_delete=models.CASCADE)  # added as foreign key
    r_free = models.TextField(blank=True, null=True)
    reference_pdb = models.TextField(blank=True, null=True)
    res_high = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dimple'


class Lab(models.Model):
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    compound_code = models.TextField(blank=True, null=True)
    cryo_frac = models.TextField(blank=True, null=True)
    cryo_status = models.TextField(blank=True, null=True)
    cryo_stock_frac = models.TextField(blank=True, null=True)
    cryo_transfer_vol = models.TextField(blank=True, null=True)
    crystal_name = models.ForeignKey(Crystal, on_delete=models.CASCADE)  # changed to foreign key
    data_collection_visit = models.TextField(blank=True, null=True)
    expr_conc = models.TextField(blank=True, null=True)
    file_id = models.ForeignKey(SoakdbFiles, on_delete=models.CASCADE)  # changed to use soakdb file
    harvest_status = models.TextField(blank=True, null=True)
    library_name = models.TextField(blank=True, null=True)
    library_plate = models.TextField(blank=True, null=True)
    mounting_result = models.TextField(blank=True, null=True)
    mounting_time = models.TextField(blank=True, null=True)
    protein = models.ForeignKey(Target, on_delete=models.CASCADE) # added as foreign key
    smiles = models.TextField(blank=True, null=True)
    soak_status = models.TextField(blank=True, null=True)
    soak_time = models.TextField(blank=True, null=True)
    soak_vol = models.TextField(blank=True, null=True)
    solv_frac = models.TextField(blank=True, null=True)
    stock_conc = models.TextField(blank=True, null=True)
    visit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab'


class LigandEdstats(models.Model):
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    baa = models.TextField(blank=True, null=True)  # Field name made lowercase.
    ccpa = models.TextField(blank=True, null=True)  # Field name made lowercase.
    ccsa = models.TextField(blank=True, null=True)  # Field name made lowercase.
    npa = models.TextField(blank=True, null=True)  # Field name made lowercase.
    rga = models.TextField(blank=True, null=True)  # Field name made lowercase.
    ra = models.TextField(blank=True, null=True)  # Field name made lowercase.
    srga = models.TextField(blank=True, null=True)  # Field name made lowercase.
    zccpa = models.TextField(blank=True, null=True)  # Field name made lowercase.
    zd_a = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    zd_a_0 = models.TextField(blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    zda = models.TextField(blank=True, null=True)  # Field name made lowercase.
    zoa = models.TextField(blank=True, null=True)  # Field name made lowercase.
    crystal_name = models.ForeignKey(Crystal, on_delete=models.CASCADE)  # changed to foreign key # changed from crystal
    protein = models.ForeignKey(Target, on_delete=models.CASCADE)  # added as foreign key
    ligand = models.TextField(blank=True, null=True)
    strucid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ligand_edstats'


class ProasisHits(models.Model):
    # level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    bound_conf = models.TextField(blank=True, null=True)
    crystal_name = models.ForeignKey(Crystal, on_delete=models.CASCADE)  # changed to foreign key
    modification_date = models.TextField(blank=True, null=True)
    protein = models.ForeignKey(Target, on_delete=models.CASCADE)  # added as foreign key
    smiles = models.TextField(blank=True, null=True)
    strucid = models.TextField(blank=True, null=True)
    ligand_list = models.TextField(blank=True, null=True)
    exists_pdb = models.TextField(blank=True, null=True)
    exists_mtz = models.TextField(blank=True, null=True)
    exists_2fofc = models.TextField(blank=True, null=True)
    exists_fofc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proasis_hits'


class ProasisLeads(models.Model):
    # level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    pandda_path = models.TextField(blank=True, null=True)
    protein = models.ForeignKey(Target, on_delete=models.CASCADE)  # added as foreign key
    reference_pdb = models.TextField(blank=True, null=True)
    strucid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proasis_leads'


class Refinement(models.Model):
    index = models.BigIntegerField(blank=False, null=False, primary_key=True)
    bound_conf = models.TextField(blank=True, null=True)
    cif = models.TextField(blank=True, null=True)
    cif_prog = models.TextField(blank=True, null=True)
    cif_status = models.TextField(blank=True, null=True)
    crystal_name = models.ForeignKey(Crystal, on_delete=models.CASCADE)  # changed to foreign key
    file_id = models.ForeignKey(SoakdbFiles, on_delete=models.CASCADE)  # changed to use soakdb file
    lig_bound_conf = models.TextField(blank=True, null=True)
    lig_cc = models.TextField(blank=True, null=True)
    lig_confidence = models.TextField(blank=True, null=True)
    matrix_weight = models.TextField(blank=True, null=True)
    molprobity_score = models.TextField(blank=True, null=True)
    molprobity_score_tl = models.TextField(db_column='molprobity_score_TL', blank=True, null=True)  # Field name made lowercase.
    mtz_free = models.TextField(blank=True, null=True)
    mtz_latest = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    pdb_latest = models.TextField(blank=True, null=True)
    protein = models.ForeignKey(Target, on_delete=models.CASCADE)  # added as foreign key
    r_free = models.TextField(blank=True, null=True)
    ramachandran_favoured = models.TextField(blank=True, null=True)
    ramachandran_favoured_tl = models.TextField(db_column='ramachandran_favoured_TL', blank=True, null=True)  # Field name made lowercase.
    ramachandran_outliers = models.TextField(blank=True, null=True)
    ramachandran_outliers_tl = models.TextField(db_column='ramachandran_outliers_TL', blank=True, null=True)  # Field name made lowercase.
    rcryst = models.TextField(blank=True, null=True)
    rcryst_tl = models.TextField(db_column='rcryst_TL', blank=True, null=True)  # Field name made lowercase.
    refinement_path = models.TextField(blank=True, null=True)
    res = models.TextField(blank=True, null=True)
    res_tl = models.TextField(db_column='res_TL', blank=True, null=True)  # Field name made lowercase.
    rfree_tl = models.TextField(db_column='rfree_TL', blank=True, null=True)  # Field name made lowercase.
    rmsd_angles = models.TextField(blank=True, null=True)
    rmsd_angles_tl = models.TextField(db_column='rmsd_angles_TL', blank=True, null=True)  # Field name made lowercase.
    rmsd_bonds = models.TextField(blank=True, null=True)
    rmsd_bonds_tl = models.TextField(db_column='rmsd_bonds_TL', blank=True, null=True)  # Field name made lowercase.
    spacegroup = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refinement'
