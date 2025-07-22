import typer
from code_review_ai.core import review_code
from pathlib import Path

app = typer.Typer()

@app.command()
def main(file: Path):
    if not file.exists():
        print("File not found.")
        raise typer.Exit()
    code = file.read_text()
    suggestions = review_code(code)
    print("\nAI Code Review Suggestions:\n")
    print(suggestions)

if __name__ == "__main__":
    app()
