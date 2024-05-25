from canPDU import *

class DBC():
    
    def __init__(self, pdus:list[canPDU]) -> None:
        self.dbc_pdus: dict[str, canPDU] = {}
        
        for pdu in pdus:
            print("Add new PDU to DBC: " + pdu.name)            
            self.dbc_pdus[pdu.id] = pdu
        
            
    def __str__(self) -> str:
        strRep = ""
        for pdu in self.dbc_pdus:
            strRep += pdu.name
        return strRep
            
            
bosch_dbc = DBC([Bordcomputer])
            