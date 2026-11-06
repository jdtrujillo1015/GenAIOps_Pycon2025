# Calificación manual del holdout

Califica sin mirar MLflow ni las notas del juez. Las respuestas están en orden aleatorio y no dicen de qué configuración salen. Escribe `si` o `no` después de cada campo.

- **correctness:** ¿la respuesta coincide con la respuesta esperada? Mismo criterio de la Parte 5: no exige las mismas palabras, sí los mismos datos.
- **groundedness:** ¿todo lo que afirma la respuesta está en el contexto recuperado? Si agrega un dato que no aparece, es `no`.

**Reglas fijadas antes de calificar** (se aplican igual a todas las respuestas):

- **Pregunta de línea base y meta (homicidio y percepción):** si la respuesta trae bien las cuatro cifras (línea base y meta de homicidio y de percepción), cuenta como correcta aunque no mencione la dependencia responsable, porque la pregunta no la pide.
- **Datos adicionales:** en correctness, agregar información correcta que la pregunta no pide no la vuelve incorrecta; omitir un dato central de la respuesta esperada, sí. En groundedness, cualquier dato agregado que no esté en el contexto recuperado es `no`.

calificador: Juan David Trujillo

---

## Respuesta 1 (directa)

<!-- trace_id: tr-e9cac1d6f330bdeabe8702a0015bb91c -->

**Pregunta:** ¿Cómo regulan La Terraza y Los Triana la violencia intrafamiliar en las comunas Santa Cruz, Manrique y Aranjuez?

**Respuesta esperada:** Mediante la mediación en casos de violencia intrafamiliar, con multas desde $400.000, que se incrementan de forma arbitraria si el agresor tiene mayor capacidad económica, y con amenazas si no se cumple el pago.

*Fuente:* Diagnóstico para la política pública, p. 91 (tabla "Regulación de la violencia intrafamiliar por parte de estructuras criminales en los territorios")

**Respuesta del bot:**

En las comunas **Santa Cruz, Manrique y Aranjuez**, las estructuras criminales denominadas **La Terraza** y **Los Triana** regulan la violencia intrafamiliar mediante:

- **Mediación** de los casos de violencia intrafamiliar.  
- Imposición de **multas o sanciones económicas** a partir de **$400.000**, con un **incremento arbitrario** si el agresor tiene mayor capacidad económica.  
- **Amenazas** de represalias en caso de incumplimiento del pago.

> “Mediación en casos de violencia intrafamiliar. Desde $400.000 (incremento arbitrario si el agresor tiene mayor capacidad económica). Amenazas por incumplimiento en el pago.”  

No se encontró información adicional sobre otras medidas aplicadas por estas estructuras en los territorios mencionados.

correctness: si

groundedness: si

<details><summary>Ver contexto recuperado</summary>

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 91)**

```text
Tabla XX. Regulación de la violencia Intrafamiliar por parte de estructuras criminales en 
los territorios
Comunas  /  
Sectores
Estructuras 
criminales 
Modalidad  de  
control
Multas  /  
sanciones 
económicas
Otras  medidas  
aplicadas
2- Santa Cruz, 3 –  
Manrique  y  4  –
Aranjuez. 
La Terraza.
Los Triana.
Mediación  en  
casos de violencia 
intrafamiliar.
Desde $400.000 
(incremento 
arbitrario  si  el  
agresor  tiene  
mayor 
capacidad 
económica).
Amenazas  por  
incumplimiento  en  
el pago.
```

**PISCC 2024-2027 (posición de página 180)**

```text
atender   violencia basada en género. 
4. Grupos delincuenciales como regularizadores de la violencia 
intrafamiliar en el territorio, lo que permite el aumento de las 
rentas criminales. 
5. Desplazamiento de las víctimas como medida de autocuidado. 
Violencia intrafamiliar en general
Violencia intrafamiliar contra las mujeres
Causas
Causas
Efectos
Efectos
Tabla 26 Resumen explicativo de la violencia intrafamiliar en Medellín
180
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 19)**

```text
lesionados en los barrios La Pradera, Los Alcázares, El Socorro y El Danubio, según policía 
judicial consultada por el SISC.
Por otro lado, además de las confrontaciones externas entre estructuras, se han presentado 
varias disputas internas, las cuales han dinamizado el homicidio al interior de los territorios 
de injerencia. Si bien prácticamente todos los grupos criminales han tenido un historial de  
confrontaciones al interior de su propia organización, vale la pena resaltar dos de las más
```

**PISCC 2024-2027 (posición de página 198)**

```text
escenarios violentos como mecanismos de resolución del conflicto, situación que 
se relaciona con la priorización de problemáticas de convivencia, relacionadas con 
la agresión y validación del maltrato físico; además de la posible regulación de estas 
confrontaciones por parte de los grupos delincuenciales que tienen injerencia en 
estas comunas, promoviendo el control de la conductas ciudadanas.
```

</details>

---

## Respuesta 2 (directa)

<!-- trace_id: tr-0c03cede9f1e6791ffff7429928276e8 -->

**Pregunta:** ¿Cuál es la línea base y la meta del cuatrienio para la tasa de homicidio y para la percepción de seguridad en el Plan de Desarrollo 2024-2027?

**Respuesta esperada:** La tasa de homicidio tiene una línea base de 14,24 por 100.000 habitantes (2023) y una meta de 12,82 para el cuatrienio; la percepción de seguridad tiene una línea base de 43 % (2023) y una meta de 50,7 %. Ambos indicadores están a cargo de la Secretaría de Seguridad y Convivencia.

*Fuente:* Plan de Desarrollo 2024-2027, p. 392; la misma tabla está en el PISCC 2024-2027, p. 255

**Respuesta del bot:**

No tengo suficiente información en los documentos proporcionados para indicar la línea base ni la meta del cuatrienio de la tasa de homicidio y de la percepción de seguridad en el Plan de Desarrollo 2024‑2027.

correctness: no

groundedness: no aplica

<details><summary>Ver contexto recuperado</summary>

**PISCC 2024-2027 (posición de página 87)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Mapa 1 Homicidios por comuna y corregimiento. 2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia 
(SISC), con información de SIJIN, CTI e INMLCF
87
El comportamiento del homicidio en el período de tiempo analizado (2019-2023) 
implica tener en consideración tres hipótesis al respecto. En primer lugar, la 
reducción de homicidios asociados a las estructuras criminales no supone que
```

**PISCC 2024-2027 (posición de página 85)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Fuente: Sistema de Información para la Seguridad y la Convivencia 
(SISC), con información de SIJIN, CTI e INMLCF
Gráfica 11 Participación porcentual de cada modalidad dentro del total de 
homicidios. 2019-2023
85
puesto que en homicidios asociados a estructuras criminales suelen emplearse más 
armas de fuego, mientras que homicidios por convivencia, violencia intrafamiliar
```

**PISCC 2024-2027 (posición de página 9)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Participación porcentual de cada caracterización dentro del total  
de homicidios categorizados. 2019-2023.
Participación porcentual de cada modalidad dentro del total de  
homicidios. 2019-2023. 
Variación anual promedio en los homicidios por comuna y 
corregimiento. 2019-2023. 
Número de presuntos feminicidios y variación porcentual con   
respecto al año anterior en Medellín, 2019-2023.
```

