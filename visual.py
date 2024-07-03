import tkinter as tk
from tkinter import messagebox

from group4.toolbox.emergency_k import Emergency, EmergencyType
from group4.toolbox.minheap_k import MinHeap

class EmergencyQueueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emergency Queue Management")
        
        self.queue = MinHeap()  # 使用MinHeap作为优先级队列

        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.queue_listbox = tk.Listbox(self.frame, height=15, width=50)
        self.queue_listbox.pack(side=tk.LEFT, padx=10)
        self.queue_listbox.bind('<Motion>', self.show_details)
        self.queue_listbox.bind('<Button-1>', self.remove_item)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.queue_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.queue_listbox.yview)

        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Emergency ID:").grid(row=0, column=0, padx=5)
        self.id_entry = tk.Entry(self.add_frame)
        self.id_entry.grid(row=0, column=1, padx=5)

        tk.Label(self.add_frame, text="Type:").grid(row=1, column=0, padx=5)
        self.type_entry = tk.Entry(self.add_frame)
        self.type_entry.grid(row=1, column=1, padx=5)

        tk.Label(self.add_frame, text="Severity:").grid(row=2, column=0, padx=5)
        self.severity_entry = tk.Entry(self.add_frame)
        self.severity_entry.grid(row=2, column=1, padx=5)

        tk.Label(self.add_frame, text="Location:").grid(row=3, column=0, padx=5)
        self.location_entry = tk.Entry(self.add_frame)
        self.location_entry.grid(row=3, column=1, padx=5)

        tk.Label(self.add_frame, text="X:").grid(row=4, column=0, padx=5)
        self.x_entry = tk.Entry(self.add_frame)
        self.x_entry.grid(row=4, column=1, padx=5)

        tk.Label(self.add_frame, text="Y:").grid(row=5, column=0, padx=5)
        self.y_entry = tk.Entry(self.add_frame)
        self.y_entry.grid(row=5, column=1, padx=5)

        self.add_button = tk.Button(self.root, text="Add Emergency", command=self.add_emergency)
        self.add_button.pack(pady=10)

    def add_emergency(self):
        emergency_id = self.id_entry.get()
        emergency_type = self.type_entry.get().upper()
        severity = int(self.severity_entry.get())
        location = self.location_entry.get()
        x = int(self.x_entry.get())
        y = int(self.y_entry.get())

        try:
            emergency = Emergency(emergency_id, EmergencyType[emergency_type], severity, location, x, y)
            self.queue.insert(emergency, severity)
            self.update_listbox()
            self.clear_entries()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_item(self, event):
        selection = self.queue_listbox.curselection()
        if selection:
            index = selection[0]
            self.queue_listbox.delete(index)
            self.queue.heap.pop(index)
            self.queue._heapify_down(index)
            self.update_listbox()

    def show_details(self, event):
        selection = self.queue_listbox.curselection()
        if selection:
            index = selection[0]
            emergency = self.queue.heap[index][1]
            details = f"ID: {emergency.emergency_id}, Type: {emergency.emergency_type.name}, Severity: {emergency.severity}, Location: {emergency.location}, Coordinates: ({emergency.x}, {emergency.y})"
            self.queue_listbox.config(tooltip=details)
        else:
            self.queue_listbox.config(tooltip="")

    def update_listbox(self):
        self.queue_listbox.delete(0, tk.END)
        for priority, emergency in self.queue.heap:
            self.queue_listbox.insert(tk.END, f"ID: {emergency.emergency_id}, Type: {emergency.emergency_type.name}, Severity: {emergency.severity}, Location: {emergency.location}")

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.severity_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.x_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = EmergencyQueueApp(root)
    root.mainloop()
