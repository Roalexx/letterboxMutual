import tkinter as tk
from tkinter import messagebox
from movie_functions import save_common_movies, compare_movies  # Fonksiyonları içe aktar

def show_compare_movies_page():
    # Ana sayfayı gizle
    main_frame.pack_forget()

    # Karşılaştırma sayfasını göster
    compare_frame.pack(pady=20)

def show_main_page():
    # Karşılaştırma sayfasını gizle
    compare_frame.pack_forget()

    # Ana sayfayı göster
    main_frame.pack(pady=20)

def create_gui():
    global user1_entry, user2_entry, result_text, main_frame, compare_frame, save_button

    # Ana pencereyi oluştur
    root = tk.Tk()
    root.title("Letterboxd İşlemleri")
    root.geometry("600x500")  # Pencere boyutunu artırdım

    # Ana sayfa frame
    main_frame = tk.Frame(root)
    main_frame.pack(pady=20)

    # Ana sayfa başlık etiketi
    main_title_label = tk.Label(main_frame, text="Hangi işlemi yapmak istersiniz?", font=("Helvetica", 12))
    main_title_label.pack()

    # Filmleri karşılaştır butonu
    compare_movies_button = tk.Button(main_frame, text="Filmleri Karşılaştır", command=show_compare_movies_page)
    compare_movies_button.pack(pady=10)

    # Diğer işlemler için butonlar (örnek olarak)
    other_option1_button = tk.Button(main_frame, text="Diğer İşlem 1", command=lambda: messagebox.showinfo("Bilgi", "Bu işlem henüz uygulanmadı."))
    other_option1_button.pack(pady=5)

    other_option2_button = tk.Button(main_frame, text="Diğer İşlem 2", command=lambda: messagebox.showinfo("Bilgi", "Bu işlem henüz uygulanmadı."))
    other_option2_button.pack(pady=5)

    # Karşılaştırma sayfası frame
    compare_frame = tk.Frame(root)

    # Geri butonu
    back_button = tk.Button(compare_frame, text="Geri", command=show_main_page)
    back_button.pack(side=tk.TOP, pady=10)

    # Kullanıcı adı girişi için etiket ve giriş alanları
    user1_label = tk.Label(compare_frame, text="Birinci Kullanıcı Adı:")
    user1_label.pack()
    user1_entry = tk.Entry(compare_frame)
    user1_entry.pack(pady=5)

    user2_label = tk.Label(compare_frame, text="İkinci Kullanıcı Adı:")
    user2_label.pack()
    user2_entry = tk.Entry(compare_frame)
    user2_entry.pack(pady=5)

    # Filmleri karşılaştır butonu
    compare_movies_button = tk.Button(compare_frame, text="Filmleri Karşılaştır", 
                                       command=lambda: compare_movies(user1_entry.get(), user2_entry.get(), result_text, save_button))
    compare_movies_button.pack(pady=10)

    # Sonuçların gösterileceği metin alanı
    result_text = tk.Text(compare_frame, height=10, width=50)
    result_text.pack(pady=10)
    result_text.config(state=tk.DISABLED)  # Metin kutusunu yalnızca okunur hale getir

    # Kaydet butonu
    save_button = tk.Button(compare_frame, text="Kaydet", command=save_common_movies, state=tk.DISABLED)
    save_button.pack(pady=5)  # Kaydet butonu, Filmleri Karşılaştır butonunun altında yer alacak

    # Çıkış butonu
    exit_button = tk.Button(main_frame, text="Çıkış", command=root.quit)
    exit_button.pack(pady=20)

    # Ana döngüyü başlat
    root.mainloop()

