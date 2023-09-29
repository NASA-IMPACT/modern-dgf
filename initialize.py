import shutil
import typer
import shutil

from enum import Enum
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from typing import List, Optional

try:
    from typing import Annotated, Literal
except ImportError:
    from typing_extensions import Annotated, Literal

app = typer.Typer(
    help="CLI to tailor the mDGF framework to your project-specific needs."
)

console = Console()

ENTITIES = ["Data", "Metadata", "Digital Content", "Code", "Storage", "People"]

ENTITIY_FOLDERS = ['data', 'metadata', 'digital_content', 'code', 'resources/storage', 'resources/people']

ENTITIES_PROMPT = "Provide the comma separated IDs of entities applicable to your project:"

FOUNDATIONAL_CODES = [1, 6]

INFO = """There are two steps to customizing the framework for your project. 
1. Selection of entities applicable to your project
2. Selection of phases for selected entities 

Note: Only selected entities and phases will be retained, everything else will be removed from the repo.

Instructions on selecting entities and phases:
1. Select all documents for an entity by typing in a whole number. For example, 1 will select all documents for the entity "Data".
2. Select individual phases by typing in a number between 1 and 6. For example, 1 will select the Plan/Design phase for the entity "Data", if you had selected 1 from the Entity list.
3. Select multiple documents by typing in a comma-separated list of numbers.

Note: Foundational Phases are selected by default.
"""

PHASES = [
    "Plan/Design",
    "Generation/Curation",
    "Sharing",
    "Use/Reuse",
    "Preservation",
    "Monitoring",
]
PHASES_FOLDERS = ['plan_design', 'generation_curation', 'sharing', 'use_reuse', 'preservation', 'monitoring']

PHASES_PROMPT = "Provide the IDs of Phases applicable to {entity}:"


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


def formatted_part(parts: list, entity_code: str = '') -> list:
    if ValidCodeOptions.OPTION_all.value in parts:
        # Change this to use ENUMs
        parts = [str(index) for index in range(1, 7)]    
    return [f'{entity_code}.{part.strip()}' if entity_code else part.strip() for part in parts]

def is_valid(code: str, entity_code: str = '') -> bool:
    parts = code.split(',')
    val = [f"{entity_code}.{part.strip().replace('-', '')}" if entity_code else part.strip().replace('-', '') in ValidCodeOptions._value2member_map_ for part in parts]
    return all(val)

def parse_options(code: str, entity_code: str = '') -> List[str]:
    parts = code.split(",")
    return formatted_part(parts, entity_code)

def prepare_final_phase_list(entity_code: str, phase_list: list) -> list:
    required_phases = [f"{entity_code}.{foundational_code}" for foundational_code in FOUNDATIONAL_CODES]
    final_phases = list(set(phase_list).union(set(required_phases)))

    if entity_code == ValidCodeOptions.OPTION_6.value:
        final_phases = [f"{entity_code}.{FOUNDATIONAL_CODES[0]}"]
    
    return final_phases

def _get_table():
    table = Table("Entities \u2193 / Phases \u2192", *PHASES)

    for index, entity in enumerate(ENTITIES):
        index += 1
        if entity == "People":
            codes = ["6.1"]
        else:
            codes = [f"{index}.{subindex}" for subindex in range(1, 7)]
        table.add_row(f"{index}. {entity}", *codes)
    return table

def prepare_directories(valid_entities_and_phases: dict):
    for entity_code, entity in enumerate(ENTITIY_FOLDERS, 1):
        if phases := valid_entities_and_phases.get(f"{entity_code}"):
            console.print(f"Keep Entity: {entity}" )
            for phase_index, phase in enumerate(PHASES_FOLDERS, 1):
                if entity_code == int(ValidCodeOptions.OPTION_6.value) and phase_index > 1:
                    continue
                if f"{entity_code}.{phase_index}" in phases:
                    console.print(f"    Keep Phase: {phase}")    
                else:
                    console.print(f"    Remove Phase: {phase}")
                    shutil.rmtree(f'{entity}/{phase}')
        else:
            console.print(f"Remove Entity: {entity}" )
            shutil.rmtree(entity)

@app.command()
def wizard():
    """
    Answer some simple questions to tailor the mDGF framework to your project.
    """

    welcome_message = typer.style(
        "\nWelcome to the Modern Data Governance framework wizard!\n", fg=typer.colors.GREEN, bold=True
    )
    typer.echo(welcome_message)
    
    information = typer.style(
        INFO, fg=typer.colors.YELLOW
    )

    typer.echo(information)

    typer.echo("Below you will find a table of all steps in the mDGF framework.\n")

    console.print(_get_table())
    
    entities_selected = Prompt.ask(ENTITIES_PROMPT, default="all")

    print(entities_selected)

    while not is_valid(entities_selected):
        entities_selected = Prompt.ask(
            "Invalid selection. Please enter values listed in the table above.\n", default="all"
        )

    valid_entities = parse_options(entities_selected)

    valid_entities_and_phases = dict()
    for entity in valid_entities:
        phases_selected = Prompt.ask(PHASES_PROMPT.format(entity=entity), default="all")
        while not is_valid(phases_selected, entity):
            phases_selected = Prompt.ask(
                f"Invalid selection. Please enter proper for phases of {entity} listed in the table above.\n", default="all"
            )
        phase_list = prepare_final_phase_list(entity, parse_options(phases_selected, entity))
        valid_entities_and_phases[entity] = phase_list
    print(valid_entities_and_phases)
    prepare_directories(valid_entities_and_phases)

if __name__ == "__main__":
    app()
