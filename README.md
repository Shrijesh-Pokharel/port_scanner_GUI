# Port Scanner GUI

This project is a graphical user interface (GUI) for a network port scanner, developed by [Shrijesh Pokharel](https://shrijesh.com.np/). It allows users to input an IP address and scan a specified range of ports to identify which ports are open. The application provides an intuitive interface to perform network reconnaissance tasks efficiently.

## Features

- **IP Address Input**: Enter the target IP address to initiate the port scanning process.
- **Port Range Specification**: Define the range of ports to scan, allowing for customized scanning based on user requirements.
- **Scan Results Display**: View the list of open ports identified during the scan within the application.
- **Save Scan Results**: Option to save the list of open ports to a text file for further analysis or record-keeping.

## Requirements

- Python 3.10 or higher
- Required Python libraries:
  - `socket`
  - `tkinter`

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Shrijesh-Pokharel/port_scanner_GUI.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd port_scanner_GUI
   ```

3. **Install the Required Libraries**:

   The `socket` and `tkinter` libraries are included with standard Python installations. If `tkinter` is not available, install it using your system's package manager.

## Usage

1. **Run the Application**:

   ```bash
   python3 network_scanning_GUI.py
   ```

2. **Using the GUI**:

   - Enter the target IP address in the designated input field.
   - Specify the starting and ending ports for the scan.
   - Click the "Scan" button to initiate the port scanning process.
   - The application will display the open ports identified during the scan.
   - Use the "Save Results" button to save the list of open ports to a text file for future reference.
