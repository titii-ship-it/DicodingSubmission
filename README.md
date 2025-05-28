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

Sumber data: [Dataset Students Performance Dicoding](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

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
🧠 Streamlit App Link: [Prototipe Streamlit](https://titii-ship-it-dicodingsubmission-app-19c7wt.streamlit.app/)

## Conclusion
Model machine learning yang dibangun menggunakan Random Forest Classifier berhasil mencapai akurasi ~77%, dengan f1-score terbaik untuk kelas Graduate dan Dropout. Prototipe sistem ini dapat digunakan untuk:
- Mengidentifikasi mahasiswa berisiko tinggi sejak awal
- Membantu tim akademik melakukan intervensi tepat waktu
- Memberikan dasar pengambilan keputusan berbasis data

### Rekomendasi Action Items
1. Implementasi Sistem Prediksi Dropout dan Intervensi Dini <br>
   Gunakan sistem machine learning untuk mengidentifikasi mahasiswa yang berisiko tinggi mengalami dropout secara berkala. Hasil prediksi ini dapat digunakan oleh manajemen akademik untuk melakukan intervensi dini seperti konseling, dukungan finansial, atau program mentoring.
2. Optimalisasi Dukungan Akademik dan Finansial <br>
   Tingkatkan akses mahasiswa terhadap program beasiswa, terutama bagi yang mengalami kesulitan finansial agar tidak bergantung pada hutang. Selain itu, lakukan pengawasan khusus terhadap mahasiswa di kelas malam dan mereka yang menunjukkan performa akademik rendah di semester awal.
3. Evaluasi dan Penyesuaian Kurikulum Mata Kuliah Risiko Tinggi <br>
   Lakukan analisis terhadap mata kuliah dengan tingkat kegagalan atau dropout tinggi, seperti mata kuliah manajemen. Gunakan data ini untuk meninjau kembali metode pengajaran, beban tugas, dan efektivitas kurikulum agar lebih adaptif terhadap kebutuhan mahasiswa.
