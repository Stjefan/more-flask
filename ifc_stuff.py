import ifcopenshell.util
import ifcopenshell.util.element
from ifcopenshell.api import run



def showModifiedIfcFile(name: str, express_id: int):
    model = ifcopenshell.open('uploads/edited.ifc')

    element_2_edit = model.by_id(int(express_id))
    print(element_2_edit)
    print(ifcopenshell.util.element.get_psets(element_2_edit))
    
def modifyIfcFilePset(filename: str, express_id: int):
    # 3_ABDS_AM_F0_00_03_XX_000_20_Slab_unten_Mitte_erweitert_um_Bauphysik_PSet.ifc 70971
    model = ifcopenshell.open(f'uploads/{filename}')

    element_2_edit = model.by_id(int(express_id))
    print(element_2_edit)


    print(ifcopenshell.util.element.get_psets(element_2_edit))

    pset = ifcopenshell.api.run("pset.add_pset", model, product=element_2_edit, name="Pset_KuFi")

    ifcopenshell.api.run("pset.edit_pset", model,
        pset=pset, properties={"FireRating": "2HR", "ThermalTransmittance": 42.3, "NobodyLikesYou": False, "EveryoneHatesYou": True, "Kreditwuerdigkeit": "A"})

    model.write("uploads/edited.ifc")

if __name__ == "__main__":
    if True:
        modifyIfcFilePset("3_ABDS_AM_F0_00_03_XX_000_20_Slab_unten_Mitte_erweitert_um_Bauphysik_PSet.ifc", 70971)

    if True:
        showModifiedIfcFile("edited.ifc", 70971)