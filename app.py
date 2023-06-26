import time
import statistics
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ping3 import ping
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from threading import Thread


class PingApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Application")

        self.ip_label = ttk.Label(root, text="IP:")
        self.ip_label.grid(row=0, column=0, padx=5, pady=5)

        self.ip_entry = ttk.Entry(root, width=20)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        self.duration_label = ttk.Label(root, text="Duración:")
        self.duration_label.grid(row=1, column=0, padx=5, pady=5)

        self.duration_var = tk.StringVar()
        self.duration_combobox = ttk.Combobox(root, textvariable=self.duration_var, state="readonly")
        self.duration_combobox["values"] = ["60", "Custom"]
        self.duration_combobox.current(0)
        self.duration_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.duration_combobox.bind("<<ComboboxSelected>>", self.handle_duration_selection)

        self.custom_duration_entry = ttk.Entry(root, width=10, state=tk.DISABLED)
        self.custom_duration_entry.grid(row=1, column=2, padx=5, pady=5)

        self.start_button = ttk.Button(root, text="Iniciar", command=self.start_ping)
        self.start_button.grid(row=1, column=3, padx=5, pady=5)

        self.stop_button = ttk.Button(root, text="Detener", command=self.stop_ping, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=4, padx=5, pady=5)

        self.table = ttk.Treeview(root)
        self.table["columns"] = ("timestamp", "rtt")
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("timestamp", anchor=tk.W, width=150)
        self.table.column("rtt", anchor=tk.W, width=150)
        self.table.heading("timestamp", text="Timestamp")
        self.table.heading("rtt", text="RTT (ms)")
        self.table.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

        self.fig = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=5, padx=5, pady=5)

        self.progress_bar = ttk.Progressbar(root, mode='indeterminate')
        self.progress_bar.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

        self.failure_counter = 0
        self.is_ping_running = False

    def start_ping(self):
        ip_address = self.ip_entry.get()
        if not ip_address:
            messagebox.showerror("Error", "Por favor, ingresa una dirección IP válida.")
            return

        duration = self.get_duration()
        if duration is None:
            messagebox.showerror("Error", "Por favor, ingresa una duración válida.")
            return

        self.table.delete(*self.table.get_children())
        self.ax.clear()
        self.fig.canvas.draw()

        self.failure_counter = 0
        self.is_ping_running = True

        self.start_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)

        self.progress_bar.start()

        # Ejecutar el proceso de ping en un hilo separado
        thread = Thread(target=self.ping_ip, args=(ip_address, duration))
        thread.start()

    def stop_ping(self):
        self.is_ping_running = False

    def ping_ip(self, ip, duration):
        timestamps = []
        rtt_times = []

        start_time = time.time()
        end_time = start_time + duration

        while time.time() < end_time and self.is_ping_running:
            timestamp = time.time()
            rtt = ping(ip)

            if rtt is not None:
                timestamps.append(timestamp)
                rtt_times.append(rtt)
            else:
                self.failure_counter += 1

            time.sleep(1)  # Esperar 1 segundo antes de cada ping

        self.display_statistics(timestamps, rtt_times)
        self.plot_statistics(timestamps, rtt_times)

        self.start_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)

        self.progress_bar.stop()
        self.progress_bar.grid_remove()

    def display_statistics(self, timestamps, rtt_times):
        self.table.delete(*self.table.get_children())

        for timestamp, rtt in zip(timestamps, rtt_times):
            self.table.insert("", tk.END, values=(timestamp, rtt))

        messagebox.showinfo("Estadísticas de Ping", f"Total de pings exitosos: {len(rtt_times)}\n"
                                                    f"Total de fallos: {self.failure_counter}")

    def plot_statistics(self, timestamps, rtt_times):
        self.ax.clear()
        self.ax.plot(timestamps, rtt_times)
        self.ax.set(xlabel='Tiempo (s)', ylabel='RTT (ms)', title='Estadísticas de Ping')
        self.ax.grid()
        self.canvas.draw()

     
    def handle_duration_selection(self, event):
        selected_option = self.duration_combobox.get()
        if selected_option == "Custom":
            self.custom_duration_entry.configure(state=tk.NORMAL)
        else:
            self.custom_duration_entry.configure(state=tk.DISABLED)

    def get_duration(self):
        selected_option = self.duration_combobox.get()
        if selected_option == "Custom":
            custom_duration = self.custom_duration_entry.get()
            try:
                duration = int(custom_duration)
                return duration
            except ValueError:
                return None
        else:
            try:
                duration = int(selected_option)
                return duration
            except ValueError:
                return None


if __name__ == "__main__":
    root = tk.Tk()
    app = PingApplication(root)
    root.mainloop()
