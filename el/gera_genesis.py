import json

signer = "ENDEREÇO_DA_SUA_WALLET"

extraData = "0x" + "00"*32 + signer + "00"*65

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
    "mixHash": "0x" + "00"*32,
    "coinbase": "0x0000000000000000000000000000000000000000",
    "alloc": {
        "0x" + signer: {
            "balance": "0x56bc75e2d63100000"
        }
    },
    "number": "0x0",
    "gasUsed": "0x0",
    "parentHash": "0x" + "00"*32
}

with open("genesis.json", "w") as f:
    json.dump(genesis, f, indent=2)

print("Arquivo genesis.json criado com sucesso.")
