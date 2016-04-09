print "1 Calculadora"
print "2 Par o Impar"
operacion=int(raw_input("elejir opcion"))
if operacion==1:
  var=int(raw_input("Elejir Nuemro"))
  var2=int(raw_input("Elejir Numero 2"))  
  val1=(raw_input("ingresar una operacion"))
  if val1== "+"or"suma":
    print var+var2
  elif val1== "-"or"resta":
    print var-var2
  elif val1== "*"or"multiplicacion":
    print var*var2
  elif val1== "/"or"division":
    print var/var2
else:
    ver=int(raw_input("Elejir Nuemro"))
  if(ver%2==0):  
    print(str(ver)+" es par")  
  else:
    print(str(ver)+" es impar")

    

