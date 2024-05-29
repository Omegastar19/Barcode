import asyncio
import json
from article_database import increase_inventory, decrease_inventory

async def handle_client(reader, writer):
    """Deze coroutine handelt een verbinding met een client af"""
    while True:
        data = await reader.read(1024)
        if not data:
            break
        barcode = json.loads(data.decode())

        if barcode[1] == "+":
            increase_inventory("magazijn", "voorraad", str(barcode[0]))
        elif barcode[1] == "-":
            decrease_inventory("magazijn", "voorraad", str(barcode[0]))

        writer.write(b'Barcode ontvangen en voorraad succesvol aangepast in database\n')
        await writer.drain()

    writer.close()

async def start_server():
    """Deze coroutine start de barcode server"""
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 65432
    )
    async with server:
        print("Server is gestart en luistert naar barcodes.")
        await server.serve_forever()

async def main():
    """Hoofdprogramma om de server te starten"""
    await start_server()

# Start de asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())









