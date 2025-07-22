# 🚀 Ethereum Private Network (Clique PoA) com Geth

Este projeto cria uma rede Ethereum privada usando o Geth com consenso Proof of Authority (Clique).

---

## Requisitos

- Go Ethereum (geth) instalado — [https://geth.ethereum.org/docs/install-and-build/installing-geth](https://geth.ethereum.org/docs/install-and-build/installing-geth)
- Sistema com pelo menos 2GB de RAM (idealmente 3GB ou mais)
- Terminal com bash ou zsh
- Python 3 para gerar o arquivo genesis

---

## 🚀 Tecnologias Utilizadas

<p align="center">
  <img height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/go/go-original.svg" />
  <img height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
  <img height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" />
  <img height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/json/json-original.svg" />
  <img height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg" />
</p>

---

## Passos para rodar

### 1. Sugestão de estrutura de pastas (opcional)

```
/ethereum-poa
├── data/                  # Diretório dos dados da blockchain
├── genesis.json           # Arquivo de configuração da rede
├── senha.txt              # Senha da conta a ser desbloqueada
├── gera_genesis.py        # Scripts úteis, como o de geração do genesis
└── README.md
```

---

### 2. Criar o arquivo `genesis.json`

Você pode gerar o arquivo `genesis.json` automaticamente com o script Python abaixo.

```
python3 gera_genesis.py
```

> **Atenção:** Substitua `"ENDEREÇO_DA_SUA_WALLET"` pelo endereço real da sua conta (sem `0x`).

```python
import json

signer = "ENDEREÇO_DA_SUA_WALLET"

extraData = "0x" + "00" * 32 + signer + "00" * 65

genesis = {
    "config": {
        "chainId": 1337,
        "homesteadBlock": 0,
        "eip150Block": 0,
        "eip155Block": 0,
        "eip158Block": 0,
        "byzantiumBlock": 0,
        "constantinopleBlock": 0,
        "petersburgBlock": 0,
        "istanbulBlock": 0,
        "berlinBlock": 0,
        "londonBlock": 0,
        "terminalTotalDifficulty": 1152921504606846976,
        "clique": {
            "period": 5,
            "epoch": 30000
        }
    },
    "nonce": "0x0",
    "timestamp": "0x0",
    "extraData": extraData,
    "gasLimit": "0x1C9C380",
    "difficulty": "0x1",
    "mixHash": "0x" + "00" * 32,
    "coinbase": "0x0000000000000000000000000000000000000000",
    "alloc": {
        "0x" + signer: {
            "balance": "0x56bc75e2d63100000"
        }
    },
    "number": "0x0",
    "gasUsed": "0x0",
    "parentHash": "0x" + "00" * 32
}

with open("genesis.json", "w") as f:
    json.dump(genesis, f, indent=2)

print("Arquivo genesis.json criado com sucesso.")
```

---

### 3. Inicializar a rede com o genesis

```
geth --datadir ./data init genesis.json
```

---

### 4. Rodar o nó

```
geth --datadir ./data --networkid 1337 --http --http.addr 0.0.0.0 --http.port 8545 \
--http.api eth,net,web3,miner,admin --unlock 0xENDEREÇO_DA_SUA_WALLET --password senha.txt --mine --allow-insecure-unlock
```

---

### 5. Conectar ao console em outro terminal

```
geth attach ipc:./data/geth.ipc

ou

geth attach http://localhost:8545
```

---

### 6. Verificar o saldo da sua WALLET

```
eth.getBalance("0xENDEREÇO_DA_SUA_WALLET")
```

---

### 7. Enviar transferência entre contas

```
eth.sendTransaction({
  from: "0xENDEREÇO_DA_SUA_WALLET",
  to: "0xENDEREÇO_DA_WALLET_DESTINO",
  value: web3.toWei(1, "ether")
})
```

---

### 🛠️ Comandos Úteis no Console

```
// Listar contas disponíveis
eth.accounts
// Ver saldo
eth.getBalance("0xSEU_ENDERECO")
// Ver informações da rede
net.version
eth.blockNumber
// Ver transações de um bloco
eth.getBlock("latest", true)
```

---

### ✅ Dica: Múltiplas carteiras no alloc

```
"alloc": {
  "0xENDERECO1": { "balance": "0xDE0B6B3A7640000" },
  "0xENDERECO2": { "balance": "0xDE0B6B3A7640000" }
}
```

---

### 📘 Documentação Oficial

- Documentação Geth https://geth.ethereum.org/docs
- Clique PoA https://geth.ethereum.org/docs/interface/consensus/clique

### ✍️ Autor

Desenvolvido por **Leonardo Toledo**  
📧 leotoledo010@gmail.com  
🔗 [github.com/leonardotoledo0](https://github.com/LeonardoToledo0)

---

### 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.

Veja o arquivo [LICENSE](./LICENSE) para detalhes completos.

---
