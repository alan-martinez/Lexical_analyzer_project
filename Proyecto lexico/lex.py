class Type:
    def __init__(self):
        self.ERROR = -1
        self.IDENTIFICADOR = 0
        self.ENTERO = 1
        self.REAL = 2
        self.CADENA = 3
        self.TIPO = 4
        self.OPSUMA = 5
        self.OPRESTA = 6
        self.OPMULTIPLICACION = 7
        self.OPDIVISION = 8
        self.OPOR = 9
        self.OPAND = 10
        self.OPNOT = 11
        self.OPMAYORQ = 12
        self.OPMENORQ = 13
        self.OPMAYOROIGUAL = 14
        self.OPMENOROIGUAL = 15
        self.OPIGUAL = 16
        self.OPESIGUAL = 17
        self.OPESDIFERENTE = 18
        self.PUNTOYCOMA = 19
        self.COMA = 20
        self.PARENTESIOSABIERTO = 21
        self.PARENTESISCERRADO = 22
        self.LLAVEABIERTA = 23
        self.LLAVECERRADA = 24
        self.BRACKETABIERTO = 25
        self.BRACKETCERRADO = 26
        self.DOSPUNTOS = 27
        self.IF = 50
        self.WHILE = 51 
        self.RETURN = 52
        self.ELSE = 53
        self.INT = 54
        self.FLOAT = 55
        self.VOID = 56
        self.PESO = 34
        
        
