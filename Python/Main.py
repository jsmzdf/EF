# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:28:40 2019

@author: (╯°□°)╯︵ ┻━┻
"""

import ArreglarCSV as ac
import FiabilidadCronbach as fc
import Kr20  as kr
class Main:
    
    def __init__(self):
       self.alfaCronbach=0     
       
    
    def seleccion(self,numero):
             
        if numero==1:
            ac.ArreglarCSV()
        elif numero==2:
            fc.FiablidadCronbach().resultado()   
        elif numero==3:
            kr.Kr20().resultado()
            
    
if __name__ == "__main__":
   
    opcion=0
    while opcion >= 0:
        Main()
        print('\n\n\n Para crear CSV escriba 1')
        print('Para calcular alfa de crombach escriba 2')
        print('para calcular kr20 escriba 3')
        print('Para salir ponga 0')
        opcion=int(input('selecciona una opción\n'))
        opcion=int(opcion)
        Main().seleccion(opcion)
        if(opcion==0):
            opcion=-1
        
    