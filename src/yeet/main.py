"""
yeet - deploy your slop using AI inference
yoten - check if your slop is fire or not
"""
import json
import os
import sys
from pathlib import Path
from typing import Optional
import time

import typer
from anthropic import Anthropic
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
import requests

from . import vibes

console = Console()
app = typer.Typer()


YEET_DIR = Path(".yeet")
MANIFEST_FILE = YEET_DIR / "manifest.json"


def get_anthropic_client() -> Anthropic:
    """Get Anthropic client or die trying"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]ANTHROPIC_API_KEY not found in environment[/red]")
        console.print("[yellow]get your key from https://console.anthropic.com/[/yellow]")
        sys.exit(1)
    return Anthropic(api_key=api_key)


def analyze_project() -> dict:
    """Use Claude to analyze the project and suggest deployment"""
    console.print(f"[cyan]{vibes.random_analyzing()}[/cyan]")

    # Get project files
    cwd = Path.cwd()
    files = []

    # Look for key files
    key_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "Cargo.toml",
        "go.mod",
        "Gemfile",
        "Dockerfile",
        "docker-compose.yml",
        "vercel.json",
        "netlify.toml",
        "fly.toml",
        "README.md",
    ]

    for file in key_files:
        file_path = cwd / file
        if file_path.exists():
            try:
                content = file_path.read_text()[:2000]  # Limit content
                files.append(f"=== {file} ===\n{content}\n")
            except Exception:
                pass

    # List directory structure
    try:
        dir_listing = os.listdir(cwd)
        files.append(f"=== Directory listing ===\n{', '.join(dir_listing)}\n")
    except Exception:
        pass

    project_info = "\n".join(files)

    # Call Claude
    client = get_anthropic_client()

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        progress.add_task(description="asking claude what this slop is...", total=None)

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""You are an unhinged deployment expert. Analyze this project and tell me:
1. What kind of app this is
2. The best/easiest platform to deploy it on (Fly.io, Vercel, Railway, Render, Netlify, etc.)
3. The EXACT shell commands to deploy it (be specific, include any setup needed)
4. What URL pattern to expect after deployment

Project files:
{project_info}

Respond in JSON format:
{{
    "app_type": "brief description with personality",
    "platform": "platform name",
    "why": "why this platform in one unhinged sentence",
    "commands": ["command1", "command2", ...],
    "url_pattern": "description of where to find the URL after running commands",
    "roast": "optional roast of their tech stack"
}}

Be specific with commands. Include account setup if needed. Be funny but accurate."""
                }
            ]
        )

    # Parse response
    response_text = response.content[0].text

    # Try to extract JSON from response
    try:
        # Find JSON in response
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        json_str = response_text[start:end]
        result = json.loads(json_str)
        return result
    except Exception as e:
        console.print(f"[red]Failed to parse Claude's response: {e}[/red]")
        console.print(f"[dim]{response_text}[/dim]")
        sys.exit(1)


def save_manifest(url: str, platform: str, app_type: str):
    """Save deployment info to manifest"""
    YEET_DIR.mkdir(exist_ok=True)

    manifest = {
        "url": url,
        "platform": platform,
        "app_type": app_type,
        "yeeted_at": time.time(),
    }

    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))


def load_manifest() -> Optional[dict]:
    """Load deployment manifest"""
    if not MANIFEST_FILE.exists():
        return None

    try:
        return json.loads(MANIFEST_FILE.read_text())
    except Exception:
        return None


def yeet_cli():
    """yeet your slop to the cloud"""
    console.print(Panel.fit(
        "[bold magenta]yeet[/bold magenta] - deploy your slop using AI",
        border_style="magenta"
    ))

    # Analyze project
    analysis = analyze_project()

    # Show results
    console.print()
    console.print(Panel.fit(
        f"[bold cyan]Detected:[/bold cyan] {analysis['app_type']}\n"
        f"[bold cyan]Platform:[/bold cyan] {analysis['platform']}\n"
        f"[bold cyan]Why:[/bold cyan] {analysis['why']}",
        title="Analysis Complete",
        border_style="cyan"
    ))

    if "roast" in analysis and analysis["roast"]:
        console.print(f"[dim italic]{analysis['roast']}[/dim italic]\n")

    # Show deployment commands
    console.print(f"[bold yellow]Run these commands to yeet your slop:[/bold yellow]\n")
    for i, cmd in enumerate(analysis["commands"], 1):
        console.print(f"  [green]{i}.[/green] {cmd}")

    console.print()
    console.print(f"[bold cyan]Where to find your URL:[/bold cyan] {analysis['url_pattern']}")
    console.print()

    # Ask for URL
    console.print("[yellow]After deploying, enter your app URL to save it:[/yellow]")
    url = input("URL (or press Enter to skip): ").strip()

    if url:
        save_manifest(url, analysis["platform"], analysis["app_type"])
        console.print(f"\n[green]{vibes.random_success()}[/green]")
        console.print(f"[dim]Run 'yoten' to check if it's fire[/dim]")
    else:
        console.print("[dim]Skipped saving URL. Run yoten manually with your URL.[/dim]")


def yoten_cli():
    """check if your yeeted slop is fire or not"""
    console.print(Panel.fit(
        "[bold magenta]yoten[/bold magenta] - check if your slop is fire",
        border_style="magenta"
    ))

    # Load manifest
    manifest = load_manifest()

    if not manifest:
        console.print("[red]No yeet manifest found. Did you yeet yet?[/red]")
        console.print("[yellow]Run 'yeet' first to deploy your slop[/yellow]")
        sys.exit(1)

    url = manifest["url"]
    platform = manifest["platform"]
    app_type = manifest["app_type"]
    yeeted_at = manifest["yeeted_at"]

    # Calculate time since deploy
    hours_ago = (time.time() - yeeted_at) / 3600
    if hours_ago < 1:
        time_str = f"{int(hours_ago * 60)} minutes ago"
    elif hours_ago < 24:
        time_str = f"{int(hours_ago)} hours ago"
    else:
        time_str = f"{int(hours_ago / 24)} days ago"

    console.print(f"\n[cyan]Your {app_type} was yeeted to {platform} {time_str}[/cyan]")
    console.print(f"[dim]URL: {url}[/dim]\n")

    # Check if it's fire
    console.print("[cyan]checking if it's fire...[/cyan]")

    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        response_time = time.time() - start_time

        if response.status_code == 200:
            if response_time < 1.0:
                verdict = vibes.random_fire()
                color = "green"
            else:
                verdict = vibes.random_mid()
                color = "yellow"

            console.print(f"[{color}]{verdict}[/{color}]")
            console.print(f"[dim]Status: {response.status_code} | Response time: {response_time:.2f}s[/dim]")
        else:
            verdict = vibes.random_cooked()
            console.print(f"[red]{verdict}[/red]")
            console.print(f"[dim]Status: {response.status_code}[/dim]")

    except requests.exceptions.Timeout:
        console.print(f"[red]{vibes.random_cooked()}[/red]")
        console.print("[dim]Request timed out after 10s[/dim]")

    except requests.exceptions.ConnectionError:
        console.print(f"[red]{vibes.random_cooked()}[/red]")
        console.print("[dim]Could not connect to server[/dim]")

    except Exception as e:
        console.print(f"[red]{vibes.random_error()}[/red]")
        console.print(f"[dim]Error: {e}[/dim]")


if __name__ == "__main__":
    app()
