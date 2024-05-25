class CanSignal():
    def __init__(self, _name:str, _startPosition:int, _endPosition:int, _offset:int = None, _gain:int = None, _conversionTable:dict = None, _unit:str = None) -> None:
        self.name = _name
        self.startPosition = _startPosition
        self.endPosition = _endPosition
        self.offset = _offset
        self.gain = _gain
        self.converionTable = _conversionTable
        self.unit = _unit
        
    def __str__(self) -> str:
        return self.name
    
    def __iter__(self):
        return self
        
#Bordcomputer
st_light_button = CanSignal("Status light button", 1, 1, _conversionTable = {'0x80':'Light button activated', '0x00':'Light button not activated'})
st_push_button = CanSignal("Status push button", 2, 2, _conversionTable = {'0x01':'Push button activated', '0x00':'Push button not activated'})

#Unterstützung
st_support_setting = CanSignal("Support setting",0,0, _conversionTable = {'0x09':'Off', '0x01':'Eco', '0x02':'Tour', '0x03':'Sport', '0x04':'Turbo', })

#Pedalsensor
tq_pedalsensor = CanSignal("Pedalsensor Torque", 0, 1, _gain = 0.1, _unit = "Nm")
ti_pedalsensor = CanSignal("Pedalsensor Timer", 2, 3, _gain = 0.1, _unit = "ms")

#Startbutton
st_start_button = CanSignal("Status startbutton", 0,0,_conversionTable={'0x00':'Off', '0x01':'On'})
