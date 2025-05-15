

# Konfigurasi ACI Controller menggunakan Direct API

Program ini melakukan konfigurasi pada ACI Controller menggunakan Direct API. Terdapat tiga tahapan/menu dalam program ini:

1. **Pencatatan Jumlah Tenant dan Application Profile**: Menghitung jumlah Tenant dan Application Profile yang sudah ada.
2. **Konfigurasi Tenant dan Application Profile**: Menambahkan 1 Tenant (Normativitas) dan 3 Application Profile.
3. **Menampilkan Informasi Anggota**: Menampilkan nama dan NIM anggota kelompok, serta menghapus konfigurasi yang telah ditambahkan.

## Persyaratan

Sebelum menjalankan program, pastikan Anda telah menginstal dependensi yang diperlukan. Gunakan perintah berikut:

```bash
pip install -r requirements.txt
```

## Cara Menjalankan Program

Setelah menginstal dependensi, Anda dapat menjalankan program dengan perintah berikut:

```bash
python aci-controller-direct-api.py
```

## Struktur Nama

- **Tenant**:  
  - Normativitas  

- **Application Profile**:  
  - Kritis  
  - Kreatif  
  - Inovatif  

### Atribut yang dikonfigurasi

- `descr`
- `annotation`
