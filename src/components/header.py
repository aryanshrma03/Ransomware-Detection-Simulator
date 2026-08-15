import customtkinter as ctk

def create_header(parent):
    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(fill="x", padx=30, pady=(24, 8))

    ctk.CTkLabel(
        frame,
        text="🛡️ Ransomware Detection Simulator",
        font=("Segoe UI", 28, "bold"),
    ).pack(anchor="w")

    ctk.CTkLabel(
        frame,
        text="Safe behavioral simulation — no real files are encrypted, deleted, or modified.",
        text_color="#9aa4b2",
        font=("Segoe UI", 13),
    ).pack(anchor="w", pady=(5, 0))

    return frame
