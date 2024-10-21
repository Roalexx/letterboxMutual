import tkinter as tk
from tkinter import messagebox, filedialog
from letterboxd_scraper import get_movies  # get_movies fonksiyonunu içe aktar

common_movies = set()  # Ortak filmleri tutmak için bir set oluştur

def save_common_movies():
    global common_movies  # common_movies'u global olarak tanımla
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                               title="Ortak Filmleri Kaydet")
    if file_path:
        with open(file_path, 'w') as file:
            for movie in common_movies:
                file.write(f"{movie}\n")
        messagebox.showinfo("Başarılı", "Ortak filmler başarıyla kaydedildi!")

def compare_movies(user1, user2, result_text, save_button):
    global common_movies  # common_movies'u global olarak tanımla
    
    if user1 and user2:
        # Kullanıcı adlarıyla filmleri çek
        movies_user1 = get_movies(user1)
        movies_user2 = get_movies(user2)

        # Filmleri karşılaştır
        common_movies = set(movies_user1) & set(movies_user2)  # Ortak filmleri bul

        result_text.config(state=tk.NORMAL)  # Metin kutusunu düzenlenebilir yap
        result_text.delete(1.0, tk.END)  # Önceki sonuçları temizle
        if common_movies:
            result_message = f"{user1} ve {user2} kullanıcısının izlediği ortak filmler:\n" + "\n".join(common_movies)
            result_text.insert(tk.END, result_message)

            # Kaydet butonunu aktifleştir
            save_button.config(state=tk.NORMAL)  # Kaydet butonunu aktifleştir
            
        else:
            result_text.insert(tk.END, f"{user1} ve {user2} kullanıcısının ortak filmi bulunamadı.")
            save_button.config(state=tk.DISABLED)  # Ortak film yoksa kaydet butonunu devre dışı bırak
        
        result_text.config(state=tk.DISABLED)  # Metin kutusunu yalnızca okunur hale getir
    else:
        messagebox.showwarning("Uyarı", "Kullanıcı adları boş olamaz.")
