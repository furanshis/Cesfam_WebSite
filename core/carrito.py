class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")

        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, remedio):
        id = str(remedio.idRemedio)
        
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id" : remedio.idRemedio,
                "nombre_carrito" : remedio.nombreRemedio,
                "precio_producto": remedio.precioProducto,
                "precio_acumulado" : remedio.precioRemedio,
                "descripcion_producto" : remedio.descripcionRemedio,
                "cantidad" : 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio_acumulado"] += remedio.precioRemedio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self,remedio):
        id = str(remedio.idRemedio)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, remedio):
        id = str(remedio.idRemedio)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio_acumulado"] -= remedio.precioRemedio
            if self.carrito[id]["cantidad"] == 0:
                self.eliminar(remedio)
            
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
