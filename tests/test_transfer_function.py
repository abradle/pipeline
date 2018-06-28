import unittest
import setup_django
from db.models import *
from django.db.models import Q
from functions import db_functions
import json

class TestTasks(unittest.TestCase):

    sql_result = '''[{"ID": 3, "LabVisit": "lb17884-1", "LibraryPlate": "DMSO", "SourceWell": "G12", "LibraryName": "DMSO", "CompoundSMILES": "DMSO", "CompoundCode": "DMSO", "CrystalPlate": "441330301243_rcah-door", "CrystalWell": "A02c", "EchoX": 321, "EchoY": 276, "DropVolume": 400, "ProteinName": "SagaMurD", "BatchNumber": "1", "CompoundStockConcentration": 500, "CompoundConcentration": 0, "SolventFraction": 0, "SoakTransferVol": 0, "SoakStatus": "done", "SoakTimestamp": "04/10/2017 16:30:52", "CryoStockFraction": "", "CryoFraction": "", "CryoWell": "", "CryoTransferVolume": "", "CryoStatus": "", "CryoTimestamp": "", "SoakingTime": "01:14:57", "HarvestStatus": "done", "CrystalName": "SagaMurD-x0002", "Puck": "DLS-566", "PuckPosition": 2, "PinBarcode": "DF075C0994", "MountingResult": "Mounted_Clear", "MountingArrivalTime": "04/10/2017 17:44:53", "MountedTimestamp": "04/10/2017 17:45:49", "MountingTime": "3.88888888888889E-02", "ispybStatus": "exported to ispybLB17884-2_2017-10-05_09-32-52_ispyb", "DataCollectionVisit": "lb17884-2", "SoakDBComments": "", "ProjectDirectory": null, "CrystalTag": null, "CrystalFormName": null, "CrystalFormSpaceGroup": null, "CrystalFormPointGroup": null, "CrystalFormA": null, "CrystalFormB": null, "CrystalFormC": null, "CrystalFormAlpha": null, "CrystalFormBeta": null, "CrystalFormGamma": null, "CrystalFormVolume": null, "DataCollectionBeamline": "i04-1", "DataCollectionDate": "2017-10-05 10:01:51", "DataCollectionOutcome": "success", "DataCollectionRun": "1", "DataCollectionComment": null, "DataCollectionWavelength": "n/a", "DataCollectionPinBarcode": null, "DataProcessingPathToImageFiles": null, "DataProcessingProgram": "3dii-run", "DataProcessingSpaceGroup": "C 1 2 1", "DataProcessingUnitCell": "162 61 53 90 105 90", "DataProcessingAutoAssigned": "True", "DataProcessingA": "162", "DataProcessingB": "61", "DataProcessingC": "53", "DataProcessingAlpha": "90", "DataProcessingBeta": "105", "DataProcessingGamma": "90", "DataProcessingResolutionOverall": "78.35 - 2.51", "DataProcessingResolutionLow": "78.35", "DataProcessingResolutionLowInnerShell": "11.23", "DataProcessingResolutionHigh": "2.51", "DataProcessingResolutionHigh15sigma": "2.79", "DataProcessingResolutionHighOuterShell": "2.58", "DataProcessingRmergeOverall": "0.104", "DataProcessingRmergeLow": "0.047", "DataProcessingRmergeHigh": "0.830", "DataProcessingIsigOverall": "5.6", "DataProcessingIsigLow": "19.7", "DataProcessingIsigHigh": "1.1", "DataProcessingCompletenessOverall": "97.3", "DataProcessingCompletenessLow": "99.7", "DataProcessingCompletenessHigh": "99.5", "DataProcessingMultiplicityOverall": "3.2", "DataProcessingMultiplicityLow": "3.3", "DataProcessingMultiplicityHigh": "3.3", "DataProcessingCChalfOverall": "0.995", "DataProcessingCChalfLow": "0.996", "DataProcessingCChalfHigh": "0.816", "DataProcessingPathToLogfile": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0002/autoprocessing/lb17884-2-SagaMurD-x0002_1_3dii-run", "DataProcessingPathToMTZfile": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0002/autoprocessing/lb17884-2-SagaMurD-x0002_1_3dii-run", "DataProcessingLOGfileName": "lb17884v2_xSagaMurDx00021_aimless.log", "DataProcessingMTZfileName": "lb17884v2_xSagaMurDx00021_free.mtz", "DataProcessingDirectoryOriginal": "/dls/i04-1/data/2017/lb17884-2/processed/SagaMurD/SagaMurD-x0002/SagaMurD-x0002_1_/xia2/3dii-run", "DataProcessingUniqueReflectionsOverall": "17062", "DataProcessingLattice": "monoclinic_C", "DataProcessingPointGroup": "2", "DataProcessingUnitCellVolume": "505899.8", "DataProcessingAlert": "#FF9900", "DataProcessingScore": "36.753296048", "DataProcessingStatus": null, "DataProcessingRcryst": "999", "DataProcessingRfree": "999", "DataProcessingPathToDimplePDBfile": null, "DataProcessingPathToDimpleMTZfile": null, "DataProcessingDimpleSuccessful": "True", "DimpleResolutionHigh": null, "DimpleRcryst": "0.30497", "DimpleRfree": "0.35568", "DimplePathToPDB": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0002/dimple.pdb", "DimplePathToMTZ": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0002/dimple.mtz", "DimpleReferencePDB": "/dls/labxchem/data/2017/lb17884-1/processing/reference/murd_c21_ref.pdb", "DimpleStatus": "finished", "DimplePANDDAwasRun": "True", "DimplePANDDAhit": "False", "DimplePANDDAreject": "False", "DimplePANDDApath": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/panddas", "PANDDAStatus": null, "DatePanDDAModelCreated": null, "RefinementResolution": null, "RefinementResolutionTL": null, "RefinementRcryst": null, "RefinementRcrystTraficLight": null, "RefinementRfree": null, "RefinementRfreeTraficLight": null, "RefinementSpaceGroup": "C 1 2 1", "RefinementLigandCC": null, "RefinementRmsdBonds": null, "RefinementRmsdBondsTL": null, "RefinementRmsdAngles": null, "RefinementRmsdAnglesTL": null, "RefinementOutcome": "1 - Analysis Pending", "RefinementMTZfree": "SagaMurD-x0002.free.mtz", "RefinementCIF": null, "RefinementCIFStatus": "restraints failed", "RefinementCIFprogram": "phenix.elbow", "RefinementPDB_latest": null, "RefinementMTZ_latest": null, "RefinementMatrixWeight": null, "RefinementComment": null, "RefinementPathToRefinementFolder": null, "RefinementLigandConfidence": null, "RefinementLigandBoundConformation": null, "RefinementBoundConformation": null, "RefinementMolProbityScore": null, "RefinementMolProbityScoreTL": null, "RefinementRamachandranOutliers": null, "RefinementRamachandranOutliersTL": null, "RefinementRamachandranFavored": null, "RefinementRamachandranFavoredTL": null, "RefinementProgram": null, "RefinementStatus": null, "Deposition_PDB_ID": null, "Deposition_PDB_file": null, "Deposition_Date": null, "Deposition_mmCIF_model_file": null, "Deposition_mmCIF_SF_file": null, "AssayIC50": null, "LastUpdated": "2018-01-23 07:17", "LastUpdated_by": "mny37354"}]'''

    '''[{"ID": 398, "LabVisit": "lb17884-1", "LibraryPlate": "DSIpoised_001_Set1", "SourceWell": "V09", "LibraryName": "DSIpoised", "CompoundSMILES": "CC(CO)(CO)NC(=O)NC=1C=CC=CC1", "CompoundCode": "Z57472297", "CrystalPlate": "441330300161_rcah-door", "CrystalWell": "B11d", "EchoX": -28, "EchoY": -416.25, "DropVolume": 400, "ProteinName": "SagaMurD", "BatchNumber": "10", "CompoundStockConcentration": 500, "CompoundConcentration": 100, "SolventFraction": 20, "SoakTransferVol": 100, "SoakStatus": "done", "SoakTimestamp": "22/11/2017 12:50:26", "CryoStockFraction": "", "CryoFraction": "", "CryoWell": "", "CryoTransferVolume": "", "CryoStatus": "", "CryoTimestamp": "", "SoakingTime": "08:23:12", "HarvestStatus": "done", "CrystalName": "SagaMurD-x0374", "Puck": "DF-034", "PuckPosition": 13, "PinBarcode": "DF075C0976", "MountingResult": "OK: Mounted Clear", "MountingArrivalTime": "22/11/2017 21:13:10", "MountedTimestamp": "22/11/2017 21:13:38", "MountingTime": "3.19444444444444E-04", "ispybStatus": "exported to ispyb\\LB17884-2_2017-11-22_23-05-57_ispyb", "DataCollectionVisit": "lb17884-5", "SoakDBComments": "", "ProjectDirectory": null, "CrystalTag": null, "CrystalFormName": null, "CrystalFormSpaceGroup": null, "CrystalFormPointGroup": null, "CrystalFormA": null, "CrystalFormB": null, "CrystalFormC": null, "CrystalFormAlpha": null, "CrystalFormBeta": null, "CrystalFormGamma": null, "CrystalFormVolume": null, "DataCollectionBeamline": "i04-1", "DataCollectionDate": "2017-11-26 05:04:50", "DataCollectionOutcome": "success", "DataCollectionRun": "1", "DataCollectionComment": null, "DataCollectionWavelength": "n/a", "DataCollectionPinBarcode": null, "DataProcessingPathToImageFiles": null, "DataProcessingProgram": "3d-run", "DataProcessingSpaceGroup": "C 1 2 1", "DataProcessingUnitCell": "161 65 52 90 107 90", "DataProcessingAutoAssigned": "True", "DataProcessingA": "161", "DataProcessingB": "65", "DataProcessingC": "52", "DataProcessingAlpha": "90", "DataProcessingBeta": "107", "DataProcessingGamma": "90", "DataProcessingResolutionOverall": "40.54 - 1.58", "DataProcessingResolutionLow": "40.54", "DataProcessingResolutionLowInnerShell": "7.07", "DataProcessingResolutionHigh": "1.58", "DataProcessingResolutionHigh15sigma": "1.63", "DataProcessingResolutionHighOuterShell": "1.62", "DataProcessingRmergeOverall": "0.056", "DataProcessingRmergeLow": "0.028", "DataProcessingRmergeHigh": "0.730", "DataProcessingIsigOverall": "11.1", "DataProcessingIsigLow": "36.1", "DataProcessingIsigHigh": "1.3", "DataProcessingCompletenessOverall": "99.7", "DataProcessingCompletenessLow": "97.9", "DataProcessingCompletenessHigh": "99.4", "DataProcessingMultiplicityOverall": "3.2", "DataProcessingMultiplicityLow": "2.5", "DataProcessingMultiplicityHigh": "2.5", "DataProcessingCChalfOverall": "0.998", "DataProcessingCChalfLow": "0.998", "DataProcessingCChalfHigh": "0.549", "DataProcessingPathToLogfile": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0374/autoprocessing/lb17884-5-SagaMurD-x0374_1_3d-run", "DataProcessingPathToMTZfile": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0374/autoprocessing/lb17884-5-SagaMurD-x0374_1_3d-run", "DataProcessingLOGfileName": "lb17884v5_xSagaMurDx03741_aimless.log", "DataProcessingMTZfileName": "lb17884v5_xSagaMurDx03741_free.mtz", "DataProcessingDirectoryOriginal": "/dls/i04-1/data/2017/lb17884-5/processed/SagaMurD/SagaMurD-x0374/SagaMurD-x0374_1_/xia2/3d-run", "DataProcessingUniqueReflectionsOverall": "72158", "DataProcessingLattice": "monoclinic_C", "DataProcessingPointGroup": "2", "DataProcessingUnitCellVolume": "520401.9", "DataProcessingAlert": "#00FF00", "DataProcessingScore": "306.897779812", "DataProcessingStatus": null, "DataProcessingRcryst": "999", "DataProcessingRfree": "999", "DataProcessingPathToDimplePDBfile": null, "DataProcessingPathToDimpleMTZfile": null, "DataProcessingDimpleSuccessful": "True", "DimpleResolutionHigh": null, "DimpleRcryst": "0.20636", "DimpleRfree": "0.22748", "DimplePathToPDB": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0374/dimple.pdb", "DimplePathToMTZ": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0374/dimple.mtz", "DimpleReferencePDB": "/dls/labxchem/data/2017/lb17884-1/processing/reference/murd_c21_ref.pdb", "DimpleStatus": "finished", "DimplePANDDAwasRun": "True", "DimplePANDDAhit": "True", "DimplePANDDAreject": "False", "DimplePANDDApath": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/panddas", "PANDDAStatus": null, "DatePanDDAModelCreated": null, "RefinementResolution": "1.53", "RefinementResolutionTL": "green", "RefinementRcryst": "0.20636", "RefinementRcrystTraficLight": "green", "RefinementRfree": "0.22748", "RefinementRfreeTraficLight": "green", "RefinementSpaceGroup": "C 1 2 1", "RefinementLigandCC": null, "RefinementRmsdBonds": "0.023", "RefinementRmsdBondsTL": "orange", "RefinementRmsdAngles": "2.170", "RefinementRmsdAnglesTL": "orange", "RefinementOutcome": "2 - PANDDA model", "RefinementMTZfree": "SagaMurD-x0374.free.mtz", "RefinementCIF": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0374/compound/Z57472297.cif", "RefinementCIFStatus": "restraints generated", "RefinementCIFprogram": "acedrg", "RefinementPDB_latest": "/dls/labxchem/data/2017/lb17884-1/processing/analysis/initial_model/SagaMurD-x0374/dimple/dimple_rerun_on_selected_file/dimple/final.pdb", "RefinementMTZ_latest": null, "RefinementMatrixWeight": null, "RefinementComment": null, "RefinementPathToRefinementFolder": null, "RefinementLigandConfidence": null, "RefinementLigandBoundConformation": null, "RefinementBoundConformation": null, "RefinementMolProbityScore": "-", "RefinementMolProbityScoreTL": "gray", "RefinementRamachandranOutliers": "-", "RefinementRamachandranOutliersTL": "gray", "RefinementRamachandranFavored": "-", "RefinementRamachandranFavoredTL": "gray", "RefinementProgram": null, "RefinementStatus": null, "Deposition_PDB_ID": null, "Deposition_PDB_file": null, "Deposition_Date": null, "Deposition_mmCIF_model_file": null, "Deposition_mmCIF_SF_file": null, "AssayIC50": null, "LastUpdated": "2018-01-29 07:42", "LastUpdated_by": "mny37354"}]'''

    def test_transfer_sagamurd(self):
        results = json.loads(self.sql_result)
        filename = 'whatever'
        model = Crystal
        translate_dict = db_functions.crystal_translations()

        db_functions.transfer(filename, results, translate_dict, model)

        d, model_fields = db_functions.transfer_row(results[0], model, translate_dict, filename)

        print(d)
        print(model_fields)

