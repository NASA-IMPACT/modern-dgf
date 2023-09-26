from typing import List, Optional

try:
    from typing import Annotated, Literal
except ImportError:
    from typing_extensions import Annotated, Literal

from enum import Enum

import typer
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

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

PROMPT = """Please enter codes for documents relevant to your project. All other documents will be deselected.

Select all documents for all entities by typing in "all". This is the default option.

Select all documents for an entity by typing in a whole number. For example, 1 will select all documents for the entity "Data".

Select individual documents by typing in a decimal number. For example, 1.1 will select the first activity for the entity "Data".

Select multiple documents by typing in a comma-separated list of numbers.

Deselect a document by typing in a negative number. For example, -1 will deselect all documents for the entity "Data". -2.1 will Deselct the first document for the entity "Metadata".

Example input: all
Example input: 1, 2.3, 2.4, 2.5, -3.2, 6.1

"""


class ValidCodeOptions(Enum):
    OPTION_all = "all"
    OPTION_1 = "1"
    OPTION_2 = "2"
    OPTION_3 = "3"
    OPTION_4 = "4"
    OPTION_5 = "5"
    OPTION_6 = "6"
    OPTION_1_1 = "1.1"
    OPTION_1_2 = "1.2"
    OPTION_1_3 = "1.3"
    OPTION_1_4 = "1.4"
    OPTION_1_5 = "1.5"
    OPTION_1_6 = "1.6"
    OPTION_2_1 = "2.1"
    OPTION_2_2 = "2.2"
    OPTION_2_3 = "2.3"
    OPTION_2_4 = "2.4"
    OPTION_2_5 = "2.5"
    OPTION_2_6 = "2.6"
    OPTION_3_1 = "3.1"
    OPTION_3_2 = "3.2"
    OPTION_3_3 = "3.3"
    OPTION_3_4 = "3.4"
    OPTION_3_5 = "3.5"
    OPTION_3_6 = "3.6"
    OPTION_4_1 = "4.1"
    OPTION_4_2 = "4.2"
    OPTION_4_3 = "4.3"
    OPTION_4_4 = "4.4"
    OPTION_4_5 = "4.5"
    OPTION_4_6 = "4.6"
    OPTION_5_1 = "5.1"
    OPTION_5_2 = "5.2"
    OPTION_5_3 = "5.3"
    OPTION_5_4 = "5.4"
    OPTION_5_5 = "5.5"
    OPTION_5_6 = "5.6"
    OPTION_6_1 = "6.1"


def is_valid(code: str) -> bool:
    parts = code.split(",")
    return all(part in ValidCodeOptions._value2member_map_ for part in parts)


def parse_options(code: str) -> List[str]:
    parts = code.split(",")
    return [part for part in parts if part in ValidCodeOptions._value2member_map_]


def _get_table():
    table = Table("Entities \u2193 / Activities \u2192", *ACTIVITIES)

    for index, entity in enumerate(ENTITIES):
        index += 1
        if entity == "People":
            codes = ["6.1"]
        else:
            codes = [f"{index}.{subindex}" for subindex in range(1, 7)]
        table.add_row(f"{index}. {entity}", *codes)
    return table


@app.command()
def wizard():
    """
    Answer some simple questions to tailor the mDGF framework to your project.
    """

    welcome_message = typer.style(
        "\nWelcome to the mDGF framework wizard!\n", fg=typer.colors.GREEN, bold=True
    )
    typer.echo(welcome_message)
    typer.echo("Below you will find a table of all documents in the mDGF framework.\n")

    console.print(_get_table())
    options_selected = Prompt.ask(PROMPT, default="all")
    while not is_valid(options_selected):
        options_selected = Prompt.ask(
            "Invalid input. Please enter a valid input.\n", default="all"
        )
    options_selected = parse_options(options_selected)
    print(options_selected)


if __name__ == "__main__":
    app()
