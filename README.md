# Proyecto guiado – Sistema de Gestión de Inventario para emprendimientos locales

## 1. Contexto General

Muchos negocios locales (como minimarkets, ferreterías, librerías o farmacias) no cuentan con sistemas digitales para controlar su inventario, sus proveedores ni su personal. Llevan registros en papel o planillas, lo que genera errores, pérdida de información y dificultades para hacer seguimiento de las operaciones.
El objetivo de este proyecto es diseñar e implementar un sistema funcional y simple de gestión de inventario, combinando una base de datos relacional y una base no relacional, y luego desarrollar una API web y un cliente para interactuar con dicho sistema.

## 2. Funcionalidades esperadas

- Registrar y consultar productos, categorías, proveedores y usuarios (trabajadores).

- Registrar compras y ventas, manteniendo actualizado el stock.

- Controlar que el stock no caiga por debajo de un mínimo establecido.

- Llevar un historial de eventos importantes del sistema (en una base no relacional).

- Asociar cada venta o compra a la persona que la realizó (vendedor o encargado).

- Consultar información clave mediante SQL y también mediante consultas en MongoDB o Redis.

## 3. Base de Datos Relacional

Tu sistema debe incluir al menos las siguientes entidades:

- **Catálogo de productos:** nombre, descripción, categoría, precio unitario, unidad de medida, stock actual, stock mínimo permitido.

- **Categorías de productos:** por ejemplo, abarrotes, limpieza, ferretería.

- **Proveedores:** datos de contacto, productos que proveen.

- **Trabajadores:** nombre, correo, rol (vendedor, administrador, etc.).

- **Compras:** fecha, proveedor, productos comprados y cantidades.

- **Ventas:** fecha, productos vendidos, cantidades, total y vendedor responsable.

Todas las relaciones deben estar normalizadas y tener claves primarias y foráneas apropiadas.

## 4. Base de Datos No Relacional (MongoDB o Redis)

Se utilizará una base de datos no relacional para almacenar eventos del sistema. Esto permite tener una auditoría flexible de lo que ocurre dentro del sistema sin sobrecargar el modelo relacional.

### ¿Qué es un evento del sistema?

Un evento representa algo que ocurrió en el sistema y que podría interesar al administrador del local. No es una transacción en sí misma, sino un registro para tener trazabilidad o para posibles futuras automatizaciones o notificaciones.