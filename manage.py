from app import create_app, db
import click

app = create_app()

@app.cli.command("init-db")
def init_db():
    """Crear tablas iniciales."""
    with app.app_context():
        db.create_all()
        click.echo("Base de datos inicializada ✅")
