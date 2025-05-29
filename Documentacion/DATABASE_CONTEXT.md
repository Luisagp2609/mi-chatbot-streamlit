# Contexto de la Base de Datos - Mercado Eléctrico

## Tabla: pos_generacion

### Descripción General
La tabla `pos_generacion` contiene el histórico de energía otorgada por cada una de las plantas que existen en Panamá. Esta tabla es fundamental para el seguimiento y análisis del mercado eléctrico panameño.

### Estructura de la Tabla
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | int | Identificador único del registro (autoincremental) |
| planta_pos_generacion | varchar(255) | Nombre de la unidad o planta del registro |
| valor_pos_generacion | float | Promedio de energía suministrada durante la hora (MWh) |
| hora_pos_generacion | time | Hora del registro que contempla el comportamiento de la planta |
| fecha_pos_generacion | date | Fecha del registro |
| precio_pos_generacion | float | Costo de la planta o unidad en el mercado spot ($/MWh) |
| datetime_pos_generacion | datetime | Combinación de fecha y hora del registro |

### Notas Importantes

#### Sobre valor_pos_generacion
- Unidad: MWh (Megavatio-hora)
- Valor 0: Indica que la planta no generó energía en esa hora
- Cualquier otro valor: Representa la cantidad de energía generada en MWh

#### Sobre precio_pos_generacion
- Unidad: $/MWh (Dólares por Megavatio-hora)
- Plantas Renovables: Típicamente tienen precio 0
- Plantas Térmicas: Generalmente tienen precios superiores a 100 $/MWh
- Variabilidad: Los precios pueden cambiar debido a:
  - Alzas en los precios del combustible
  - Condiciones meteorológicas
  - Otros factores del mercado

#### Sobre el Seguimiento Temporal
- Cada planta debe tener un registro por hora
- El seguimiento del precio es importante para:
  - Análisis de costos
  - Eficiencia operativa
  - Tendencias del mercado
  - Planificación estratégica

### Relaciones y Dependencias
*[Se completará cuando se documenten las otras tablas]*

### Uso Típico
Esta tabla se utiliza principalmente para:
1. Análisis histórico de generación
2. Seguimiento de precios en el mercado spot
3. Evaluación de la eficiencia de las plantas
4. Planificación de la generación
5. Análisis de costos del sistema eléctrico

### Fuente de Datos
Los datos provienen de los documentos "POSDESPACHO DIARIO", que registran el comportamiento real de las plantas durante el día.

## Tabla: generacion

### Descripción General
La tabla `generacion` contiene la planificación semanal de la energía que se espera sea generada por cada una de las plantas en Panamá. Esta tabla es fundamental para la planificación y gestión del sistema eléctrico.

### Estructura de la Tabla
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | int | Identificador único del registro (autoincremental) |
| planta_generacion | varchar(255) | Nombre de la unidad o planta del registro |
| rango_horario_generacion | varchar(255) | Rango horario del registro planificado |
| valor_generacion | decimal(10,0) | Energía planificada para la hora (MWh) |
| hora_generacion | time | Hora del registro planificado |
| fecha_generacion | date | Fecha del registro planificado |
| precio_generacion | decimal(10,0) | Precio estimado de la planta o unidad ($/MWh) |
| datetime_generacion | datetime | Combinación de fecha y hora del registro |

### Notas Importantes

#### Sobre valor_generacion
- Unidad: MWh (Megavatio-hora)
- Valor 0: Indica que la planta no está planificada para generar en esa hora
- Cualquier otro valor: Representa la cantidad de energía planificada en MWh

#### Sobre precio_generacion
- Unidad: $/MWh (Dólares por Megavatio-hora)
- Plantas Renovables: Típicamente tienen precio 0
- Plantas Térmicas: Generalmente tienen precios superiores a 100 $/MWh
- Variabilidad: Los precios pueden cambiar debido a:
  - Estimaciones de costos de combustible
  - Pronósticos meteorológicos
  - Expectativas del mercado

