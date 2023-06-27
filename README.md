# Project_PAA2_F55121023
Project Akhir PAA 2 (Indira Yulianti_F55121023)

## Analysis Algorithm untuk Mengevaluasi Worst Case, Best Case, dan Average Case pada Bubble Sort dan Insertion Sort:

**Bubble Sort:**
- Worst Case: Terjadi ketika array sudah terurut secara terbalik. Kompleksitas waktu worst case Bubble Sort adalah O(n^2).
- Best Case: Terjadi ketika array sudah terurut secara ascending. Dalam implementasi di atas, optimasi telah dilakukan dengan menambahkan variabel `swapped` untuk menghentikan iterasi jika tidak ada pertukaran yang dilakukan. Dalam kasus ini, kompleksitas waktu best case Bubble Sort adalah O(n).
- Average Case: Dalam rata-rata kasus, kompleksitas waktu Bubble Sort adalah O(n^2).

**Insertion Sort:**
- Worst Case: Terjadi ketika array sudah terurut secara terbalik. Kompleksitas waktu worst case Insertion Sort juga O(n^2).
- Best Case: Terjadi ketika array sudah terurut secara ascending. Kompleksitas waktu best case Insertion Sort adalah O(n).
- Average Case: Dalam rata-rata kasus, kompleksitas waktu Insertion Sort juga O(n^2).

## Analysis Algorithm untuk Mengevaluasi Worst Case, Best Case, dan Average Case pada TSP dan Dijkstra:

**Analisis Algoritma TSP:**
- Worst Case: Algoritma TSP menggunakan pendekatan brute force dengan kompleksitas O(n!) di mana n adalah jumlah kota. Dalam kasus terburuk, di mana ada n kota, waktu eksekusi algoritma akan tumbuh secara eksponensial. Oleh karena itu, dalam kasus terburuk, algoritma TSP memiliki kompleksitas waktu yang sangat tinggi, tidak dapat ditangani secara efisien untuk jumlah kota yang besar.
- Best Case: Dalam implementasi kode yang diberikan, tidak ada optimasi khusus yang dapat menghasilkan kasus terbaik dengan cepat. Oleh karena itu, dalam kasus terbaik, algoritma TSP masih memiliki kompleksitas waktu O(n!).
- Average Case: Karena algoritma TSP menggunakan pendekatan brute force, kompleksitas waktu rata-rata juga tetap O(n!).

**Analisis Algoritma Dijkstra:**
- Worst Case: Dalam algoritma Dijkstra, di setiap iterasi, kita mencari kota dengan jarak terpendek yang belum dikunjungi, dan kemudian memperbarui jarak ke kota-kota tetangganya. Dalam kasus terburuk, setiap kota akan dikunjungi dan diperbarui. Oleh karena itu, kompleksitas waktu algoritma Dijkstra dalam kasus terburuk adalah O(|V|^2), di mana |V| adalah jumlah simpul (kota) dalam graf.
- Best Case: Dalam kasus terbaik, algoritma Dijkstra dapat memiliki kompleksitas waktu O(|V| + |E| * log|V|), di mana |E| adalah jumlah tepi (jalur antar kota) dalam graf. Namun, dalam implementasi kode yang diberikan, kompleksitas waktu Dijkstra adalah O(|V|^2) karena kita menggunakan representasi graf berupa kamus dengan daftar tetangga dalam setiap simpul.
- Average Case: Dalam kasus rata-rata, kompleksitas waktu algoritma Dijkstra masih O(|V|^2) dalam implementasi kode yang diberikan.


