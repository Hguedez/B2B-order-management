CREATE SCHEMA B2B;

CREATE TABLE B2B.TCInventory (
    Inventory_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Quantity INT,
    Reposition_Date smalldatetime
);

CREATE TABLE B2B.TCProduct (
    Product_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Product_Name nvarchar(100) UNIQUE NOT NULL,
    Description nvarchar(500),
    FK_Inventory_Id INT,
    CONSTRAINT FK_Producto_Inventory FOREIGN KEY (FK_Inventory_Id)
    REFERENCES B2B.TCInventory(Inventory_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE B2B.TCUser (
    User_Id INT NOT NULL IDENTITY PRIMARY KEY,
    First_Name nvarchar(100) NOT NULL,
    Family_Name nvarchar(100) NOT NULL,
    Telephone nvarchar(100) NOT NULL,
    Email nvarchar(255) UNIQUE NOT NULL,
    Password nvarchar(255) NOT NULL,
    Rol nvarchar(50) NOT NULL
);

CREATE TABLE B2B.TCOrder (
    Order_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Order_Date smalldatetime NOT NULL,
    Order_Quantity INT NOT NULL, 
    FK_User_Id INT,
    FK_Product_Id INT,
    CONSTRAINT FK_Orden_Usuario FOREIGN KEY (FK_User_Id)
    REFERENCES B2B.TCUser(User_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT FK_Order_Product FOREIGN KEY (FK_Product_Id)
    REFERENCES B2B.TCProduct(Product_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);