#### Sobre el Seguimiento Temporal
- Cada planta debe tener un registro por hora
- El seguimiento del precio es importante para:
  - Planificación de costos
  - Optimización de la generación
  - Análisis de tendencias
  - Gestión del sistema

### Relaciones y Dependencias
*[Se completará cuando se documenten las otras tablas]*

### Uso Típico
Esta tabla se utiliza principalmente para:
1. Planificación semanal de la generación
2. Estimación de costos del sistema
3. Optimización de la operación
4. Gestión de recursos
5. Análisis de escenarios

### Fuente de Datos
Los datos provienen de los documentos "PREDESPACHO SEMANAL", que contienen la planificación del comportamiento esperado de las plantas a lo largo de la semana.

### Relación con pos_generacion
- `generacion`: Contiene la planificación semanal (PREDESPACHO)
- `pos_generacion`: Contiene los datos reales diarios (POSDESPACHO)
- La comparación entre ambas tablas permite:
  - Evaluar la precisión de la planificación
  - Identificar desviaciones
  - Mejorar los procesos de planificación
  - Optimizar la operación del sistema

### Diferencias de Formato entre Tablas
Se han identificado las siguientes diferencias en los formatos de datos entre las tablas `pos_generacion` y `generacion`:

| Campo | pos_generacion | generacion | Nota |
|-------|---------------|------------|------|
| valor_* | float | decimal(10,0) | Necesita estandarización |
| precio_* | float | decimal(10,0) | Necesita estandarización |
| rango_horario_* | No existe | varchar(255) | Campo adicional en generacion |

#### Recomendaciones para Estandarización:
1. **Campos numéricos**:
   - Evaluar si mantener `float` o migrar a `decimal(10,0)`
   - Considerar la precisión necesaria para cada tipo de dato
   - Documentar la razón de la elección final

2. **Campo rango_horario**:
   - Evaluar si agregar este campo a `pos_generacion`
   - O si es específico solo para la planificación

3. **Acciones pendientes**:
   - [ ] Decidir el tipo de dato estándar para valores numéricos
   - [ ] Planificar la migración de datos
   - [ ] Actualizar la estructura de las tablas
   - [ ] Actualizar el código de la aplicación 

## Tabla: plantas

### Descripción General
La tabla `plantas` funciona como un catálogo que relaciona cada planta o unidad generadora con su tipo de tecnología. Esta tabla es fundamental para clasificar y categorizar las diferentes fuentes de generación en el sistema eléctrico panameño.

### Estructura de la Tabla
| Campo | Tipo | Descripción |
|-------|------|-------------|
| tipo_plantas | varchar(255) | Tipo de tecnología de generación |
| planta_plantas | varchar(255) | Nombre de la planta o unidad (Clave Primaria) |

### Notas Importantes

#### Sobre tipo_plantas
- Clasifica la tecnología de generación
- Tipos de plantas en el sistema:
  - AUTOGENERACIÓN
  - CONTRATOS
  - GENERACIÓN EÓLICA
  - GENERACIÓN HIDRO
  - GENERACIÓN SOLAR
  - GENERACIÓN TÉRMICA

#### Sobre planta_plantas
- Identificador único de cada planta
- Se usa como clave primaria
- Debe coincidir con los nombres de plantas en otras tablas

### Relaciones y Dependencias
- Se relaciona con `pos_generacion` a través de `planta_pos_generacion`
- Se relaciona con `generacion` a través de `planta_generacion`
- Proporciona el contexto tecnológico para el análisis de generación

### Uso Típico
Esta tabla se utiliza principalmente para:
1. Clasificación de plantas por tecnología
2. Análisis de generación por tipo de tecnología
3. Validación de nombres de plantas
4. Reportes de generación por tecnología
5. Análisis de mix energético

### Importancia en el Sistema
- Permite analizar la composición del parque generador
- Facilita el seguimiento de la generación por tecnología
- Ayuda en la planificación del sistema
- Contribuye al análisis de la matriz energética

