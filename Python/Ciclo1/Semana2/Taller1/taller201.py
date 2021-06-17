""" Taller 2.1 Salida Estandar:Pantalla #
    Alejandro Tamayo
    Mayo 12-2021 """ 
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def presentar_datos_personales():
  #TODO: Completa el código fuente incluyendo comentarios
  nombre="Alejandro"
  apellido="Tamayo"
  direccion="Carrera 12 50-25"
  telefono=3008710153
  barrio="Caribe"
  ciudad="Manizales"
  print("Su nombre es: ",nombre," ",apellido)
  print("Su Dirección es: ",direccion)
  print("Su número de Teléfono es: ",telefono)
  print("Vive en: Barrio ",barrio," en la ciudad de ",ciudad)

def dibujar_C_3_PO():
  #TODO: Completa el código fuente incluyendo comentarios
  print("")
  print("       /~\ ")
  print("      |oo )")
  print("      _\=/_")
  print("     /     \ ")
  print("    //|/.\|\\")
  print("   ||  \_/  ||")
  print("   || |\ /| ||")
  print("    # \_ _/  #")
  print("      | | |")
  print("      | | |")
  print("      []|[]")
  print("      | | |")
  print("     /_]_[_\ ")


def esribir_nombre_sw():
  #TODO: Completa el código fuente incluyendo comentariose 
  print("")
  print("             _        ______        _              _   _   _____    _____     ____  ")
  print("     /\     | |      |  ____|      | |     /\     | \ | | |  __ \  |  __ \   / __ \ ")
  print("    /  \    | |      | |__         | |    /  \    |  \| | | |  | | | |__) | | |  | | ")
  print("   / /\ \   | |      |  __|    _   | |   / /\ \   | . ` | | |  | | |  _  /  | |  | | ")
  print("  / ____ \  | |____  | |____  | |__| |  / ____ \  | |\  | | |__| | | | \ \  | |__| | ")
  print(" /_/    \_\ |______| |______|  \____/  /_/    \_\ |_| \_| |_____/  |_|  \_\  \____/  ")

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

presentar_datos_personales()
dibujar_C_3_PO()
esribir_nombre_sw()