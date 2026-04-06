# Generador de Contraseñas Seguras

## Descripción

Este proyecto es una herramienta desarrollada en Python que permite generar contraseñas seguras de forma aleatoria, en función de la longitud definida por el usuario.

El script utiliza distintos conjuntos de caracteres (letras, números y símbolos) para construir contraseñas con mayor nivel de entropía, reduciendo la probabilidad de ataques por fuerza bruta o patrones predecibles.

---

## Funcionamiento

El programa solicita al usuario la longitud de la contraseña y genera una combinación aleatoria utilizando:

- Letras (mayúsculas y minúsculas)
- Números
- Caracteres especiales

La generación se realiza mediante selección aleatoria de caracteres en cada iteración hasta alcanzar la longitud indicada.

---

## Tecnologías utilizadas

- Python 3
- Librerías estándar:
  - `string`
  - `random`

---
