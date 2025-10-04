import pandas as pd
pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)

file_path = "FC26_20250921"

try:
    df = pd.read_csv(file_path)

    wanted_columns = ["player_id", "short_name", "long_name", "club_name", "player_positions", "overall", "potential"]
    wanted_df = df[wanted_columns].copy()

    player_data = wanted_df.set_index("player_id")
    original = player_data.copy()


except FileNotFoundError:
    print(f"{file_path} isimli dosya bulunamadı.")
    print(f"Lütfen {file_path} dosyanızın players.py dosyası ile aynı konumda olduğundan emin olunuz.")

print("\n" + "="*100 + "\n")

def save(wanted_save):
    global player_data
    print("Yaptığınız filte/sıralamayı kaydetmek istiyor musun?\n 1- Evet\n 2- Hayır")
    saving_input = input("\nİstediğiniz seçeneğin numarasını giriniz: ")
    match str(saving_input):
        case "1":
            player_data = wanted_save.copy()
        
        case "2":
            return
        
        case _:
            print("Geçerli bir sayı girmediniz!\n")

def want_player():
    wanted_player_inp = input("\nBilgilerini istediğiniz oyuncunun ismini giriniz: ")
    wanted_player = player_data[player_data["long_name"].str.contains(wanted_player_inp, case=False)]
    print("\n")
    print(wanted_player)
    save(wanted_player)

def filter_players():
    print("Filtrelemek istediğiniz kategori nedir?\n 1- Kulüp İsmi\n 2- Pozisyon\n 3- Yetenek\n 4- Potansiyel\n 5- Geri")
    wanted_filter_input = input("\nİstediğiniz filtrenin numarasını giriniz: ")
    print("\n")
    match str(wanted_filter_input):
        case "1":
            wanted_club_name = input("Kulüp ismi giriniz: ")
            wanted_filter = player_data[player_data["club_name"].str.contains(wanted_club_name, case=False, na=False)]
            print("\n")
            print(wanted_filter)
            print("\n")
            save(wanted_filter)
        
        case "2":
            wanted_position = input("Posizyon giriniz (GK - RB - CB - LB - CDM - CM - CAM - RM - RW - LM - LW - ST): ")
            wanted_filter = player_data[player_data["player_positions"].str.contains(wanted_position, case=False)]
            print("\n")
            print(wanted_filter)
            print("\n")
            save(wanted_filter)
        
        case "3":
            wanted_overall = input("İstediğiniz minimum yeteneği seçiniz (0-100): ")
            wanted_filter = player_data[player_data["overall"] >= int(wanted_overall)]
            print("\n")
            print(wanted_filter)
            print("\n")
            save(wanted_filter)
        
        case "4":
            wanted_potential = input("İstediğiniz minimum potansiyeli seçiniz (0-100): ")
            wanted_filter = player_data[player_data["potential"] >= int(wanted_potential)]
            print("\n")
            print(wanted_filter)
            print("\n")
            save(wanted_filter)
        
        case "5":
            return
        
        case _:
            print("Geçerli bir sayı girmediniz!\n")

def sort_players():
    print("Oyuncuları sıralamak istediğiniz kategori nedir?\n 1- Kulüp (A-Z)\n 2- Yetenek (Artan)\n 3- Yetenek (Azalan)\n 4- Potansiyel (Artan)\n 5- Potansiyel (Azalan)\n 6- Geri")
    wanted_sort_input = input("\nİstediğiniz sıralamanın numarasını giriniz: ")
    match str(wanted_sort_input):
        case "1":
            club_sorted = player_data.sort_values(by=["club_name"], na_position="last")
            print(club_sorted)
            save(club_sorted)
        
        case "2":
            overall_sorted_asc = player_data.sort_values(by=["overall"], na_position="last")
            print(overall_sorted_asc)
            save(overall_sorted_asc)
        
        case "3":
            overall_sorted_desc = player_data.sort_values(by=["overall"], ascending=False, na_position="last")
            print(overall_sorted_desc)
            save(overall_sorted_desc)
        
        case "4":
            potential_sorted_asc = player_data.sort_values(by=["potential"], na_position="last")
            print(potential_sorted_asc)
            save(potential_sorted_asc)
        
        case "5":
            potential_sorted_desc = player_data.sort_values(by=["potential"], ascending=False, na_position="last")
            print(potential_sorted_desc)
            save(potential_sorted_desc)
        
        case "6":
            return
        
        case _:
            print("Geçerli bir sayı girmediniz!\n")


def Main():
    global player_data
    finish = True
    while (finish):
        print("Hangi işlemi yapmak istiyorsunuz?\n 1- Oyuncu Aratma\n 2- Filtre Ekleme\n 3- Oyuncuları Sıralama\n 4- Kayıtlı filtre/sıralamayı sil\n 5- Çıkış")
        islem = input("\nLütfen yapmak istediğiniz işlemin numarasını girin: ")

        match str(islem):
            case "1":
                print("\n")
                want_player()
                print("\n")
            
            case "2":
                print("\n")
                filter_players()
                print("\n")

            case "3":
                print("\n")
                sort_players()
                print("\n")

            case "4":
                player_data = original
                print("\nFiltre/Sıralama temizlendi")

            case "5":
                print("\nÇıkış yaptınız...")
                finish=False
            
            case _:
                "Hatalı sayı girdiniz. Lütfen tekrar deneyin.\n"



        
Main()

print("\n" + "="*100 + "\n")