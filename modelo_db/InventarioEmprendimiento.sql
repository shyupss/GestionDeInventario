CREATE TABLE "productos" (
  "id_producto" integer PRIMARY KEY,
  "nombre" varchar(100),
  "descripcion" text,
  "precio_unitario" numeric(10,2),
  "unidad_medida" varchar(100),
  "stock" integer,
  "min_stock" integer,
  "id_categoria" integer NOT NULL
);

CREATE TABLE "categorias" (
  "id_categoria" integer PRIMARY KEY,
  "nombre" varchar(100)
);

CREATE TABLE "proveedores" (
  "id_proveedor" integer PRIMARY KEY,
  "nombre" varchar(100),
  "correo" varchar(100),
  "telefono" varchar(100)
);

CREATE TABLE "trabajador" (
  "id_trabajador" integer PRIMARY KEY,
  "nombre" varchar(100),
  "telefono" varchar(100),
  "correo" varchar(100),
  "rol" varchar(100)
);

CREATE TABLE "compras" (
  "id_compra" integer PRIMARY KEY,
  "fecha" timestamp,
  "precio_total" numeric(10,2),
  "id_proveedor" integer NOT NULL
);

CREATE TABLE "ventas" (
  "id_venta" integer PRIMARY KEY,
  "fecha" timestamp,
  "precio_total" numeric(10,2),
  "id_vendedor" integer NOT NULL
);

CREATE TABLE "productos_ventas" (
  "id_producto" integer NOT NULL,
  "id_venta" integer NOT NULL,
  "precio_unitario" numeric(10,2),
  "cantidad" integer,
  "primary" key(id_producto,id_venta)
);

CREATE TABLE "productos_compras" (
  "id_producto" integer NOT NULL,
  "id_compra" integer NOT NULL,
  "precio_unitario" numeric(10,2),
  "cantidad" integer,
  "primary" key(id_producto,id_venta)
);

ALTER TABLE "productos" ADD FOREIGN KEY ("id_categoria") REFERENCES "categorias" ("id_categoria");

ALTER TABLE "compras" ADD FOREIGN KEY ("id_proveedor") REFERENCES "proveedores" ("id_proveedor");

ALTER TABLE "ventas" ADD FOREIGN KEY ("id_vendedor") REFERENCES "trabajador" ("id_trabajador");

ALTER TABLE "productos_ventas" ADD FOREIGN KEY ("id_producto") REFERENCES "productos" ("id_producto");

ALTER TABLE "productos_ventas" ADD FOREIGN KEY ("id_venta") REFERENCES "ventas" ("id_venta");

ALTER TABLE "productos_compras" ADD FOREIGN KEY ("id_producto") REFERENCES "productos" ("id_producto");

ALTER TABLE "productos_compras" ADD FOREIGN KEY ("id_compra") REFERENCES "compras" ("id_compra");
