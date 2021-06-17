""" Reto 3 Priorizacion de Vacunas  #
    Tu nombre aquí
    Mayo xx-XX """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def etapas(nombre,fecha_nac,edad,correo,ts,th,th1,teb,td,tir,tvih,tc,tb,te,ta,to,tls,tpl,tp,tpol,tam,tre,tbc,tcr,tdc,tca,tba,tpt,tav,tec):
    if (ts=="s" and th=="s") or edad>=80:
        msg="Usted será vacunado en la Etapa 1"
        etapa="Trabajadores de la salud y apoyo de atención a áreas COVID-19, y personas de 80 y más años."
    elif (ts=="s" and th1=="s") or 60<=edad<=79:
        msg="Usted será vacunado en la Etapa 2"
        etapa="Los demás trabajadores de la salud, personal de apoyo que no trabajen en áreas COVID-19 y personas entre 60 y 79 años."
    elif 50<=edad<=59 or tp=="s" or tpol=="s" or teb=="s":
        msg="Usted será vacunado en la Etapa 3"
        etapa="Personas entre 50 y 59 años. Docentes, directivos y personal educativo, Fuerzas Militares y Policía, Guardia Indígena y Cimarrona, y personas entre 16 y 59 años con comorbilidades o enfermedades hipertensivas: Diabetes, Insuficiencia renal, VIH, Cáncer, Tuberculosis, EPOC, ASMA, Obesidad, en lista de espera de trasplante de órganos vitales o Postransplante de órganos vitales."
    elif 40<=edad<=49 or tam=="s" or tre=="s":
        msg="Usted será vacunado en la Etapa 4"
        etapa="Personas entre 40 y 49 años. Personas privadas de libertad, cuidadores institucionales, población en riesgo de brotes, en ocupaciones de alto riesgo, bomberos, socorristas, pilotos y auxiliares."
    elif edad>=16 and teb=="n" and th=="n" and th1=="n" and tre=="n":
        msg="Usted será vacunado en la Etapa 5"
        etapa="Población mayor de 16 años no priorizada en las etapas 1 al 4. En esta etapa se vacunará a la población de 16 años y más que no se encuentren en las poblaciones indicadas en las etapas, 1, 2, 3 y 4. Se mantendrá el orden de aplicación comenzando con los adultos entre 50 y 59 años, hasta llegar a los jóvenes y adolescentes que se encuentren dentro de la población objeto del Plan Nacional de Vacunación."
    return etapa, msg


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación 
# =====================================================================
