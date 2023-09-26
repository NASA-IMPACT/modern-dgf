from typing import Optional
from rich.console import Console
from rich.table import Table

import typer

app = typer.Typer(
    help="CLI to tailor the mDGF framework to your project-specific needs."
)

console = Console()

ENTITIES = ["Data", "Metadata", "Digital Content", "Code", "Storage", "People"]
ACTIVITIES = [
    "1. Plan/Design",
    "2. Gen/Curation",
    "3. Sharing",
    "4. Use/Reuse",
    "5. Preservation",
    "6. Monitoring",
]


@app.command()
def wizard():
    """
    Answer some simple questions to tailor the mDGF framework to your project.
    """
    table = Table("Entities \u2193 / Activities \u2192", *ACTIVITIES)

    for index, entity in enumerate(ENTITIES):
        index += 1
        if entity == "People":
            codes = ["6.1"]
        else:
            codes = [f"{index}.{subindex}" for subindex in range(1, 7)]
        table.add_row(f"{index}. {entity}", *codes)

    console.print(table)


if __name__ == "__main__":
    app()
