from ctypes import *

class case(Union):
	_fields_ = [
	("evidencia_long", c_long),
	("evidencia_int", c_int),
	("evidencia_char", c_char * 4),
	]

value = raw_input("Entre o novo numero da evidencia:")
new_evidencia = case(int(value))
print "Evidencia de numero long: %ld" % new_evidencia.evidencia_long
print "Evidencia de numero int: %d" % new_evidencia.evidencia_int
print "Evidencia de numero char: %s" % new_evidencia.evidencia_char
