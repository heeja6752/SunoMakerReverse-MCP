from pathlib import Path
from mcp.server.fastmcp import FastMCP

print("MCP STARTING")

BASE_DIR = Path(__file__).parent

def load_file(filename):
    path = BASE_DIR / filename

    if not path.exists():
        return ""

    return path.read_text(encoding="utf-8")

RULES = load_file("규칙.txt")
GENRES = load_file("Ai노래연구.txt")
LYRICS = load_file("가사목록.txt")

mcp = FastMCP("SunoMakerReverse")


@mcp.tool()
def showRules():
    """Returns songwriting rules."""
    return RULES[:3000]


@mcp.tool()
def showLyrics():
    """Returns lyric examples."""
    return LYRICS[:3000]


@mcp.tool()
def searchGenre(keyword: str):
    """Search genre styles."""
    results = []

    for line in GENRES.splitlines():
        if keyword.lower() in line.lower():
            results.append(line)

    return "\n".join(results[:30])


@mcp.tool()
def songFormat():
    """Returns Suno song structure."""
    return """
[Instrumental intro]

[Verse 1]

[Verse 2]

[Chorus]

[Instrumental]

[Verse 3]

[Chorus]

[Bridge]

[Chorus]

[Outro]
"""

if __name__ == "__main__":
    print("BEFORE RUN")
    mcp.run()
    print("AFTER RUN")
