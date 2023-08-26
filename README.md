# VitalCare

This project is developed as part of our DBMS course in the 5th semester. The goal of this project is to create a web-based application that facilitates efficient management of blood donation and distribution within a blood bank.

<p align="center">
  <img src="https://github.com/SigdelAsmita/blood_bank_management_system/blob/main/assets/HomeScreen.jpg" alt="HomePage" width="70%">
</p>



## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Contributors](#contributors)

## About

The Blood Bank Management System provides a platform for blood banks to manage their donor information, blood inventory, and blood requests. It aims to streamline the blood donation process, and facilitate timely distribution of blood to hospitals in need.

## Features

- **Donor Registration:** Allow donors to register and provide their personal information.
- **Blood Donation:** Record blood donation details including blood type, donation date, and health status.
- **Donor Database:** Maintain a centralized database of donors with their contact information.
- **Blood Requests:** Hospitals can place requests for specific blood types.

## Technologies Used

- **Frontend:** HTML, CSS
- **Backend:** Django (Python Web Framework)
- **Database:** PostgreSQL

## Getting Started

To run the Blood Bank Management System locally on your machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/SigdelAsmita/blood-bank-management-system.git
   cd blood-bank-management-system
2. Install project dependencies:
   ```bash
   pip install -r requirements.txt
3. Create a PostgreSQL database and update the database settings in `settings.py.`
4. Run migrations:
   ```bash
   python manage.py migrate
5. Start the development server:
   ```bash
   python manage.py runserver
6. Open your web browser and navigate to http://localhost:8000 to access the application.

## Contributors

- **Aditi Kharel** - 077BEI008
- **Asmita Sigdel** - 077BEI013
- **Aviyanshu Adhikari** - 077BEI014

