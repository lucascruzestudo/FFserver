
import unitypack
from unitypack.asset import Asset

f = open('TableData.resourceFile', 'rb')
asset = unitypack.load(f).assets[0]
asset.load()
xdt = asset.objects[2139558964].contents
print(xdt['m_pWeaponItemTable']['m_pItemStringData'][1]['m_strName'])

# Abrir o arquivo em modo leitura e escrita binária
# with open('TableData.resourceFile', 'r+b') as f:
#     tabledata = Asset.from_file(f)
#     xdtdata = tabledata.objects
    
    # print(xdtdata.keys())


    # # trocar level minimo da quest do nano
    # for item in xdtdata['m_pMissionTable']['m_pMissionData']:
    #     if item['m_iHMissionType'] == 2:
    #         if item['m_iSTNanoID'] == 16: # id do nano
    #                 offset = item.getmemboffset('m_iCTRReqLvMin')
    #                 f.seek(offset)
    #                 value_bytes = f.read(2)
    #                 current_value = int.from_bytes(value_bytes, byteorder='little')
    #                 print('Valor atual:', current_value)
    #                 new_value = 12 # nivel pro qual a quest vai
    #                 new_value_bytes = new_value.to_bytes(2, byteorder='little')
    #                 f.seek(offset)
    #                 f.write(new_value_bytes)
    #                 print('Valor alterado com sucesso!')



    # cont = 0
    # for item in xdtdata['m_pWeaponItemTable']['m_pItemData']:
    #     # print(item)
    #     itemstringdata = xdtdata['m_pWeaponItemTable']['m_pItemStringData'][cont]
    #     # print(itemstringdata)
    #     type = item['m_iTargetMode']
    #     name = itemstringdata['m_strName']
    #     if type == 6:
    #         print(name)
    #         print(cont)
    #         print(type)
    #     # 1 - melee , 2 - pistol, shattergun-3, 4- rifle, rocket-5, 6-grenade
    #     # if type == 1:   
    #     #     offset = item.getmemboffset('m_iDelayTime')
    #     #     f.seek(offset)
    #     #     value_bytes = f.read(2)
    #     #     current_value = int.from_bytes(value_bytes, byteorder='little')
    #     #     print('Valor atual:', current_value)
    #     #     new_value = 15
    #     #     new_value_bytes = new_value.to_bytes(2, byteorder='little')
    #     #     f.seek(offset)
    #     #     f.write(new_value_bytes)
    #     #     print('Valor alterado com sucesso!')
    

    #     cont+=1
    