# Run this on the Raspberry Pi with Build HAT installed.
# It will keep running until you press Ctrl-C.

import asyncio
from buildhat import Motor

TURRET_DELTA = 165  # Adjust this as needed
TURRET_MAX = 4

turret = Motor('A')
turret_shot = 0

async def handler(reader, writer):
    global turret_shot
    turret.run_for_degrees(TURRET_DELTA, 100)
    turret_shot += 1
    if turret_shot == TURRET_MAX:
        turret.run_for_degrees(TURRET_MAX * TURRET_DELTA, -100)
        turret_shot = 0
    
async def main():
    # Replace juniaspi with the hostname of your Raspberry Pi.
    server = await asyncio.start_server(handler, 'juniaspi.local', 8888)
    try:
        async with server:
            await server.serve_forever()
    finally:
        turret.run_for_degrees(turret_shot * TURRET_DELTA, -100)

asyncio.run(main())