### Recomendaciones de Mantenimiento
1. **Actualización de Catálogo**:
   - [ ] Mantener actualizada la lista de tipos de plantas
   - [ ] Documentar nuevos tipos de tecnología
   - [ ] Revisar periódicamente la consistencia de nombres

2. **Estandarización**:
   - [ ] Definir lista estándar de tipos de plantas
   - [ ] Establecer convención de nombres para plantas
   - [ ] Documentar reglas de nomenclatura 

## Tabla: pos_cms

### Descripción General
La tabla `pos_cms` registra información crítica del mercado eléctrico panameño, incluyendo la demanda, exportaciones, flujos de transmisión y el Costo Marginal del Sistema (CMS). Esta tabla es fundamental para el análisis del mercado spot y la operación del sistema eléctrico.

### Estructura de la Tabla
| Campo | Tipo | Descripción |
|-------|------|-------------|
| planta_pos_cms | varchar(255) | Tipo de registro o variable del sistema |
| valor_pos_cms | float | Valor del registro |
| hora_pos_cms | time | Hora del registro |
| fecha_pos_cms | date | Fecha del registro |
| datetime_pos_cms | datetime | Combinación de fecha y hora del registro |

### Tipos de Registros (planta_pos_cms)
1. **Carga Real**
   - Representa la demanda real de energía de la ciudad
   - Unidad: MW
   - Importancia: Indica el consumo real del sistema

2. **Exportación**
   - Energía exportada a países vecinos
   - Unidad: MW
   - Importancia: Muestra el intercambio internacional de energía

3. **Generación**
   - Suma de Carga Real más Exportación
   - Unidad: MW
   - Importancia: Representa la generación total requerida

4. **Flujo de Potencia Limitado (MW)**
   - Límite de capacidad de la línea de transmisión
   - Unidad: MW
   - Importancia: Restricción operativa del sistema

5. **Flujo de Potencia Real (MW)**
   - Flujo actual en la línea de transmisión
   - Unidad: MW
   - Importancia: Monitoreo de la operación

6. **CMS (B./)**
   - Costo Marginal del Sistema
   - Unidad: B/. (Balboas)
   - Importancia: Precio spot del mercado eléctrico

### Notas Importantes

#### Sobre el CMS
- Es la variable más importante del mercado
- Indica el precio spot de la energía
- Determina el costo de compra/venta de energía
- Refleja las condiciones del mercado en tiempo real

#### Sobre los Flujos de Potencia
- Monitorean la línea de transmisión Este-Oeste
- Evitan sobrecargas en el sistema
- Son críticos para la operación segura
- Requieren monitoreo constante

### Relaciones y Dependencias
- Se relaciona con `pos_generacion` para análisis de precios
- Complementa la información de generación
- Proporciona contexto para decisiones de mercado

### Uso Típico
Esta tabla se utiliza principalmente para:
1. Análisis del mercado spot
2. Monitoreo de la demanda
3. Control de flujos de transmisión
4. Seguimiento de exportaciones
5. Toma de decisiones operativas

### Importancia en el Sistema
- Permite el análisis del mercado en tiempo real
- Facilita la toma de decisiones operativas
- Contribuye a la seguridad del sistema
- Ayuda en la planificación de la operación

### Recomendaciones de Mantenimiento
1. **Monitoreo de Datos**:
   - [ ] Verificar consistencia de los flujos de potencia
   - [ ] Validar cálculos de CMS
   - [ ] Revisar registros de exportación

2. **Análisis de Tendencias**:
   - [ ] Seguimiento de precios spot
   - [ ] Monitoreo de flujos de transmisión
   - [ ] Análisis de patrones de demanda 

### Relación con cms
- `pos_cms`: Contiene los datos reales del sistema (POSDESPACHO)
- `cms`: Contiene la planificación semanal (PREDESPACHO)

#### Diferencias de Formato entre Tablas
Se han identificado las siguientes diferencias en los formatos de datos entre las tablas `pos_cms` y `cms`:

| Campo | pos_cms | cms | Nota |
|-------|---------|-----|------|
| valor_* | float | decimal(10,0) | Necesita estandarización |
| rango_horario_* | No existe | varchar(255) | Campo adicional en cms |

#### Diferencias en Tipos de Registros
1. **Registros Comunes**:
   - Carga Real
   - CMS (B./)
   - Exportación
   - Generación

2. **Registros Específicos de cms**:
   - Max Falla Simple (MW)
   - R Disponible (MW) - Reserva rodante para contingencias

#### Recomendaciones para Estandarización:
1. **Campos numéricos**:
   - [ ] Decidir entre `float` y `decimal(10,0)` para valores
   - [ ] Mantener consistencia con otras tablas del sistema

2. **Campo rango_horario**:
   - [ ] Evaluar si agregar este campo a `pos_cms`
   - [ ] O si es específico solo para la planificación

3. **Acciones pendientes**:
   - [ ] Estandarizar tipos de datos
   - [ ] Revisar necesidad de campos adicionales
   - [ ] Actualizar estructura de las tablas
   - [ ] Actualizar el código de la aplicación 

## Tablas de Niveles de Embalse

### Descripción General
Las tablas `bayano_msnm` y `fortuna_msnm` registran los niveles de agua de dos importantes plantas hidroeléctricas de embalse en Panamá. Estas plantas son fundamentales para el sistema eléctrico nacional debido a su capacidad de regulación mayor a 90 días, funcionando como "baterías energéticas" del país.

### Estructura de las Tablas

#### Tabla: bayano_msnm
| Campo | Tipo | Descripción |
|-------|------|-------------|
| bayano_msnm_id | int | Identificador único del registro (autoincremental) |
| valor_bayano_msnm | decimal(10,0) | Nivel del embalse en metros sobre el nivel del mar (msnm) |
| fecha_bayano_bayano_msnm | date | Fecha del registro |

#### Tabla: fortuna_msnm
| Campo | Tipo | Descripción |
|-------|------|-------------|
| fortuna_msnm_id | int | Identificador único del registro (autoincremental) |
| valor_fortuna_msnm | decimal(10,0) | Nivel del embalse en metros sobre el nivel del mar (msnm) |
| fecha_fortuna_fortuna_msnm | date | Fecha del registro |

### Notas Importantes

#### Sobre los Embalses
- **Capacidad de Regulación**: > 90 días
- **Función**: Actúan como "baterías energéticas" del sistema
- **Importancia**: 
  - Almacenamiento de energía
  - Regulación del sistema
  - Respuesta a contingencias
  - Gestión de recursos hídricos

#### Sobre los Niveles (msnm)
- Unidad: metros sobre el nivel del mar
- Monitoreo: Fundamental para:
  - Planificación de generación
  - Gestión de recursos hídricos
  - Prevención de contingencias
  - Optimización de operación

### Relaciones y Dependencias
- Se relacionan con la planificación de generación
- Influyen en las decisiones operativas del sistema
- Afectan la disponibilidad de energía hidroeléctrica

### Uso Típico
Estas tablas se utilizan principalmente para:
1. Monitoreo de niveles de embalse
2. Planificación de generación hidroeléctrica
3. Gestión de recursos hídricos
4. Análisis de disponibilidad de energía
5. Toma de decisiones operativas

### Importancia en el Sistema
- Permiten la gestión eficiente de recursos hídricos
- Facilitan la planificación de generación
- Contribuyen a la seguridad del sistema
- Ayudan en la optimización de la operación

### Recomendaciones de Mantenimiento
1. **Monitoreo de Datos**:
   - [ ] Verificar consistencia de los niveles
   - [ ] Validar rangos de operación
   - [ ] Revisar tendencias de niveles

2. **Análisis de Tendencias**:
   - [ ] Seguimiento de niveles históricos
   - [ ] Monitoreo de patrones estacionales
   - [ ] Análisis de correlación con generación 