**PISCC 2024-2027 (posición de página 81)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Gráfica 7 Homicidios por caracterización y rango etario de la víctima. 2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia
(SISC), con información de SIJIN, CTI e INMLCF
81
violencia de género afectan principalmente a las mujeres   jóvenes y adultas (29 
a 59 años). También se observa cómo los adolescentes son más propensos a 
ser víctimas de homicidios asociados a las estructuras criminales y a la violencia
```

</details>

---

## Respuesta 3 (directa)

<!-- trace_id: tr-913baef02352d2ba0662fa6e9242bdad -->

**Pregunta:** ¿Qué dificultades enfrenta la población desplazada que llega a Medellín, según el PISCC?

**Respuesta esperada:** Además del desplazamiento intraurbano, Medellín es uno de los principales receptores de población desplazada, que enfrenta impactos psicosociales por el cambio de entornos rurales a urbanos: dificultades para conseguir alimentos, un techo digno, acceso a servicios públicos, trabajo y dinero, sumadas a la sensación de desarraigo de no tener un lugar propio.

*Fuente:* PISCC 2024-2027, p. 185

**Respuesta del bot:**

Según el **Plan Integral de Seguridad y Convivencia Ciudadana (PISCC) 2024‑2027**, la población desplazada que llega a Medellín enfrenta varias dificultades:

- **Violencia y coerción ejercida por estructuras criminales**:  
  “las estructuras criminales son los mayores causantes de desplazamientos forzado intraurbano… bajo una lógica de control territorial para la extracción de recursos económicos o humanos” (PISCC).  
  Esta dinámica “afecta el ejercicio de los derechos, del liderazgo político y comunitario, el tejido social y la seguridad de las personas” (PISCC).

- **Amenazas, extorsiones y pérdida de derechos**:  
  “el desplazamiento se ancló a los contextos de violencia y coerción específicos de las estructuras criminales y se antecedió, recurrentemente, de amenazas y extorsiones” (PISCC).

- **Débil articulación institucional y subregistro de la información**:  
  “existen dificultades para el seguimiento cuantitativo del fenómeno dado que no se cuenta con la suficiente articulación entre los sectores competentes para la atención –salud, protección y justicia‑ y porque persisten subregistros de la información” (PISCC).

- **Baja cantidad de denuncias**:  
  En la tabla de diagnóstico se señala “Baja cantidad de denuncias por desplazamiento forzado” (PISCC).

- **Factores de vulnerabilidad que aumentan la exposición al desplazamiento**:  
  Se identifican ocho patrones de mayor propensión a ser desplazados, entre ellos “ser parte de un grupo poblacional de especial protección”, “residencia en zonas donde se producen disputas o enfrentamientos frecuentes” y “control de grupos armados en diferentes ámbitos de la vida comunitaria” (PISCC).

En conjunto, estas condiciones generan un entorno de inseguridad, limitan el acceso a servicios básicos y dificultan la integración y la protección de los desplazados que llegan a la ciudad.

correctness: no

groundedness: no

<details><summary>Ver contexto recuperado</summary>

**PISCC 2024-2027 (posición de página 184)**

```text
Tabla de contenido6. Diagnóstico
Gráfica 51 Número de reportes por desplazamiento forzado en Medellín por año, 
2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC), con información del 
Equipo para la Atención y Reparación de las Víctimas del Conflicto Armado (EARV).
184
Según la fuente de información señalada anteriormente, las comunas de Medellín 
donde más se reportaron casos de desplazamiento forzado, durante 2019 a 2023,
fue 13 – San Javier (459), 8 – Villa Hermosa (308), 60 – San Cristóbal (262), 1 – 
Popular (229), y 7 – Robledo (225); solo estas cinco comunas de la ciudad agrupan 
el 54,74% del total de hechos victimizantes por desplazamiento forzado en los que 
se cuenta con el dato del territorio de ocurrencia. Asimismo, en coherencia con 
el dato general, todas las comunas y los corregimientos de Medellín presentaron 
disminución en la variación porcentual de los registros de casos en el periodo
analizado, excepto el corregimiento 90 – Santa Elena y la comuna 4 – Aranjuez; el 
primero pasó de 4 a 10 casos (150% de aumento) y la segunda de 19 a 22 hechos 
(15,79%).
```

**PISCC 2024-2027 (posición de página 284)**

```text
Tabla de contenido12. Referencias
284
https://www.un.org/es/coronavirus/what-is-domestic-abuse.
Organización de las Naciones Unidas. (2015). The World´s Women 2015 Trends 
and Statistcs. In IEEE Transactions on Magnetics (Vol. 15, Issue 8). https://doi.
org/10.1109/TMAG.1978.1059915.
Organización Internacional para las Migraciones (OIM). (2021). Guía para la 
identificación y asistencia a víctimas de trata de personas en Colombia dirigida a
líderes, lideresas y representantes de organizaciones sociales. https://repository.
iom.int/handle/20.500.11788/2330
Organización Mundial de la Salud (OMS) (2022). Maltrato de las personas 
mayores. https://www.who.int/es/news-room/fact-sheets/detail/abuse-of-older-
people
Painter, M., & Pierre, J. (2005). Challenges to state policy capacity: Global trends 
and com parative perspectives. London: Palgrave Macmillan.
Personería de Medellín (9 de febrero de 2023). El desplazamiento forzado
intraurbano en Medellín aumentó 280% en enero 2023 con respecto al 
2022. Personería de Medellín. https://www.personeriamedellin.gov.co/el-
desplazamiento-forzado-intraurbano-en-medellin-aumento-280-en-enero-2023-
con-respecto-al-2022/.
Plataforma Regional de Coordinación Interagencial (R4V). (2023). Análisis de 
las Necesidades de Refugiados y Migrantes (RMNA). https://www.r4v.info/es/
document/rmna-2023-analisis-de-necesidades
PNUD - Programa de las Naciones Unidas para el Desarrollo (2009). Manual
de Planificación, Seguimiento y Evaluación de los Resultados de Desarrollo. 
Recuperado de:http://web.undp.org/evaluation/handbook/spanish/documents/
manual_completo.pdf  
Policía Nacional de Colombia (s.f.) Modelo de planeación y gestión operacional 
del Servicio de Policía. Bogotá: Direccionamiento Integral Operativo para la 
Reducción del Delito (DIORE).
Prieto, C. (2013). Las Bacrim y el crimen organizado en Colombia. Policy paper 47. 
Friedrich Ebert Stiftung.
Friedrich Ebert Stiftung.
Proyecto de Acuerdo [Concejo de Medellín]. Por el cual se adopta el Plan de 
Desarrolla 2024-2027 “Medellín Te Quiere”.
Putnam, R. D. (1993). The prosperous community. The american prospect, 4(13), 
35-42.
Restrepo, J. (2015). Las vueltas de la oficina de envigado. Medellín: Icono.
Rojas Aravena, F; Solís, L. (2008). El crimen organizado en América Latina y El 
Caribe. Santiago: FLACSO.
Rojas, D., y Echavarría, A. (2022). El diseño del seguimiento de las políticas
```

**PISCC 2024-2027 (posición de página 206)**

```text
Tabla de contenido6. Diagnóstico
Mapa 15 Número de llamadas reportando basuras por comuna y corregimiento, 
2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC) 
con información del Número Único de Seguridad y Emergencias 123. 
206
En conclusión, Medellín enfrenta una serie de desafíos en términos de convivencia 
que surgen de la combinación de factores sociales, económicos, culturales y 
ambientales que influyen en la dinámica cotidiana de sus habitantes. Ahora bien,
las dinámicas descritas que afectan la convivencia deben tener en consideración 
dos hipótesis para revisión, la primera es el ejercicio de control por parte de las 
estructuras criminales como consecuencia de la debilidad de otras alternativas de
```

**Plan de Desarrollo Distrital 2024-2027 (posición de página 9)**

```text
385
o solicitar dinero por su liberación, moda-
lidad conocida como secuestro exprés.
- Tráfico de estupefacientes
El tráfico de estupefacientes fue otra de
las principales rentas criminales de los
grupos delincuenciales presentes en el
distrito de Medellín. Se relaciona de ma-
nera transversal con otras problemáticas,
tales como el uso de niñas, niños y ado-
lescentes para la comisión de delitos, la
instrumentalización de población históri-
camente vulnerada, el homicidio asociado
camente vulnerada, el homicidio asociado
al control territorial para la expansión de la
renta criminal y la salud pública.
En el número único de seguridad y emer-
gencias (NUSE) 123, en 2023, se
atendieron 8224 llamadas en las que se
reportaron sitios de expendio y/o consumo
de narcóticos que representaron un pro-
medio mensual de 685 llamadas.
- Instrumentalización de niñas, ni-
ños y adolescentes
Por otro lado, la instrumentalización de ni-
ñas, niños, adolescentes y jóvenes en el
ñas, niños, adolescentes y jóvenes en el
Distrito se constituyó como una violación
a los derechos humanos de esta población
con protección constitucional reforzada. El
fenómeno se dio a partir del aprovecha-
miento por parte de las estructuras
criminales de condiciones de vulnerabili-
dad asociadas a la situación
socioeconómica, pertenencia étnica (es-
pecialmente niñez y adolescencia
indígena), estatus migratorio, vida en ca-
lle, deserción escolar, consumo
problemático de estupefacientes, entre
problemático de estupefacientes, entre
otras. En 2023 se presentaron solamente
14 denuncias por delitos relacionados con
la instrumentalización de esta población,
mientras que 477 menores de edad fueron
aprehendidos por cometer conductas de-
lictivas.
Relacionado con los riesgos de la instru-
mentalización por parte de grupos
delincuenciales, se encontró el homicidio
de jóvenes entre los 14 y 28 años, los cua-
les constituyeron el 37.3 % de las víctimas
totales de la violencia letal durante 2023,
totales de la violencia letal durante 2023,
equivalente a 141 hechos.
- Loteo o invasión ilegal de predios
El fenómeno del loteo o invasión ilegal de
predios se constituyó en una problemática
enmarcada, también, dentro de las rentas
criminales de las estructuras delincuencia-
les que tienen injerencia en el Distrito. El
delito tuvo una estrecha vinculación con
graves violaciones a los derechos de la
población en Medellín, tales como el des-
plazamiento forzado y el despojo y/o
plazamiento forzado y el despojo y/o
abandono forzado de inmuebles.
- Desplazamiento forzado
Medellín ha sido, de manera histórica, re-
ceptora de población desplazada por el
conflicto armado interno y fenómenos de
violencia en municipios del departamento
de Antioquia y regiones próximas. Asi-
mismo, los grupos delincuenciales de la
ciudad replicaron formas de operar simila-
res al expulsar de sus lugares de
residencia a sectores de la población, es
decir, el desplazamiento se ancló a los
decir, el desplazamiento se ancló a los
contextos de violencia y coerción específi-
cos de las estructuras criminales y se
antecedió, recurrentemente, de amenazas
y extorsiones.
Vale la pena aclarar que cuando un grupo
familiar es desplazado dentro de las fron-
teras de la misma ciudad, se identifica
como desplazamiento forzado intraur-
bano, reconocido por la Sentencia T-268
ESTRUCTURA ESTRATÉGICA PLAN DE DESARROLLO DISTRITAL 
Plan de Desarrollo Medellín Te Quiere 2024-2027
PILAR 3
```

**PISCC 2024-2027 (posición de página 186)**

```text
Tabla de contenido6. Diagnóstico
Problemática
1. Método de control 
territorial y de rentas.
3. Bajo nivel de 
gobernabilidad 
de Estado y sus 
instituciones en los 
territorios controlados.
2. Instrumento de 
invasión a otros 
territorios.
1. Optimización de rentas criminales por parte de las estructuras 
delictivas.
2. Disminución de delitos de tasa de violencia en delitos 
de mayor impacto como el homicidio, permitiendo pasar 
desapercibido a las estructuras criminales.
desapercibido a las estructuras criminales.
3. Debilitamiento del tejido social y comunitario del sector 
controlado. 
4. Baja cantidad de denuncias por desplazamiento forzado.
1. Participación, dominio y captación de espacios de liderazgo 
público y comunitario por parte de estructuras criminales.
2. Captación de recursos públicos. 
3. Cooptación de funciones de seguridad, convivencia y 
administración y de justicia por parte de los grupos delictivos 
organizados.
organizados.
4. Aumento de la materialización de otras prácticas delictivas 
por parte de la criminalidad, sin que estas sean denunciadas por 
parte de la ciudadanía.
1. Aumento de las rentas criminales de las estructuras criminales.
2. Aumento de otros delitos durante enfrentamiento entre 
bandos.
3. Modificación en la forma de funcionar internamente los grupos 
delictivos organizados (alianzas horizontales).
4. Afectación de los derechos de la población civil que reside
durante el lugar de los enfrentamientos.
Fenómeno del desplazamiento forzado por 
estructuras criminales.
Causas Efectos
Tabla 27 Resumen explicativo de desplazamiento forzado en Medellín
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC)
186
Por último, se presenta la tabla 27 que expone un resumen explicativo del fenómeno 
de desplazamiento forzado en Medellín, a partir de las causas y los efectos de esta 
violación a los derechos humanos.
```

**PISCC 2024-2027 (posición de página 192)**

```text
Tabla de contenido6. Diagnóstico
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC)
Mapa 11 Denuncias por desaparición forzada, 2019-2023
192
En el periodo analizado, en todas las comunas de Medellín se registraron casos de 
desaparición forzada. La comuna en la que más se registraron fue 10 – La Candelaria 
con 127, el dato puede corresponder a que es un punto central y de concentración 
de diferentes dinámicas. Le sigue la comuna 5 – Castilla con 73, la comuna 6 – Doce
de Octubre con 43 y la comuna 16 – Belén con 35. Ver mapa a continuación.
```

**PISCC 2024-2027 (posición de página 158)**

```text
Tabla de contenido6. Diagnóstico
Fuente: ICBF, 2021, pág. 19
Tabla 24 Tipos penales asociados a la ESCNNA
Artículo 141
Artículo 213
Artículo 217A
Artículo 141B
Artículo 214
Artículo 141A
Artículo 213 A
Artículo 188A
Artículo 217
Prostitución forzada en persona protegida
Inducción a la prostitución
Demanda de explotación sexual comercial de persona 
menor de 18 años de edad
Trata de personas en persona protegida con fines de 
explotación sexual
Constreñimiento a la prostitución
Constreñimiento a la prostitución
Esclavitud sexual en persona protegida
Proxenetismo con menor de edad
Trata de personas
Estímulo a la prostitución de menores
Artículo 219
Artículo 218
Artículo 219A
Turismo sexual
Pornografía con personas menores de 18 años
Utilización o facilitación de medios de comunicación para 
ofrecer actividades sexuales con persona menor de 18 años.
158
Esta definición debe tener en cuenta que la explotación como las demás violencias
sexuales comporta una importante carga del género, por lo que afecta de manera 
diferenciada a niñas y población LGBTI. (ONU, 2017).
La ESCNNA es central en el diagnóstico actual de seguridad y convivencia en 
Medellín como una grave afectación a los Derechos Humanos y al interés superior 
de la niñez y la adolescencia, a pesar de lo anterior, existen dificultades para el 
seguimiento cuantitativo del fenómeno dado que no se cuenta con la suficiente
articulación entre los sectores competentes para la atención –salud, protección y 
justicia- y porque  persisten subregistros de la información. Esta situación implica 
la necesidad de lecturas eminentemente cualitativas. 
En términos generales, y en coincidencia con lo expuesto por el Instituto colombiano 
de Bienestar Familiar (ICBF) la ESCNNA se encuentra regulada penalmente en por 
lo menos doce (12) tipos, sin embargo, la lista de posibles formas de explotación
se encuentra abierta a la configuración de los actores involucrados y las nuevas 
manifestaciones del delito-.Para efectos de este diagnóstico se considerarán los 
datos de los siguientes artículos del Código Penal:
```

**PISCC 2024-2027 (posición de página 182)**

```text
Tabla de contenido6. Diagnóstico
182
ocurre en razón de la disputa territorio, y no por motivos étnicos, culturales y 
religiosos. Otras causas están asociadas a la violencia políticas generadas por la 
represión estatal, crímenes consumados por agentes estatales o victimizaciones 
provocadas por la acción política de una persona o comunidad (Alcaldía de Medellín, 
2019). Además, tal como se explica en el informe Una nación desplazada (CNMH,
2015), el desplazamiento forzado también ha sido consecuencia del accionar de 
“empresas criminales” por motivos ideológico-políticos, y/o rentísticos.
En Medellín, las estructuras criminales son los mayores causantes de desplazamientos 
forzado intraurbano en el distrito bajo una lógica de control territorial para la 
extracción de recursos económicos o humanos, y en consecuencia, al margen  con 
el conflicto armado nacional (Alcaldía de Medellín, 2019, p. 32).
Con relación a las víctimas, la Alcaldía de Medellín (2019) pudo caracterizar este 
fenómeno, y se identificaron patrones que permiten inferir que algunos grupos 
familiares son más propensos a sufrir esta victimización. Estos factores son: “(1) la 
composición del hogar; (2) ser parte de un grupo poblacional de especial protección, 
(3) el género del jefe del hogar, (4) la actividad económica del jefe del hogar, 
(5) el ejercicio de liderazgo  en los territorios, (6) la residencia en zonas donde se
producen disputas o enfrentamientos frecuentes, (7) el control de grupos armados 
en diferentes ámbitos de la vida comunitaria de un territorio y (8) ser víctima de 
desplazamiento de otro municipio o zona de la ciudad” (Alcaldía de Medellín, 2019, 
p. 33).
Existen múltiples hipótesis explicativas sobre el desplazamiento forzado intraurbano 
en Medellín. Primero, el desplazamiento forzado intraurbano se ha empleado 
por actores armados ilegales como una expresión del control territorial a cargo
de poderes armados ilegales, que se movilizan en favor de la administración de 
las rentas criminales (Alcaldía de Medellín, 2020). Por medio de la violencia o su 
amenaza, estos grupos armados ilegales influyen en el control territorial, económico 
y social que tiene consecuencias en la vida afectiva, familiar y cotidianeidad de las 
personas que residen o laboran en su jurisdicción, afectando el ejercicio de los 
derechos, del liderazgo político y comunitario, el tejido social y la seguridad de las
personas (Alcaldía de Medellín, 2019). 
Segundo, las estructuras armadas que emplean esta estrategia de estabilización y 
control territorial operan bajo una lógica de red para dominar territorios controlados 
por otras bandas antagónicas. Estas redes no operan bajo estructuras verticales, 
sino por medio de alianzas y acuerdos en función de obtener réditos económicos 
y del intercambio de recursos (armamento e información) entre actores legales e
ilegales de distintas naturalezas (Alcaldía de Medellín, 2019). 
Tercero, el desplazamiento forzado es resultado de la ocurrencia de hechos 
(o delitos) que vulneran los derechos a la vida, libertad, integridad y seguridad 
personal, lo que categoriza a este fenómeno como multicausal y heterogéneo. 
Este fenómeno es fruto de hechos vulneradores de derechos fundamentales como:
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 80)**

```text
La violencia intrafamiliar comprende un conjunto de formas de maltrato físico, psicológico y 
sexual en el marco de relaciones familiares. En el caso particular de la forma en que este  
fenómeno opera contra las mujeres, el análisis económico ha demostrado que el consumo 
de alcohol y las rutinas de ocio incrementan la probabilidad de episodios violentos en los  
hogares, por ejemplo, en un estudio sobre las causas de la violencia intrafamiliar en
Medellín  se  identificó  “que  los  hogares  que  reportaron  tomar  licor  hasta  la  ebriedad 
presentan al menos un 6% más de probabilidad de presentar episodios de violencia que  
aquellos que reportaron un consumo moderado de alcohol” (Barrientos, Molina, & Salinas,  
2013, p.107). En lo relativo a las mujeres adultas es significativo considerar el escenario de 
las relaciones de pareja como objeto de este diagnóstico, desde la mirada sociocultural, la
exposición previa a violencia intrafamiliar, las creencias que legitiman la violencia como  
forma de corrección, la proveeduría económica masculina y el entendimiento de la unión de 
pareja para toda la vida, constituyen predictores significativos de agresión física o sexual  
hacia las mujeres por parte de sus parejas (Ariza, 2011; Restrepo, 2023).
En el plano comunitario, residir en barrios con mayor concentración de pobreza eleva el
riesgo de victimización femenina, lo que evidencia el impacto de la desorganización social y 
la tensión económica en la escalada de los conflictos domésticos, según el estudio  La 
violencia en las relaciones de pareja en Medellín y sus representaciones sociales  (Ariza, 
2011), “dadas la sobrecarga laboral y la necesidad de trabajar para la supervivencia, se  
presentan dificultades para mantener ciertos rituales mercantilizados de cortejo como las
citas, los paseos y los obsequios, lo cual produce conflictos, que en ocasiones derivan en  
violencia”  (p.  202).  Por  último,  influyen  factores  situacionales  como  los  procesos  de 
separación, los celos y la coparentalidad.
Por otro lado, la violencia intrafamiliar que afecta de forma central a las niñas, niños y  
adolescentes, se trata de un daño contra una población con alta dependencia de sus  
personas cuidadoras y que, en muchos casos, enfrenta barreras culturales y familiares para
que el maltrato sea identificado como una vulneración de derechos y no como una práctica 
normalizada dentro de la crianza o el ejercicio de autoridad. En particular “esta situación  
pasa desapercibida en la sociedad y en la familia dado que usualmente se considera al  
maltrato físico como un hecho común, propio de la educación del menor [de edad] y reflejo 
de la autoridad de los progenitores” (Arias, 2021). 
Por otro lado, las personas adultas mayores también sufren importantes afectaciones a sus
derechos en el marco de la familia de forma reiterativa. Según la Personería de Medellín
(2020), las causas de violencia contra las personas mayores en la ciudad se encuentran  
asociadas al abandono por factores económicos que influyen en la desatención por parte de 
los familiares que no pueden dejar de trabajar para ser cuidadores y tampoco tienen los  
medios para pagar por un cuidado especializado. Por otro lado, la falta de control y vigilancia
a  los  hogares  gerontológicos  ha  posibilitado  hechos  de  maltrato  y  la  vulneración  de 
derechos de esta población. 
Interamericana sobre la Protección de los Derechos Humanos de las Personas Mayores, adoptada en el seno de 
la OEA en 2015.
```

**PISCC 2024-2027 (posición de página 90)**

```text
Tabla de contenido
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC), con datos de Subcomisión 
de clasificación de feminicidios del Consejo de Seguridad Pública para las Mujeres.
Gráfica 13 Número de presuntos feminicidios y variación porcentual con respecto 
al año anterior en Medellín, 2019-2023 
90
El fenómeno del feminicidio tiene sus raíces en la cultura patriarcal, que se plantea 
como objetivo disciplinar a las mujeres para hacerlas encajar en lo que sería “el deber
ser mujer”, comprendido como una serie de comportamientos que respaldan los 
estereotipos de género. La violencia contra las mujeres en general, y el feminicidio 
como una manifestación particular, es violatoria de los derechos humanos y 
así mismo todo acercamiento debería proponerse en términos estructurales e 
integrales. 
Definir las causas de los feminicidios constituye un desafío metodológico para 
cualquier análisis, toda vez que estos hechos son, en esencia multifacéticos,
multicausales y contextuales, a esto se suma que la Subcomisión de clasificación 
de feminicidios del Consejo de Seguridad Pública para las Mujeres del Distrito 
de Medellín ha transitado por dificultades de articulación interinstitucional que 
representan obstáculos en la definición y adecuada presentación del dato, muestra 
de ello es que a la fecha treinta (30) de los casos sometidos a clasificación entre 
2019 y 2023 carecen de suficiente información para determinar si se trata o no de
feminicidios, y que persisten casos “en análisis” sin que se cuente con actualización 
al respecto.
Una de las principales discusiones acerca de este tema en el país tiene que ver 
con la inclusión de un tipo penal autónomo para la protección de la vida de las 
mujeres frente a crímenes producidos por el hecho de serlo, teniendo en cuenta 
6. Diagnóstico
```

