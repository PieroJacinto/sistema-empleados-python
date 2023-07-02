CREATE database IF NOT EXISTS empleados;
use empleados;

CREATE TABLE IF NOT EXISTS empleados (
	id INT NOT NULL auto_increment,
	nombre varchar(255),
	correo varchar(255),
	foto varchar(5000),
	PRIMARY key(id)
);

-- INSERT INTO empleados(nombre, correo, foto) VALUES('test', 'test@gmail.com', 'foto.jpg');
-- SELECT * FROM empleados;