import qrcode
import io
import base64

def generate_qr_code(tool_code, tool_name):
    """Generuje kod QR dla narzędzia"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Dane w kodzie QR
    qr_data = f"TOOL:{tool_code}|{tool_name}"
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Konwertuj do base64 dla wysłania
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return img_base64