from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print

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
    options_selected = Prompt.ask(
        """Please enter codes for relevant documents to your project. All other documents will be deselected.

Select all documents for all entities by typing in "all".

Select all documents for an entity by typing in a whole number. For example, 1 will select all documents for the entity "Data".

Select individual documents by typing in a decimal number. For example, 1.1 will select the first activity for the entity "Data".

Select multiple documents by typing in a comma-separated list of numbers.

Deselect a document by typing in a negative number. For example, -1 will deselect all documents for the entity "Data". -2.1 will Deselct the first document for the entity "Metadata".

Example input: all
Example input: 1, 2.3, 2.4, 2.5, -3.2, 6.1
        """,
    )
    print(options_selected)


if __name__ == "__main__":
    app()
