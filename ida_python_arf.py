#---------------------------------------------------------------------------------------------
#Get a address's all callers
def GetAddrCallers(targAddr):
	listCallers=[]
	if targAddr == BADADDR:
		print "Parameter error in GetAddrCallers"
	else:
		nIndex=0
		for addr in XrefsTo(targAddr, flags=0):
			if nIndex%8==0:
				print ""
			print "[{0:02d}] {1:08X}\t".format(nIndex, addr.frm),
			listCallers.append(addr.frm)
			nIndex+=1
	return listCallers


#Travesing call depth path
def TraveseCallDepth(targAddr, nDeep=0x20):
	if targAddr == BADADDR:
		print "Parameter error in GetAddrCallers"
		return
	for k in range(nDeep):
		for addr in XrefsTo(targAddr, flags=0):
			#if have multipley refrence, only use the first one
			funcStart=GetFunctionAttr(addr.frm, FUNCATTR_START)
			if funcStart==0xFFFFFFFF:
				targAddr=addr.frm
			else:
				targAddr=funcStart
			print "[{0:04X}]:sub_ {1:08X} at addr_ {2:08X}".format( k, funcStart, addr.frm)
			break
		k+=1
	print ""

################################################################################
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
    	
def CreateStructPtrList():
    sid = FindOrCreateStructSid("wbxPDPtrList")
    print AddStrucMember(sid,"vft",		-1, idc.FF_DWORD,  -1,4)
    print AddStrucMember(sid,"dwFlag",	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dw_1",    -1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dw_2",	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dw_3", 	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dw_4", 	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dw_5", 	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dw_6", 	-1, idc.FF_DWORD|FF_0NUMH,	-1,4)
    return sid

def CreateStructDWNode():
    sid = FindOrCreateStructSid("wbxDWNode")
    print AddStrucMember(sid,"dw1",	-1, idc.FF_DWORD,-1,4)
    print AddStrucMember(sid,"dw2",	-1, idc.FF_DWORD,-1,4)
    return sid

def CreateStructCFFSpace():
    sid = FindOrCreateStructSid("wbxCFFSpace")
    print AddStrucMember(sid,"vft",		-1, idc.FF_DWORD,   -1,4)
    print AddStrucMember(sid,"dwFlag",	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dwOff_8",    -1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dwOff_c",	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dwOff_10", 	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dwOff_14", 	-1, idc.FF_DWORD,	-1,4)
    idx = GetStrucIdByName("wbxPDPtrList")
    print AddStrucMember(sid,"objPDPtrList", 	-1, idc.FF_DATA|FF_STRUCT,	idx,	GetStrucSize(idx))
    print AddStrucMember(sid,"dwOff_38", 	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"dwOff_3c", 	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"objPDPtrList1", -1, idc.FF_DATA|FF_STRUCT,	idx,	GetStrucSize(idx))
    print AddStrucMember(sid,"dwOff_60", 	-1, idc.FF_DWORD,	-1,4*0x81)
    idx = GetStrucIdByName("wbxDWNode")
    print AddStrucMember(sid,"dwOff_264", 	-1, idc.FF_DATA|FF_STRUCT,	idx,8*0x80)
    print AddStrucMember(sid,"dwUNknow",	-1, idc.FF_DWORD,	-1,4)
    print AddStrucMember(sid,"chOff_668",	-1, idc.FF_BYTE,	-1,1*0x70)
    print AddStrucMember(sid,"chOff_6d8",	-1, idc.FF_BYTE,	-1,1*0x24)
    return sid
################################################################################	
	
def test1():
	#Crash2_path_function_1
	addr = "1025ead2 1026467e 100f42a0 1011244a 10114592 100d78ed 100d74fb 100b5836 100b6d69 100b682e 100b65b7 100b701d 1008f367 1003eb88 1003e578 10040407 10042cf7 1007b08f 100853a9 100400a2 10108295 1010881b 100557dd 10024bd2 1008a0e0 1008b239 10053480"
	addrList = addr.split()
	for item in addrList:
	   #print "{0:08X}".format(int(item,16))
	   print "bp atpdmod+%08x ;"%(PrevHead(int(item,16))-0x10000000),

	
	
	#MakeNameEx()
	#GetAddrCallers(0x10002694)
	#GetAddrCallers(0x1000EBC7)
	#TraveseCallDepth(0x1000EBC7)
	

################################################################################
def main():
	CreateStructCFFSpace()
	
if __name__=='__main__':
	main()
	print "\r\nOK!"
	