# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:26:03 2019

@author: (╯°□°)╯︵ ┻━┻
"""
import pandas as pd
import numpy as np
import scipy.stats as ssc
EFelicdad=pd.read_csv('DFnumericoInvertido.csv' )
Col=pd.DataFrame(EFelicdad.columns)

x=EFelicdad.iloc[:,29:42]
#x=EFelicdad[['Es creyente','Promedio académico:','Trabaja:','Edad:']]
y=EFelicdad.iloc[:,42: 43]
import statsmodels.api as sm

prueba=ssc.chisquare(x)
chi2_stat, p_val, dof, ex=ssc.chi2_contingency(x,correction=False)
ex2=ssc.chi2.stats(x)
modelo_logistico=sm.Logit(y,x)
#metodos del fit newton, cg
resultado=modelo_logistico.fit()

print(resultado)
result=resultado.summary()
print(result)
"""
file = open("prueba.txt", "w")
file.write(str(result))
file.close()"""
result=resultado.summary2()
print(result)

from sklearn.linear_model import LogisticRegression
modelo_logisticoSk=LogisticRegression()
modelo_logisyco_fit=modelo_logisticoSk.fit(x,y)
modelo_logisyco_score=modelo_logisticoSk.score(x,y)

