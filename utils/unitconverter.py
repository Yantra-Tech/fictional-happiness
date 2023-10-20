__unrecognized_units = ValueError("The units are not recognized.")

def convert_temperature(value:float, from_unit:str, to_unit:str):
    if from_unit not in ('C', 'K', 'F'):
        raise __unrecognized_units
    elif to_unit not in ('C', 'K', 'F'):
        raise __unrecognized_units

    if from_unit == to_unit:
        return value
    elif from_unit == "C":
        if to_unit == "K":
            value = value + 273.15
        elif to_unit == "F":
            value = (value * 9/5) + 32
    elif from_unit == "K":
        if to_unit == "C":
            value = value - 273.15
        elif to_unit == "F":
            value = ((value - 273.15) * 9/5) + 32
    elif from_unit == "F":
        if to_unit == "C":
            value = (value - 32) * 5/9
        elif to_unit == "K":
            value = ((value - 32) * 5/9) + 273.5
        
    return value

def convert_length(value:float, from_unit:str, to_unit:str):
    if from_unit not in ('km', 'm', 'cm', 'mm'):
        raise __unrecognized_units
    elif to_unit not in ('km', 'm', 'cm', 'mm'):
        raise __unrecognized_units

    if from_unit == to_unit:
        return value
    elif from_unit == "km":
        if to_unit == "m":
            value = value*1000
        elif to_unit == "cm":
            value = value*100000
        elif to_unit == "mm":
            value = value*1000000
    elif from_unit == "m":
        if to_unit == "km":
            value = value/1000
        elif to_unit == "cm":
            value = value*100
        elif to_unit == "mm":
            value = value*1000
    elif from_unit == "cm":
        if to_unit == "km":
            value = value/100000
        elif to_unit == "m":
            value = value/100
        elif to_unit == "mm":
            value = value*10
    elif from_unit == "mm":
        if to_unit == "km":
            value = value/1000000
        elif to_unit == "m":
            value = value/1000
        elif to_unit == "cm":
            value = value/10
    
    return value

def convert_time(value:float, from_unit:str, to_unit:str):
    if from_unit not in ('H', 'M', 'S'):
        raise __unrecognized_units
    elif to_unit not in ('H', 'M', 'S'):
        raise __unrecognized_units
    
    if from_unit == to_unit:
        return value
    elif from_unit == "H":
        if to_unit == "M":
            value = value*60
        elif to_unit == "S":
            value = value*3600
    elif from_unit == "M":
        if to_unit == "H":
            value = value*1/60
        elif to_unit == "S":
            value = value*60
    elif from_unit == "S":
        if to_unit == "H":
            value = value*1/3600
        elif to_unit == "M":
            value = value*1/60
    
    return value

def convert_weight(value:float, from_unit:str, to_unit:str):
    if from_unit not in ('kg','g'):
        raise __unrecognized_units
    elif to_unit not in ('kg','g'):
        raise __unrecognized_units

    if from_unit == to_unit:
        return value
    elif from_unit == "kg":
        if to_unit == "g":
            value = value *1000
    elif from_unit == "g":
        if to_unit == "kg":
            value = value /1000
        
    return value

_SANITIZE_UNITS = {
    convert_temperature   : lambda unit : unit.upper()[0] ,    # First Charachter only, UPPER CASE
    convert_length        : lambda unit : unit.lower()[:2],    # First 2 Characters, lowercase
    convert_time          : lambda unit : unit.upper()[0] ,    # First Charachter only, UPPER CASE
    convert_weight        : lambda unit : unit.lower()[:2]     # First 2 Characters, lowercase
}

def _calc_value(bot:str, from_:list, to_:list) -> [float, str, str]:
    from_value, from_unit = from_

    from_value = float(from_value)
    from_unit  = _SANITIZE_UNITS[bot](from_unit)
    to_unit    = _SANITIZE_UNITS[bot](to_[0])

    return bot(from_value, from_unit, to_unit)

def wrapper(from_:list, bot, to_:list) -> str:
    return f"Sure. {' '.join(from_)}, is {_calc_value(bot, from_, to_)} {to_[0]}."

MICRO_BOTS = {
    'temperature'   : lambda from_, to_ : wrapper( from_,    convert_temperature, to_ ),
    'length'        : lambda from_, to_ : wrapper( from_,    convert_length,      to_ ),
    'time'          : lambda from_, to_ : wrapper( from_,    convert_time,        to_ ),
    'weight'        : lambda from_, to_ : wrapper( from_,    convert_weight,      to_ )
}
