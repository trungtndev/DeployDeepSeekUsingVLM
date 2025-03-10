import subprocess
import time

MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
PORT = "8000"  # Change if needed

def start_vllm():
    try:
        process = subprocess.Popen([
            "vllm",
            "serve",
            MODEL_NAME,
            "--trust-remote-code",
            "--dtype", "half",
            "--max-model-len", "16384",
            "--disable-chunked-prefill",  # Fix incorrect flag
            "--tensor-parallel-size", "1",
            "--port", PORT  # Explicitly set port
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)

        time.sleep(5)  # Give some time for the server to start
        
        # Check if the server is running
        if process.poll() is not None:
            stdout, stderr = process.communicate()
            print("Error starting VLLM server:\n", stderr)
            return False
        
        print(f"✅ VLLM server started on port {PORT}")
        return True

    except Exception as e:
        print(f"❌ Failed to start VLLM: {e}")
        return False

if __name__ == "__main__":
    start_vllm()
