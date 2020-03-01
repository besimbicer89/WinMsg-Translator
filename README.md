# WinMsg-Translator
Traductor de Mensajes de Windows (WM).  
Contiene un JSON, wm.json, que hace de base de datos, guardando todos los Mensajes de Windows con su respectivo ID, tanto en decimal como en hexadecimal.  
Los campos del JSON son:  
- wm: Parámetro de tipo String. Contiene el identificador de dicho mensaje.  
- id_hex: Parámetro de tipo String. Contiene el número hexadecimal de dicho mensaje.  
- id: Parámetro de tipo Integer. Contiene el número decimal de dicho mensaje.  
  
En este repo se puede encontrar win.py, un script en python que sirve para realizar las busquedas del mensaje, pasandole como argumento el número hexadecimal del mensaje.  
  
  
# English
  
Windows Message Translator  
It contains a JSON, wm.json, which acts as a database, saving every Windows Message with its respective IDs, in decimal and hexadecimal.  
Its fields are:  
- wm: String type parameter. Contains the identifier of said message.  
- id_hex: String type parameter. Contains the hexadecimal number of said message.  
- id: Integer type parameter. Contains the decimal number of said message.  
  
In this repo win.py can be found, a python script that can be used to search for messages, passing it a parameter of its hexadecimal number.
