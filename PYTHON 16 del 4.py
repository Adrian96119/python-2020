Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=('46')
>>> int(x)
46
>>> type('x')
<class 'str'>
>>> x=int(x)
>>> type(x)
<class 'int'>
>>> 1+x
47
>>> ¿
  File "<stdin>", line 1
    ¿
    ^
SyntaxError: invalid character in identifier
>>> "buen dia"
'buen dia'
>>> a="buen"
>>> b="dia"
>>> a + b
'buendia'
>>> a "+" b
  File "<stdin>", line 1
    a "+" b
      ^
SyntaxError: invalid syntax
>>> a+" "+b
'buen dia'
>>> c=a+" "+b
>>> c
'buen dia'
>>> len c
  File "<stdin>", line 1
    len c
        ^
SyntaxError: invalid syntax
>>> len (c)
8
>>> c[0]
'b'
>>> c[1+1]
'e'
>>> c[len(c)-1]
'a'
>>> 4<10
True
>>> "hola"=="adios"
False
>>> 5=<5
  File "<stdin>", line 1
    5=<5
      ^
SyntaxError: invalid syntax
>>> 5<=5
True
>>> 100/5
20.0
>>> a=20
>>> type(a)
<class 'int'>
>>> type(7//2)
<class 'int'>
>>> type("tiza"+".")
<class 'str'>
>>> "hola"[1+1]
'l'
>>> type("hola"[1+1])
<class 'str'>
>>> len("hola")
4
>>> type(len("hola"))
<class 'int'>
>>> int("145")
145
>>> type(int("145"))
<class 'int'>
>>> float("145")
145.0
>>> type(float("145"))
<class 'float'>
>>> str(32)
'32'
>>> type(str(32))
<class 'str'>
>>> 1+2!=3
False
>>> type(1+2!=3)
<class 'bool'>
>>> 177%2==0
False
>>> type(177%2==0)
<class 'bool'>
>>> len("nube")<=20
True
>>> type(len("nube")<=20)
<class 'bool'>
>>> n=167/10
>>> n
16.7
>>> n=167//10
>>> n
16
>>> n=167%10
>>> n
7
>>> letra='a'
>>> letra
'a'
>>> tipe(letra)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tipe' is not defined
>>> type(letra)
<class 'str'>
>>> saludo="hola"+letra
>>> saludo
'holaa'
>>> c=saludo[0]
>>> c
'h'
>>> c=saludo[1+3]3
  File "<stdin>", line 1
    c=saludo[1+3]3
                 ^
SyntaxError: invalid syntax
>>> c=saludo[1+3]
>>> c
'a'
>>> L=len(saludo)
>>> L
5
>>> c=saludo[len(saludo)-1]
>>> c
'a'
>>> menor="a"<"b"
>>> menor
True
>>> D=1!=1
>>> D
False
>>> D="cinta">="canto"
>>> D
True
>>> c="z"+"a"+"paz"[0]
>>> c
'zap'
>>> x=c[0]=="z"
>>> x
True
>>> 11-(4%2/10)
11.0
>>> "30"+2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> "30"+"2"
'302'
>>> "hola"[len("hola")]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> len(124)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> "hola"[len("fin")]
'a'
>>> "hola"[11-(4%2+10)]
'o'
>>> int("4")
4
>>> int(4)
4
>>> int("z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'z'
>>> int("4.")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '4.'
>>> 4<" in xrange(1,10):
	pass"
  File "<stdin>", line 1
    4<" in xrange(1,10):
                       ^
SyntaxError: EOL while scanning string literal
>>>   File "<stdin>", line 1
    pass"
    ^
IndentationError: unexpected indent
>>> 
>>> 
>>> 4<"f"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
>>> "palabra"="rama"
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> "palabra"=="rama"
False
>>> 11-(4%2+10)
1
5+6