</details>

---

## Respuesta 4 (directa)

<!-- trace_id: tr-a47a954d4a730ebd44fcc86e9754b92f -->

**Pregunta:** ¿Por qué el Diagnóstico considera los procedimientos estéticos clandestinos un riesgo para las mujeres de Medellín?

**Respuesta esperada:** Porque la mala praxis en procedimientos estéticos amenaza su integridad; el Diagnóstico lo relaciona con estereotipos de belleza que, reforzados por las redes sociales y el mundo del espectáculo, generan en algunas mujeres un mandato cultural de buscar ese estándar mediante procedimientos estéticos.

*Fuente:* Diagnóstico para la política pública, p. 88

**Respuesta del bot:**

El Diagnóstico señala que los procedimientos estéticos clandestinos representan un riesgo para las mujeres porque :

- “Una amenaza adicional a la integridad de las mujeres de Medellín se constituye por la mala praxis en procedimientos estéticos…”.  
- Además, “el acceso a este tipo de procedimientos de servicios no regulados, ponen en riesgo la salud, la integridad y, en algunos casos, la vida de quienes se someten a ellos, evidenciando cómo los mandatos de género también se expresan en el campo de la estética corporal”.  

En conjunto, el documento indica que la falta de regulación y la presión de los estereotipos de belleza obligan a algunas mujeres a buscar estos servicios, exponiéndolas a daños físicos graves e incluso a la muerte.

correctness: si

groundedness: no

<details><summary>Ver contexto recuperado</summary>

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 88)**

```text
modo que se reduzcan los impactos negativos de la actividad y se limite el poder de las  
redes criminales que hoy la instrumentalizan.
1.2.3. Procedimientos estéticos irregulares
Una amenaza adicional a la integridad de las mujeres de Medellín se constituye por la mala 
praxis en procedimientos estéticos, al respecto es relevante considerar que la imagen de las 
mujeres de la ciudad ha atravesado diferentes tipos de representación en los dispositivos
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 88)**

```text
culturales; en la última década el grado de exposición corporal y de sexualización se ancla a 
la expansión de las redes sociales y el mundo del espectáculo. Ahora bien, la existencia de 
marcados estereotipos de belleza implica para algunas mujeres un mandato cultural de lo  
considerado deseable conllevando a la búsqueda del estándar a partir de procedimientos  
con fines estéticos. 
Este es un tema de interés teniendo en cuenta que el acceso a este tipo de procedimientos
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 84)**

```text
de servicios no regulados, ponen en riesgo la salud, la integridad y, en algunos casos, la  
vida de quienes se someten a ellos, evidenciando cómo los mandatos de género también se 
expresan en el campo de la estética corporal.
1.2.1. Nuevas formas de la ESCNNA
La  ESCNNA  en  Medellín  ha  adoptado  características  complejas  y  poco  visibles 
relacionadas con el auge del turismo y el entorno digital, las cuales encarnan retos para su
```

**PISCC 2024-2027 (posición de página 90)**

```text
Tabla de contenido
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC), con datos de Subcomisión 
de clasificación de feminicidios del Consejo de Seguridad Pública para las Mujeres.
Gráfica 13 Número de presuntos feminicidios y variación porcentual con respecto 
al año anterior en Medellín, 2019-2023 
90
El fenómeno del feminicidio tiene sus raíces en la cultura patriarcal, que se plantea 
como objetivo disciplinar a las mujeres para hacerlas encajar en lo que sería “el deber
```

</details>

---

## Respuesta 5 (directa)

<!-- trace_id: tr-db57532db8852da75140b3edd27c55ee -->

**Pregunta:** ¿Por qué el Diagnóstico considera los procedimientos estéticos clandestinos un riesgo para las mujeres de Medellín?

**Respuesta esperada:** Porque la mala praxis en procedimientos estéticos amenaza su integridad; el Diagnóstico lo relaciona con estereotipos de belleza que, reforzados por las redes sociales y el mundo del espectáculo, generan en algunas mujeres un mandato cultural de buscar ese estándar mediante procedimientos estéticos.

*Fuente:* Diagnóstico para la política pública, p. 88

**Respuesta del bot:**

El Diagnóstico señala que los procedimientos estéticos clandestinos constituyen un riesgo para las mujeres de Medellín porque:

* **Presión cultural y estereotipos de belleza** – “la imagen de las mujeres de la ciudad ha atravesado diferentes tipos de representación… la existencia de marcados estereotipos de belleza implica… un mandato cultural de lo considerado deseable” que lleva a muchas a buscar estos procedimientos.

* **Acceso limitado por recursos económicos** – “el acceso a este tipo de procedimientos se ve limitado por los recursos económicos, lo que trae consigo riesgos como la exposición a intervenciones por parte de personal no cualificado y en espacios que no cuentan con los requerimientos necesarios”.

* **Prácticas inseguras y falta de regulación** – se describen “el uso de medicamentos y sustancias no aptas… la realización de procedimientos quirúrgicos en espacios no adecuados… la transmisión de infecciones por mala praxis y las intervenciones invasivas por parte de personal sin la formación en cirugía plástica”. Además, “la regulación de la cosmetología en Colombia prohíbe expresamente la realización de actividades reservadas a profesionales de la salud, sin embargo, persisten prácticas informales que ponen en riesgo la vida y la integridad de quienes acceden a estos procedimientos”.

* **Consecuencias mortales y de integridad** – entre 2015 y 2024 se han registrado “22 muertes de mujeres asociadas a procedimientos estéticos irregulares, así como múltiples afectaciones a la integridad personal”.

* **Implicaciones para la seguridad y convivencia** – la ausencia de regulación y controles “profundizan las consecuencias de las prácticas irregulares y acentúan los riesgos derivados de ellas”, generando “clínicas de garaje” donde se realizan procedimientos sin la preparación necesaria.

En conjunto, estos factores hacen que el Diagnóstico considere los procedimientos estéticos clandestinos una amenaza directa a la vida, la salud y la seguridad de las mujeres en la ciudad.

correctness: si

groundedness: si

<details><summary>Ver contexto recuperado</summary>

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 88)**

```text
modo que se reduzcan los impactos negativos de la actividad y se limite el poder de las  
redes criminales que hoy la instrumentalizan.
1.2.3. Procedimientos estéticos irregulares
Una amenaza adicional a la integridad de las mujeres de Medellín se constituye por la mala 
praxis en procedimientos estéticos, al respecto es relevante considerar que la imagen de las 
mujeres de la ciudad ha atravesado diferentes tipos de representación en los dispositivos
culturales; en la última década el grado de exposición corporal y de sexualización se ancla a 
la expansión de las redes sociales y el mundo del espectáculo. Ahora bien, la existencia de 
marcados estereotipos de belleza implica para algunas mujeres un mandato cultural de lo  
considerado deseable conllevando a la búsqueda del estándar a partir de procedimientos  
con fines estéticos. 
Este es un tema de interés teniendo en cuenta que el acceso a este tipo de procedimientos
se ve limitado por los recursos económicos, lo que trae consigo riesgos como la exposición 
a intervenciones por parte de personal no cualificado y en espacios que no cuentan con los 
requerimientos necesarios, constituyéndose en una amenaza para la seguridad de locales y 
visitantes, principalmente extranjeras atraídas por el valor de los procedimientos favorable  
al cambio de moneda (generalmente dólares y euros). Entre 2015 y 2024 se han presentado
en Medellín 22 muertes de mujeres asociadas a procedimientos estéticos irregulares, así  
como múltiples afectaciones a la integridad personal en el mismo contexto. 
Dentro de las principales situaciones irregulares relacionadas en la ciudad se encuentran: el 
uso de medicamentos y sustancias no aptas para la aplicación en seres humanos, la  
realización de procedimientos quirúrgicos en espacios no adecuados como viviendas o
quirófanos clandestinos, la transmisión de infecciones por mala praxis y las intervenciones 
invasivas por parte de personal sin la formación en cirugía plástica (Seccional de Salud de 
Antioquia,  2016), sobre  este  último  punto  cabe  aclarar  que  la  regulación36 de  la  
cosmetología en Colombia prohíbe expresamente la realización de actividades reservadas 
a profesionales de la salud, sin embargo,  persisten prácticas informales que ponen en
riesgo la vida y la integridad de quienes acceden a estos procedimientos como  la práctica  
por parte de personas sin el cumplimiento de requisitos.
Para concluir, cabe mencionar que este problema compete a la gestión de la seguridad y la 
convivencia en la medida en que la ausencia de regulación y la carencia de controles  
efectivos profundizan las consecuencias de las prácticas irregulares y acentúan los riesgos
derivados de ellas, uno de los resultados de este estado de anomia relativa es la existencia 
de  las  llamadas  clínicas  de  garaje,  en  las  cuales  se  realizan  procedimientos  sin  la 
preparación necesaria. Un estudio del año 2023 en la ciudad de Cali concluyó que “ el 
principal  problema  que  hoy  se  debe  afrontar  es  que,  a  pesar  de  existir  normativas 
relacionadas con la práctica de estos procedimientos, falta mayor control y leyes más
estrictas, para no permitir a médicos generales, cirujanos, ginecólogos, enfermeras e  
incluso a personal no médico, realizar estas cirugías, pues ponen en riesgo la vida de los  
36 Artículo 11 de la Ley 711 de 2001
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 84)**

```text
agresor percibe baja probabilidad de intervención inmediata, lo cual facilita la concreción del 
feminicidio.
Teniendo en cuenta lo anterior, el entramado que posibilita la comisión del delito de  
feminicidio en Medellín se encuentra construido sobre factores relacionales, contextuales y 
estructurales que potencian el riesgo para la vida de las mujeres. Lo anterior, es relevante  
para la seguridad y la convivencia desde diferentes ópticas por las repercusiones sociales,
económicas y culturales, uno de los impactos es el identificado por el Banco Interamericano 
de Desarrollo, citado por el Instituto Nacional de Medicina Legal y Ciencias Forenses, quien 
indica que este fenómeno puede “generar pérdidas que oscilan entre el 1,6% y el 4% del  
producto  interno  bruto,  de  acuerdo  con  gastos  de  procesos  jurídicos,  programas  de 
prevención,  promoción,  atención  y  tratamientos  psicoterapéuticos,  además  de
incapacidades temporales o permanentes y el deterioro en la salud física y mental de las  
víctimas” (2023, p. 51).
1.2. Fenómenos emergentes
En los últimos años, Medellín ha sido escenario de la visibilización de nuevas expresiones  
de violencias basadas en género que, si bien no son fenómenos completamente inéditos,  
han adquirido mayor reconocimiento por su magnitud, sus impactos y la forma en que se  
entrelazan  con  nuevas  dinámicas  urbanas  y  tecnológicas.  Entre  ellas,  destaca  la
Explotación Sexual Comercial de Niñas, Niños y Adolescentes (ESCNNA), que combina la 
vulneración de derechos fundamentales con redes de criminalidad organizada y circuitos de 
explotación económica. A este fenómeno se suman las actividades sexuales pagas que, si 
bien no son en sí una manifestación delictiva, en ellas sí persisten prácticas abusivas y  
coercitivas, al igual que facilitan la exposición a riesgos asociados a trata de personas y
violencia física y sexual, especialmente contra las mujeres y personas con orientación  
sexual e identidad de género diversas. 
Por  otra  parte,  el  entorno  digital  ha  abierto  nuevas  rutas  para  la  agresión  mediante 
hostigamiento, difusión no consentida de imágenes íntimas y fraude a través de redes  
sociales o aplicaciones de citas. Finalmente, los procedimientos estéticos irregulares han  
emergido como una forma de violencia que, amparada en ideales de belleza y en la oferta
de servicios no regulados, ponen en riesgo la salud, la integridad y, en algunos casos, la  
vida de quienes se someten a ellos, evidenciando cómo los mandatos de género también se 
expresan en el campo de la estética corporal.
1.2.1. Nuevas formas de la ESCNNA
La  ESCNNA  en  Medellín  ha  adoptado  características  complejas  y  poco  visibles 
relacionadas con el auge del turismo y el entorno digital, las cuales encarnan retos para su
análisis y judicialización. Así, como se relacionó al inicio de este diagnóstico, el turismo en la 
ciudad ha aumentado de manera notable y exponencial en los últimos diez años; sin  
embargo, parte de quienes visitan Medellín la continúan asociando con el imaginario del  
narcotráfico, la percepción de impunidad, la normalización de espacios públicos ligados a  
las actividades sexuales pagas y sus bajas tarifas, lo que ha contribuido al incremento de
```

**PISCC 2024-2027 (posición de página 90)**

```text
Tabla de contenido
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC), con datos de Subcomisión 
de clasificación de feminicidios del Consejo de Seguridad Pública para las Mujeres.
Gráfica 13 Número de presuntos feminicidios y variación porcentual con respecto 
al año anterior en Medellín, 2019-2023 
90
El fenómeno del feminicidio tiene sus raíces en la cultura patriarcal, que se plantea 
como objetivo disciplinar a las mujeres para hacerlas encajar en lo que sería “el deber
ser mujer”, comprendido como una serie de comportamientos que respaldan los 
estereotipos de género. La violencia contra las mujeres en general, y el feminicidio 
como una manifestación particular, es violatoria de los derechos humanos y 
así mismo todo acercamiento debería proponerse en términos estructurales e 
integrales. 
Definir las causas de los feminicidios constituye un desafío metodológico para 
cualquier análisis, toda vez que estos hechos son, en esencia multifacéticos,
multicausales y contextuales, a esto se suma que la Subcomisión de clasificación 
de feminicidios del Consejo de Seguridad Pública para las Mujeres del Distrito 
de Medellín ha transitado por dificultades de articulación interinstitucional que 
representan obstáculos en la definición y adecuada presentación del dato, muestra 
de ello es que a la fecha treinta (30) de los casos sometidos a clasificación entre 
2019 y 2023 carecen de suficiente información para determinar si se trata o no de
feminicidios, y que persisten casos “en análisis” sin que se cuente con actualización 
al respecto.
Una de las principales discusiones acerca de este tema en el país tiene que ver 
con la inclusión de un tipo penal autónomo para la protección de la vida de las 
mujeres frente a crímenes producidos por el hecho de serlo, teniendo en cuenta 
6. Diagnóstico
```

**PISCC 2024-2027 (posición de página 146)**

```text
Tabla de contenido6. Diagnóstico
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC), 
con información de la Secretaría de Salud – SIVIGILA. Información preliminar
Gráfica 34 Número de registros de violencias sexuales en Medellín por año, 2019 
– 2023
146
De acuerdo con la información del periodo analizado (2019-2023), a partir de 2020 
se presenta un aumento lineal del número de registros. Ahora bien, en el año 2021,
comparado con 2020, se presenta un incremento de 675 registros por violencias 
sexuales, lo que equivale a un 25,6% de variación porcentual; en cuanto al año 
2022, la variación porcentual fue la mayor registrada en el periodo analizado con un 
37,9% comparado con el 2021, es decir, se registraron 1.254 casos más, finalmente, 
en el año 2023, aunque la tendencia creciente se sostiene, la variación porcentual 
es la más baja con un 7%, es decir 319 registros más que al año anterior. Esto último
puede deberse a que la base de datos aún no ha cerrado para 2023.
Igualmente, poder entender cómo afectan las violencias sexuales a la población 
del Distrito de Medellín desde el enfoque de género, es determinante para 
comprender la manera en que se comporta este fenómeno de manera diferencial. 
En el siguiente gráfico, y continuando con las cifras reportadas por la Secretaría de 
Salud (SIVIGILA), se evidencia que las mujeres tienen mayor afectación por esta
vulneración, representando el 83,5% del total de registros del periodo analizado, 
lo que corresponde a que esta población presentó 15.703 víctimas entre 2019 y 
2023.
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 77)**

