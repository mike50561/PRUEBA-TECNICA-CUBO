## prueba técnica de CUBO+ (test.1)
 
## 📚 Descripción de la prueba 
Este repositorio con tiene ejercicio que  consiste en desarrollar un programa en Python que interactúa con la API pública de mempool.space para consultar la información relacionada con la dirección de Bitcoin de la tesorería de El Salvador. 

###El objetivo es obtener y calcular los siguientes datos:
Balance On-Chain: El saldo total confirmado en la blockchain para una dirección específica.

Balance en el Mempool: El saldo que está pendiente de confirmación, es decir, las transacciones que aún no han sido incluidas en un bloque.

Variación del Balance en un Periodo de 30 Días: La diferencia entre el saldo al inicio y al final de los últimos 30 días.

Variación del Balance en un Periodo de 7 Días: Similar al anterior, pero tomando un periodo de 7 días.

## 🤝Resumen de lo Realizado
Obtención de Información a través de la API:

El programa usa la API de mempool.space para obtener datos detallados sobre la dirección de Bitcoin proporcionada.
Se realizan dos solicitudes principales a la API:
-Para obtener los balances confirmados (on-chain) y pendientes (mempool).
-Para consultar todas las transacciones de la dirección y calcular la variación del balance en un periodo específico.

### Cálculos de Balance:
Balance On-Chain: Se obtiene restando el total de bitcoins gastados del total recibido en la dirección.

Balance en el Mempool: Se calcula de manera similar, pero sobre transacciones pendientes de confirmación.

Variación del Balance: Se compara el saldo actual con el saldo de hace 7 o 30 días, considerando únicamente las transacciones confirmadas en ese intervalo.
Formato de Tiempo y Saldos en Satoshis (SATS):

Las fechas se manejan en formato de tiempo Unix (epoch), que es el estándar en Bitcoin.
Los valores de los balances se expresan en Satoshis (SAT), la unidad más pequeña de Bitcoin (1 BTC = 100,000,000 SATS).


## 🛠️Tecnologías Utilizadas
-Python: Lenguaje de programación para el desarrollo 

-visual Studio code: editor de codigo fuente para el desarrollo.

### 🛠️ prueba técnica de CUBO+

[VIDEO]:( https://drive.google.com/file/d/1UTMQ1QsqSWw7X-Mu9W8RZGHKXrgp4BzK/view?usp=sharing )


## 📧 Contacto
-  👨‍💻 Desarrollador: Miguel Angel Herrera
-  📧 Correo electrónico: miguel50561@gmail.com
