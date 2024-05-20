import socket

def scan_port(ip, port):
    try:
        # Buat objek socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Atur timeout koneksi (opsional)
        s.settimeout(1)
        
        # Coba terhubung ke alamat IP dan port tertentu
        result = s.connect_ex((ip, port))

        # Periksa hasil koneksi
        if result == 0:
            print(f"Port {port} pada IP {ip} terbuka")
        else:
            print(f"Port {port} pada IP {ip} tertutup")

        # Tutup koneksi socket
        s.close()
    except KeyboardInterrupt:
        print("Pengguna membatalkan pemindaian.")
    except socket.gaierror:
        print("Alamat IP tidak valid.")
    except socket.error:
        print("Tidak dapat terhubung ke alamat IP.")

if __name__ == "__main__":
    target_ip = input("Masukkan alamat IP yang ingin dianalisis: ")
    target_ports = input("Masukkan daftar port yang akan dianalisis (pisahkan dengan koma): ").split(",")

    for port in target_ports:
        scan_port(target_ip.strip(), int(port.strip()))
