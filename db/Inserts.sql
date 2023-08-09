--INVENTORY
SET IDENTITY_INSERT TCInventory ON;

INSERT INTO TCInventory(
	Inventory_Id,
	Quantity	
    )
VALUES 
(1,20),
(2,6),
(3,55),
(4,10),
(5,0)

SET IDENTITY_INSERT TCInventory OFF;

--PRODUCT
SET IDENTITY_INSERT TCProduct ON;

INSERT INTO TCProduct(
	Product_Id,
	Product_Name,
	Description,
    Price,
	FK_Inventory_Id
	)
VALUES 
(1,'Desodorante','El Antitranspirante Roll Farmatodo mantiene su piel seca, dando protección continua.',55,1),
(2,'Crema Dental','Protege tu salud bucal y la de toda tu familia, brindándoles la confianza que necesitan, manteniendo un aliento súper fresco por mucho más tiempo',10,2),
(3,'Cepillo Dental','Proporciona una limpieza profunda y genera espuma superior al mismo tiempo. Su diseño innovador incluye un mango ergonómico y cerdas súper densas.',132,3),
(4,'Refresco','Refresco sabor a cola negra 2lts',5,4),
(5,'Snack Doritos Mega Queso','Hojuelas de maíz tostadas con sabor a queso',28,5)

SET IDENTITY_INSERT TCProduct OFF;

--ORDER
SET IDENTITY_INSERT TCOrder ON;

INSERT INTO TCOrder(
	Order_Id,
    Order_Quantity,
	Order_Date,
    FK_User_Id,
    FK_Product_Id
    )
VALUES 
(1, 12, '2023-08-06', 1, 1),
(2, 1, '2023-08-07', 1, 2)

SET IDENTITY_INSERT TCOrder OFF;