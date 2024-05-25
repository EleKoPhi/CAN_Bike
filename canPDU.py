from canSignal import *

class canPDU():
    def __init__(self, _name:str, _id:int, _dcl:int, _signals:list[CanSignal]) -> None:
        self.name = _name
        self.id = _id
        self.dlc = _dcl
        self.signals = _signals
        
    def __iter__(self):
        return self
    
    def __str__(self) -> str:
        return self.name

        
        
Bordcomputer = canPDU("Bordcomputer", "0x37", 3, [st_light_button,st_push_button])
