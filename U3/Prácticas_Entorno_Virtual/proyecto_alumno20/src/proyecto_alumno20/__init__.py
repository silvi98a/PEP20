from faker import Faker
from rich.console import Console
from rich.table import Table

def main() -> None:
    fake = Faker("es_ES")
    console = Console()
    table = Table(title="Alumnos ficticios")
    table.add_column("Nombre")
    table.add_column("Correo electrónico")
    for _ in range(5):
        table.add_row(fake.name(), fake.email())
    console.print(table)