```text
Durante  la  última  década,  las  violencias  basadas  en  género  en  Medellín  se  han 
caracterizado por una persistencia estructural que trasciende coyunturas, más allá de los  
episodios  individuales,  estas  violencias  se  han  entrelazado  con  dinámicas  sociales 
históricas de la ciudad: relaciones de poder desiguales, patrones culturales que normalizan 
el control sobre las mujeres y personas con orientaciones o identidades de género diversas,
y un contexto urbano donde las violencias privadas y públicas se retroalimentan. En este  
escenario, la violencia se proyecta hacia el trabajo, la educación, el transporte y la vida  
comunitaria, adoptando formas físicas, psicológicas, económicas y simbólicas.
En términos de su relación con la seguridad y la convivencia, estas violencias han mostrado 
un vínculo estrecho con los ecosistemas de criminalidad y control territorial. En algunos
barrios, las estructuras armadas ilegales operan como reguladores de la vida social, lo que 
condiciona la denuncia y la protección de las víctimas. Esta intersección entre violencia de 
género y orden social impuesto genera un efecto doble: por un lado, invisibiliza ciertos casos 
al  mantenerlos  fuera  del  alcance  institucional;  por  el  otro,  expone  a  las  víctimas  a 
represalias o negociaciones informales que no garantizan sus derechos. Así, el fenómeno
no puede entenderse solo como un problema interpersonal, sino como un síntoma de  
sistemas de dominación más amplios.
Otro rasgo distintivo ha sido la coexistencia de avances normativos y programáticos con  
barreras prácticas para la garantía de derechos. Medellín ha fortalecido sus rutas de  
atención y prevención, pero su eficacia se ve afectada por la fragmentación institucional, la 
saturación de los servicios y la dificultad para llegar a territorios donde la autoridad del
Estado es disputada por las estructuras criminales. Además, persisten narrativas culturales 
que responsabilizan a las víctimas o minimizan las agresiones, lo que ralentiza los cambios 
en la percepción social. En conjunto, esto configura un panorama en el que las violencias  
basadas en género se presentan como un fenómeno profundamente enraizado en la  
estructura social y en las tensiones propias de una ciudad atravesada por desigualdades  
históricas.
históricas.
Este apartado aborda en primer lugar las violencias basadas en género contra las mujeres, 
iniciando con aquellas que, aunque han permanecido en el tiempo, han adoptado nuevas  
manifestaciones en la ciudad, como la violencia intrafamiliar, las violencias sexuales y el  
feminicidio. Posteriormente, se examinan fenómenos emergentes, entre ellos la explotación 
sexual comercial de niñas, niños y adolescentes, las actividades sexuales pagas y su
relación con la vulneración de derechos humanos y los procedimientos estéticos irregulares. 
Finalmente,  se  analiza  la  relación  entre  estas  violencias  y  el  crimen  organizado, 
considerando sus implicaciones en la seguridad y la convivencia.
En segundo momento, se ofrece un panorama general de las violencias motivadas por la  
orientación  sexual  y  la  identidad  de  género.  Se  cierra  con  la  identificación  de
manifestaciones actuales de este tipo de agresiones, observadas en dinámicas recientes  
como el hurto mediante redes sociales o aplicaciones de citas, que reflejan la adaptación de 
las violencias a nuevos entornos y tecnologías.
En conjunto, ambos segmentos permiten comprender no solo la diversidad y evolución de  
las violencias basadas en género en Medellín, sino también las interconexiones entre
```

</details>

---

## Respuesta 6 (directa)

<!-- trace_id: tr-7dee5486fb2f140bb429acb1526433aa -->

**Pregunta:** ¿Qué función cumple el Comité Territorial de Orden Público (CTOP) frente al PISCC y los recursos del FONSET?

**Respuesta esperada:** Es el escenario directivo dispuesto por ley para tomar decisiones sobre la implementación y el seguimiento del PISCC y sobre la destinación de los recursos del Fondo Territorial de Seguridad (FONSET). Allí se discuten y aprueban los proyectos FONSET de los organismos de seguridad y justicia, que deben estar alineados con el componente estratégico del PISCC y su plan de acción, y se presentan informes periódicos de seguimiento y evaluación del PISCC.

*Fuente:* PISCC 2024-2027, sección 10. Escenarios, p. 265

**Respuesta del bot:**

El **Comité Territorial de Orden Público (CTOP)** constituye el escenario directivo dispuesto por la ley para la toma de decisiones relacionadas con la **implementación y el seguimiento del PISCC**, así como para la **destinación de los recursos del Fondo Territorial de Seguridad (FONSET)**. En este espacio se **discuten y aprueban los proyectos FONSET** presentados por los organismos de seguridad y justicia, garantizando la articulación entre los distintos instrumentos de planeación de la seguridad y la convivencia a nivel nacional, departamental, metropolitano y distrital.

> “Este es el escenario directivo dispuesto por ley para la toma de decisiones relacionadas con el proceso de implementación y seguimiento del PISCC, así como la destinación de los recursos del Fondo Territorial de Seguridad (FONSET). En este contexto, se discuten y aprueban los proyectos FONSET…”  

Además, el CTOP actúa como garante de la coordinación interinstitucional y genera los entregables necesarios para el control y la rendición de cuentas:

> “Periodicidad: Cuatro veces al año de acuerdo con lo dispuesto por la ley y sesiones extraordinarias a demanda.  
> Evidencias / entregables: Listados de asistencia, actas, presentaciones y fotografías.”  

En síntesis, la función del CTOP es **coordinar, articular y decidir sobre la ejecución del PISCC y la asignación de los recursos FONSET**, asegurando la participación de los actores corresponsables y la generación de evidencia documental del proceso.

correctness: si

groundedness: si

<details><summary>Ver contexto recuperado</summary>

**PISCC 2024-2027 (posición de página 7)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
10. Escenarios 
10.1.  Comité Territorial de Orden Público -CTOP- 
10.2. Escenarios para la coordinación y la articulación de los actores  
    corresponsables del PISCC  
10.3. Mesas técnicas de proyectos FONSET 
10.4. Espacios de interacción y gobernanza interinstitucional
11. Sistema de Evaluación del PISCC 
11.1.   Evaluación de Procesos 
11.2.  Evaluación de Resultados 
11.3.  Evaluación de Impacto
12. Referencias
266
266
267
267
268
270
271
12. Referencias
266
266
267
267
268
270
271
272
272
274
 
31
39
44
48
51
73
77
88
92
105
107
108
112
115
117
123
129
133
139
142
143
149
157
158
170
180
Tabla 1   
Tabla 2   
Tabla 3   
Tabla 4  
Tabla 5  
Tabla 6  
Tabla 7   
Tabla 8  
Tabla 9   
Tabla 10  
Tabla 11   
Tabla 12
Tabla 13
Tabla 14  
Tabla 15  
Tabla 16  
Tabla 17  
Tabla 18  
Tabla 19
  
Tabla 20
Tabla 21
  
Tabla 22
Tabla 23
Tabla 24
Tabla 25
Tabla 26
Marco normativo.
ODS y alienación con el PISCC.
Marco de instrumentos de planeación.
Marco de instrumentos de planeación.
Principales elementos estructurales de los PISCC de Medellín
(2012-2020).
Problemas estructurales priorizados 2012-2020.
GDO y territorios.
Resumen explicativo crimen organizado.
Resumen explicativo del homicidio en Medellín.
Resumen explicativo del feminicidio.
Otras conductas y modalidades de hurto en Medellín.
Resumen explicativo del hurto en Medellín.
Artículos de la Ley 1273 sobre ciberdelitos.
Resumen explicativo del Ciberdelito en Medellín.
Resumen explicativo del Ciberdelito en Medellín.
Prácticas violentas y derechos vulnerados.
Resumen explicativo de la extorsión en Medellín.
Resumen explicativo del Secuestro en Medellín.
Resumen explicativo tráfico de estupefacientes en Medellín.
Marco conceptual reclutamiento, uso y utilización.
Resumen explicativo de instrumentalización, reclutamiento, uso y 
utilización de niños, niñas y adolescentes en Medellín.
Comunas y corregimientos con problemáticas de loteo y 
construcción ilegal.
construcción ilegal.
Resumen explicativo del fenómeno de loteo y construcción ilegal 
en la ciudad de Medellín.
Resumen explicativo de violencias sexuales en Medellín.
Resumen explicativo de la trata de personas en Medellín.
Tipos penales asociados a la ESCNNA.
Resumen explicativo de la explotación sexual en Medellín.
Resumen explicativo de la violencia intrafamiliar en Medellín.
Tablas
```

**PISCC 2024-2027 (posición de página 262)**

```text
Tabla de contenido9. Sistema de implementación, seguimiento y evaluación
Evaluación del PISCC
Gráfica 67 Sistema de implementación, seguimiento y evaluación del PISCC
Instrumentos Escenarios
Política Pública de Seguridad y Convivencia
Plan de accción del PISCC
Planes Locales de Seguridad, Convivencia y 
Justicia cercana al ciudadano (PLSCJ)
Comité Territorial de Orden Público
Escenarios para la coordinación y la articulación 
de los actores corresponsables del PISCC
Mesas técnicas de proyectos FONSET
Mesas técnicas de proyectos FONSET
Espacios de interacción y gobernanza 
interinstitucional
Fuente: Elaboración propia 
262
Instrumentos 
Plan de acción del PISCC
Es un instrumento que permite operacionalizar el componente estratégico del PISCC 
en clave de acciones e indicadores concretos que ejecutarán los organismos de 
seguridad y de justicia y las dependencias que integran la Secretaría de Seguridad 
y Convivencia en el marco del proceso de implementación del PISCC.
La construcción de este instrumento se realizó de manera participativa con 
todos los actores corresponsables involucrados, logrando que tanto las acciones 
como indicadores sean coherentes con la misionalidad de cada uno de ellos, que 
respondan a los fenómenos de seguridad y convivencia identificados y priorizados 
en el diagnóstico, y que su cumplimiento se pueda dar en el tiempo establecido 
para este PISCC respondiendo a una visión compartida de ciudad. Es importante
señalar que este ejercicio es una construcción colectiva que se realizará de manera 
anual, ello teniendo en cuenta los cambios que puedan generarse en el proceso 
de priorización y comportamiento de las problemáticas en la ciudad, así como la 
actualización que en materia operativa y de planeación se da año a año desde el 
nivel central para cada uno de los organismos de seguridad y justicia que operan 
en la ciudad. 
En el marco de este proceso de construcción y con el ánimo de diseñar un
instrumento riguroso y técnico que recogiese las lecciones aprendidas de planes 
de acción previos, la Secretaría de Seguridad y Convivencia en conjunto con sus 
dependencias y los organismos de seguridad y justicia elaboró fichas metodológicas
```

**PISCC 2024-2027 (posición de página 19)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
19
19
tecnológicos, entre otros, dedicados a la mitigación del impacto de los fenómenos 
que afectan la seguridad y la convivencia, mejorando las condiciones sociopolíticas 
y socioeconómicas de la población de la ciudad.
El PISCC 2024-2027 se constituye como un esfuerzo mancomunado entre los 
distintos actores encargados de la gestión de la seguridad, la convivencia y el
acceso a la justicia en el distrito, esfuerzo que hoy presenta una visión nuevamente 
compartida de ciudad relacionada con un abordaje que sobresalta la unión de 
voluntades para que desde la integralidad de los asuntos asociados a la seguridad 
y la convivencia se formulen estrategias basadas en  la  gobernanza territorial para 
la intervención de problemáticas complejas y de orden multicausal como las que 
son analizadas en el diagnóstico de este documento.
Sumado a ello, este PISCC  2024-2027 recoge distintas lecciones aprendidas y 
buenas prácticas en clave de instrumentos de planeación de la seguridad, siendo 
el punto de partida un análisis retrospectivo en clave del diseño, implementación, 
seguimiento y evaluación de los distintos PISCC con los que ha contado la ciudad. 
Así, este instrumento plantea mejoras en clave de la presentación y construcción de 
un diagnóstico que transite de lo descriptivo a la identificación de los mecanismos
causales asociados a la ocurrencia de las problemáticas de seguridad y convivencia, 
ello desde apuestas asociadas a la cualificación de sus instrumentos de medición 
de capacidades, los criterios relacionados con la metodología de priorización a ser 
empleada, así como el diseño de instrumentos para su implementación, seguimiento 
y evaluación. 
Este instrumento de planeación estratégica busca plantear mejoras sustanciales 
a la gestión de la seguridad y la convivencia en la ciudad, erigiéndose como la
hoja de ruta para los próximos cuatro años en términos de gestión y asignación 
de recursos de carácter estratégico. El PISCC presenta el horizonte estratégico 
para el trabajo articulado con los organismos de seguridad y justicia en torno a las 
dimensiones y líneas fruto del trabajo conjunto y participativo con distintos actores 
y sectores de la ciudad, permitiendo a la Secretaría de Seguridad y Convivencia 
contar con información para la toma de decisiones basada en evidencia empírica
desde un análisis causal de las problemáticas, identificar los principales escenarios 
en los cuales debe fortalecerse la interacción entre actores corresponsables, las 
áreas de oportunidad y mejora en términos de gestión y un direccionamiento 
adecuado de la inversión en seguridad, convivencia y acceso a la justicia, con el 
fin de cualificar las capacidades para la articulación y la coordinación cuya función 
resulta vital en la consolidación de  un modelo distrital de gobernanza territorial.
```

**PISCC 2024-2027 (posición de página 265)**

```text
Tabla de contenido
265
10. Escenarios
Este es el escenario directivo dispuesto por ley para la toma de decisiones 
relacionadas con el proceso de implementación y seguimiento del PISCC, así como 
la destinación de los recursos del Fondo Territorial de Seguridad (FONSET). En 
este contexto, se discuten y aprueban los proyectos FONSET presentados por 
los organismos de seguridad y justicia, los cuales deben estar necesariamente
alineados con el componente estratégico del PISCC y con las acciones e indicadores 
definidos en el plan de acción correspondiente. Asimismo, actúa como garante de 
la articulación entre los distintos instrumentos de planeación de la seguridad y la 
convivencia a nivel nacional, departamental, metropolitano y distrital. 
Adicionalmente, en este escenario se presentan informes periódicos de seguimiento 
y evaluación del PISCC, promoviendo espacios de construcción conjunta con
los actores corresponsables para el continuo mejoramiento del proceso de 
implementación, así como la definición de agendas de trabajo que respondan a las 
diversas necesidades del distrito.
Comité Territorial de Orden Público -CTOP
Periodicidad Evidencias / entregables
Cuatro veces al año de acuerdo con lo 
dispuesto por la ley y sesiones extraordinarias 
a demanda
Listados de asistencia, actas, 
presentaciones y fotografías.
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
265
```

