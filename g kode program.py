import tkinter as tk
from tkinter import messagebox, font as tkfont


def generate_gcode(Y_spacing, X_spacing, Y_length, X_length, S_shoot, S_retract, XY_feed_rate, dwell_time):
    gcode = f"""G90
G21
G92 X0 Y0


"""

    for Y_nails in range(0, Y_length + 1, Y_spacing):
        for X_nails in range(0, X_length + 1, X_spacing):
            gcode += f"G1 X{X_nails} Y{Y_nails} F{XY_feed_rate}\n"
            gcode += f"M03 S{S_shoot}\n"  # Activate the nail gun
            gcode += f"G4 P{dwell_time}\n"  # Dwell (pause) for the specified time
            gcode += f"M03 S{S_retract}\n"  # Deactivate the nail gun

    gcode += "G1 X0 Y0 F3000\n"
    gcode += "M30\n"

    return gcode


if __name__ == "__main__":
    Y_spacing = 100
    X_spacing = 50
    Y_length   = 1500
    X_length =  350
    S_shoot = 1000  # Adjust the nail gun activation value here
    S_retract = 2000  # Adjust the nail gun deactivation value here
    XY_feed_rate = 10000  # Adjust the XY feed rate here
    dwell_time = 0.4  # Adjust the dwell time in seconds here

    gcode = generate_gcode(Y_spacing, X_spacing, Y_length, X_length, S_shoot, S_retract, XY_feed_rate, dwell_time)

    with open("nail_shooting_gcode.nc", "w") as output_file:
        output_file.write(gcode)

    print("G-code has been generated and saved as 'nail_shooting_gcode.nc'")


def save_gcode():
    Y_spacing = int(Y_spacing_entry.get())
    X_spacing = int(X_spacing_entry.get())
    Y_length = int(Y_length_entry.get())
    X_length = int(X_length_entry.get())
    S_shoot = int(S_shoot_entry.get())
    S_retract = int(S_retract_entry.get())
    XY_feed_rate = int(XY_feed_rate_entry.get())
    dwell_time = float(dwell_time_entry.get())
    file_name = file_name_entry.get()

    gcode = generate_gcode(Y_spacing, X_spacing, Y_length, X_length, S_shoot, S_retract, XY_feed_rate, dwell_time)

    with open(file_name, "w") as output_file:
        output_file.write(gcode)

    messagebox.showinfo("Success", f"G-code has been generated and saved as '{file_name}'")


# Create the tkinter GUI
app = tk.Tk()
app.title("G kode generator stifterobot")
app.geometry("600x300")  # Adjust the window size

# Define fonts
label_font = tkfont.Font(size=12)
entry_font = tkfont.Font(size=12)
button_font = tkfont.Font(size=12)

# Create input fields and labels
Y_spacing_label = tk.Label(app, text="Mellomrom lengderetning", font=label_font)
Y_spacing_label.grid(row=0, column=0)
Y_spacing_entry = tk.Entry(app, font=entry_font)
Y_spacing_entry.insert(0, "100")
Y_spacing_entry.grid(row=0, column=1)
Y_spacing_mm = tk.Label(app, text="mm", font=label_font)
Y_spacing_mm.grid(row=0, column=2)

X_spacing_label = tk.Label(app, text="Mellomrom bredderetning", font=label_font)
X_spacing_label.grid(row=1, column=0)
X_spacing_entry = tk.Entry(app, font=entry_font)
X_spacing_entry.insert(0, "50")
X_spacing_entry.grid(row=1, column=1)
X_spacing_mm = tk.Label(app, text="mm", font=label_font)
X_spacing_mm.grid(row=1, column=2)

Y_length_label = tk.Label(app, text="Total lengde", font=label_font)
Y_length_label.grid(row=2, column=0)
Y_length_entry = tk.Entry(app, font=entry_font)
Y_length_entry.insert(0, "1500")
Y_length_entry.grid(row=2, column=1)
Y_length_mm = tk.Label(app, text="mm", font=label_font)
Y_length_mm.grid(row=2, column=2)


X_length_label = tk.Label(app, text="Total bredde", font=label_font)
X_length_label.grid(row=3, column=0)
X_length_entry = tk.Entry(app, font=entry_font)
X_length_entry.insert(0, "350")
X_length_entry.grid(row=3, column=1)
X_length_mm = tk.Label(app, text="mm", font=label_font)
X_length_mm.grid(row=3, column=2)

S_shoot_label = tk.Label(app, text="S_shoot:", font=label_font)
S_shoot_label.grid(row=4, column=0)
S_shoot_entry = tk.Entry(app, font=entry_font)
S_shoot_entry.insert(0, "1000")
S_shoot_entry.grid(row=4, column=1)

S_retract_label = tk.Label(app, text="S_retract:", font=label_font)
S_retract_label.grid(row=5, column=0)
S_retract_entry = tk.Entry(app, font=entry_font)
S_retract_entry.insert(0, "2000")
S_retract_entry.grid(row=5, column=1)

XY_feed_rate_label = tk.Label(app, text="XY_feed_rate:", font=label_font)
XY_feed_rate_label.grid(row=6, column=0)
XY_feed_rate_entry = tk.Entry(app, font=entry_font)
XY_feed_rate_entry.insert(0, "10000")
XY_feed_rate_entry.grid(row=6, column=1)

dwell_time_label = tk.Label(app, text="dwell_time:", font=label_font)
dwell_time_label.grid(row=7, column=0)
dwell_time_entry = tk.Entry(app, font=entry_font)
dwell_time_entry.insert(0, "0.4")
dwell_time_entry.grid(row=7, column=1)

file_name_label = tk.Label(app, text="File name:", font=label_font)
file_name_label.grid(row=8, column=0)
file_name_entry = tk.Entry(app, font=entry_font)
file_name_entry.insert(0, "nail_shooting_gcode.nc")
file_name_entry.grid(row=8, column=1)
file_name_hint = tk.Label(app, text="husk .nc bak filnavn", font=label_font)
file_name_hint.grid(row=8, column=2)

# Create the "Generate G-code" button
generate_button = tk.Button(app, text="Generate G-code", command=save_gcode, font=button_font)
generate_button.grid(row=9, column=1, columnspan=2)

# Run the GUI
app.mainloop()