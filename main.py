import sys
import glob
import asyncio
import logging
import importlib
import urllib3
from pathlib import Path
from config import X1

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_plugins(plugin_name):
    path = Path(f"ROYEDITX/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"ROYEDITX.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["ROYEDITX.modules." + plugin_name] = load
    print("ROYEDITX has Imported " + plugin_name)


files = glob.glob("ROYEDITX/modules/*.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("♥︎ Bot Deployed Successfully, By - @ROY_EDITX")

async def main():
    await X1.run_until_disconnected()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
