import customtkinter as ctk

def create_controls(parent, normal_command, suspicious_command, reset_command):
    frame = ctk.CTkFrame(parent, fg_color="transparent")
    frame.pack(fill="x", padx=30, pady=(4, 8))

    ctk.CTkButton(
        frame,
        text="▶ Simulate Normal Activity",
        command=normal_command,
        width=210,
        height=42,
        corner_radius=10,
    ).pack(side="left")

    ctk.CTkButton(
        frame,
        text="⚠ Simulate Suspicious Activity",
        command=suspicious_command,
        width=225,
        height=42,
        corner_radius=10,
    ).pack(side="left", padx=10)

    ctk.CTkButton(
        frame,
        text="Reset Sandbox",
        command=reset_command,
        width=140,
        height=42,
        corner_radius=10,
        fg_color="#3b3f46",
        hover_color="#4b5058",
    ).pack(side="right")

    return frame
