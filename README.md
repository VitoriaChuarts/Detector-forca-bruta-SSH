# Detector e Bloqueador de Força Bruta SSH

Mini laboratório de cibersegurança com duas VMs (atacante e alvo), simulando um ataque de força bruta via SSH e implementando detecção e bloqueio automático em Python.

## Como funciona

1. Uma VM Kali Linux simula um ataque de força bruta contra o SSH de uma VM Ubuntu Server, usando a ferramenta Hydra.
2. Um script em Python (`detector.py`) se conecta via SSH na VM alvo, analisa o log de autenticação (`/var/log/auth.log`) e conta quantas tentativas de login falharam por IP.
3. Se um IP ultrapassa o limite definido (5 tentativas), o script:
   - Gera um alerta no terminal
   - Bloqueia automaticamente o IP malicioso usando `iptables`, via SSH

## Tecnologias usadas

- Python 3 (subprocess, re, regex)
- SSH (autenticação por chave pública)
- iptables
- Hydra (simulação de ataque)
- VirtualBox (ambiente com duas VMs: Kali Linux e Ubuntu Server)

## Como executar

1. Configure duas VMs em rede host-only no VirtualBox (uma Kali, uma Ubuntu Server)
2. Configure autenticação SSH por chave entre as VMs
3. Rode `python3 detector.py` na VM atacante

## Autora

Vitória Chuarts
