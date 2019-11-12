# pip --> gestor de paquetes y modulos para python.
#pip --version
# pip -list --> para ver modulos que hay installados

import camelcase  # pip install camelcase  en consola para instalarlo

camel = camelcase.CamelCase()  # nombremodulo.nombreclase()

texto = "hola soy anggie"

print(camel.hump(texto))

# pip uninstall nombrepaqute
