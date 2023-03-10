'''
RKD-MpyCode
Copyright (C) 2023 PCX-LK
https://github.com/PCX-LK/RKD-MpyCode

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from machine import Pin
import json

stats =  Pin(2, Pin.OUT)
sw1 = Pin(9, Pin.IN, Pin.PULL_UP)
sw2 = Pin(10, Pin.IN, Pin.PULL_UP)
sw3 = Pin(11, Pin.IN, Pin.PULL_UP)
sw4 = Pin(12, Pin.IN, Pin.PULL_UP)
sw5 = Pin(14, Pin.IN, Pin.PULL_UP)
sw6 = Pin(15, Pin.IN, Pin.PULL_UP)

DefConfig="""
{
"k1": "D",
"k2": "F",
"k3": "J",
"k4": "K",
"k5": "V",
"k6": "N",
"ST": "Space",
"SR1L": "W",
"SR1R": "E",
"SR2L": "O",
"SR2R": "P",
"N1": "n1",
"N2": "n2",
"N3": "n3",
"N4": "n4",
"N5": "n5",
"N6": "n6",
"N7": "n7",
"N8": "n8",
"N9": "n9",
"Na": "n0",
"Nb": "nEnter",
"Nc": "n.",
"Nd": "NumLock"
}

"""

keydict = {'`':0x35,'1':0x1e,'2':0x1f,'3':0x20,'4':21,'5':0x22,'6':0x23,'7':0x24,'8':0x25,'9':0x26,'0':0x27,'-':0x2d,'=':0x2e,'BackSpace':0x2a,
           'Tab':0x2b,'Q':0x14,'W':0x1a,'E':0x08,'R':0x15,'T':0x17,'Y':0x1c,'U':0x18,'I':0x0c,'O':0x12,'P':0x13,'[':0x2f,']':0x30,'\\':0x31,
           'CapsLock':0x39,'A':0x04,'S':0x16,'D':0x07,'F':0x09,'G':0x0a,'H':0x0b,'J':0x0d,'K':0x0e,'L':0x0f,';':0x33,'\'':0x34,'Enter':0x58,
           'ShiftL':0xe1,'Z':0x1d,'X':0x1b,'C':0x06,'V':0x19,'B':0x05,'N':0x11,'M':0x10,',':0x36,'.':0x37,'/':0x38,'ShiftR':0xe5,
           'CtrlL':0xe0,'WinL':0xe3,'AltL':0xe2,'Space':0x2c,'AltR':0xe6,'WinR':0xe7,'App':0x65,'CtrlR':0xe4,
           'Insert':0x49,'Home':0x4a,'PageUp':0x4b,'Delete':0x49,'End':0x4d,'PageDown':0x4e,
           'UpArrow':0x52,'LeftArrow':0x50,'DownArrow':0x51,'RightArrow':0x4f,
           'ESC':0x3a,'F1':0x3a,'F2':0x3b,'F3':0x3c,'F4':0x3d,'F5':0x3e,'F6':0x3f,'F7':0x40,'F8':0x41,'F9':0x42,'F10':0x43,'F11':0x44,'F12':0x45,'PrintScreen':0x46,'ScrollLock':0x47,'Pause':0x48,
           'NumLock':0x53,'n1':0x59,'n2':0x5a,'n3':0x5b,'n4':0x5c,'n5':0x5d,'n6':0x5e,'n7':0x5f,'n8':0x60,'n9':0x61,'n0':0x62,'n/':0x54,'n*':0x55,'n-':0x56,'n+':0x57,'nEnter':0x58,'n.':0x63}

def write_defconf():
    file=open('config.json',mode='w+')
    raw=DefConfig
    file.seek(0)
    file.write(raw)
    file.flush()
    file.close()
    return {'k1': 7,'k2': 9,'k3': 13,'k4': 14,'k5': 25,'k6': 17,'ST': 44,'SR1L': 26,'SR1R': 8,'SR2L': 18,'SR2R': 19}

def load_config():
    try:
        file=open('config.json',mode='r')
    except ValueError:
        return write_defconf()
    except OSError:
        return write_defconf()
    else:
        data=json.load(file)
        for i in data :
            data[i]=keydict[data[i]]
        file.close()
        return data
    
        
def key():
    file=open('config.json',mode='r')
    j=json.load(file)
    return [j['k1'],j['k2'],j['k3'],j['k4'],j['k5'],j['k6']]
