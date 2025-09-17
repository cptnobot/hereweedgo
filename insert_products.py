from app import create_app, db
from app.models import Product

def insert_products():
    try:
        app = create_app()  # Crear la instancia de la aplicación
        with app.app_context():
            if Product.query.count() == 0:
                products = [
                    Product(
                        name="Mantequilla Mágica",
                        description="Mantequilla infusionada con cannabis, perfecta para cocinar.",
                        price=25.0,
                        image="images/products/product1.jpg",  # Ruta relativa desde static
                        stock=10
                    ),
                    Product(
                        name="Brownie de CBD",
                        description="Brownie relajante con 10mg de CBD por unidad.",
                        price=15.0,
                        image="images/products/product2.jpg",  # Ruta relativa desde static
                        stock=20
                    ),
                ]
                db.session.add_all(products)
                db.session.commit()
                print("Productos añadidos ✅")
            else:
                print("Ya existen productos en la base de datos.")
    except Exception as e:
        print(f"Error al insertar productos: {str(e)}")

if __name__ == "__main__":
    insert_products()