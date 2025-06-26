# **URL Shortener & Link Expander**
*A Python tool to shorten long URLs, expand shortened links, and generate QR codes for easy sharing.*

## **Project Overview**
This project solves two key problems:
1. **Shortening lengthy URLs** (e.g., for social media or professional use).
2. **Reversing shortened links** to reveal their original source (useful for verifying suspicious links).
3. **Optional QR code generation** for sharing links offline (e.g., in presentations or print materials).

**Why I Built This**:
Long URLs are cumbersome, especially in professional contexts (e.g., resumes, emails). This tool ensures clean, shareable links while maintaining functionality.

**Key Features**:
- Shorten URLs via TinyURL (default) or other services.
- Expand shortened links to their original form.
- Generate scannable QR codes for any link.
- User-friendly CLI interface with input validation.

---

## **File Descriptions**
### **1. `linkshorten.py` (Main Script)**
Contains 4 core functions:

#### **`link_shortener(link)`**
- **Purpose**: Shortens a URL using the `pyshorteners` library (default: TinyURL).
- **Key Logic**:
  - Uses `shortener.tinyurl.short()` for shortening.
  - Handles errors gracefully (e.g., invalid URLs).
- **Output**: Returns shortened link or error message.

####link_opener(link)`**
- **Purpose**: Expands a shortened URL to its original form.
- **Key Logic**:
  - Sends a GET request with custom headers (to mimic a browser).
  - Follows redirects to resolve the final URL.
- **Output**: Returns original link or HTTP error details.

#### **`optionalqrcode(link)`**
- **Purpose**: Generates a QR code for a link (shortened or original).
- **Key Logic**:
  - Uses `qrcode` library to create QR images.
  - Displays the QR code in a Tkinter window with adjustable settings (size, error correction).
- **User Interaction**: Prompts the user to confirm QR generation.

#### **`main()`**
- **Purpose**: Orchestrates the CLI workflow.
- **Features**:
  - Input validation (forces choices `1` or `2`).
  - Loop to reprompt on invalid inputs.

### **2. `requirements.txt`**
Lists dependencies:
```plaintext
pyshorteners
requests
qrcode
pillow
tkinter
```
Install via:
```bash
pip install -r requirements.txt
```

### **3. `test_linkshorten.py`**
*(Not shown in your code, but mentioned—describe its purpose if it exists.)*
- **Purpose**: Unit tests for `link_shortener()`, `link_opener()`, and edge cases.
- **Libraries Used**: `pytest`.

---

## **Design Choices & Debates**
### **1. Why `pyshorteners`?**
- **Pros**: Supports multiple services (TinyURL, Bit.ly) with minimal code.
- **Debated Alternative**: Building a custom shortener (e.g., with Flask + hash IDs).
- **Decision**: Chose `pyshorteners` for speed and reliability.

### **2. QR Code Implementation**
- **Library Choice**: `qrcode` + `Pillow` for simplicity and Tkinter compatibility.
- **User Experience**: Added a pop-up window (`Tkinter`) instead of saving files for immediate feedback.

### **3. Error Handling**
- **Approach**: Used `try-except` blocks to catch:
  - Invalid URLs in `link_shortener()`.
  - HTTP errors in `link_opener()`.
- **Trade-off**: Simplified error messages for users (no stack traces).

### **4. CLI vs. GUI**
- **Choice**: CLI for lightweight usage (easy to script).
- **Future Work**: Could add a GUI (Tkinter/PyQt) or web interface.

---

## **Usage Instructions**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python linkshorten.py
   ```
3. Follow prompts:
   - Enter `1` to shorten a URL or `2` to expand it.
   - Paste your link.
   - Choose to generate a QR code (`Y/N`).

**Example Workflow**:
```python
# Shorten a URL:
Shortened Link: https://tinyurl.com/abc123

# Expand a URL:
Real Link: https://original-site.com/long-path

# QR Code:
[Opens a Tkinter window with scannable QR]
```

---

## **Future Improvements**
1. **Multiple Shortening Services**: Let users choose between TinyURL, Bit.ly, etc.
2. **Bulk Processing**: Shorten/expand multiple URLs from a file.
3. **API Integration**: Deploy as a web service (e.g., Flask/Django).

---

## **Conclusion**
This tool simplifies URL management for both technical and non-technical users. By combining shortening, expansion, and QR generation, it addresses real-world needs while maintaining a clean codebase.

**Feel free to contribute or report issues!**