**PISCC 2024-2027 (posición de página 66)**

```text
Tabla de contenido6. Diagnóstico
66
interacciones conducentes a resultados sociales deseables, y a condiciones de 
sociabilidad menos conflictivas y más favorables a la resolución de las problemáticas 
comunes (Eslava, Silva, Tobón y Vélez, 2014). 
En el caso de Medellín, el capital social y la confianza como una de sus principales 
dimensiones constitutivas han propiciado el aprovechamiento de los recursos 
disponibles para la generación de oportunidades y de importantes transformaciones
sociales y culturales. Consolidando así una visión compartida de territorio que a 
través de la alianza Estado, empresa, academia y sociedad civil, se orienta hacia una 
visión de desarrollo sostenible cuya apuesta principal es la inclusión y el bienestar 
social. Desde esta apuesta, la confianza y el capital social serán pilares para los 
procesos de toma de decisiones orientados a la gestión de las problemáticas de 
seguridad y convivencia de la ciudad, posibilitando la construcción de visiones
compartidas con los distintos actores que orienten una construcción conjunta de 
alternativas de solución y de instrumentos de gestión y planeación. 
En este orden de ideas, las múltiples interacciones basadas en la confianza y la 
consolidación del capital social que tienen lugar en el ecosistema de la ciudad 
facilitan la respuesta institucional  a las problemáticas que tienen injerencia en el 
territorio. Legitimando la intervención del Estado y contribuyendo al tejido de redes
de cooperación y corresponsabilidad que permitan el despliegue de acciones 
coordinadas para el fomento del progreso y el mejoramiento de las condiciones 
de vida de los habitantes de Medellín. 
De igual manera, se entiende que el fortalecimiento constante de las capacidades 
institucionales para la gestión de la seguridad y la convivencia en Medellín debe 
apoyar la generación de confianza entre sus habitantes. En este sentido, el trabajo
coordinado y articulado entre la Secretaría de Seguridad y Convivencia, los 
organismos de seguridad y de justicia, y de las dependencias de la administración 
corresponsables, apunta a que la formulación e implementación de acciones 
y estrategias en el marco de este PISCC estén orientadas a proteger las 
interacciones del ecosistema y a soportar los procesos de capital social positivo 
que se desarrollan en él. De tal manera que el servicio que se presta a la ciudad
desde la institucionalidad sirva de facilitador de la cohesión en/y entre personas, 
comunidades, territorios y, al mismo tiempo, incida en la reducción de la capacidad 
del crimen organizado para hacer daño a través de la generación de  delitos.   
Uno de los principales objetivos de la nueva visión de gestión de la seguridad y la 
convivencia en Medellín es garantizar que las personas puedan vivir en libertad bajo 
una visión de progreso diverso, productivo y multicultural dentro del ecosistema.
¿Qué significa esto? Que puedan vivir sin temor a ser afectados en sus preferencias 
de vida —cualquiera que estas sean— dentro de la Constitución y la Ley.
De otro lado existe una perspectiva en la que el capital social es aprovechado con 
fines negativos o trasgresores. En este caso se conocen como órdenes particulares
```

**PISCC 2024-2027 (posición de página 25)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
25
Enfoque de seguridad como un sistema 
integral
Enfoque territorial
Propone una visión holística que aborda la seguridad la convivencia y el acceso 
a la justicia desde una perspectiva interconectada, interdependiente e integral 
que reconoce el carácter complejo y multicausal asociado a la inseguridad y la 
ausencia de entornos de convivencia como permanentes retos públicos, los cuales
son dinámicos y se encuentran en continua evolución. Este abordaje, si bien no 
deja de lado la comprensión de estos fenómenos como resultado de diversos 
factores asociados a conflictividades sociales y prácticas delictivas derivadas de 
la delincuencia organizada y los mercados ilícitos, incluye la preocupación por 
otras causas de diferente naturaleza que están detrás de la ocurrencia de estas 
problemáticas que aquejan a los habitantes de Medellín, tales como las sociales,
económicas, culturales, entre otras que configuran el carácter estructural de los 
asuntos a intervenir. 
Bajo este enfoque la gestión de la seguridad y la convivencia en el distrito trasciende 
una visión exclusivamente dedicada a los efectos manifestados en la criminalidad, 
los delitos y contravenciones desde un nivel  operativo-reactivo, y propone una 
perspectiva que abarca de manera integral las causas que originan los fenómenos
de seguridad y las conflictividades sociales en la ciudad; incorporando nuevos 
factores asociados a los retos que subyacen a la gestión territorial de la seguridad 
ciudadana, estos de índole comportamental, cultural y social. Esta comprensión de 
integralidad se caracteriza por la apuesta decidida a la protección de derechos, el 
respeto por las instituciones y la legalidad, así como la identificación y diagnóstico 
de las múltiples causas asociadas a las problemáticas que afectan la seguridad y
la convivencia para la intervención efectiva de sus efectos. En ese sentido, este 
PISCC incorpora una visión holística de la seguridad y convivencia que funciona 
como un sistema integral, que pretende trascender la visión fragmentada que 
desconoció la complejidad de los fenómenos en los últimos cuatro años en Medellín 
transitando hacia un horizonte compartido de ciudad. En este orden de ideas, la 
materialización de este enfoque precisa pasar a una gestión de la seguridad desde
una perspectiva de gobernanza territorial, la cual tenga como pilar fundamental 
el fortalecimiento de las capacidades institucionales para la gestión coordinada y 
articulada de problemas complejos y la definición de  corresponsabilidades entre 
los actores involucrados en el proceso de implementación del PISCC. 
Esta perspectiva reconoce la importancia de tener en cuenta las características, 
particularidades, diferencias, necesidades y dinámicas propias de cada uno
de los territorios que conforman el distrito, buscando diseñar estrategias que
```

**PISCC 2024-2027 (posición de página 261)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
261
Partiendo de la anterior premisa, los instrumentos y escenarios que aquí se 
proponen están estructurados de tal manera que sea posible hacer operativos los 
objetivos, líneas estratégicas y metas trazadas por el PISCC para prevenir, atender 
y gestionar las problemáticas de seguridad y convivencia identificadas en la ciudad 
de Medellín. Este sistema es un componente fundamental para el funcionamiento
de un instrumento de gestión como este plan, de su estructura dependerá la 
identificación de los fallos y aciertos de la planeación, así como las decisiones 
políticas que se tomen en el marco del proceso de implementación del PISCC. 
Como lo refiere Bertranou (2019) el seguimiento es un factor del proceso de diseño 
que debe planearse desde un principio y durante el desarrollo de la ejecución 
de un instrumento o intervención, dado que su principal objetivo es proporcionar
evidencia sobre la efectividad y resultados de la materialización de los programas 
y proyectos formulados. En otras palabras, este componente del PISCC permite 
medir el progreso y efectividad de las intervenciones planeadas por los organismos 
de seguridad y de justicia, así como la gestión de la Secretaría de Seguridad y 
Convivencia en el marco del proceso de prevención y atención a las problemáticas 
priorizadas en la ciudad de Medellín. Asimismo, provee de los recursos suficientes
y necesarios para la promoción de la gobernanza colaborativa, la rendición de 
cuentas y transparencia institucional, así como el reporte de resultados tangibles 
(DNP, 2023; Rojas y Echavarría, 2022; Rossi, 2017; PNUD, 2009). 
Por este motivo, se consideraron las lecciones aprendidas, las buenas prácticas y 
los resultados de los ejercicios de planeación previos, y se estructuró un modelo 
que, por un lado, se basa en instrumentos que aportan datos e información
relevante para la toma de decisiones informadas tomando como punto de partida 
la Política Pública de Seguridad y Convivencia, el plan de acción —a partir de todos 
los indicadores que lo componen—, y los Planes Locales de Seguridad, Convivencia 
y Justicia cercana al ciudadano (PLSCJ). Del otro lado, se encuentran los escenarios 
que integran este sistema como el Comité Territorial de Orden Público —CTOP—, 
los escenarios para la coordinación y la articulación de los actores corresponsables
de la implementación del PISCC, las mesas técnicas de proyectos FONSET y los 
espacios de interacción y gobernanza interinstitucional que, en su conjunto, tienen 
como objetivo la discusión y toma de decisiones sobre asuntos clave, la gestión 
de los recursos disponibles, el trabajo conjunto y articulado entre actores, y el 
seguimiento y evaluación a la ejecución del componente estratégico.
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 71)**

```text
debido al déficit de espacio asociado con la compleja topografía del territorio, así como  
vacíos en la reglamentación y el control de la construcción y el desarrollo de infraestructura. 
A esta problemática estructural se suman prácticas informales derivadas de la necesidad de 
subsistencia, producto de la histórica desigualdad social y la reciente ola migratoria, tales  
como instalación de ventas informales no reguladas (ambulantes y estacionarias) en
andenes, plazas, parques y vías públicas que agravan el problema. Adicionalmente, la baja 
corresponsabilidad ciudadana que se evidencia en la apropiación del espacio por parte de  
establecimientos  comerciales,  el  parqueo  indebido  de  vehículos,  la  instalación  no 
autorizada de vallas publicitarias, y la disposición inadecuada de escombros y residuos, son 
aspectos  que  dinamizan  la  ocupación  indebida  del  espacio  público  y  que,  además,
aumentan la percepción inseguridad y los riesgos de problemas de convivencia ciudadana.
Las formas de ocupación y uso indebido del espacio público, producto de estos tres factores 
(planificación deficiente, desigualdad estructural y falta de corresponsabilidad), afectan  
negativamente la movilidad peatonal y vehicular, obstaculizan la circulación de personas  
con  discapacidad,  deterioran  el  mobiliario  urbano  y  generan  paisajes  urbanos
desordenados que son percibidos como inseguros. Desde la perspectiva de seguridad, esta 
problemática adquiere una dimensión aún más crítica, pues de acuerdo con información  
recogida en el territorio por el SISC, en el centro de Medellín el espacio público ha sido  
cooptado por estructuras ilegales que extorsionan a los comerciantes ambulantes por el uso 
de las zonas. Según la Subsecretaría de Espacio Público y reportes de medios locales, (El
Colombiano, 2022; El Colombiano, 2024 & EAFIT es noticia, 2025),dicha situación es  
especialmente crítica en sectores como la Avenida Maturín y el Parque Berrío, donde el  
comercio informal ha crecido de forma exponencial, pese a los esfuerzos institucionales por 
ejercer control.
En este sentido, la recuperación del espacio público requiere un enfoque integral que  
articule la planeación urbana, el control institucional y la corresponsabilidad ciudadana, con
el propósito de garantizar su función social, el orden urbano y la equidad en el acceso.  
Algunas estrategias clave incluyen la asignación regulada de espacios para actividades  
económicas, la intervención oportuna frente a usos no autorizados y el fortalecimiento de la 
gestión pública conforme a lo estipulado en la Ley de Ordenamiento Territorial. Por ello, es 
fundamental  comprender  que  la  ocupación  indebida  del  espacio  público  no  se  debe
únicamente a la falta de control, sino también a factores estructurales como el desempleo, la 
informalidad y la desigualdad. 
En esta línea, la Sentencia C-211 de 2017 de la Corte Constitucional, si bien establece la  
prohibición de la ocupación del espacio público en contravención de las normas y autoriza  
sanciones  y  decomisos,  también  reconoce  que  su  recuperación  puede  alterar  las 
condiciones económicas de los comerciantes informales. Ante esta realidad, Medellín tiene
el deber de diseñar e implementar políticas públicas que puedan mitigar los impactos  
negativos de los desalojos, basadas en estudios que reflejen las condiciones reales de  
quienes resultan afectados. Finalmente, el compromiso activo de la ciudadanía en el  
cuidado, uso responsable y defensa del espacio público debe complementar la acción  
institucional. Solo a través de un enfoque corresponsable será posible mitigar las dinámicas
```

**PISCC 2024-2027 (posición de página 270)**

```text
Tabla de contenido
Gráfica 68 Sistema de evaluación del PISCC
Sistema de evaluación del PISCC
Fuente: Elaboración propia 
Evaluación de procesos Evaluación de resultados Evaluación de impacto
270
Uno de los principales retos que en términos de evaluación se presenta hoy 
para el PISCC de la ciudad refiere a la necesidad de establecer una trazabilidad y 
articulación efectiva entre lo dispuesto en el componente estratégico, el plan de
acción, la ejecución de los recursos FONSET y la manera en que esto se traduce 
en indicadores de resultado y ejercicios de evaluación asociados al impacto. 
Por lo tanto, el objetivo asociado a los ejercicios de evaluación del PISCC 2024 
- 2027 es determinar el nivel de cumplimiento de las metas concertadas entre la 
administración distrital y los organismos de seguridad y justicia dentro del marco 
metodológico de priorización de problemáticas desarrollado por la Secretaría de
Seguridad y Convivencia del Distrito de Medellín, con la legitimidad de aquellos 
actores que hicieron parte de los ejercicios participativos de priorización, ello en 
relación con los niveles de inversión, resultado e impacto. 
Para desarrollar esta apuesta, a continuación se detalla cada una de las evaluaciones 
y su ejecución.
Evaluación de Procesos
La evaluación de procesos busca proporcionar información sobre el proceso de
presentación, análisis, aprobación y ejecución de los proyectos y recursos FONSET, 
con el fin de medir el progreso de su intervención al comparar los avances logrados 
frente a las metas establecidas en el Plan de Acción del PISCC. Esta evaluación es 
llevada a cabo por todos los responsables de los proyectos FONSET en la fase 
de implementación, y su finalidad es optimizar la ejecución de los proyectos, 
detectando fortalezas, debilidades, oportunidades y amenazas en términos
normativos, estructurales y funcionales, en el marco del comité interno para el 
análisis y aprobación de los proyectos FONSET de la Secretaría de Seguridad y 
Convivencia. 
Además de tener en cuenta el Plan de Acción del PISCC y los cronogramas de los 
proyectos, se realiza un análisis cualitativo desarrollado por los entes responsables 
de los proyectos FONSET, con el apoyo de los profesionales de la Subsecretaría 
de Planeación, con el propósito de elaborar un análisis DOFA que identifique los
factores internos y externos que dificulten la implementación de los proyectos. 
11. Sistema de Evaluación del PISCC
```

</details>

---

## Respuesta 7 (directa)

<!-- trace_id: tr-68467ca2ea165c3a1ea3b84d04d4c459 -->

**Pregunta:** ¿Cómo regulan La Terraza y Los Triana la violencia intrafamiliar en las comunas Santa Cruz, Manrique y Aranjuez?

**Respuesta esperada:** Mediante la mediación en casos de violencia intrafamiliar, con multas desde $400.000, que se incrementan de forma arbitraria si el agresor tiene mayor capacidad económica, y con amenazas si no se cumple el pago.

*Fuente:* Diagnóstico para la política pública, p. 91 (tabla "Regulación de la violencia intrafamiliar por parte de estructuras criminales en los territorios")

**Respuesta del bot:**

En las comunas **Santa Cruz, Manrique y Aranjuez**, las estructuras criminales **La Terraza** y **Los Triana** regulan la violencia intrafamiliar mediante los siguientes mecanismos:

- **Modalidad de control:** “Mediación en casos de violencia intrafamiliar”.
- **Multas / sanciones económicas:** “Desde $400.000 (incremento arbitrario si el agresor tiene mayor capacidad económica)”.
- **Otras medidas aplicadas:** “Amenazas por incumplimiento en el pago” (para ambas estructuras).

Estos tres elementos aparecen de forma idéntica para **La Terraza** y **Los Triana** en la tabla de regulación de la violencia intrafamiliar del Diagnóstico para la política pública de seguridad y convivencia. No falta información adicional respecto a la forma en que regulan la violencia intrafamiliar en esas comunas.

correctness: si

groundedness: si

<details><summary>Ver contexto recuperado</summary>

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 91)**

```text
Tabla XX. Regulación de la violencia Intrafamiliar por parte de estructuras criminales en 
los territorios
Comunas  /  
Sectores
Estructuras 
criminales 
Modalidad  de  
control
Multas  /  
sanciones 
económicas
Otras  medidas  
aplicadas
2- Santa Cruz, 3 –  
Manrique  y  4  –
Aranjuez. 
La Terraza.
Los Triana.
Mediación  en  
casos de violencia 
intrafamiliar.
Desde $400.000 
(incremento 
arbitrario  si  el  
agresor  tiene  
mayor 
capacidad 
económica).
Amenazas  por  
incumplimiento  en  
el pago.
Amenazas  por  
incumplimiento  en  
el pago.
5- Castilla, 6 – Doce 
de  Octubre  y  7  – 
Robledo. 
No especificada.
Sistema de multas 
y  sanciones  
proporcionales  a  
la gravedad de la  
falta  y  
reincidencia.
Entre  $200.000 
y  $1.000.000;  
reincidencia: 
sanción  se  
duplica.
Desplazamiento 
forzado  en  casos  
graves.
8 – Villa Hermosa y  
9 – Buenos Aires. 
La Terraza. 
Caicedo.
Control  social  
mediante 
sanciones  y  
multas.
Entre  $100.000 
y $500.000.
Agresiones  físicas
y $500.000.
Agresiones  físicas  
en algunos casos.
9 – Buenos Aires. Caicedo.
Control  social  
mediante 
sanciones  y  
multas.
Desde 
$500.000;  hasta 
$2.000.000 si la  
policía interviene 
en territorio.
Agresiones  físicas  
como represalia.
13 – San Javier. 
 Las  
