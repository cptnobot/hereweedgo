from app import create_app, db
from app.models import User, Product

app = create_app()

with app.app_context():
    # Añadir un usuario de ejemplo si no existe
    if User.query.filter_by(username='admin').first() is None:
        admin = User(username='admin', email='admin@example.com')
        admin.set_password('password123')
        admin.is_admin = True
        db.session.add(admin)
        db.session.commit()
        print("Usuario admin añadido ✅")

    # Actualizar o añadir productos
    products_data = [
        {
            "id": 1,
            "name": "Mantequilla Canábica",
            "description": "Mantequilla infusionada con cannabis, perfecta para cocinar",
            "price": 60000.0,
            "stock": 50,
            "image": "images/products/product1.jpg"
        },
        {
            "id": 2,
            "name": "Brownie con Cannabis",
            "description": "Brownie relajante con infusión de cannabis",
            "price": 20000.0,
            "stock": 30,
            "image": "images/products/product2.jpg"
        }
    ]

    for product_data in products_data:
        product = db.session.get(Product, product_data["id"])
        if product:
            # Actualizar producto existente
            product.name = product_data["name"]
            product.description = product_data["description"]
            product.price = product_data["price"]
            product.stock = product_data["stock"]
            product.image = product_data["image"]
        else:
            # Añadir nuevo producto
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                stock=product_data["stock"],
                image=product_data["image"]
            )
            db.session.add(product)

    try:
        db.session.commit()
        print("Productos actualizados/añadidos ✅")
    except Exception as e:
        db.session.rollback()
        print(f"Error al actualizar productos: {str(e)}")