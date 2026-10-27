import json
import sys
import urllib.request

# Zavolá nástroj MCP serveru editoru přímo přes HTTP, aby velký výstup šel do souboru, ne do kontextu agenta:
#   python3 tools/unreal_mcp.py call_tool '{"toolset_name": "...", "tool_name": "...", "arguments": {...}}' [výstup]
#   python3 tools/unreal_mcp.py describe_toolset '{"toolset_name": "..."}' popis.json
# Skript pro ProgrammaticToolset.execute_tool_script: python3 tools/unreal_mcp.py --script skript.py [výstup]

URL = "http://127.0.0.1:8765/mcp"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}


def post(body, session=None):
    headers = dict(HEADERS)
    if session:
        headers["Mcp-Session-Id"] = session
    request = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=headers)
    with urllib.request.urlopen(request, timeout=300) as response:
        session = response.headers.get("Mcp-Session-Id") or session
        raw = response.read().decode()
    if raw.startswith(("event:", "data:")):
        raw = "\n".join(line[5:].strip() for line in raw.splitlines() if line.startswith("data:"))
    return (json.loads(raw) if raw.strip() else {}), session


def call(tool, arguments):
    _, session = post({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "unreal_mcp.py", "version": "1"}}})
    post({"jsonrpc": "2.0", "method": "notifications/initialized"}, session)
    result, _ = post({"jsonrpc": "2.0", "id": 2, "method": "tools/call",
                      "params": {"name": tool, "arguments": arguments}}, session)
    if "result" not in result:
        return json.dumps(result)
    return "\n".join(part.get("text", "") for part in result["result"].get("content", []))


if sys.argv[1] == "--script":
    tool, arguments = "call_tool", {
        "toolset_name": "editor_toolset.toolsets.programmatic.ProgrammaticToolset",
        "tool_name": "execute_tool_script", "arguments": {"script": open(sys.argv[2]).read()}}
    out_path = sys.argv[3] if len(sys.argv) > 3 else None
else:
    tool, arguments = sys.argv[1], json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    out_path = sys.argv[3] if len(sys.argv) > 3 else None
output = call(tool, arguments)
if out_path:
    open(out_path, "w").write(output)
    print(f"{len(output)} znaků do {out_path}")
else:
    print(output)
