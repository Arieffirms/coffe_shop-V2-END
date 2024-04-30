-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 06, 2024 at 12:47 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `coffe_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_member`
--

CREATE TABLE `customer_member` (
  `id_member` varchar(20) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `waktu_pembuatan` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_member`
--

INSERT INTO `customer_member` (`id_member`, `nama`, `waktu_pembuatan`) VALUES
('#rpsmbr3953243', 'maulana', '2024-04-06 07:36:32');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `nama_barang` varchar(35) NOT NULL,
  `stock` int(30) NOT NULL,
  `harga` int(30) NOT NULL,
  `waktu_restock` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`nama_barang`, `stock`, `harga`, `waktu_restock`) VALUES
('Caffe Americano', 209, 27000, '2024-04-13 07:36:20'),
('Caffe Mocha', 329, 31000, '2024-04-13 07:31:39'),
('Cappuccino', 209, 29000, '2024-04-13 07:24:31'),
('Caramel Macchiato', 333, 37000, '2024-04-13 07:45:55'),
('Flat White', 117, 25000, '2024-04-12 08:07:48'),
('Iced Espresso and Matcha Fusion', 105, 31000, '2024-04-13 07:31:45');

-- --------------------------------------------------------

--
-- Table structure for table `pesanan`
--

CREATE TABLE `pesanan` (
  `id` varchar(11) NOT NULL,
  `id_member` varchar(30) NOT NULL,
  `nama_pesanan` varchar(30) NOT NULL,
  `quantity` int(30) NOT NULL,
  `harga` int(30) NOT NULL,
  `diskon` int(11) NOT NULL,
  `total_harga` int(30) NOT NULL,
  `waktu_pembuatan` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id` varchar(11) NOT NULL,
  `id_member` varchar(11) DEFAULT NULL,
  `nama` varchar(30) NOT NULL,
  `nama_pesanan` varchar(30) NOT NULL,
  `quantity` int(30) NOT NULL,
  `harga` int(30) NOT NULL,
  `diskon` int(11) NOT NULL,
  `total_harga` int(30) NOT NULL,
  `metode_pembayaran` varchar(10) NOT NULL,
  `uang_customer` int(30) NOT NULL,
  `kembalian` int(11) NOT NULL,
  `waktu_pembuatan` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user_karyawan`
--

CREATE TABLE `user_karyawan` (
  `id` varchar(11) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `no_tlp` varchar(14) NOT NULL,
  `akun_dibuat` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_karyawan`
--

INSERT INTO `user_karyawan` (`id`, `nama`, `username`, `password`, `no_tlp`, `akun_dibuat`) VALUES
('KRYW044097', 'arief firmansyah', 'firmans2@gmail.com', '123', '081311403063', '2024-04-06 07:35:38'),
('KRYW583789', 'Arief Smith', 'Smith@gmail.com', '123', '081311403063', '2024-03-31 14:18:10'),
('KRYW893004', 'Aisyah ', 'aish@gmail.com', '123', '08342342314', '2024-03-31 14:20:29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_member`
--
ALTER TABLE `customer_member`
  ADD PRIMARY KEY (`id_member`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`nama_barang`);

--
-- Indexes for table `pesanan`
--
ALTER TABLE `pesanan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_karyawan`
--
ALTER TABLE `user_karyawan`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