class Lexico(Type):
    def __init__(self, input, indice = 0, continua = True, character = "", state = 1, symbol = "", type = -1, typeString = ""): 
        self.input = input
        self.indice = indice
        self.continua = continua
        self.character = character
        self.state = state
        self.symbol = symbol
        self.type = type
        self.typeString = typeString

        Type.__init__(self)

    def tipoCadena(self, type):
        self.typeString = ""

        switch = {
            self.ERROR: self.message_ERROR,
            self.IDENTIFICADOR: self.message_IDENTIFICADOR,
            self.ENTERO: self.message_ENTERO,
            self.REAL: self.message_REAL,
            self.CADENA: self.message_CADENA,
            self.OPSUMA: self.message_OPMAS,
            self.OPRESTA: self.message_OPMENOS,
            self.OPMULTIPLICACION: self.message_OPMULTI,
            self.OPDIVISION: self.message_OPDIV,
            self.OPMAYORQ: self.message_MAYORQUE,
            self.OPMENORQ: self.message_MENORQUE,
            self.OPMAYOROIGUAL: self.message_MAYORIGUAL,
            self.OPMENOROIGUAL: self.message_MENORIGUAL,
            self.OPOR: self.message_OR,
            self.OPAND: self.message_AND,
            self.OPNOT: self.message_NOT,
            self.OPIGUAL: self.message_IGUAL,
            self.OPESIGUAL: self.message_ESIGUAL,
            self.OPESDIFERENTE: self.message_ESDIFERENTE,
            self.PUNTOYCOMA: self.message_PUNTOCOMA,
            self.COMA: self.message_COMA,
            self.PARENTESIOSABIERTO: self.message_PARENTESISABIERTO,
            self.PARENTESISCERRADO: self.message_PARENTESISCERRADO,
            self.LLAVEABIERTA: self.message_LLAVEABIERTA,
            self.LLAVECERRADA: self.message_LLAVECERRADA,
            self.BRACKETABIERTO: self.message_BRACKETABIERTO,
            self.BRACKETCERRADO: self.message_BRACKETCERRADO,
            self.DOSPUNTOS: self.message_DOSPUNTOS,
            self.IF: self.message_IF,
            self.WHILE: self.message_WHILE,
            self.RETURN: self.message_RETURN,
            self.ELSE: self.message_ELSE,
            self.INT: self.message_INT,
            self.FLOAT: self.message_FLOAT,
            self.VOID: self.message_VOID,
            self.PESO: self.message_PESO
        }

        switch[type]()

        return self.typeString

    def nextSymbol(self):
        self.state = 1
        self.continua = True
        self.symbol = ""
        self.type = -1

        while self.continua:
            self.character = self.nextCharacter()

            switch = {
                0: self.state00,
                1: self.state01,
                2: self.state02,
                3: self.state03,
                4: self.state04,
                5: self.state05,
                6: self.state06,
                7: self.state07,
                8: self.state08,
                9: self.state09,
                10: self.state10,
                11: self.state11,
                12: self.state12,
                13: self.state13,
                14: self.state14,
                15: self.state15,
                16: self.state16,
                17: self.state17,
                18: self.state18,
                19: self.state19,
                20: self.state20,
                21: self.state21,
                22: self.state22,
                23: self.state23,
                24: self.state24,
                25: self.state25,
                26: self.state26,
                27: self.state27,
                28: self.state28,
                29: self.state29,
                30: self.state30,
                31: self.state31,
                32: self.state32
                
            }

            switch.get(self.state, self.error)()

        if self.type < 50:

            switch = {
                -1: self.error, # ERROR
                2: self.type00, # Identificador
                3: self.type01, # Entero
                5: self.type02, # Real
                7: self.type03, # Cadena
                8: self.type05, # Suma
                9: self.type06, # Resta
                10: self.type07, # Multiplicacion
                11: self.type08, # Division
                17: self.type09, # OR
                19: self.type10, # AND
                20: self.type11, # NOT
                14: self.type12, # Mayor que
                12: self.type13, # Menor que
                15: self.type14, # Mayor o igual que
                13: self.type15, # Menor o igual que
                22: self.type16, # Igual
                23: self.type17, # Es igual
                21: self.type18, # Es diferente
                24: self.type19, # Punto y coma
                25: self.type20, # Coma
                26: self.type21, # Parantesis abierto
                27: self.type22, # Parentesis cerrado
                28: self.type23, # Llave abierta
                29: self.type24, # Llave cerrada
                30: self.type25, # Bracket abierto
                31: self.type26, # Bracket cerrado
                32: self.type27, # Dos puntos
                34: self.type34 # Peso
            }

            switch.get(self.state, self.error)()

    def verificarPalabraReservada(self, symbol):
        palabrasReservadas = {
            "int": self.INT,
            "float": self.FLOAT,
            "void": self.VOID,
            "if": self.IF,
            "while": self.WHILE,
            "return": self.RETURN,
            "else": self.ELSE
        }
        self.type = palabrasReservadas.get(symbol, self.type)


    def nextCharacter(self):
        if self.terminado():
            return "$"
        character = self.input[self.indice]
        self.indice += 1
        return character

    def nextState(self, state):      
        self.state = state
        self.symbol += self.character

        
    def retroceso(self):
        if not self.esPeso(self.character):
            self.indice -= 1
        self.continua = False
        self.verificarPalabraReservada(self.symbol)

    def terminado(self):
        return self.indice >= len(self.input)
    

    def esPeso(self, character):
        return character == "$"

    def esEspacio(self, character):
        return character == " "

    def esCaracter(self, character):
        return ord(character) == 32 or ord(character) == 33 or ord(character) >= 35 and ord(character) <= 126

    def esLetra(self, character):
        return character.isalpha() or character == "_"

    def esNumero(self, character):
        return character.isdigit()

    def esPunto(self, character):
        return character == "."
   
    def esComilla(self, character):
        return character == "\""
        
    def esSuma(self, character):
        return character == "+"

    def esResta(self, character):
        return character == "-"

    def esMultiplicacion(self, character):
        return character == "*"

    def esDivision(self, character):
        return character == "/"

    def esMayorQue(self, character):
        return character == ">"

    def esMenorQue(self, character):
        return character == "<"

    def esPipe(self, character):
        return character == "|"

    def esAmpersand(self, character):
        return character == "&"

    def esFactorial(self, character):
        return character == "!"

    def esPuntoYComa(self, character):
        return character == ";"

    def esComa(self, character):
        return character == ","

    def esParentesisAbierto(self, character):
        return character == "("

    def esParentesisCerrado(self, character):
        return character == ")"

    def esLlaveAbierta(self, character):
        return character == "{"

    def esLlaveCerrada(self, character):
        return character == "}"

    def esBracketAbierto(self, character):
        return character == "["

    def esBracketCerrado(self, character):
        return character == "]"

    def esIgual(self, character):
        return character == "="

    def esDosPuntos(self, character):
        return character == ":"
   
    # TODO posibles states

    def state00(self):
        self.continua = False

    def state01(self):
        if self.esPeso(self.character):
            self.nextState(0)
        elif self.esLetra(self.character):
            self.nextState(2)
        elif self.esNumero(self.character):
            self.nextState(3)
        elif self.esComilla(self.character):
            self.nextState(6)
        elif self.esSuma(self.character):
            self.nextState(8)
        elif self.esResta(self.character):
            self.nextState(9)
        elif self.esMultiplicacion(self.character):
            self.nextState(10)
        elif self.esDivision(self.character):
            self.nextState(11)
        elif self.esMenorQue(self.character):
            self.nextState(12)
        elif self.esMayorQue(self.character):
            self.nextState(14)
        elif self.esPipe(self.character):
            self.nextState(16)
        elif self.esAmpersand(self.character):
            self.nextState(18)
        elif self.esFactorial(self.character):
            self.nextState(20)
        elif self.esIgual(self.character):
            self.nextState(22)
        elif self.esPuntoYComa(self.character):
            self.nextState(24)
        elif self.esComa(self.character):
            self.nextState(25)
        elif self.esParentesisAbierto(self.character):
            self.nextState(26)
        elif self.esParentesisCerrado(self.character):
            self.nextState(27)
        elif self.esLlaveAbierta(self.character):
            self.nextState(28)
        elif self.esLlaveCerrada(self.character):
            self.nextState(29)
        elif self.esBracketAbierto(self.character):
            self.nextState(30)
        elif self.esBracketCerrado(self.character):
            self.nextState(31)
        elif self.esDosPuntos(self.character):
            self.nextState(32)
        elif self.esEspacio(self.character):
            self.state = 1
        else:
            self.symbol += self.character
            self.continua = False

    def state02(self):
        if self.esLetra(self.character):
            self.nextState(2)
        elif self.esNumero(self.character):
            self.nextState(2)
        elif self.esEspacio(self.character):
            self.continua = False
            self.verificarPalabraReservada(self.symbol)
        else:
            self.retroceso()

    def state03(self):
        if self.esNumero(self.character):
            self.nextState(3)
        elif self.esPunto(self.character):
            self.type = -1
            self.nextState(4)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state04(self):
        if self.esNumero(self.character):
            self.nextState(5)
        else:
            self.retroceso()

    def state05(self):
        if self.esNumero(self.character):
            self.nextState(5)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state06(self):
        if self.esComilla(self.character):
            self.nextState(7)
        elif self.esCaracter(self.character):
            self.nextState(6)
        else:
            self.retroceso()
    
    def state07(self):
        self.retroceso()

    def state08(self):
        self.retroceso()

    def state09(self):
        self.retroceso()

    def state10(self):
        self.retroceso()

    def state11(self):
        self.retroceso()
    
    def state12(self):
        if self.esIgual(self.character):
            self.nextState(13)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()
    
    def state13(self):
        self.retroceso()

    def state14(self):
        if self.esIgual(self.character):
            self.nextState(15)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()
    
    def state15(self):
        self.retroceso()

    def state16(self):
        if self.esPipe(self.character):
            self.nextState(17)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state17(self):
        self.retroceso()

    def state18(self):
        if self.esAmpersand(self.character):
            self.nextState(19)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state19(self):
        self.retroceso()

    def state20(self):
        if self.esIgual(self.character):
            self.nextState(21)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state21(self):
        self.retroceso()

    def state22(self):
        if self.esIgual(self.character):
            self.nextState(23)
        elif self.esEspacio(self.character):
            self.continua = False
        else:
            self.retroceso()

    def state23(self):
        self.retroceso()

    def state24(self):
        self.retroceso()

    def state25(self):
        self.retroceso()

    def state26(self):
        self.retroceso()

    def state27(self):
        self.retroceso()

    def state28(self):
        self.retroceso()

    def state29(self):
        self.retroceso()

    def state30(self):
        self.retroceso()

    def state31(self):
        self.retroceso()

    def state32(self):
        self.retroceso()
    # tipos validos

    def error(self):
        self.type = self.ERROR

    def type00(self):
        self.type = self.IDENTIFICADOR

    def type01(self):
        self.type = self.ENTERO
    
    def type02(self):
        self.type = self.REAL
    
    def type03(self):
        self.type = self.CADENA

    def type04(self):
        self.type = self.TIPO

    def type05(self):
        self.type = self.OPSUMA

    def type06(self):
        self.type = self.OPRESTA

    def type07(self):
        self.type = self.OPMULTIPLICACION

    def type08(self):
        self.type = self.OPDIVISION

    def type09(self):
        self.type = self.OPOR

    def type10(self):
        self.type = self.OPAND

    def type11(self):
        self.type = self.OPNOT

    def type12(self):
        self.type = self.OPMAYORQ

    def type13(self):
        self.type = self.OPMENORQ

    def type14(self):
        self.type = self.OPMAYOROIGUAL

    def type15(self):
        self.type = self.OPMENOROIGUAL

    def type16(self):
        self.type = self.OPIGUAL

    def type17(self):
        self.type = self.OPESIGUAL

    def type18(self):
        self.type = self.OPESDIFERENTE

    def type19(self):
        self.type = self.PUNTOYCOMA

    def type20(self):
        self.type = self.COMA

    def type21(self):
        self.type = self.PARENTESIOSABIERTO

    def type22(self):
        self.type = self.PARENTESISCERRADO

    def type23(self):
        self.type = self.LLAVEABIERTA

    def type24(self):
        self.type = self.LLAVECERRADA

    def type25(self):
        self.type = self.BRACKETABIERTO

    def type26(self):
        self.type = self.BRACKETCERRADO

    def type27(self):
        self.type = self.DOSPUNTOS

    def type34(self):
        self.type = self.PESO

    
    # Tipos posibles
    
    def message_PESO(self): # Cortar la cadena
        self.typeString = "Fin de Cadena"

    def message_ERROR(self):
        self.typeString = "No esta definido"
    
    def message_IDENTIFICADOR(self):
        self.typeString = "Identificador"

    def message_ENTERO(self):
        self.typeString = "Entero"

    def message_REAL(self):
        self.typeString = "Real"
        
    def message_CADENA(self):
        self.typeString = "Cadena"

    def message_OPMAS(self):
        self.typeString = "Mas"

    def message_OPMENOS(self):
        self.typeString = "Menos"

    def message_OPMULTI(self):
        self.typeString = "Multiplicacion"

    def message_OPDIV(self):
        self.typeString = "Division"

    def message_MAYORQUE(self):
        self.typeString = "Mayor que"

    def message_MENORQUE(self):
        self.typeString = "Menor que"

    def message_MAYORIGUAL(self):
        self.typeString = "Mayor o igual que"

    def message_MENORIGUAL(self):
        self.typeString = "Menor o igual que"

    def message_OR(self):
        self.typeString = "Or"

    def message_AND(self):
        self.typeString = "And"

    def message_NOT(self):
        self.typeString = "Not"

    def message_IGUAL(self):
        self.typeString = "Igual"

    def message_ESIGUAL(self):
        self.typeString = "Es igual a"

    def message_ESDIFERENTE(self):
        self.typeString = "Es diferente de"

    def message_PUNTOCOMA(self):
        self.typeString = "Punto y coma"

    def message_COMA(self):
        self.typeString = "Coma"

    def message_PARENTESISABIERTO(self):
        self.typeString = "Parentesis abierto"

    def message_PARENTESISCERRADO(self):
        self.typeString = "Parentesis abierto"

    def message_LLAVEABIERTA(self):
        self.typeString = "Llave abierta"

    def message_LLAVECERRADA(self):
        self.typeString = "Llave cerrada"

    def message_BRACKETABIERTO(self):
        self.typeString = "Bracket abierto"

    def message_BRACKETCERRADO(self):
        self.typeString = "Bracket cerrado"

    def message_DOSPUNTOS(self):
        self.typeString = "Dos puntos"

    def message_IF(self):
        self.typeString = "If"

    def message_WHILE(self):
        self.typeString = "While"

    def message_RETURN(self):
        self.typeString = "Return"

    def message_ELSE(self):
        self.typeString = "Else"

    def message_INT(self):
        self.typeString = "Int"

    def message_FLOAT(self):
        self.typeString = "Float"

    def message_VOID(self):
        self.typeString = "Void"
