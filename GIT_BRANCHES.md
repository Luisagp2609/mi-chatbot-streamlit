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

### Eliminar ramas
```bash
# Eliminar una rama local
git branch -d nombre-rama

# Forzar la eliminación de una rama local (si tiene cambios no fusionados)
git branch -D nombre-rama

# Eliminar una rama remota
git push origin --delete nombre-rama
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

## Ejemplo Práctico: Creación y Manejo de Ramas

### 1. Crear una nueva rama
```bash
git checkout -b feature/dashboard    # Crear y cambiar a nueva rama
```

### 2. Trabajar en la rama
```bash
# Crear un nuevo archivo
touch GIT_BRANCHES.md

# Agregar cambios
git add GIT_BRANCHES.md

# Guardar cambios
git commit -m "Agregar guía de uso de ramas en Git"

# Subir cambios a GitHub
git push origin feature/dashboard
```

### 3. Fusionar con main
```bash
# Cambiar a main
git checkout main

# Fusionar cambios
git merge feature/dashboard

# Subir cambios fusionados
git push origin main
```

### 4. Eliminar la rama
```bash
# Eliminar la rama local
git branch -d feature/dashboard

# Eliminar la rama remota
git push origin --delete feature/dashboard
```

### 5. Verificar estado
```bash
# Ver en qué rama estamos
git branch

# Ver estado actual
git status
```

## Notas importantes
- Usar `git reset --hard` elimina cambios permanentemente
- Usar `git push -f` reescribe la historia en GitHub
- Siempre verificar en qué rama estamos antes de hacer cambios
- Mantener un registro de los commits importantes 