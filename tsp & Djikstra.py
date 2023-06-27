import time
import sys


# Fungsi untuk menghitung jalur terpendek menggunakan algoritma TSP
def tsp(graph, start):
    # Simpan semua kota dalam list
    cities = list(graph.keys())
    cities.remove(start)
    shortest_path = []
    shortest_distance = sys.maxsize

    # Fungsi rekursif untuk mencari jalur terpendek
    def find_shortest_path(curr_city, cities_to_visit, path, distance):
        nonlocal shortest_path, shortest_distance

        if len(cities_to_visit) == 0:
            # Jika sudah mengunjungi semua kota, kembali ke kota awal
            path.append(start)
            distance += graph[curr_city][start]
            if distance < shortest_distance:
                # Update jalur terpendek jika ditemukan jalur yang lebih pendek
                shortest_path[:] = path
                shortest_distance = distance
            return

        for city in cities_to_visit:
            new_path = path[:]
            new_path.append(city)
            new_cities = cities_to_visit[:]
            new_cities.remove(city)
            find_shortest_path(city, new_cities, new_path, distance + graph[curr_city][city])

    # Panggil fungsi rekursif untuk mencari jalur terpendek
    find_shortest_path(start, cities, [], 0)

    return shortest_path, shortest_distance


# Fungsi untuk menghitung jalur terpendek menggunakan algoritma Dijkstra
def dijkstra(graph, start):
    # Inisialisasi jarak awal dari start ke semua kota dengan nilai tak hingga
    distances = {city: sys.maxsize for city in graph}
    distances[start] = 0

    # Set untuk melacak kota yang sudah dikunjungi
    visited = set()

    # Looping sampai semua kota dikunjungi
    while len(visited) < len(graph):
        # Temukan kota dengan jarak terpendek yang belum dikunjungi
        min_distance = sys.maxsize
        min_city = None
        for city in graph:
            if city not in visited and distances[city] < min_distance:
                min_distance = distances[city]
                min_city = city

        # Tandai kota yang telah dikunjungi
        visited.add(min_city)

        # Perbarui jarak ke kota tetangga yang belum dikunjungi
        for neighbor in graph[min_city]:
            if neighbor not in visited:
                new_distance = distances[min_city] + graph[min_city][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


# Fungsi untuk menampilkan jalur dan jarak
def print_result(path, distance):
    print("Jalur terpendek:", "->".join(path))
    print("Jarak terpendek:", distance)


# Fungsi untuk menjalankan program
def main():
    graph = {
        'a': {'a': 0, 'b': 12, 'c': 10, 'd': sys.maxsize, 'e': sys.maxsize, 'f': sys.maxsize, 'g': 12},
        'b': {'a': 12, 'b': 0, 'c': 8, 'd': 12, 'e': sys.maxsize, 'f': sys.maxsize, 'g': sys.maxsize},
        'c': {'a': 10, 'b': 8, 'c': 0, 'd': 11, 'e': 3, 'f': sys.maxsize, 'g': 9},
        'd': {'a': sys.maxsize, 'b': 12, 'c': 11, 'd': 0, 'e': 11, 'f': 10, 'g': sys.maxsize},
        'e': {'a': sys.maxsize, 'b': sys.maxsize, 'c': 3, 'd': 11, 'e': 0, 'f': 6, 'g': 7},
        'f': {'a': sys.maxsize, 'b': sys.maxsize, 'c': sys.maxsize, 'd': 10, 'e': 6, 'f': 0, 'g': 9},
        'g': {'a': 12, 'b': sys.maxsize, 'c': 9, 'd': sys.maxsize, 'e': 7, 'f': 9, 'g': 0}
    }

    print("Program Penghitungan Jalur Terpendek")

    while True:
        print("\nPilih algoritma:")
        print("1. TSP")
        print("2. Dijkstra")
        print("0. Keluar")
        choice = input("Masukkan pilihan (0-2): ")

        if choice == '1':
            start_time = time.time()
            path, distance = tsp(graph, 'a')
            elapsed_time = time.time() - start_time
            print("\nAlgoritma: TSP")
            print("Waktu komputasi: %.5f detik" % elapsed_time)
            print_result(path, distance)

        elif choice == '2':
            start_time = time.time()
            distances = dijkstra(graph, 'a')
            elapsed_time = time.time() - start_time
            print("\nAlgoritma: Dijkstra")
            print("Waktu komputasi: %.5f detik" % elapsed_time)
            for city, distance in distances.items():
                print("Jarak dari 'a' ke '%s': %d" % (city, distance))

        elif choice == '0':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


if __name__ == '__main__':
    main()
