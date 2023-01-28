cambios en el modelo de django:
    <!-- genera la migracion -->
    python manage.py makemigrations <nombreApp> 
    <!-- nos muestra el SQL generado por la migracion -->
    python manage.py sqlmigrate <nombreApp>  <numeroMigracion>
    <!-- efectua los cambios en la base de datos-->
    python manage.py migrate


la logica va en:
    <!-- DUH... esperaba que sea en los services, pero no hay-->
    los modelos
    
    <!-- ver que son -->
    signals