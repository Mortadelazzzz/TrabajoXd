CREATE USER 'usuario_prueba'@'192.168.100.52' IDENTIFIED BY 'Balinsa2023';
GRANT ALL PRIVILEGES ON bd_proyectosullana.* TO 'usuario_prueba'@'192.168.100.52';
FLUSH PRIVILEGES;
