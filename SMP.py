import tkinter as tk
from tkinter import messagebox

# Blaze SMP - Python interface demo
# Uses only Python's built-in Tkinter library.
# This is a visual demo; it does not connect to a real Minecraft server.

BG = "#101722"
PANEL = "#172331"
PANEL_DARK = "#0b111a"
GOLD = "#ffb51b"
ORANGE = "#ff6a16"
GREEN = "#20e879"
WHITE = "#f5f7fb"
MUTED = "#b6c2d2"
BORDER = "#34465a"

root = tk.Tk()
root.title("Blaze SMP | Survival")
root.geometry("1200x760")
root.minsize(950, 650)
root.configure(bg=BG)

def make_label(parent, text, size=12, color=WHITE, bold=False, **kwargs):
    return tk.Label(
        parent, text=text, bg=kwargs.pop("bg", parent.cget("bg")),
        fg=color, font=("Segoe UI", size, "bold" if bold else "normal"),
        **kwargs
    )

def make_button(parent, text, command, bg=PANEL, fg=WHITE, active=GOLD):
    return tk.Button(
        parent, text=text, command=command, bg=bg, fg=fg,
        activebackground=active, activeforeground="#101722",
        relief="flat", bd=0, cursor="hand2",
        font=("Segoe UI", 11, "bold"), padx=12, pady=10
    )

def show_page(page):
    for child in content.winfo_children():
        child.destroy()

    if page == "Home":
        make_label(content, "WELCOME TO", 15, WHITE, True).pack(pady=(22, 2))
        make_label(content, "BLAZE SMP", 30, GOLD, True).pack()
        make_label(content, "BUILD  •  EXPLORE  •  TRADE  •  SURVIVE", 12, MUTED, True).pack(pady=8)
        hero = tk.Frame(content, bg="#223a43", highlightbackground=BORDER, highlightthickness=1)
        hero.pack(fill="both", expand=True, padx=22, pady=18)
        make_label(hero, "🌄", 46, GOLD, True, bg="#223a43").pack(pady=(35, 8))
        make_label(hero, "Your world. Your rules.", 22, WHITE, True, bg="#223a43").pack()
        make_label(hero, "Collect resources, build your base, make friends,", 13, MUTED, bg="#223a43").pack(pady=(12, 3))
        make_label(hero, "and sell your items to grow your in-game balance.", 13, MUTED, bg="#223a43").pack()
        make_button(hero, "▶  PLAY NOW", lambda: messagebox.showinfo("Blaze SMP", "Connect this button to your server details!"),
                    bg=GREEN, fg="#07130d", active="#8dffbd").pack(pady=22)
    elif page == "Shop":
        make_label(content, "PLAYER SHOP", 23, GOLD, True).pack(anchor="w", padx=22, pady=(22, 4))
        make_label(content, "Demo prices — customize these for your server economy.", 11, MUTED).pack(anchor="w", padx=22, pady=(0, 14))
        tabs = tk.Frame(content, bg=BG)
        tabs.pack(fill="x", padx=22, pady=(0, 12))
        make_button(tabs, "SELL ITEMS", lambda: show_shop_items("Sell"), bg="#075d3a", active=GREEN).pack(side="left", padx=(0, 8))
        make_button(tabs, "BUY ITEMS", lambda: show_shop_items("Buy"), bg=PANEL, active=GOLD).pack(side="left")
        show_shop_items("Sell")
    elif page == "Inventory":
        make_label(content, "YOUR INVENTORY", 23, GOLD, True).pack(anchor="w", padx=22, pady=(22, 12))
        for item in ["🪵  Oak Logs          x 32", "🪨  Cobblestone     x 64", "⛓  Iron Ingots       x 12", "💎  Diamonds          x 3"]:
            row = tk.Frame(content, bg=PANEL, highlightbackground=BORDER, highlightthickness=1)
            row.pack(fill="x", padx=22, pady=5)
            make_label(row, item, 13, WHITE, True, bg=PANEL, anchor="w").pack(fill="x", padx=14, pady=12)
    elif page == "Community":
        make_label(content, "BLAZE SMP COMMUNITY", 23, GOLD, True).pack(pady=(28, 12))
        make_label(content, "Make friends • Build together • Trade fairly", 14, MUTED).pack()
        make_label(content, "Add your Discord invite and server rules here.", 12, WHITE).pack(pady=20)
        make_button(content, "OPEN COMMUNITY INFO", lambda: messagebox.showinfo("Community", "Add your Discord invite URL in the Python code."),
                    bg=GREEN, fg="#07130d").pack(pady=8)
    else:
        make_label(content, page.upper(), 23, GOLD, True).pack(pady=28)
        make_label(content, "This section is a placeholder. Add your own features here.", 12, MUTED).pack()

def show_shop_items(mode):
    for child in shop_items.winfo_children():
        child.destroy()
    make_label(shop_items, f"POPULAR ITEMS ({mode.upper()})", 12, WHITE, True).pack(anchor="w", pady=(0, 8))
    items = [
        ("🪵", "Oak Log", 5),
        ("🪨", "Cobblestone", 3),
        ("⛓", "Iron Ingot", 15),
        ("💎", "Diamond", 50),
        ("🟪", "Netherite Ingot", 100),
    ]
    for emoji, name, price in items:
        row = tk.Frame(shop_items, bg=PANEL_DARK, highlightbackground=BORDER, highlightthickness=1)
        row.pack(fill="x", pady=4)
        make_label(row, emoji, 18, WHITE, True, bg=PANEL_DARK, width=3).pack(side="left", padx=(8, 2), pady=8)
        make_label(row, name, 11, WHITE, True, bg=PANEL_DARK, anchor="w").pack(side="left", fill="x", expand=True, pady=8)
        action_text = f"${price} / item"
        make_button(row, action_text, lambda n=name, p=price, m=mode: messagebox.showinfo)