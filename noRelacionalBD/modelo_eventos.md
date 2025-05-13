## Tipos de eventos:
- `venta_realizada`
- `stock_bajo`
- `producto_agotado`
- `nueva_compra`
- `producto_agregado`
- `usuario_creado`
- `login_fallido`

### Modelo `venta_realizada`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        mensaje: string,
        precio_total: float
        vendedor: string,
        id_venta: int
    }
]
```
### Modelo `stock_bajo`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        mensaje: string, 
        id_producto: int,
        stock: int 
    }
]
```
### Modelo `producto_agotado`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        mensaje: string,
        id_producto: int
    }
]
```
### Modelo `nueva_compra`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        id_proveedor: int,
        mensaje: string,
        id_compra: int
    }
]
```
### Modelo `producto_agregado`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        mensaje: string,
        id_producto: int,
        id_categoria: int
    }
]
```
### Modelo `usuario_creado`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        mensaje: string,
        id_trabajador: int,
        rol: string
    }
]
```
### Modelo `login_fallido`:
```
[
    {
        id_evento: int,
        tipo_evento: string,
        fecha_hora: timestamp (string),
        mensaje: string,
        nombre_usuario: string
    }
]
```