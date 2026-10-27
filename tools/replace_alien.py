import json
import subprocess
import sys
from pathlib import Path

# Nahradí mimozemšťana umístěného v L_Plizeni čerstvou instancí BP_KratoAlien. Potřeba po každé nové komponentě
# v blueprintu: umístěný actor ji dostane jen s výchozími hodnotami a nastavení šablony se k němu nepropíše
# (viz docs/unreal-mcp.md, Level a Play). Převezme polohu, label, složku a body hlídky, uložení levelu je na volajícím.
#   python3 tools/replace_alien.py
# Volá MCP editoru přes tools/unreal_mcp.py; editor musí být otevřený a Play nesmí běžet.

MCP = str(Path(__file__).with_name("unreal_mcp.py"))
LEVEL = "/Game/Krato/Maps/L_Plizeni.L_Plizeni:PersistentLevel."
SC, A, O = "editor_toolset.toolsets.scene.SceneTools", "editor_toolset.toolsets.actor.ActorTools", "editor_toolset.toolsets.object.ObjectTools"
LABEL, FOLDER = "Alien", "Blockout/3a_Chodba"


def call(toolset, name, args):
    payload = json.dumps({"toolset_name": toolset, "tool_name": name, "arguments": args})
    out = subprocess.run([sys.executable, MCP, "call_tool", payload], capture_output=True, text=True).stdout
    print(name, out[:300])
    return json.loads(out)["returnValue"]


old = call(SC, "find_actors", {"root": None, "name": LABEL, "actor_type": {"refPath": "/Game/Krato/AI/BP_KratoAlien.BP_KratoAlien_C"}, "tag": "", "bounds": None, "collision_channels": []})
assert len(old) == 1, old
xform = call(A, "get_actor_transform", {"actor": old[0]})
points = json.loads(call(O, "get_properties", {"instance": old[0], "properties": ["PatrolPoints"]}))["PatrolPoints"]
call(SC, "remove_from_scene", {"actor": old[0]})
new = call(SC, "add_to_scene_from_asset", {"asset_path": "/Game/Krato/AI/BP_KratoAlien", "name": LABEL, "xform": xform, "parent": None, "snap_to_ground": False})["refPath"]
call(A, "set_label", {"actor": {"refPath": new}, "label": LABEL})
call(SC, "set_actor_folder", {"actor": {"refPath": new}, "folder_path": FOLDER})
call(O, "set_properties", {"instance": {"refPath": new}, "values": json.dumps({"PatrolPoints": points})})
# Kontrola: body hlídky, světlo zahlédnutí a zrychlení na cestách (bez něj se nehýbou nohy, viz Zjištění T7).
call(O, "get_properties", {"instance": {"refPath": new}, "properties": ["PatrolPoints"]})
call(O, "get_properties", {"instance": {"refPath": new + ".AlertLight"}, "properties": ["RelativeLocation", "LightColor", "Intensity"]})
call(O, "get_properties", {"instance": {"refPath": new + ".CharMoveComp"}, "properties": ["NavMovementProperties"]})
print("nový actor:", new.replace(LEVEL, ""))
