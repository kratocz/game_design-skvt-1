import json
import subprocess
import sys
import time
from pathlib import Path

# Test mimozemšťana v Play bez vstupu z klávesnice: spustí Play od Player Startu, přesune hráče na zadané
# místo a vzorkuje polohu mimozemšťana, hráče a stav pronásledování. Volá MCP editoru přes tools/unreal_mcp.py.
#   python3 tools/pie_ai_test.py <x> <y> <yaw> <sekund> [PlayMode_InViewPort|PlayMode_InEditorFloating]
# Scénáře z T7 DÚ č. 2 (výsledky v postup-editor.md, Zjištění T7):
#   -650 0 0 12     hráč ve skladu: jen hlídka
#   1000 800 0 14   hráč ve stoje v chodbě: zahlédne, dohoní, hráč skončí na checkpointu (220, 0)
#   100 800 0 18    hráč v severní části křižovatky: dohoní a chytí
#   100 100 0 20    hráč u dveří skladu: z chodby ho nevidí
# Vzorky jsou po 3–4 s, protože každý dotaz spouští nový proces klienta.

MCP = str(Path(__file__).with_name("unreal_mcp.py"))
LEVEL = "/Game/Krato/Maps/UEDPIE_0_L_Plizeni.L_Plizeni:PersistentLevel."
ALIEN, PLAYER = "BP_KratoAlien_C_1", "BP_KratoCharacter_C_0"


def tool(toolset, name, args):
    payload = json.dumps({"toolset_name": toolset, "tool_name": name, "arguments": args})
    return subprocess.run([sys.executable, MCP, "call_tool", payload], capture_output=True, text=True).stdout.strip()


def where(actor):
    raw = tool("editor_toolset.toolsets.actor.ActorTools", "get_actor_transform", {"actor": {"refPath": LEVEL + actor}})
    try:
        t = json.loads(raw)["returnValue"]
        return "(%5.0f %5.0f yaw %4.0f)" % (t["location"]["x"], t["location"]["y"], t["rotation"]["yaw"])
    except (ValueError, KeyError):
        return raw[:120]


def props(obj, names):
    raw = tool("editor_toolset.toolsets.object.ObjectTools", "get_properties", {"instance": {"refPath": LEVEL + obj}, "properties": names})
    try:
        return json.loads(raw)["returnValue"]
    except (ValueError, KeyError):
        return raw[:120]


x, y, yaw, seconds = (float(v) for v in sys.argv[1:5])
mode = sys.argv[5] if len(sys.argv) > 5 else "PlayMode_InViewPort"
tool("EditorToolset.EditorAppToolset", "StartPIE", {"options": {"playMode": mode, "warmupSeconds": 1}})
transform = {"location": {"x": x, "y": y, "z": 92}, "rotation": {"pitch": 0, "yaw": yaw, "roll": 0}, "scale": {"x": 1, "y": 1, "z": 1}}
tool("editor_toolset.toolsets.actor.ActorTools", "set_actor_transform", {"actor": {"refPath": LEVEL + PLAYER}, "xform": transform, "worldspace": True})
start = time.time()
while time.time() - start < seconds:
    light = props(ALIEN + ".AlertLight", ["LightColor", "Intensity"])
    print("%5.1f s  mimozemšťan %s  hráč %s  %s  světlo %s" % (time.time() - start, where(ALIEN), where(PLAYER), props(ALIEN, ["IsChasing", "PatrolIndex"]), light))
    time.sleep(0.3)
tool("EditorToolset.EditorAppToolset", "StopPIE", {})
