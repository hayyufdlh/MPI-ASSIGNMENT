# MPI-ASSIGNMENT

Parallel Sum Calculator Menggunakan Message Passing Interface (MPI)

Tujuan

Mempelajari penggunaan Message Passing Interface (MPI) dalam pemrograman paralel untuk membagi pekerjaan komputasi ke beberapa proses dan menggabungkan hasilnya menjadi satu keluaran.

MPI Assignment – Parallel Sum Calculator

Message Passing Interface (MPI) merupakan teknologi yang digunakan dalam komputasi paralel untuk memungkinkan beberapa proses bekerja secara bersamaan pada tugas yang sama. MPI menggunakan mekanisme pertukaran pesan (message passing) sehingga setiap proses dapat berkomunikasi dan bertukar informasi meskipun memiliki ruang memori yang terpisah.

Pada tugas ini, MPI diterapkan untuk melakukan perhitungan jumlah bilangan dari 1 sampai 1000 secara paralel. Rentang bilangan dibagi ke beberapa proses sehingga setiap proses hanya menangani sebagian data. Setelah seluruh proses menyelesaikan perhitungannya, hasil dari masing-masing proses dikumpulkan dan dijumlahkan untuk memperoleh hasil akhir.
