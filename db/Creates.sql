CREATE SCHEMA B2B;

CREATE TABLE B2B.Inventario (
    Inventario_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Cantidad INT,
    Fecha_Reposicion smalldatetime
);

CREATE TABLE B2B.Producto (
    Producto_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Nombre_Producto nvarchar(100) NOT NULL,
    Descripcion nvarchar(500),
    FK_Inventario_Id INT,
    CONSTRAINT FK_Inventario_Producto FOREIGN KEY (FK_Inventario_Id)
    REFERENCES B2B.Inventario(Inventario_Id),
);

CREATE TABLE B2B.Usuario (
    Usuario_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Primer_Nombre nvarchar(100) NOT NULL,
    Primer_Apellido nvarchar(100) NOT NULL,
    Telefono nvarchar(100) NOT NULL,
    Email nvarchar(255) NOT NULL,
    Clave nvarchar(255) NOT NULL,
    Rol nvarchar(50) NOT NULL
);

CREATE TABLE B2B.Orden (
    Orden_Id INT NOT NULL IDENTITY PRIMARY KEY,
    Fecha_Orden smalldatetime NOT NULL,
    Cantidad_Ordenada INT NOT NULL, 
    FK_Usuario_Id INT,
    FK_Producto_Id INT,
    CONSTRAINT FK_Orden_Usuario FOREIGN KEY (FK_Usuario_Id)
    REFERENCES B2B.Usuario(Usuario_Id),
    CONSTRAINT FK_Orden_Producto FOREIGN KEY (FK_Producto_Id)
    REFERENCES B2B.Producto(Producto_Id)
);
