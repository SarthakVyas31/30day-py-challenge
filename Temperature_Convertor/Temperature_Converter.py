import typer
from rich.console import Console
from rich.table import Table

from model import TempConv
from database import insert_conversion, get_all_conversion

app = typer.Typer()
console = Console()

@app.command()
def convert(value: float, from_unit: str, to_unit: str):
    result = None
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        result = value
    elif from_unit == 'C' and to_unit == 'F':
        result = (value * 9/5)+32
    elif from_unit == 'C' and to_unit == 'K':
        result = value + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        result = (value - 32)*5/9
    elif from_unit == 'F' and to_unit == 'K':
        result = ((value -32) * 5/9)+273.15 
    elif from_unit == 'K' and to_unit == 'C':
        result = value - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        result = ((value - 273.15)* 9/5)+32
    else:
        console.print("[red]Invalid Conversion Unit [/red]")
    
    conversion = TempConv(value , from_unit , to_unit, round(result,2))
    insert_conversion(conversion)
    console.print(f"[bold green]{value} {from_unit} = {round(result,2)} {to_unit}[/bold green]")

@app.command()
def history():
    conversions = get_all_conversion()
    table = Table(title= "Conversion Log Book")
    table.add_column("Value")
    table.add_column("From")
    table.add_column("Result")
    table.add_column("To")

    for c in conversions:
        table.add_row(str(c.value), c.from_unit, str(c.result), c.to_unit)  

    console.print(table)


if __name__ == "__main__":
    app()