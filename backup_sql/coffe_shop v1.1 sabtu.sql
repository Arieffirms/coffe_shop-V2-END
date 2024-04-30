-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2024 at 03:08 AM
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
('Caffe Americano', 10, 27000, '2024-04-13 07:36:20'),
('Caffe Mocha', 10, 31000, '2024-04-19 01:56:30'),
('Cappuccino', 10, 29000, '2024-04-13 07:24:31'),
('Caramel Macchiato', 10, 37000, '2024-04-13 10:49:17'),
('Flat White', 10, 25000, '2024-04-12 08:07:48'),
('Iced Espresso and Matcha Fusion', 10, 31000, '2024-04-13 10:50:19');

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

--
-- Dumping data for table `pesanan`
--

INSERT INTO `pesanan` (`id`, `id_member`, `nama_pesanan`, `quantity`, `harga`, `diskon`, `total_harga`, `waktu_pembuatan`) VALUES
('#RCO1570', '', 'Caffe Mocha', 1, 31000, 0, 31000, '2024-04-12 01:56:30'),
('#RCO6524', '', 'Caffe Mocha', 1, 31000, 0, 31000, '2024-04-09 12:40:30');

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

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id`, `id_member`, `nama`, `nama_pesanan`, `quantity`, `harga`, `diskon`, `total_harga`, `metode_pembayaran`, `uang_customer`, `kembalian`, `waktu_pembuatan`) VALUES
('#RCO1570', '', '', 'Caffe Mocha', 1, 31000, 0, 31000, 'QRIS', 31000, 0, '2024-04-12 01:56:43'),
('#RCO4580', '', '', 'Caffe Mocha', 1, 31000, 0, 31000, 'QRIS', 31000, 0, '2024-04-06 10:49:41'),
('#RCO5462', '#rpsmbr3953', 'maulana', 'Iced Espresso and Matcha Fusio', 1, 31000, 3100, 27900, 'CASH', 30000, 2100, '2024-04-06 10:50:33'),
('#RCO6524', '', '', 'Caffe Mocha', 1, 31000, 0, 31000, 'QRIS', 31000, 0, '2024-04-09 12:41:35'),
('#RCO7039', '', '', 'Caffe Mocha', 1, 31000, 0, 31000, 'CASH', 35000, 4000, '2024-04-07 12:05:40');

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
