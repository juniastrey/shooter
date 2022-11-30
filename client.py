# Trigger this script on PC per redeem.
# This can be done using Streamer.bot, for instance.

import asyncio
import platform

# Work around silly bug on Windows.
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def shoot():
    await asyncio.open_connection('juniaspi.local', 8888)

asyncio.run(shoot())
