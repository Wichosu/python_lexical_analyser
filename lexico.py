import ply.lex as lex
import os

tokens = ['ID', 'ANZAHL', 'PLUS', 'MINUS', 'MAL', 'TEILEN', 'ZUORDNEN', 'NG', 'WA', 'WAG', 'GA', 'GAG', 'LK', 'RK', 'KOMMA', 'SEMMIKOLOM', 'PUNKT', 'AKTUALISIEREN']
#tokensEn [ID,  NUMBER,   PLUS,   MINUS,  TIMES,  DIVIDE,   ASSIGN,     NE,   LT,   LTE,   GT,   GTE, LPARENT,RPARENT,COMMA, SEMMICOLOM,     DOT,    UPDATE]
reservadas = ['START', 'ENDE', 'WENN', 'DANN', 'WAHREND', 'MACHEN', 'ANRUF', 'KONST', 'VAR', 'VERFAHREN', 'AUS', 'IN', 'ANDERS', 'UNGERADE']
#reservadasEN[ BEGIN,  END,     IF,     THEN,   WHILE,     DO,       CALL,    CONST,   VAR,   PROCEDURE,   OUT,   IN,   ELSE,     ODD]
tokens = tokens + reservadas

t_ignore = r'\t '
t_PLUS=r'\+'
t_MINUS=r'\-'
t_MAL=r'\*'
t_TEILEN=r'/'
t_ZUORDNEN=r'='
t_NG=r'!='
t_WA=r'<'
t_WAG=r'<='
t_GA=r'>'
t_GAG=r'>='
t_LK=r'\('
t_RK=r'\)'
t_KOMMA=r','
t_SEMMIKOLOM=r';'
t_PUNKT=r'\.'
t_AKTUALISIEREN=r'=='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

#token numero [0-9]
def t_ANZAHL(t):
    r'\d+'
    t.value = int(t.value)
    return t
#token comentario
def t_KOMMENTAR(t):
    r'\#.*'
    pass
#token retorno de linea
def t_NEUEZEILE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_START(t):
    r'START'
    return t
#diagonal invertida + - * () .
def t_ENDE(t):
    r'ENDE'
    return t

def t_WENN(t):
    r'WENN'
    return t

def t_DANN(t):
    r'DANN'
    return t

def t_WAHREND(t):
    r'WAHREND'
    return t

def t_MACHEN(t):
    r'MACHEN'
    return t

def t_ANRUF(t):
    r'ANRUF'
    return t

def t_KONST(t):
    r'KONST'
    return t

def t_VAR(t):
    r'VAR'
    return t

def t_VERFAHREN(t):
    r'VERFAHREN'
    return t

def t_AUS(t):
    r'AUS'
    return t

def t_IN(t):
    r'IN'
    return t

def t_ANDERS(t):
    r'ANDERS'
    return t

def t_UNGERADE(t):
    r'UNGERADE'
    return t

#token error
def t_error(t):
    print("Caracter Ilegal '%s' "% t.value[0])
    t.lexer.skip(1)

def elegirArchivo():
    os.chdir(os.getcwd() + "/test")
    archivos = os.listdir()
    numeracion = 1
    if len(archivos) != 0:
        for i in archivos:
            print(f"[{numeracion}] {i}")
            numeracion += 1
    else:
        print("No hay archivos en la carpeta test")
    entrada = int(input())
    seleccion = open(archivos[entrada-1], "rt")
    return seleccion.read()

analizador = lex.lex()
codigo = elegirArchivo()
analizador.input(codigo)

os.chdir("/home/adminq/Desktop/lexico/out")
salida = open("salida.txt", "w")

while True:
    tok = analizador.token()
    if not tok:
        break
    print(tok)
    salida.write(str(tok)+"\n")

salida.close()