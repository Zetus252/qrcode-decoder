# QR Code Decoder (Python)

Project sederhana untuk **membaca / decode QR Code dari gambar** menggunakan **OpenCV (`cv2`)** dan **pyzbar**.

---

## 📌 Fitur

* Membaca QR Code dari file gambar
* Menampilkan teks hasil decode di terminal
* Sederhana dan cocok untuk pemula

---

## 🛠️ Requirement

* Python **3.10+** (disarankan 3.12)
* OS: Linux / Windows / macOS

Library Python:

* `opencv-python`
* `pyzbar`
* `numpy` (dependency OpenCV)

---

## 📂 Struktur Project

```text
qrcode-decoder/
├── qrcodedeco.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup (WAJIB IKUT URUTAN)

### 1️⃣ Clone repository

```bash
git clone https://github.com/Zetus252/qrcode-decoder.git
cd qrcode-decoder
```

---

### 2️⃣ Buat virtual environment (disarankan)

```bash
python3 -m venv venv
```

Aktifkan:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

Jika berhasil, terminal akan muncul:

```text
(venv)
```

---

### 3️⃣ Install dependency

```bash
pip install -r requirements.txt
```

Jika belum ada `requirements.txt`, install manual:

```bash
pip install opencv-python pyzbar
```

---

## ▶️ Cara Menjalankan Program

### 1️⃣ Siapkan gambar QR Code

Simpan file QR Code, contoh:

```text
qrcode.png
```

Letakkan di folder yang sama dengan `qrcodedeco.py`.

---

### 2️⃣ Edit path gambar

Buka `qrcodedeco.py` dan ubah:

```python
image = cv2.imread('put your qrcode path here')
```

Menjadi contoh:

```python
image = cv2.imread('qrcode.png')
```

Atau path lengkap:

```python
image = cv2.imread('/home/user/Pictures/qrcode.png')
```

---

### 3️⃣ Run program

```bash
python qrcodedeco.py
```

---

## 📤 Contoh Output

Jika QR Code berhasil terbaca:

```text
Decoded Text: https://example.com
```

Jika gagal:

```text
No QR code found or could not be decoded
```

---

## ⚠️ Catatan Penting

* Pastikan gambar **jelas dan tidak blur**
* QR Code harus **terbaca kamera normal**
* Gunakan **venv** agar dependency tidak bentrok

---

## 📦 Generate `requirements.txt`

Jika ingin update dependency:

```bash
pip freeze > requirements.txt
```

---

## 📜 License

Project ini bebas digunakan untuk belajar.

