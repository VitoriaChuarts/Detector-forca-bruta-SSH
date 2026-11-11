import re
import subprocess

resultado_ssh = subprocess.run(
    ["ssh", "vitoria@192.168.56.101", "sudo cat /var/log/auth.log"],
    capture_output=True,
    text=True
)

linhas = resultado_ssh.stdout.split("\n")

contagem = {}

for linha in linhas:
    if "Failed password" in linha:
        resultado = re.search(r"from (\d+\.\d+\.\d+\.\d+)", linha)
        if resultado:
            ip = resultado.group(1) 
            if ip in contagem:  
                contagem[ip] = contagem[ip] + 1
            else: 
                 contagem[ip] = 1

LIMITE =  5

for ip, quantidade in contagem.items():
    if quantidade >= LIMITE:
        print(f"ALERTA :  IP {ip} fez {quantidade} tentativas de login falhas!")
        print(f"Bloqueando o IP {ip} ...")
        subprocess.run(
            ["ssh", "vitoria@192.168.56.101", f"sudo iptables -A INPUT -s {ip} -j DROP"] 
        )
        print(f"IP {ip} bloqueado com sucesso.")
    else: 
        print(f"IP {ip}: {quantidade} tentativa (s) - dentro do normal")
