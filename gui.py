import tkinter as tk
from tkinter import messagebox, filedialog
from movie_functions import compare_movies_ui, save_common_movies_ui, get_movies
from letterboxd_scraper import get_movies as scrape_movies

def create_gui():
    global user1_entry, user2_entry, result_text_compare, save_common_button
    global main_frame, compare_frame, user_movies_frame, user_result_text, save_user_button
    global user2_label, selection_var  # Global değişkenler

    root = tk.Tk()
    root.title("Letterboxd İşlemleri")
    root.geometry("600x500")

    # Ana sayfa frame
    main_frame = tk.Frame(root)
    main_frame.pack(pady=20)

    main_title_label = tk.Label(main_frame, text="Hangi işlemi yapmak istersiniz?", font=("Helvetica", 12))
    main_title_label.pack()

    # Filmleri karşılaştır butonu
    compare_movies_button = tk.Button(main_frame, text="Filmleri Karşılaştır", command=show_compare_movies_page)
    compare_movies_button.pack(pady=10)

    # Kullanıcının filmlerini göster butonu
    user_movies_button = tk.Button(main_frame, text="Filmleriniz", command=show_user_movies_page)
    user_movies_button.pack(pady=10)

    # Karşılaştırma frame'ini oluştur
    global compare_frame
    compare_frame = create_compare_frame(root)

    # Kullanıcının filmlerini gösteren frame
    user_movies_frame = create_user_movies_frame(root)

    exit_button = tk.Button(main_frame, text="Çıkış", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

def create_compare_frame(root):
    global user1_entry, user2_entry, result_text_compare, save_common_button
    global user2_label, selection_var  # Global değişkenler

    frame = tk.Frame(root)

    back_button = tk.Button(frame, text="Geri", command=show_main_page)
    back_button.grid(row=0, column=0, pady=10, sticky="w")

    user1_label = tk.Label(frame, text="Birinci Kullanıcı Adı:")
    user1_label.grid(row=1, column=0, sticky="w")
    user1_entry = tk.Entry(frame)
    user1_entry.grid(row=1, column=1, pady=5)

    # Seçim için radio butonlar
    selection_var = tk.StringVar(value="user")  # Global değişken burada tanımlandı
    user_radio = tk.Radiobutton(frame, text="İkinci Kullanıcı Adı", variable=selection_var, value="user", command=toggle_user2_entry)
    txt_radio = tk.Radiobutton(frame, text="TXT Dosyası", variable=selection_var, value="txt", command=toggle_user2_entry)
    user_radio.grid(row=2, column=0, sticky="w")
    txt_radio.grid(row=2, column=1, sticky="w")

    user2_label = tk.Label(frame, text="İkinci Kullanıcı Adı:")
    user2_label.grid(row=3, column=0, sticky="w")
    user2_entry = tk.Entry(frame)
    user2_entry.grid(row=3, column=1, pady=5)

    # Filmleri karşılaştır butonu
    compare_button = tk.Button(frame, text="Filmleri Karşılaştır",
                               command=lambda: compare_movies_ui(user1_entry, user2_entry, selection_var, result_text_compare, save_common_button))
    compare_button.grid(row=4, column=0, columnspan=2, pady=10)

    result_text_compare = tk.Text(frame, height=10, width=50)
    result_text_compare.grid(row=5, column=0, columnspan=2, pady=10)
    result_text_compare.config(state=tk.DISABLED)

    save_common_button = tk.Button(frame, text="Kaydet", command=lambda: save_common_movies_ui(get_common_movies()), state=tk.DISABLED)
    save_common_button.grid(row=6, column=0, columnspan=2, pady=5)

    return frame

def create_user_movies_frame(root):
    global user_result_text, save_user_button

    frame = tk.Frame(root)

    back_button = tk.Button(frame, text="Geri", command=show_main_page)
    back_button.grid(row=0, column=0, pady=10, sticky="w")

    user_label = tk.Label(frame, text="Kullanıcı Adı:")
    user_label.grid(row=1, column=0, sticky="w")
    user_entry = tk.Entry(frame)
    user_entry.grid(row=1, column=1, pady=5)

    fetch_button = tk.Button(frame, text="Filmleri Getir", command=lambda: fetch_and_display_user_movies(user_entry.get()))
    fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

    global user_result_text  # global olarak tanımlandı
    user_result_text = tk.Text(frame, height=10, width=50)
    user_result_text.grid(row=3, column=0, columnspan=2, pady=10)
    user_result_text.config(state=tk.DISABLED)

    global save_user_button  # global olarak tanımlandı
    save_user_button = tk.Button(frame, text="Kaydet", command=lambda: save_user_movies(user_result_text.get(1.0, tk.END)), state=tk.DISABLED)
    save_user_button.grid(row=4, column=0, columnspan=2, pady=5)

    return frame

def fetch_and_display_user_movies(username):
    """Kullanıcının filmlerini al ve göster."""
    movies = scrape_movies(username)
    user_result_text.config(state=tk.NORMAL)
    user_result_text.delete(1.0, tk.END)
    if movies:
        user_result_text.insert(tk.END, "Kullanıcının Filmleri:\n" + "\n".join(movies))
        user_result_text.config(state=tk.DISABLED)
        save_user_button.config(state=tk.NORMAL)  # Kaydet butonunu etkinleştir
    else:
        user_result_text.insert(tk.END, "Film bulunamadı.")
        user_result_text.config(state=tk.DISABLED)

def save_user_movies(movies):
    """Kullanıcının filmlerini kaydet."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                             title="Filmleri Kaydet")
    if file_path:
        with open(file_path, 'w') as file:
            for movie in movies.splitlines():
                if movie:  # Boş satırları kaydetmemek için
                    file.write(f"{movie}\n")
        messagebox.showinfo("Başarılı", "Filmler başarıyla kaydedildi!")

def show_user_movies_page():
    global main_frame, user_movies_frame  # Global değişkenler
    main_frame.pack_forget()
    user_movies_frame.pack(pady=20)

def toggle_user2_entry():
    """TXT Dosyası seçildiğinde ikinci kullanıcı adını gizle, aksi halde göster."""
    if selection_var.get() == "txt":
        user2_label.grid_remove()
        user2_entry.grid_remove()
    else:
        user2_label.grid()
        user2_entry.grid()

def show_compare_movies_page():
    global main_frame, compare_frame  # Global değişkenler
    main_frame.pack_forget()
    compare_frame.pack(pady=20)

def show_main_page():
    global main_frame, compare_frame, user_movies_frame  # Global değişkenler
    compare_frame.pack_forget()
    user_movies_frame.pack_forget()
    main_frame.pack(pady=20)

def get_common_movies():
    """Ortak filmleri almak için bir fonksiyon ekleyelim."""
    result_text_compare.config(state=tk.NORMAL)
    movies = result_text_compare.get(1.0, tk.END).strip()
    result_text_compare.config(state=tk.DISABLED)
    return movies.splitlines() if movies else []
