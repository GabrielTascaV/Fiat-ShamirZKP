# Fiat-ShamirZKP
Fiat-Shamit Zero Knowledge Proof Implementation on Python


## Local Setup (Without Docker)

### 🐧 Running with WSL (Windows Subsystem for Linux)

To run both APIs locally using WSL:

---

### ▶️ Start the APIs

#### **Server API**
```bash
uvicorn server_api:app --host 0.0.0.0 --port 8001
```

#### **User API**
```bash
uvicorn user_api:app --host 0.0.0.0 --port 8000
```

---

### 🪟 If you're running on **Windows**:

Find your WSL IP address by running:
```bash
ip addr | grep inet
```

Look for a line similar to:
```
inet 172.17.8.9/20 brd 172.17.15.255 scope global eth0
```
➡️ The WSL IP in this case is: **`172.17.8.9`**

---

### 🌐 Access the API Documentation

- **User API:** [http://172.17.8.9:8000/docs](http://172.17.8.9:8000/docs)  
- **Server API:** [http://172.17.8.9:8001/docs](http://172.17.8.9:8001/docs)
