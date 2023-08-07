--INVENTORY
SET IDENTITY_INSERT B2B.TCInventory ON;

INSERT INTO B2B.TCInventory(
	Inventory_Id,
	Quantity	
    )
VALUES 
(1,20),
(2,6),
(3,55),
(4,10),
(5,0)

SET IDENTITY_INSERT B2B.TCInventory OFF;

--PRODUCT
SET IDENTITY_INSERT B2B.TCProduct ON;

INSERT INTO B2B.TCProduct(
	Product_Id,
	Product_Name,
	Description,
	FK_Inventory_Id
	)
VALUES 
(1,'Desodorante','El Antitranspirante Roll Farmatodo mantiene su piel seca, dando protección continua.',1),
(2,'Crema Dental','Protege tu salud bucal y la de toda tu familia, brindándoles la confianza que necesitan, manteniendo un aliento súper fresco por mucho más tiempo',2),
(3,'Cepillo Dental','Proporciona una limpieza profunda y genera espuma superior al mismo tiempo. Su diseño innovador incluye un mango ergonómico y cerdas súper densas.',3),
(4,'Refresco','Refresco sabor a cola negra 2lts',4),
(5,'Snack Doritos Mega Queso','Hojuelas de maíz tostadas con sabor a queso',5)

SET IDENTITY_INSERT B2B.TCProduct OFF;

--USER
SET IDENTITY_INSERT B2B.TCUser ON;

INSERT INTO B2B.TCUser(
	User_Id,
	First_Name,
    Family_Name,
    Telephone,
    Email,
    Password,
    Rol	
    )
VALUES 
(1,'Hilery', 'Guedez', '9323321', 'hileryguedez@gmail.com', '123456', 'user'),
(2,'Alejandro', 'Melendez', '1378301', 'amelendez@tribuco.mx', '123456', 'admin')

SET IDENTITY_INSERT B2B.TCUser OFF;

--ORDER
SET IDENTITY_INSERT B2B.TCOrder ON;

INSERT INTO B2B.TCOrder(
	Order_Id,
    Order_Quantity,
	Order_Date,
    FK_User_Id,
    FK_Product_Id
    )
VALUES 
(1, 12, '2023-08-06', 1, 1),
(2, 1, '2023-08-07', 2, 2),
(3, 5, '2023-08-07', 2, 4)

SET IDENTITY_INSERT B2B.TCOrder OFF;