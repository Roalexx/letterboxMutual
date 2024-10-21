import tkinter as tk
from tkinter import messagebox
from movie_functions import compare_movies_ui, save_common_movies_ui

def create_gui():
    global user1_entry, user2_entry, result_text, save_button, selection_var
    global main_frame, compare_frame, common_movies, user2_label  # Global değişkenler olarak tanımlandı

    root = tk.Tk()
    root.title("Letterboxd İşlemleri")
    root.geometry("600x500")

    # Ana sayfa frame
    main_frame = tk.Frame(root)
    main_frame.pack(pady=20)

    main_title_label = tk.Label(main_frame, text="Hangi işlemi yapmak istersiniz?", font=("Helvetica", 12))
    main_title_label.pack()

    compare_movies_button = tk.Button(main_frame, text="Filmleri Karşılaştır", command=show_compare_movies_page)
    compare_movies_button.pack(pady=10)

    compare_frame = tk.Frame(root)

    back_button = tk.Button(compare_frame, text="Geri", command=show_main_page)
    back_button.grid(row=0, column=0, pady=10, sticky="w")

    user1_label = tk.Label(compare_frame, text="Birinci Kullanıcı Adı:")
    user1_label.grid(row=1, column=0, sticky="w")
    user1_entry = tk.Entry(compare_frame)
    user1_entry.grid(row=1, column=1, pady=5)

    # Seçim için radio butonlar
    selection_var = tk.StringVar(value="user")
    user_radio = tk.Radiobutton(compare_frame, text="İkinci Kullanıcı Adı", variable=selection_var, value="user", command=toggle_user2_entry)
    txt_radio = tk.Radiobutton(compare_frame, text="TXT Dosyası", variable=selection_var, value="txt", command=toggle_user2_entry)
    user_radio.grid(row=2, column=0, sticky="w")
    txt_radio.grid(row=2, column=1, sticky="w")

    user2_label = tk.Label(compare_frame, text="İkinci Kullanıcı Adı:")
    user2_label.grid(row=3, column=0, sticky="w")
    user2_entry = tk.Entry(compare_frame)
    user2_entry.grid(row=3, column=1, pady=5)

    compare_button = tk.Button(compare_frame, text="Filmleri Karşılaştır",
                               command=lambda: compare_movies_ui(user1_entry, user2_entry, selection_var, result_text, save_button))
    compare_button.grid(row=4, column=0, columnspan=2, pady=10)

    result_text = tk.Text(compare_frame, height=10, width=50)
    result_text.grid(row=5, column=0, columnspan=2, pady=10)
    result_text.config(state=tk.DISABLED)

    save_button = tk.Button(compare_frame, text="Kaydet", command=lambda: save_common_movies_ui(common_movies), state=tk.DISABLED)
    save_button.grid(row=6, column=0, columnspan=2, pady=5)

    exit_button = tk.Button(main_frame, text="Çıkış", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

def toggle_user2_entry():
    """TXT Dosyası seçildiğinde ikinci kullanıcı adını gizle, aksi halde göster."""
    if selection_var.get() == "txt":
        user2_label.grid_remove()
        user2_entry.grid_remove()
    else:
        user2_label.grid()
        user2_entry.grid()

def show_compare_movies_page():
    global main_frame, compare_frame  # Global değişkenler olarak tanımlandı
    main_frame.pack_forget()
    compare_frame.pack(pady=20)

def show_main_page():
    global main_frame, compare_frame  # Global değişkenler olarak tanımlandı
    compare_frame.pack_forget()
    main_frame.pack(pady=20)

if __name__ == "__main__":
    create_gui()
