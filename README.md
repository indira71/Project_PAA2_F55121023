# Project_PAA2_F55121023
Project Akhir PAA 2 (Indira Yulianti_F55121023)

1. Analysis algorithm untuk mengevaluasi Worst case, Best case, Average case pada bubble sort dan Insertion Sort: 
  a. Worst Case:
     - Bubble Sort: Worst case terjadi ketika array sudah terurut secara terbalik. Kompleksitas waktu worst case bubble sort adalah O(n^2).
     - Insertion Sort: Worst case terjadi ketika array sudah terurut secara terbalik. Kompleksitas waktu worst case insertion sort juga O(n^2).
  b.Best Case:
    - Bubble Sort: Best case terjadi ketika array sudah terurut secara ascending. Namun, dalam implementasi di atas, optimasi telah dilakukan dengan  menambahkan variabel swapped untuk menghentikan iterasi jika tidak ada pertukaran yang dilakukan. Dalam kasus ini, kompleksitas waktu best case bubble sort adalah O(n).
    - Insertion Sort: Best case terjadi ketika array sudah terurut secara ascending. Kompleksitas waktu best case insertion sort adalah O(n).
  c. Average Case:
    - Bubble Sort: Dalam rata-rata kasus, kompleksitas waktu bubble sort adalah O(n^2).
    - Insertion Sort: Dalam rata-rata kasus, kompleksitas waktu insertion sort juga O(n^2).
      
2. Analysis algorithm untuk mengevaluasi Worst case, Best case, Average case pada TSP dan Dijkstra:
   a. Analisis Algoritma TSP:
   - Worst Case: Algoritma TSP menggunakan pendekatan brute force dengan kompleksitas O(n!) di mana n adalah jumlah kota. Dalam kasus terburuk, di mana ada n kota, waktu eksekusi algoritma akan tumbuh secara eksponensial. Oleh karena itu, dalam kasus terburuk, algoritma TSP memiliki kompleksitas waktu yang sangat tinggi, tidak dapat ditangani secara efisien untuk jumlah kota yang besar.
   - Best Case: Dalam implementasi kode yang diberikan, tidak ada optimasi khusus yang dapat menghasilkan kasus terbaik dengan cepat. Oleh karena itu, dalam kasus terbaik, algoritma TSP masih memiliki kompleksitas waktu O(n!).
   - Average Case: Karena algoritma TSP menggunakan pendekatan brute force, kompleksitas waktu rata-rata juga tetap O(n!).
  b. Analisis Algoritma Dijkstra:
  - Worst Case: Dalam algoritma Dijkstra, di setiap iterasi, kita mencari kota dengan jarak terpendek yang belum dikunjungi, dan kemudian memperbarui jarak ke kota-kota tetangganya. Dalam kasus terburuk, setiap kota akan dikunjungi dan diperbarui. Oleh karena itu, kompleksitas waktu algoritma Dijkstra dalam kasus terburuk adalah O(|V|^2), di mana |V| adalah jumlah simpul (kota) dalam graf.
  - Best Case: Dalam kasus terbaik, algoritma Dijkstra dapat memiliki kompleksitas waktu O(|V| + |E| * log|V|), di mana |E| adalah jumlah tepi (jalur antar kota) dalam graf. Namun, dalam implementasi kode yang diberikan, kompleksitas waktu Dijkstra adalah O(|V|^2) karena kita menggunakan representasi graf berupa kamus dengan daftar tetangga dalam setiap simpul.
  - Average Case: Dalam kasus rata-rata, kompleksitas waktu algoritma Dijkstra masih O(|V|^2) dalam implementasi kode yang diberikan.