Independencias y 
El Coco
Sanciones 
económicas.
Desde 
$300.000.
16 – Belén. Los Juaquinillos.
Sanciones 
económicas, 
según  gravedad  
de las lesiones.
Desde 
$300.000.
de las lesiones.
Desde 
$300.000.
Fuente: Equipo Territorial. Sistema de Información para la Seguridad y la Convivencia, 
2025.
Elaboración: Propia
```

**PISCC 2024-2027 (posición de página 180)**

```text
Tabla de contenido6. Diagnóstico
Problemática
Problemática
1. Nuevos modelos de 
familias.
2. La normalización 
de la violencia como 
mecanismo para 
resolver conflictos, 
el consumo 
problemático de licor 
y otras sustancias 
psicoactivas, y otros 
problemas asociados a 
la salud mental.
1. Sistema familiar 
patriarcal que sitúa 
a las mujeres y 
a aquello que se 
presenta feminizado 
dentro de la familia 
en un rol de sumisión 
y sometimiento 
injustificado frente a 
los hombres.
injustificado frente a 
los hombres.
1. Reorganización de las dinámicas familiares, que traen consigo 
retos en las dinámicas relacionales dentro del contexto familiar, 
formas de resolver sus conflictos y reconocimiento de vínculos 
de afinidad o parentescos. 
2. Alta acumulación de eventos estresantes que desencadenan 
manifestaciones de violencia que pueden dejar graves lesiones 
físicas o psicológicas en las víctimas o incluso la muerte,
(homicidios/feminicidios, asociados a la violencia intrafamiliar).
 
3. Debilitamiento de la familia como unidad básica de la sociedad 
encargada de consolidar y transmitir condiciones favorables para 
el desarrollo personal, social y económico de un individuo. 
1. Feminicidios.
2. Incapacidad para salir del continuum de violencias y 
reconocerse como víctima.
3. Pérdida de confianza en las instituciones encargadas de 
atender   violencia basada en género.
atender   violencia basada en género. 
4. Grupos delincuenciales como regularizadores de la violencia 
intrafamiliar en el territorio, lo que permite el aumento de las 
rentas criminales. 
5. Desplazamiento de las víctimas como medida de autocuidado. 
Violencia intrafamiliar en general
Violencia intrafamiliar contra las mujeres
Causas
Causas
Efectos
Efectos
Tabla 26 Resumen explicativo de la violencia intrafamiliar en Medellín
180
180
Es así como esta violencia puede manifestarse en forma de abuso físico, psicológico, 
financiero, sexual o negligencia. Las personas mayores que sufren violencia 
intrafamiliar pueden experimentar traumas emocionales graves, conductas o ideas 
suicidas, deterioro de la salud física y mental, disminución en su calidad de vida, 
lo cual aumenta el riesgo de hospitalización o muerte de esta población. De igual 
forma, el aislamiento social es una de las principales consecuencias de esta forma
de violencia, lo que a su vez dificulta la denuncia en estos casos. Esta situación 
puede explicar en parte el bajo número de casos de victimización reportados a las 
autoridades con respecto a este ciclo vital.  
Por último, el abandono representa uno de los efectos más devastadores de la 
violencia hacia esta población. Esto supone un desafío para el Distrito, que debe 
garantizar el acceso a la justicia y la existencia y fortalecimiento de centros de
protección y atención para las personas mayores, siendo fundamental para reducir 
el riesgo de que estas personas se vean avocadas a la mendicidad o a vivir en calle, 
lo que se puede derivar en problemas de seguridad pública.
```

**Diagnóstico para la política pública de seguridad y convivencia (posición de página 19)**

```text
lesionados en los barrios La Pradera, Los Alcázares, El Socorro y El Danubio, según policía 
judicial consultada por el SISC.
Por otro lado, además de las confrontaciones externas entre estructuras, se han presentado 
varias disputas internas, las cuales han dinamizado el homicidio al interior de los territorios 
de injerencia. Si bien prácticamente todos los grupos criminales han tenido un historial de  
confrontaciones al interior de su propia organización, vale la pena resaltar dos de las más
importantes, en términos de relevancia criminal en la última década. En primer lugar, se  
destaca  la  confrontación  interna  entre  diversas  facciones  del  GDO  Robledo,  
desencadenadas por diferencias entre los cabecillas, y que vio su punto más álgido con el  
homicidio de Javier Ventura Marín Álvarez, alias “Tatú”, hombre de confianza de Freyner  
Alfonso Ramírez, alias “Carlos Pesebre”, en septiembre de 2022. 
Producto de esta confrontación interna, el GDO Robledo quedó fragmentado en varias
líneas, que actualmente se encuentran en una tensa calma. En un segundo momento, se  
resalta la confrontación al interior del GDO La Terraza, y que vivió su punto más álgido en  
marzo de 2024, con el homicidio de uno de sus cabecillas, Edinson Rodolfo Rojas, alias  
“Pichi Gordo”. De acuerdo con información recolectada con organismos de seguridad y  
justicia por el SISC, esta confrontación habría dividido a La Terraza en dos facciones: la
primera correspondiente a los cabecillas de mayor antigüedad de la estructura, como Jhony 
Alberto Muñoz Laverde, alias “El Sobri” y Norbey Andrés Palacios Fernández, alias “Mocho 
Vives”,  los  cuales  se  han  venido  distanciando  de  la  segunda  línea,  liderada  por  los 
cabecillas más jóvenes, como Mauricio Alberto Zapata Orozco, alias “Chicho”, y Juan Pablo 
Taborda Zamora, alias “Yordi”, atomizando el accionar de esta estructura, generando otras
diferencias que han llevado a desencuentros, cambios de mando y, posiblemente, la  
materialización de nuevos homicidios, como el evidenciado en el mes de mayo, en la  
comuna 1 – Popular, del máximo cabecilla de su GDCO San Pablo, Adiel Fabian Covaleda 
Guzmán, alias “Adiel”.
Por su parte, es preciso mencionar que las estructuras criminales del Valle de Aburrá, desde 
su origen hasta la actualidad, han sostenido, en su mayoría, una vocación expansionista
que se ha evidenciado en el constante cambio en las fronteras criminales, y las distintas  
formas de articulación, pactismo y connivencia criminal con otras estructuras de naturaleza 
regional, nacional y transnacional. No obstante, es evidente que los últimos cinco años las  
estructuras han representado un viraje expansionista, cambiando su focalización territorial  
en Medellín,  y dirigiéndola con más ahínco hacia otros territorios del departamento y el país,
algo que responde a múltiples condiciones de posibilidad, entre las que destacan la  
definición  de  un  status  quo organizado  y  concertado  criminalmente  en  la  ciudad,  la 
instauración de la Mesa de Diálogos en Itagüí, y el acercamiento cada vez más intencionado 
de los GDO del Área Metropolitana a GAO y GAOR, como el Clan del Golfo y el ELN  
(Valencia, 2025). 
El siguiente mapa evidencia las principales expansiones de las estructuras criminales del
Área Metropolitana al departamento de Antioquia y el país, de acuerdo con la información  
proporcionada por los organismos de seguridad y justicia al SISC.
```

**PISCC 2024-2027 (posición de página 198)**

```text
Tabla de contenido6. Diagnóstico
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC) 
con información de Número Único de Seguridad y Emergencias 123
Gráfica 56 Tipo de armas utilizadas, según llamadas al 123 reportando riñas por 
año, 2019-2023
198
Según el NUSE, el registro de estas llamadas reportando riñas entre 2019-2023 
con ubicación geográfica en la ciudad, tuvo mayor participación en las comunas 
10 – La Candelaria (14%), 4 – Aranjuez (7%), 3 – Manrique (7%), 16 – Belén (7%), 8
– Villa Hermosa (6%) y 6 – Doce de Octubre (6%) y lo que representa el 47% de 
las llamadas reportando riñas en todo Medellín. Sin embargo, en seguimiento a la 
variación porcentual de las llamadas en este mismo periodo de tiempo, se evidencia 
una tendencia a la reducción de los registros de las comunas antes señaladas.
Es importante señalar, que la participación de La Candelaria puede estar relacionada 
con el alto flujo y diversidad de personas, que confluyen en el centro de Medellín,
teniendo en algunos casos diferencias en las forma de habitar el territorio, terminando 
en discusiones, amenazas y confrontaciones como la acción más práctica para 
resolver los conflictos, situación similar puede ocurrir en el corregimiento de Santa 
Elena que alberga los fines de semanas turistas locales y otros extranjeros que 
llegan a disfrutar de la ruralidad; mientras en las comunas Santa Cruz, Manrique y 
Doce de Octubre son quienes habitan el territorio los mismos que propician estos
escenarios violentos como mecanismos de resolución del conflicto, situación que 
se relaciona con la priorización de problemáticas de convivencia, relacionadas con 
la agresión y validación del maltrato físico; además de la posible regulación de estas 
confrontaciones por parte de los grupos delincuenciales que tienen injerencia en 
estas comunas, promoviendo el control de la conductas ciudadanas.
```

**PISCC 2024-2027 (posición de página 85)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Fuente: Sistema de Información para la Seguridad y la Convivencia 
(SISC), con información de SIJIN, CTI e INMLCF
Gráfica 11 Participación porcentual de cada modalidad dentro del total de 
homicidios. 2019-2023
85
puesto que en homicidios asociados a estructuras criminales suelen emplearse más 
armas de fuego, mientras que homicidios por convivencia, violencia intrafamiliar
o violencia de género se cometen principalmente con armas cortopunzantes u 
objetos contundentes.
Los homicidios también han variado sustancialmente en algunos territorios de la 
ciudad. Tal como se aprecia en la Gráfica 12, algunas comunas como San Javier 
y Belén, y corregimientos como Altavista han tenido variaciones decrecientes en 
estos cinco años, mientras que otras como El Poblado, Buenos Aires y San Antonio 
de Prado han tenido variaciones al alza, llegando incluso al 68% en el caso de
El Poblado. Este cambio de comportamiento se explica por una reducción en la 
manifestación letal del conflicto en algunos territorios de la ciudad, especialmente 
en aquellos donde existe un control territorial hegemónico por parte de una 
estructura criminal. 
Sin embargo, es importante resaltar que en muchos casos el incremento significativo 
en algunas comunas se debe al hecho de que existen pocos homicidios al año, 
por lo que incrementos nominales pequeños tienen efectos significativos sobre
las variaciones porcentuales, ejemplo de ello es el caso de El Poblado donde un 
incremento de dos casos entre 2022 y 2023 supuso un incremento del 50% en el 
indicador en esta comuna. Mientras que en comunas como La Candelaria donde se 
presenta una cantidad significativa de homicidios cada año, las variaciones anuales 
son menores, dado que las reducciones alteran en menor medida el indicador.
```

**PISCC 2024-2027 (posición de página 226)**

```text
Tabla de contenido6. Diagnóstico
Distrito
Cantidad de internos a la fecha
% de hacinamiento
Cantidad de internos estimada
Diferencia
Condenados
Condenados con documentación 
completa
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
60
10
10
102
95
112
42
85
102
70%
850%
1020%
7
6
16
5
4
11
2
2
5
Número 01
102
70%
850%
1020%
7
6
16
5
4
11
2
2
5
Número 01 
Tabla 34 Reporte diario de PPL en estaciones de policía del Distrito de Medellín 
Condenados sin documentación 
completa
Domiciliarias detención
Sindicados
Domiciliarias prisión
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
Aranjuez 
Manrique 
Popular 
91
89
96
4
0
0
0
0
0
Aranjuez 
Manrique 
Popular 
16
6
9
Extranjeros
226
```

