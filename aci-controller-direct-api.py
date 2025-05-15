

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Nonaktifkan peringatan SSL biar ga ada warningnya

# Konstanta yang dipake
APIC_URL = "https://sandboxapicdc.cisco.com"  
USERNAME = "admin"
PASSWORD = "!v3G@!4@Y"
PREFIX_TENANT = "Kelompok5Tenant_"
PREFIX_APP_PROFILE = "Kelompok5AppProfile_"
DESCR = "Configured with REST API"
ANNOTAION_TENANT = "Daniel_672022019"

TENANT_NAMES = ["Normativitas"]  #ini nama tenant
APP_PROFILE_NAMES = ["Kritis", "Kreatif", "Inovatif"]  # ini Daftar nama Application Profile
APP_PROFILE_ANNOTATIONS = ["Ayu_672022033", "Sandra_672022077", "Panji_672022110"]

# Fungsi untuk login ke APIC dan mendapatkan token otentikasi
def login():
    url = f"{APIC_URL}/api/aaaLogin.json"
    payload = {"aaaUser": {"attributes": {"name": USERNAME, "pwd": PASSWORD}}}
    response = requests.post(url, json=payload, verify=False)
    response.raise_for_status()  # Memastikan respon sukses
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]

# Fungsi untuk mendapatkan jumlah Tenant dan Application Profile yang sudah ada 
def get_existing_data(token):
    headers = {"Cookie": f"APIC-cookie={token}"}
    url = f"{APIC_URL}/api/node/class/fvTenant.json"
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    tenants = response.json()["imdata"]  # Data Tenant yang ada
    
    # Inisialisasi jumlah Tenant dan Application Profile
    tenant_count = len(tenants)
    app_profile_count = 0

    # Iterasi melalui setiap Tenant untuk menghitung Application Profile
    for tenant in tenants:
        tenant_name = tenant["fvTenant"]["attributes"]["name"]
        url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant_name}.json?query-target=children&target-subtree-class=fvAp"
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        app_profile_count += len(response.json()["imdata"]) 
    
    return tenant_count, app_profile_count

# Fungsi untuk membuat Tenant dan Application Profile baru
def configure_tenant_and_app_profiles(token, tenant_name, app_profile_names, app_profile_annotations):
    headers = {"Cookie": f"APIC-cookie={token}"}

    # Membuat Tenant
    tenant_payload = {
        "fvTenant": {
            "attributes": {"name": tenant_name, "descr": DESCR, "annotation": ANNOTAION_TENANT}
        }
    }
    url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant_name}.json"
    response = requests.post(url, json=tenant_payload, headers=headers, verify=False)
    response.raise_for_status()

    # Membuat Application Profile di dalam Tenant
    for i, app_profile_name in enumerate(app_profile_names):  # Enumerasi untuk indeks
        app_profile_annotation = app_profile_annotations[i]  # Ambil anotasi sesuai indeks

        app_profile_payload = {
            "fvAp": {
                "attributes": {
                    "name": app_profile_name,
                    "descr": DESCR,
                    "annotation": app_profile_annotation
                }
            }
        }
        url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant_name}/ap-{app_profile_name}.json"
        response = requests.post(url, json=app_profile_payload, headers=headers, verify=False)
        response.raise_for_status()

# Fungsi untuk menghapus Tenant (dan semua Application Profile di dalamnya)
def delete_tenant(token, tenant_name):
    url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant_name}.json"
    headers = {"Cookie": f"APIC-cookie={token}"}
    response = requests.delete(url, headers=headers, verify=False)
    response.raise_for_status()  # Memastikan respon sukses

# --- Bagian utama program ---
def main():
    token = login()  # Login untuk mendapatkan token
    
    # Menu pilihan utama
    while True:
        print("========================================================================")
        print(" ")
        print("Pilih menu:")
        print("1. Hitung Tenant dan Application Profile yang ada")
        print("2. Buat 1 Tenant dan 3 Application Profile")
        print("3. Tampilkan informasi dan hapus konfigurasi")
        print("4. Keluar")
        print(" ")
        print("========================================================================")
        
        # Meminta input pilihan dari user
        choice = input("Masukkan pilihan (1-4): ") 
        
        # Penanganan pilihan dari user
        if choice == '1':
            tenant_count, app_profile_count = get_existing_data(token)
            print("========================================================================")
            print(" ")
            print(f"Jumlah Tenant: {tenant_count}")
            print(f"Jumlah Application Profile: {app_profile_count}")
            print(" ")
            print("========================================================================")
        
        elif choice == '2':
            tenant_name = PREFIX_TENANT + TENANT_NAMES[0]
            app_profile_names = [PREFIX_APP_PROFILE + name for name in APP_PROFILE_NAMES]
            app_profile_annotations = [name for name in APP_PROFILE_ANNOTATIONS]
            configure_tenant_and_app_profiles(token, tenant_name, app_profile_names, app_profile_annotations)
            print("========================================================================")
            print(" ")
            print(f"Tenant {tenant_name} berhasil dibuat.")
            print(f"Application Profile {', '.join(app_profile_names)} berhasil dibuat.")
            print(" ")
            print("========================================================================")

        elif choice == '3':
            print("========================================================================")
            print(" ")
            print("Nama Anggota Kelompok 5:")
            print("Daniel Satria Mahardhika - 672022019")
            print("Ayu Faza Islami - 672022033")
            print("Herdaning Sandra Kumalasari - 672022077")
            print("Anggoro Panji Sulistyo - 672022110")
            print("Tugas: Konfigurasi Tenant dan Application Profiles di ACI Controller")
            print(" ")
            print("========================================================================")

            tenant_name = PREFIX_TENANT + TENANT_NAMES[0]
            app_profile_names = [PREFIX_APP_PROFILE + name for name in APP_PROFILE_NAMES]
            delete_tenant(token, tenant_name)
            print(f"Tenant {tenant_name} berhasil dihapus.")
            print(f"Application Profile {', '.join(app_profile_names)} berhasil dihapus.")
            print(" ")
            print("========================================================================")

        elif choice == '4':
            print("Keluar dari program.")
            break 
        else:
            print("Pilihan tidak valid.")

# Jalankan program utama
if __name__ == "__main__":
    main()
