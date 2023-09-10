import tkinter as tk
import tkinter.messagebox as messagebox
import aiohttp
import asyncio

async def fetch_data():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('') as response:
                data = await response.json()
                return data
    except Exception as e:
        return str(e)

async def fetch_and_display():
    for _ in range(20):
        data = await fetch_data()
        messagebox.showinfo("Response", f"Received Data:\n{data}")

async def main():
    await fetch_and_display()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Async Request Demo")

    start_button = tk.Button(root, text="Start Requests", command=lambda: asyncio.create_task(main()))
    start_button.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack()

    root.mainloop()
