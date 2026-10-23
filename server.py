import http.server
import socket
import socketserver

# تحديد البورت (Port) للسيرفر
PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    # إضافة الدعم الصحيح لملفات الـ Manifest لتجنب مشاكل الكاش في البلايستيشن
    def end_headers(self):
        if self.path.endswith(".manifest"):
            self.send_header("Content-Type", "text/cache-manifest")
        super().end_headers()

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

Handler = CustomHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    print("=" * 60)
    print("🚀 PS Clinic Local Test Server is Running!")
    print("=" * 60)
    print(f"👉 Open this link on your PC browser: http://localhost:{PORT}")
    print(f"👉 Or type this IP on your PS4 browser:   http://{local_ip}:{PORT}")
    print("=" * 60)
    print("Press Ctrl + C to stop the server.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server stopped successfully.")