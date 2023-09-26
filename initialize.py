from typing import Optional

import typer

app = typer.Typer()


ENTITIES = ["Data", "Metadata", "Digital Content", "Code", "Storage", "People"]
ACTIVITIES = [
    "Plan/Design",
    "Gen/Curation",
    "Sharing",
    "Use/Reuse",
    "Preservation",
    "Monitoring",
]


@app.command()
def wizard():
    for entity in ENTITIES:
        typer.echo(f"Entity: {entity}")
        for activity in ACTIVITIES:
            typer.echo(f"  Activity: {activity}")


if __name__ == "__main__":
    app()
