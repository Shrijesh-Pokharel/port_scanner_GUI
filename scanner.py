import unittest
import socket
from network_scanning_GUI import scan_port

class TestPortScanner(unittest.TestCase):
    def test_open_port(self):
        test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        test_socket.bind(("192.168.159.1", 0)) 
        test_socket.listen(1)
        port = test_socket.getsockname()[1]
        
        self.assertTrue(scan_port("192.168.159.1", port))
        
        test_socket.close()
    
    def test_closed_port(self):
        self.assertFalse(scan_port("192.168.159.1", 65535))

if __name__ == "__main__":
    unittest.main()
