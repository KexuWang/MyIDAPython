#QT Struct
# #Create a struct name "strucFuncName"
# def CreateStruct(struct_name):
    # sid = FindOrCreateStructSid(struct_name)
    # print AddStrucMember(sid,"String",   -1, idc.FF_OWRD|FF_0NUMH,    -1,16)
    # print AddStrucMember(sid,"Size",    -1, idc.FF_DWORD|FF_0NUMH,   -1,4)
    # print AddStrucMember(sid,"dwV2",    -1, idc.FF_DWORD|FF_0NUMH,   -1,4)
    # print AddStrucMember(sid,"pFunName",-1, idc.FF_DWORD|FF_0OFF,    -1,4)
    # print AddStrucMember(sid,"dwAlign", -1, idc.FF_DWORD,            -1,4)
    # return sid
    
#Find or create a struct sid  
def FindOrCreateStructSid(structName):
    sid=GetStrucIdByName(structName)
    if sid == BADADDR:
        sid =AddStrucEx(-1, structName, 0)
        print "added struct {0} and id is {1}".format(structName, sid)
    else:
        print "struct {0} already exists and it's id is {1}".format(structName, sid)
    # add struct to idb
    Til2Idb(-1, structName)
    return sid


def createstructQString():
    sid = FindOrCreateStructSid("QString")
    print AddStrucMember(sid,"dw_0",		-1, idc.FF_DWORD|FF_0NUMH,	-1,4)
    print AddStrucMember(sid,"dw_Size",		-1, idc.FF_DWORD|FF_0NUMH,	-1,4)
    print AddStrucMember(sid,"dw_8",		-1, idc.FF_DWORD|FF_0NUMH,	-1,4)
    print AddStrucMember(sid,"dw_Offset",	-1, idc.FF_DWORD|FF_0NUMH,	-1,4)
    print AddStrucMember(sid,"string",		-1, idc.FF_BYTE,			-1,4)


"""
88a6-7b9c-6240-ff0f     
struct {
QString *v1
QString *v2
QString *v3
QString *v4
}
"""
def createstructMyKey():
    sid = FindOrCreateStructSid("MyKey")
    idx = GetStrucIdByName("QString")
    print AddStrucMember(sid,"off_0_str", -1,	idc.FF_DWORD|idc.FF_0STRO,	idx,	4)
    print AddStrucMember(sid,"off_4_str", -1,	idc.FF_DWORD|idc.FF_0STRO,	idx,	4)
    print AddStrucMember(sid,"off_8_str", -1,	idc.FF_DWORD|idc.FF_0STRO,	idx,	4)
    print AddStrucMember(sid,"off_c_str", -1,	idc.FF_DWORD|idc.FF_0STRO,	idx,	4)
	print AddStrucMember(sid,"off_dw_10", 0x10,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_14", 0x14,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_18", 0x18,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_1c", 0x1c,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_20", 0x20,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
	print AddStrucMember(sid,"off_dw_24", 0x24,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_28", 0x28,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_2c", 0x2c,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_30", 0x30,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)
    print AddStrucMember(sid,"off_dw_34", 0x34,idc.FF_DWORD|idc.FF_0NUMH,	-1,	4)

    
#Make a address for structure.
def MakeStruc(targAddr, sid):
    if targAddr==BADADDR:
        return
    size=GetStrucSize(sid)
    MakeUnknown(targAddr, size, DOUNK_DELNAMES)
    idaapi.doStruct(targAddr, size, sid)
    

def main():
    createstructQString()
    
if __name__=='__main__':
    main()
    print "\r\nOK!"