**PISCC 2024-2027 (posición de página 73)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Cada uno de los GDO mencionados tiene distintos GDCO asociados, subordinados 
o aliados, lo que representa que, según los datos del último inventario criminal de 
la Alcaldía de Medellín, la Fiscalía General de la Nación y Policía Nacional (2023), 
existen al menos 81 GDCO en el Área Metropolitana, los cuales, a su vez, tienen 
bajo su mando a 196 subgrupos. Pese a esto, si bien la jerarquía suele dictar que
los subgrupos dependen de los GDCO, los cuales, a su vez, dependen de los GDO, 
en la realidad social y criminal esta jerarquización no se cumple en todos los casos, 
toda vez que hay GDCO independientes que no dependen de ningún GDO, así 
como GDO que dependen de otro GDO.
Hay que tener en cuenta que el panorama criminal actual de la ciudad de Medellín se 
enmarca en la división de la dinámica del crimen organizado en el Área Metropolitana,
entre las estructuras criminales que siguen los lineamientos de Juan Carlos Mesa 
Vallejo, alias “Tom”, máximo cabecilla histórico del GDO Los Chatas; y aquellos que 
siguen las directrices de José Leonardo Muñoz Martínez, alias “Douglas”, cabecilla 
histórico del GDO La Terraza. Estos han consolidado dos facciones principales, 
denominadas como Grupo Colegiado Oficina, y Alianza Criminal, respectivamente. 
Sin embargo, no todos los GDO se alinean a estas dos facciones, lo que genera
que otros GDO y GDCO sean reconocidos como outsourcing o independientes.
Santa Cruz – Aranjuez – Robledo – San Antonio de Prado – Bello
Envigado – Sabaneta
Los Chatas
La Unión
Robledo – La América – San Javier – Belén – San Cristóbal
Villa Hermosa – San Antonio de Prado – Altavista
El Mesa
La Terraza
Caicedo
Bello – Barbosa – Girardota - Copacabana
Bello – Copacabana – Barbosa – Girardota
Itagüí – La Estrella – Guayabal
Pachelly
Doce de Octubre – Bello – La Ceja – Soacha – Tunja y varias subregiones de
Antioquia
Popular – Manrique – Aranjuez – Caicedo – Candelaria – Laureles – 
El Poblado
Villa Hermosa – Buenos Aires – La Candelaria – El Poblado
Los Triana
Trianón
Robledo
La Sierra
GDO Territorio
Tabla 6 GDO y territorios.
Fuente: Secretaría de Seguridad y Convivencia (2024).
73
```

**PISCC 2024-2027 (posición de página 91)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
91
que estadísticamente son más los hombres que mueren asesinados. En el caso 
de Medellín, entre los años 2019 y 2023, 1.967 hombres fueron registrados 
como víctimas de homicidio, mientras que, en el mismo periodo, se hallaron 178 
hechos contra mujeres, de los cuales, como se nombró previamente, 126 fueron 
categorizados como posibles feminicidios. 
No obstante, llama la atención que, en estos últimos que el 51,58% (65 casos) de
estos hechos presuntamente fueron cometidos por parejas, exparejas o familiares 
de las víctimas, a diferencia de lo que sucede con los hombres, cuyas muertes 
acaecen en el ámbito de lo público. Lo anterior da cuenta de un elemento central: 
la violencia contra las mujeres se recrudece en las relaciones cercanas, al punto de 
que el 57,14% de los casos de feminicidio ocurren en casas, inquilinatos, residencias, 
apartamentos, hoteles y moteles, es decir: lugares en los que se tejen relaciones de
intimidad.  Esto se confirma en la Encuesta de Percepción de Seguridad del 2023, 
según la cual el 49% de las mujeres encuestadas manifiestan haber sufrido el hecho 
más grave de violencia basada en género en su casa (Secretaría de Seguridad y 
Convivencia, 2023, p. 63). 
En lo relativo a las víctimas  de feminicidio, el 93% (118 casos) se encuentran en 
el rango de 0 a 45 años, mientras que el 49,2% (62 víctimas) tenían al momento
del hecho hasta 28 años, el 11,9% (15) eran migrantes venezolanas y una de las 
víctimas se reconocía como afrodescendiente. Desde la perspectiva del territorio, 
los hechos de 2019 a 2023 ocurrieron principalmente en las comunas 1 – Popular 
(10), 2 – Santa Cruz (8), 4 – Aranjuez (8) y 16 – Belén (8), territorios que representan 
el 26% de los casos registrados. En el mismo sentido, en términos zonales, el 66% 
(84 víctimas) de los hechos ocurrieron en la Nororiental y Centroriental, esta cifra
coincide parcialmente con las zonas de residencia pues el 41% de las víctimas 
también residen en estas zonas. 
Ahora bien, en relación con el arma o medio empleado: 65 feminicidios se 
materializaron por medio de un arma cortopunzante, y 19 se ocasionaron por 
medio de ahorcamiento o estrangulamiento; entre ambos medios se halla el 64% 
total de los casos. De lo anterior, es posible deducir una intermediación del cuerpo 
del agresor en la letalidad de su mensaje indicando que “se tiene en las manos la
voluntad del otro, es el telos o finalidad de la violencia expresiva. Dominio, soberanía 
y control son su universo de significación” (Segato, 2016, p. 39). 
En relación con la descripción de los hechos alrededor de la escena del crimen, 
los estudios de psicología forense arrojan que “los homicidios en la pareja se 
caracterizan mayoritariamente por tener una sola víctima, ser impulsivos y 
situacionales, cometerse por parte de personas que reaccionan agresivamente a
determinados estímulos (p. ej., amenaza), no haber planificación y formar parte 
de reacciones emocionales ante situaciones adversas o conflictos derivados de la 
interacción interpersonal con la víctima. Por ello, las emociones son el componente 
inicial de estos homicidios” (Block y Ovcharchyn Devitt, 2001; Trojan y Salfati, 2010, 
citado en Soria, 2016, s.p.).
6. Cifra que se contrasta con el 13,11% de casos registrados en los mismos lugares en el caso de los homicidios. 
6
```

</details>

---

## Respuesta 8 (directa)

<!-- trace_id: tr-45a7da07cb42c8d80e9bbff4726a2656 -->

**Pregunta:** ¿Qué función cumple el Comité Territorial de Orden Público (CTOP) frente al PISCC y los recursos del FONSET?

**Respuesta esperada:** Es el escenario directivo dispuesto por ley para tomar decisiones sobre la implementación y el seguimiento del PISCC y sobre la destinación de los recursos del Fondo Territorial de Seguridad (FONSET). Allí se discuten y aprueban los proyectos FONSET de los organismos de seguridad y justicia, que deben estar alineados con el componente estratégico del PISCC y su plan de acción, y se presentan informes periódicos de seguimiento y evaluación del PISCC.

*Fuente:* PISCC 2024-2027, sección 10. Escenarios, p. 265

**Respuesta del bot:**

El Comité Territorial de Orden Público (CTOP) funciona como **espacio de coordinación y articulación de los actores corresponsables del Plan Integral de Seguridad y Convivencia Ciudadana (PISCC)**, según se indica en el documento:

> “Escenarios para la coordinación y la articulación de los actores corresponsables del PISCC”【1†L2-L4】.

En el mismo marco de implementación del PISCC, el CTOP está vinculado a los procesos de gestión de los recursos del Fondo de Seguridad Territorial (FONSET) a través de las **mesas técnicas de proyectos FONSET**, que forman parte de los escenarios de coordinación:

> “Mesas técnicas de proyectos FONSET”【2†L4-L6】.

**Resumen de la función:**  
- Coordina y articula a los diferentes actores involucrados en la ejecución del PISCC.  
- Facilita la interacción con las mesas técnicas que gestionan los proyectos y recursos del FONSET.

*No se encontró información adicional que detalle de manera explícita otras funciones específicas del CTOP respecto a la administración o distribución de los recursos del FONSET.*

correctness: no

groundedness: no

<details><summary>Ver contexto recuperado</summary>

**PISCC 2024-2027 (posición de página 7)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
10. Escenarios 
10.1.  Comité Territorial de Orden Público -CTOP- 
10.2. Escenarios para la coordinación y la articulación de los actores  
    corresponsables del PISCC  
10.3. Mesas técnicas de proyectos FONSET 
10.4. Espacios de interacción y gobernanza interinstitucional
11. Sistema de Evaluación del PISCC 
11.1.   Evaluación de Procesos 
11.2.  Evaluación de Resultados 
11.3.  Evaluación de Impacto
12. Referencias
266
266
267
267
268
270
271
```

**PISCC 2024-2027 (posición de página 262)**

```text
Tabla de contenido9. Sistema de implementación, seguimiento y evaluación
Evaluación del PISCC
Gráfica 67 Sistema de implementación, seguimiento y evaluación del PISCC
Instrumentos Escenarios
Política Pública de Seguridad y Convivencia
Plan de accción del PISCC
Planes Locales de Seguridad, Convivencia y 
Justicia cercana al ciudadano (PLSCJ)
Comité Territorial de Orden Público
Escenarios para la coordinación y la articulación 
de los actores corresponsables del PISCC
Mesas técnicas de proyectos FONSET
```

**PISCC 2024-2027 (posición de página 19)**

```text
hoja de ruta para los próximos cuatro años en términos de gestión y asignación 
de recursos de carácter estratégico. El PISCC presenta el horizonte estratégico 
para el trabajo articulado con los organismos de seguridad y justicia en torno a las 
dimensiones y líneas fruto del trabajo conjunto y participativo con distintos actores 
y sectores de la ciudad, permitiendo a la Secretaría de Seguridad y Convivencia 
contar con información para la toma de decisiones basada en evidencia empírica
```

**PISCC 2024-2027 (posición de página 265)**

```text
alineados con el componente estratégico del PISCC y con las acciones e indicadores 
definidos en el plan de acción correspondiente. Asimismo, actúa como garante de 
la articulación entre los distintos instrumentos de planeación de la seguridad y la 
convivencia a nivel nacional, departamental, metropolitano y distrital. 
Adicionalmente, en este escenario se presentan informes periódicos de seguimiento 
y evaluación del PISCC, promoviendo espacios de construcción conjunta con
```

</details>

---

## Respuesta 9 (directa)

<!-- trace_id: tr-fae116005818b481913a7fc7de8a2e99 -->

**Pregunta:** ¿Cuál es la línea base y la meta del cuatrienio para la tasa de homicidio y para la percepción de seguridad en el Plan de Desarrollo 2024-2027?

**Respuesta esperada:** La tasa de homicidio tiene una línea base de 14,24 por 100.000 habitantes (2023) y una meta de 12,82 para el cuatrienio; la percepción de seguridad tiene una línea base de 43 % (2023) y una meta de 50,7 %. Ambos indicadores están a cargo de la Secretaría de Seguridad y Convivencia.

*Fuente:* Plan de Desarrollo 2024-2027, p. 392; la misma tabla está en el PISCC 2024-2027, p. 255

**Respuesta del bot:**

**Tasa de homicidio**  
- Línea base (2023): “14,24” homicidios por 100 000 habitantes.  
- Meta cuatrienio 2024‑2027: “12,82” homicidios por 100 000 habitantes.  

**Percepción de seguridad**  
- Línea base (2023): “43” % de percepción de seguridad.  
- Meta cuatrienio 2024‑2027: “50,7” % de percepción de seguridad.  

*Fuente: Plan de Desarrollo Distrital 2024‑2027, tabla de indicadores de resultado.*

correctness: si

groundedness: si

<details><summary>Ver contexto recuperado</summary>

**PISCC 2024-2027 (posición de página 87)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Mapa 1 Homicidios por comuna y corregimiento. 2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia 
(SISC), con información de SIJIN, CTI e INMLCF
87
El comportamiento del homicidio en el período de tiempo analizado (2019-2023) 
implica tener en consideración tres hipótesis al respecto. En primer lugar, la 
reducción de homicidios asociados a las estructuras criminales no supone que
estos grupos hayan dejado de ejercer control sobre los territorios donde hacen 
presencia; por el contrario, esto parece reflejar un cambio en la forma en que 
se ejerce el control, ya no por la vía de la violencia homicida y la confrontación 
armada, sino por medio de las conversaciones y las treguas pactadas entre las
```

**PISCC 2024-2027 (posición de página 85)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Fuente: Sistema de Información para la Seguridad y la Convivencia 
(SISC), con información de SIJIN, CTI e INMLCF
Gráfica 11 Participación porcentual de cada modalidad dentro del total de 
homicidios. 2019-2023
85
puesto que en homicidios asociados a estructuras criminales suelen emplearse más 
armas de fuego, mientras que homicidios por convivencia, violencia intrafamiliar
o violencia de género se cometen principalmente con armas cortopunzantes u 
objetos contundentes.
Los homicidios también han variado sustancialmente en algunos territorios de la 
ciudad. Tal como se aprecia en la Gráfica 12, algunas comunas como San Javier 
y Belén, y corregimientos como Altavista han tenido variaciones decrecientes en 
estos cinco años, mientras que otras como El Poblado, Buenos Aires y San Antonio 
de Prado han tenido variaciones al alza, llegando incluso al 68% en el caso de
El Poblado. Este cambio de comportamiento se explica por una reducción en la 
manifestación letal del conflicto en algunos territorios de la ciudad, especialmente 
en aquellos donde existe un control territorial hegemónico por parte de una 
estructura criminal. 
Sin embargo, es importante resaltar que en muchos casos el incremento significativo 
en algunas comunas se debe al hecho de que existen pocos homicidios al año, 
por lo que incrementos nominales pequeños tienen efectos significativos sobre
las variaciones porcentuales, ejemplo de ello es el caso de El Poblado donde un 
incremento de dos casos entre 2022 y 2023 supuso un incremento del 50% en el 
indicador en esta comuna. Mientras que en comunas como La Candelaria donde se 
presenta una cantidad significativa de homicidios cada año, las variaciones anuales 
son menores, dado que las reducciones alteran en menor medida el indicador.
```

**PISCC 2024-2027 (posición de página 9)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Participación porcentual de cada caracterización dentro del total  
de homicidios categorizados. 2019-2023.
Participación porcentual de cada modalidad dentro del total de  
homicidios. 2019-2023. 
Variación anual promedio en los homicidios por comuna y 
corregimiento. 2019-2023. 
Número de presuntos feminicidios y variación porcentual con   
respecto al año anterior en Medellín, 2019-2023.
respecto al año anterior en Medellín, 2019-2023.
Hurtos a persona, hurtos de automotores y atraco en todos los  
tipos de hurto por año. 2019-2023.
Denuncias por hurto a personas por hora del día, como 
porcentaje del total de día Comunas 10 -La Candelaria y 14- El 
Poblado. 2019-2023.
Denuncias por hurto a personas por hora del día, como    
porcentaje del total del día. Modalidades de atraco y cosquilleo.  
2019-2023.
Porcentaje de atracos sobre el total de hurtos a persona, motos
y establecimientos comerciales por año. 2019-2023.
Denuncias por todos los tipos de hurto en modalidad atraco por 
comuna. 2019-2023.
Denuncias por hurto de carro y hurto de moto como porcentaje  
del total de hurtos a automotores. 2019-2023.
Participación de cada modalidad de hurto de motos dentro del  
total de hechos para cada una de las cuatro comunas con más 
denuncias. 2019-2023.
Denuncias por ciberdelitos. 2019-2023.
Denuncias por ciberdelitos, por artículo del Código Penal. 2019-
2023.
2023.
Denuncias por extorsión en Medellín 2019-2023 y variación   
porcentual con respecto al año anterior.
Denuncias por secuestro 2019-2023 en Medellín.
Denuncias por secuestro según modalidad 2019-2023.
Número de incautaciones de estupefacientes en Medellín por   
tipo, 2019-2023.
Número de incautaciones de estupefacientes en gramos en Medellín  
por año, 2019-2023.
Número de incautaciones de estupefacientes en unidades en   
Medellín por año, 2019-2023.
Medellín por año, 2019-2023.
Total de estupefacientes incautados en gramos, 2019-2023.
Total de estupefacientes incautados en litros, 2019-2023.
Denuncias por delitos relacionados con instrumentalización de  
niñas, niños y adolescentes, por año. 2019-2023.
Denuncias por delitos relacionados con instrumentalización de 
niñas, niños y adolescentes, por sexo. 2019-2023.
Denuncias por delitos relacionados con instrumentalización de 
niñas, niños y adolescentes, por rango de edad. 2019-2023.
Gráfica 10
Gráfica 10
Gráfica 11
Gráfica 12
Gráfica 13
Gráfica 14
Gráfica 15
Gráfica 16
Gráfica 17
Gráfica 18
Gráfica 19
Gráfica 20
Gráfica 21
Gráfica 22
Gráfica 23
Gráfica 24
Gráfica 25
Gráfica 26
Gráfica 27
Gráfica 28
Gráfica 29
Gráfica 30
Gráfica 31
Gráfica 32
Gráfica 33
84
85
86
90
94
97
98
99
101
102
104
110
111
116
120
121
125
126
126
127
128
135
136
137
```

