# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan sebuah institusi pendidikan tinggi yang mengalami tantangan dalam menjaga retensi mahasiswa. Banyak mahasiswa mengalami dropout sebelum menyelesaikan studi mereka. Permasalahan ini berisiko menurunkan reputasi lembaga dan berdampak terhadap keberlangsungan operasional.

### Permasalahan Bisnis
Permasalahan utama yang dihadapi adalah:
- Tingginya tingkat mahasiswa yang **dropout**.
- Tidak adanya sistem monitoring performa akademik mahasiswa secara prediktif.
- Sulitnya mengidentifikasi mahasiswa berisiko tinggi sejak awal semester.

### Cakupan Proyek
Proyek ini mencakup:
- Membangun **dashboard performa mahasiswa** untuk memantau status akademik dan retensi.
- Mengembangkan **model machine learning** untuk memprediksi status akhir mahasiswa (Dropout, Enrolled, Graduate).
- Membuat **prototype sistem prediktif berbasis Streamlit** yang bisa digunakan oleh pihak manajemen.

### Persiapan

Sumber data: [Dataset Students Performance Dicoding]('https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
```
# install dependencies
pip install -r requirements.txt
```

## Business Dashboard
Business dashboard ini membantu pihak manajemen dalam:
- Melihat sebaran status mahasiswa (Dropout, Enrolled, Graduate)
- Menganalisis faktor akademik dan demografis terhadap performa
- Mengidentifikasi tren berdasarkan jurusan, gender, beasiswa, dll.

📊 Link Dashboard Looker Studio: [Looker Studio Dashboard]('https://lookerstudio.google.com/reporting/1cc37a9b-2245-4f1f-9f8b-f1df3d243ad2')

## Menjalankan Sistem Machine Learning
Sistem prediktif ini memungkinkan pengguna memasukkan data mahasiswa dan mendapatkan prediksi status akhir secara langsung.

Cara menjalankan secara lokal:

```
streamlit run app.py
```

Atau akses prototipe online:
🧠 Streamlit App Link: [Prototipe Streamlit]('')

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
