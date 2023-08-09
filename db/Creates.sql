CREATE DATABASE TechCo;

CREATE TABLE TCInventory (
    Inventory_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Quantity INT,
    Reposition_Date smalldatetime
);

CREATE TABLE TCProduct (
    Product_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Product_Name nvarchar(100) UNIQUE NOT NULL,
    Description nvarchar(500),
    Price MONEY,
    FK_Inventory_Id INT,
    CONSTRAINT FK_Producto_Inventory FOREIGN KEY (FK_Inventory_Id)
    REFERENCES TCInventory(Inventory_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE TCOrder (
    Order_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Order_Date smalldatetime NOT NULL,
    Order_Quantity INT NOT NULL, 
    FK_User_Id INT,
    FK_Product_Id INT,
    CONSTRAINT FK_Order_User FOREIGN KEY (FK_User_Id)
    REFERENCES auth_user(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT FK_Order_Product FOREIGN KEY (FK_Product_Id)
    REFERENCES TCProduct(Product_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE TCShopping_Cart (
    Cart_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Cart_Quantity INT,
    FK_User_Id INT,
    FK_Product_Id INT,
    CONSTRAINT FK_ShoppingCt_User FOREIGN KEY (FK_User_Id)
    REFERENCES auth_user(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT FK_ShoppingCt_Product FOREIGN KEY (FK_Product_Id)
    REFERENCES TCProduct(Product_Id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);