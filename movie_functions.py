import tkinter as tk
from tkinter import messagebox, filedialog
from letterboxd_scraper import get_movies

def get_movies_from_txt():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            movies = [line.strip() for line in file.readlines()]
        return set(movies)
    return set()

def compare_movies_ui(user1_entry, user2_entry, selection_var, result_text, save_button):
    user1 = user1_entry.get()
    if selection_var.get() == "user":
        user2 = user2_entry.get()
        if not user2:
            messagebox.showwarning("Uyarı", "İkinci kullanıcı adı boş olamaz.")
            return
        movies_user2 = get_movies(user2)
    else:
        movies_user2 = get_movies_from_txt()
        if not movies_user2:
            messagebox.showwarning("Uyarı", "TXT dosyasından film alınamadı veya dosya boş.")
            return
    
    movies_user1 = get_movies(user1)
    common_movies = set(movies_user1) & set(movies_user2)

    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    if common_movies:
        result_message = f"{user1} ve diğer kaynak arasında ortak filmler:\n" + "\n".join(common_movies)
        result_text.insert(tk.END, result_message)
        save_button.config(state=tk.NORMAL)
    else:
        result_text.insert(tk.END, "Ortak film bulunamadı.")
        save_button.config(state=tk.DISABLED)
    result_text.config(state=tk.DISABLED)

def save_common_movies_ui(common_movies):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                             title="Ortak Filmleri Kaydet")
    if file_path:
        with open(file_path, 'w') as file:
            for movie in common_movies:
                file.write(f"{movie}\n")
        messagebox.showinfo("Başarılı", "Ortak filmler başarıyla kaydedildi!")