**PISCC 2024-2027 (posición de página 81)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Gráfica 7 Homicidios por caracterización y rango etario de la víctima. 2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia
(SISC), con información de SIJIN, CTI e INMLCF
81
violencia de género afectan principalmente a las mujeres   jóvenes y adultas (29 
a 59 años). También se observa cómo los adolescentes son más propensos a 
ser víctimas de homicidios asociados a las estructuras criminales y a la violencia
intrafamiliar, mientras que las personas adultas mayores son las víctimas más 
representativas de homicidios por esta última categorización referenciada. Ver 
Gráficas 7 y 8.
2 
2. Se incluye a las mujeres trans.
```

**PISCC 2024-2027 (posición de página 84)**

```text
Tabla de contenido6. Diagnóstico
Fuente: Sistema de Información para la Seguridad y la Convivencia 
(SISC), con información de SIJIN, CTI e INMLCF
Gráfica 10 Participación porcentual de cada caracterización dentro del total de 
homicidios categorizados.  2019-2023
84
Al revisar los homicidios de 2019 a 2023, buena parte de la reducción en los 
hechos de este período de tiempo se explica por la caída en el número de casos 
relacionados con estructuras criminales: mientras que en 2019 se clasificaron 306
homicidios como asociados a estructuras criminales, en 2023 este mismo indicador 
se ubicó en 93. Tal como se observa en la gráfica 10, la participación porcentual de 
estos homicidios dentro del total de casos categorizados pasó de ser del 72% en 
2019 al 39% en 2023. 
En contraste, las categorías que responden a los homicidios interpersonales 
aumentaron su participación. Tal es el caso de los asociados a convivencia, 
que pasaron del 16% al 33%, los homicidios por violencia de género y violencia
intrafamiliar, que aumentaron su participación conjunta del 5% al 12% en el mismo 
periodo; y los casos asociados a hurtos pasando del 7% al 15% entre 2019 y 2023.
Este comportamiento también explica el cambio de tendencia en las principales 
modalidades de homicidio en esos cinco años. Tal como se observa en la Gráfica 
11, la modalidad “arma de fuego” pasó de representar el 67% de los casos en 
2019, a representar el 43% en 2023, mientras que las modalidades cortopunzante
y contundente pasaron del  27% al 50%. Otras modalidades mantuvieron un 
comportamiento similar en el quinquenio. 
Estas dos variables, caracterización y modalidad, guardan una estrecha relación 
4
4. Los homicidios categorizados corresponden al total de homicidios, excluyendo los que se encuentran en proceso de categorización.
```

**PISCC 2024-2027 (posición de página 83)**

```text
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
Fuente: Sistema de Información para la Seguridad y la Convivencia
(SISC), con información de SIJIN, CTI e INMLCF
Gráfica 9 Homicidios por año y variación porcentual con respecto al año 
anterior. 2019-2023
83
poblacional. A esto se suma el aumento de la población habitante de calle en la 
ciudad,  debido a fenómenos sociales que se han dado en los últimos años como 
la pandemia por COVID-19 y la migración.
la pandemia por COVID-19 y la migración.
Los factores anteriormente reseñados han significado un aumento en los hechos 
de violencia homicida hacia las personas habitantes de calle, pasando de 22 hechos 
en 2019 a 30 en 2023, lo que representa un incremento del 36% y ubicando a las 
y los habitantes de calle como el 8% de las víctimas de homicidios en 2023. El 62% 
de los homicidios contra población habitante de calle categorizados estuvieron
asociados a temas de convivencia, el 22% a las estructuras criminales y el 14% a 
hurto.
De forma general, entre 2019 y 2023, en la ciudad de Medellín, 2.136 personas 
perdieron la vida en hechos de violencia homicida. En este periodo de tiempo, 
la victimización se redujo en un 36%, lo que, si bien buena parte de este 
comportamiento se explica por la reducción en los homicidios entre 2019 y 2020 a 
raíz del aislamiento social durante la pandemia del COVID-19, este comportamiento
se mantuvo en los años posteriores hasta lograr una tasa de homicidios de 14.13 en 
2023, la más baja en cinco décadas. El comportamiento de este indicador puede 
apreciarse en la Gráfica 9.
3. Si bien no hay un censo actualizado que permita sustentar esta afirmación, es un análisis en el que coincide la Alcaldía Distrital de Medellín (a través de la
Subsecretaría de Espacio Público y la Unidad de Programas Sociales Especiales [UPSE]). A lo anterior se suma que, en 2019 se tuvo a 5.128 personas en situación 
de calle con atención básica por parte del Distrito, mientras que el promedio de personas atendidas entre 2020 a 2023 fue de 9.117, lo que equivale a un aumento 
del 178%.
3
```

**PISCC 2024-2027 (posición de página 255)**

```text
Tabla 42 Indicadores de resultado componente Seguridad integral para el 
desarrollo social del Plan de Desarrollo Distrital 2024-2027 “Medellín Te Quiere”
Tasa de homicidio
Tasa de hurto a personas
Denuncias por vehículos hurtados
Denuncias por hurto a establecimientos 
comerciales
Índice de victimización Medellín
Victimización por extorsión
Tasa de riñas reportadas
Tasa de feminicidio
Percepción de la seguridad
Denuncias por motocicletas hurtadas
Denuncias por hurto a residencias
Denuncias por hurto a residencias
Tase de lesiones personales
Homicidios por convivencia
Tasa x 
100.000
Tasa x 
100.000
Número
Número
Porcentaje
Porcentaje
Número
Tasa x 
100.000
Porcentaje
Número
Número
Tasa x 
100.000
Número
2023
2023
2023
2023
2023
2023
2023
2023
2023
2023
2023
2023
2023
14,24
1.141
960
2.618
2.618
3
54.516
1,64
43
6.133
1.629
178,88
80
12,82
1.080
864
2.356
20,52
2,76
50.000
1,41
50,7
5.500
1.500
160,7
64
Nombre del indicador
Unidad 
de 
medida
Año línea 
base
Línea 
base
Meta
de 
medida
Año línea 
base
Línea 
base
Meta 
cuatrienio 
2024 -2027
255
Componente estratégico transversal del 
PISCC
A continuación, se presenta el componente estratégico transversal a todas las 
dimensiones identificadas en el PISCC. En este se encuentran los indicadores de 
resultado y producto propuestos en el componente de seguridad integral para el 
desarrollo social del Plan de Desarrollo Distrital 2024-2027 “Medellín Te Quiere”, su
unidad de medida, línea base y meta propuesta para el cuatrienio. Estos indicadores 
generales contribuyen a la gestión local de las problemáticas de seguridad y 
convivencia que afectan al Distrito de Medellín y consolidan la alineación con el 
plan de desarrollo como instrumento de planeación marco que orienta las acciones 
de la Administración Distrital. 
2024 2027/
Plan Integral de Seguridad y Convivencia Ciudadana
```

**PISCC 2024-2027 (posición de página 256)**

```text
Tabla de contenido8. Componente estratégico
Denuncias por delitos vinculados a 
explotación sexual y comercial de niños, 
niñas y adolescentes
Número 2023 170 204
Tabla 43 Indicadores de producto componente Seguridad integral para el 
desarrollo social del Plan de Desarrollo Distrital 2024-2027 “Medellín Te Quiere”
Nombre del indicador
Unidad 
de 
medida
Año línea 
base
Línea 
base
Meta 
cuatrienio 
2024 -2027
Organismos de seguridad y justicia 
fortalecidos
Reportes generados por la toma de
fortalecidos
Reportes generados por la toma de 
decisiones en seguridad y convivencia
Convenios y acuerdos de cooperación para 
el intercambio de información suscritos
Dispositivos tecnológicos instalados para la 
seguridad
Estrategia contra el ciberdelito formulada e 
implementada
Redes de confianza institucional creadas
Victimización por hurto a personas
Plan Maestro en Tecnología de información 
y Telecomunicaciones para la Seguridad 
y la Convivencia 2024-2027 diseñado e 
implementado
implementado
Investigaciones realizadas sobre temas de 
seguridad, convivencia y derechos humanos
Disponibilidad operativa en los subsistemas 
del SIES-M
Central Estratégica y Tecnológica contra 
Atracos creada y operando
Intervenciones territoriales realizadas para la 
seguridad
Equipos especiales creados y operando 
para la prevención y atención del crimen 
organizado y los delitos
Número
Número
Número
Número
Porcentaje
Número
Porcentaje
Porcentaje
Número
Porcentaje
Número
Número
Número
2023
2023
2023
Porcentaje
Número
Número
Número
2023
2023
2023
2023
No aplica
No 
disponible
2023
No aplica
2023
2023
No aplica
2023
No aplica
9
2.551
11
1.348
No aplica
No
disponible
13,16
No aplica
2
94,29
No aplica
121
No aplica
9
8.680
11
2.807
100
21
12,63
100
7
95
1
576
3
Fuente: Elaboración propia 
256
```

**Plan de Desarrollo Distrital 2024-2027 (posición de página 16)**

```text
392
policía del distrito de Medellín, con 90 custo-
dios a cargo (datos al 29/01/2024).
En cuanto a la población reclusa en estos cen-
tros, se observó que en el 2023 el       20.7 %
del total de personas en detención intramural
eran sindicados. De este porcentaje, el 18.3
% correspondía a hombres, con un hacina-
miento del 33.9 %. En estos centros se
detectaron demoras en los horarios del sumi-
nistro de alimentos, porque son elaborados
fuera de la cárcel, poca cantidad en las por-
fuera de la cárcel, poca cantidad en las por-
ciones y ausencia de calidad en las raciones
entregadas (Defensoría del Pueblo, 2024).
A raíz del aumento de la población detenida
preventivamente, el hacinamiento y las condi-
ciones tan complejas para las personas
detenidas en los centros de reclusión transito-
ria y estaciones de policía, la Corte Suprema
de Justicia, a través de la Sentencia
STP14283 de 2019, vinculó al distrito de Me-
dellín con el diseño y la construcción de una
dellín con el diseño y la construcción de una
cárcel metropolitana para población con de-
tención transitoria. Mientras que, por su parte,
la Corte Constitucional de Colombia emitió la
Sentencia SU122/22 de 2022 con otras dispo-
siciones vinculantes para Medellín, en materia
de responsabilidades con respecto a la aten-
ción de la población sindicada.
Indicadores de resultado
Nombre del indicador Unidad demedida Añolínea base Líneabase Metacuatrienio2024-2027 Dependencia oentidad responsable
Tasa de homicidio Tasa x100.000 2023 14,24 12,82 Secretaría de Seguri-dad y Convivencia
Tasa de feminicidios Tasa x100.000 2023 1,64 1,41 Secretaría de Seguri-dad y Convivencia
Tasa de hurto a personas Tasa x100.000 2023 1.141 1.080 Secretaría de Seguri-dad y Convivencia
Percepción de la seguridad Porcentaje 2023 43 50,7 Secretaría de Seguri-dad y Convivencia
Denuncias por vehículos hurtados Número 2023 960 864 Secretaría de Seguri-dad y Convivencia
Denuncias por motocicletas hurtadas Número 2023 6.133 5.500 Secretaría de Seguri-dad y Convivencia
Denuncias por hurto a establecimientos comercia-
les Número 2023 2.618 2.356 Secretaría de Seguri-dad y Convivencia
Denuncias por hurto a residencias Número 2023 1.629 1.500 Secretaría de Seguri-dad y Convivencia
ESTRUCTURA ESTRATÉGICA PLAN DE DESARROLLO DISTRITAL 
Plan de Desarrollo Medellín Te Quiere 2024-2027
PILAR 3
```

</details>

---

## Respuesta 10 (directa)

<!-- trace_id: tr-4da3a9bfc0c8a1ec6f3b29f99204c6ad -->

**Pregunta:** ¿Qué dificultades enfrenta la población desplazada que llega a Medellín, según el PISCC?

**Respuesta esperada:** Además del desplazamiento intraurbano, Medellín es uno de los principales receptores de población desplazada, que enfrenta impactos psicosociales por el cambio de entornos rurales a urbanos: dificultades para conseguir alimentos, un techo digno, acceso a servicios públicos, trabajo y dinero, sumadas a la sensación de desarraigo de no tener un lugar propio.

*Fuente:* PISCC 2024-2027, p. 185

**Respuesta del bot:**

Según el **Plan Integral de Seguridad y Convivencia Ciudadana (PISCC) 2024‑2027**, la población desplazada que llega a Medellín se enfrenta a:

- Un **aumento significativo del desplazamiento forzado intraurbano**, que creció un **280 % en enero 2023 respecto a 2022**.  
  > “intraurbano en Medellín aumentó 280 % en enero 2023 con respecto al 2022.”  

- Un contexto de **desafíos de convivencia** derivados de la combinación de factores sociales, económicos, culturales y ambientales que inciden en la vida cotidiana de los habitantes.  
  > “En conclusión, Medellín enfrenta una serie de desafíos en términos de convivencia que surgen de la combinación de factores sociales, económicos, culturales y ambientales que influyen en la dinámica cotidiana de sus habitantes.”

El documento no detalla de forma explícita otras dificultades específicas (por ejemplo, acceso a vivienda, salud, educación, empleo, etc.). Por lo tanto, la información disponible se limita a los puntos anteriores.

correctness: no

groundedness: no

<details><summary>Ver contexto recuperado</summary>

**PISCC 2024-2027 (posición de página 184)**

```text
Tabla de contenido6. Diagnóstico
Gráfica 51 Número de reportes por desplazamiento forzado en Medellín por año, 
2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC), con información del 
Equipo para la Atención y Reparación de las Víctimas del Conflicto Armado (EARV).
184
Según la fuente de información señalada anteriormente, las comunas de Medellín 
donde más se reportaron casos de desplazamiento forzado, durante 2019 a 2023,
```

**PISCC 2024-2027 (posición de página 284)**

```text
intraurbano en Medellín aumentó 280% en enero 2023 con respecto al 
2022. Personería de Medellín. https://www.personeriamedellin.gov.co/el-
desplazamiento-forzado-intraurbano-en-medellin-aumento-280-en-enero-2023-
con-respecto-al-2022/.
Plataforma Regional de Coordinación Interagencial (R4V). (2023). Análisis de 
las Necesidades de Refugiados y Migrantes (RMNA). https://www.r4v.info/es/
document/rmna-2023-analisis-de-necesidades
PNUD - Programa de las Naciones Unidas para el Desarrollo (2009). Manual
```

**PISCC 2024-2027 (posición de página 206)**

```text
Tabla de contenido6. Diagnóstico
Mapa 15 Número de llamadas reportando basuras por comuna y corregimiento, 
2019-2023
Fuente: Sistema de Información para la Seguridad y la Convivencia (SISC) 
con información del Número Único de Seguridad y Emergencias 123. 
206
En conclusión, Medellín enfrenta una serie de desafíos en términos de convivencia 
que surgen de la combinación de factores sociales, económicos, culturales y 
ambientales que influyen en la dinámica cotidiana de sus habitantes. Ahora bien,
```

**Plan de Desarrollo Distrital 2024-2027 (posición de página 9)**

```text
plazamiento forzado y el despojo y/o
abandono forzado de inmuebles.
- Desplazamiento forzado
Medellín ha sido, de manera histórica, re-
ceptora de población desplazada por el
conflicto armado interno y fenómenos de
violencia en municipios del departamento
de Antioquia y regiones próximas. Asi-
mismo, los grupos delincuenciales de la
ciudad replicaron formas de operar simila-
res al expulsar de sus lugares de
residencia a sectores de la población, es
decir, el desplazamiento se ancló a los
```

</details>

---
