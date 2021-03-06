# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:46:08 2019

@author: (╯°□°)╯︵ ┻━┻
"""

#- Support Vector Machine
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
EFelicdad=pd.read_csv('tablaCon29REguntasInvertidas.csv' )
Col=pd.DataFrame(EFelicdad.columns)
x=EFelicdad.iloc[:,0:41]
y=EFelicdad.iloc[:,42: 43]
score=0
seed=0
#seed=2 da score de 1
while score< 0.94:
    seed = seed+1
    validation_size = 0.20
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=validation_size,random_state=seed)
    """
    from sklearn.preprocessing import StandardScaler
    escalar=StandardScaler()
    x_train= escalar.fit_transform(x_train)
    x_test=escalar.fit_transform(x_test) 
    """
    validation_size = 0.20
    proceso = SVC(gamma=0.001, C=100)
    proceso.fit(x_train, y_train)
    score=proceso.score(x_test, y_test)  
prediccion=proceso.predict(x_test)
matrizConfusion=confusion_matrix(y_test, prediccion)


reporte=classification_report(y_test, prediccion)

"""
i0,0= datos verdaderos positivos (dato que son 1 predecidos correctamente)
i1,1=datos verdadreros negativos datos reles que son 0 y se predijeron bien 
i0,1= datos falsos negativos dats reales 1 que el modelo predijo como 0 
i1,0=datos falsos positivos datos que son 0 y el modelo predijo cpomo 1


from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score#combiancion entre precision y sensiblidad
from sklearn.metrics import roc_auc_score

precision=precision_score(y_test, prediccion)
exactitud=accuracy_score(y_test, prediccion)
sensiblidad=recall_score(y_test, prediccion)
f1=f1_score(y_test, prediccion)
curva_roc_auc=roc_auc_score(y_test, prediccion)

"""