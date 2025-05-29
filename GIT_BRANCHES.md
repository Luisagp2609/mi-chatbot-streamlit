# Guía de Ramas en Git

## ¿Qué son las ramas?
Las ramas en Git son como líneas de desarrollo independientes. Te permiten trabajar en nuevas características sin afectar el código principal.

## Beneficios de usar ramas
1. **Desarrollo seguro**: Puedes experimentar sin arruinar el código estable
2. **Trabajo en equipo**: Múltiples desarrolladores pueden trabajar en diferentes características
3. **Organización**: Cada característica o corrección puede tener su propia rama
4. **Control de versiones**: Fácil de revertir cambios si algo sale mal

## Comandos básicos de ramas

### Ver ramas
```bash
git branch              # Lista todas las ramas locales
git branch -a          # Lista todas las ramas (locales y remotas)
```

### Crear y cambiar de rama
```bash
git checkout -b nombre-rama    # Crea y cambia a una nueva rama
git checkout nombre-rama       # Cambia a una rama existente
```

### Trabajar en una rama
```bash
git add .                      # Agregar cambios
git commit -m "mensaje"        # Guardar cambios
git push origin nombre-rama    # Subir cambios a GitHub
```

### Fusionar ramas
```bash
git checkout main             # Ir a la rama principal
git merge nombre-rama         # Traer cambios de otra rama
```

## Buenas prácticas
1. Usar nombres descriptivos para las ramas
2. Mantener las ramas actualizadas con main
3. Eliminar ramas después de fusionarlas
4. Hacer commits pequeños y descriptivos

## Ejemplo de flujo de trabajo
1. Crear una rama para una nueva característica
2. Desarrollar y probar en la rama
3. Hacer commits regularmente
4. Fusionar con main cuando esté lista
5. Eliminar la rama después de fusionar 