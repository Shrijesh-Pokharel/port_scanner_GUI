import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.03)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.error as err:
        return False

def start_scan():
    ip = ip_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid port numbers")
        return
    
    open_ports = []
    result_text.delete(1.0, tk.END)
    
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)
            result_text.insert(tk.END, f"Port {port} is open\n")
    
    with open("open_ports.txt", "w") as file:
        for port in open_ports:
            file.write(f"Open port on {ip}: Port no {port}\n")
    
    result_text.insert(tk.END, f"\nOpen ports on {ip}: {open_ports}\n")
    result_text.insert(tk.END, "Saved to open_ports.txt\n")
    messagebox.showinfo("Scan Complete", "Port scan completed. Results saved to open_ports.txt")

# GUI Setup
root = tk.Tk()
root.title("Port Scanner")
root.geometry("700x400")

tk.Label(root, text="Target IP Address:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

tk.Label(root, text="Starting Port:").pack()
start_port_entry = tk.Entry(root)
start_port_entry.pack()

tk.Label(root, text="Ending Port:").pack()
end_port_entry = tk.Entry(root)
end_port_entry.pack()

tk.Button(root, text="Start Scan", command=start_scan).pack()

result_text = scrolledtext.ScrolledText(root, width=60, height=10)
result_text.pack()

root.mainloop()
