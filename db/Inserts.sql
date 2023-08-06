--INVENTARIO
SET IDENTITY_INSERT B2B.Inventario ON;

INSERT INTO B2B.Inventario(
	Inventario_Id,
	Cantidad	
    )
VALUES 
(1,20),
(2,6),
(3,55),
(4,10),
(5,1)

SET IDENTITY_INSERT B2B.Inventario OFF;

--PRODUCTO
SET IDENTITY_INSERT B2B.Producto ON;

INSERT INTO B2B.Producto(
	Producto_Id,
	Nombre_Producto,
	Descripcion,
	FK_Inventario_Id
	)
VALUES 
(1,'Desodorante','El Antitranspirante Roll Farmatodo mantiene su piel seca, dando protección continua.',1),
(2,'Crema Dental','Protege tu salud bucal y la de toda tu familia, brindándoles la confianza que necesitan, manteniendo un aliento súper fresco por mucho más tiempo',2),
(3,'Cepillo Dental','Proporciona una limpieza profunda y genera espuma superior al mismo tiempo. Su diseño innovador incluye un mango ergonómico y cerdas súper densas.',3),
(4,'Refresco','Refresco sabor a cola negra 2lts',4),
(5,'Snack Doritos Mega Queso','Hojuelas de maíz tostadas con sabor a queso',5)

SET IDENTITY_INSERT B2B.Producto OFF;

--USUARIO
SET IDENTITY_INSERT B2B.Usuario ON;

INSERT INTO B2B.Usuario(
	Usuario_Id,
	Primer_Nombre,
    Primer_Apellido,
    Telefono,
    Email,
    Clave,
    Rol	
    )
VALUES 
(1,'Hilery', 'Guedez', '9323321', 'hileryguedez@gmail.com', '123456', 'user'),
(2,'Alejandro', 'Melendez', '1378301', 'amelendez@tribuco.mx', '123456', 'admin')

SET IDENTITY_INSERT B2B.Usuario OFF;

--ORDEN
SET IDENTITY_INSERT B2B.Orden ON;

INSERT INTO B2B.Orden(
	Orden_Id,
    Cantidad_Ordenada,
	Fecha_Orden,
    FK_Usuario_Id,
    FK_Producto_Id
    )
VALUES 
(1, 12, '2023-08-06', 1, 1),
(2, 1, '2023-08-07', 2, 2),
(3, 5, '2023-08-07', 2, 4)

SET IDENTITY_INSERT B2B.Orden OFF;