# Resolución de Problema de Optimización Lineal

Este código es una implementación de una interfaz gráfica en Python utilizando la biblioteca `tkinter` para resolver un problema de optimización lineal. Utiliza la función `linprog` de la biblioteca `scipy.optimize` para encontrar la solución óptima.

## Requisitos

Para ejecutar este código, asegúrate de tener instaladas las siguientes bibliotecas:

- `scipy` - Puedes instalarlo ejecutando `pip install scipy`.
- `tkinter` - Esta biblioteca generalmente está incluida en la instalación de Python, pero puede requerir instalación adicional según la configuración de tu sistema.

También se proporciona un archivo `requirements.txt` para instalar las dependencias necesarias. Puedes ejecutar el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

# Uso

## Ejecutar

```bash
python3 solved.py
```

Al ejecutar el código, se abrirá una ventana de interfaz gráfica donde puedes ingresar los coeficientes de la función objetivo y las restricciones. A continuación, se describen los pasos para utilizar la interfaz:

1. **Función Objetivo (FO):** Ingresa los coeficientes de la función objetivo en los campos de entrada ubicados en la parte superior de la ventana. Por defecto, se proporcionan dos campos de entrada para dos variables. Puedes ajustar la cantidad de campos según tus necesidades.

2. **Restricciones:** Ingresa los coeficientes de las restricciones y los valores del lado derecho en los campos de entrada correspondientes. Por defecto, se proporcionan dos conjuntos de restricciones, cada uno con dos campos de entrada para dos variables. Puedes ajustar la cantidad de conjuntos de restricciones y campos según tus necesidades.

3. **Tipo de optimización:** Selecciona si deseas maximizar o minimizar la función objetivo marcando la casilla correspondiente.

4. **Resolver:** Haz clic en el botón "Resolver" para calcular la solución óptima del problema de optimización lineal.

5. **Resultado:** El resultado de la optimización se mostrará en la etiqueta de la ventana. Si se encuentra una solución, se mostrarán los valores de las variables óptimas. De lo contrario, se mostrará un mensaje indicando que no se encontró solución.

Asegúrate de proporcionar valores numéricos válidos en los campos de entrada. Ten en cuenta que este código asume un problema de optimización lineal con restricciones lineales y variables continuas.

## Ejemplo

A continuación se presenta un ejemplo de cómo utilizar esta interfaz:

1. **Función Objetivo (FO):** Supongamos que deseamos minimizar la función objetivo `2x + 3y`. Ingresa los coeficientes `2` y `3` en los campos de entrada correspondientes.

2. **Restricciones:** Supongamos que tenemos las siguientes restricciones:

   - Restricción 1: `x + y >= 5`
   - Restricción 2: `2x - y <= 8`

   Ingresa los coeficientes y los valores del lado derecho en los campos de entrada correspondientes.

3. **Tipo de optimización:** Selecciona "Minimizar" como tipo de optimización.

4. **Resolver:** Haz clic en el botón "Resolver".

5. **Resultado:** El resultado de la optimización se mostrará en la etiqueta de la ventana. Por ejemplo, si se encuentra una solución óptima, podría mostrar "Solución: x = 2.0, y = 3.0".

Recuerda que estos valores son solo un ejemplo y puedes ajustarlos según tus necesidades.
