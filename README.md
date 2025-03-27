# Sincronização de Tempo com Docker

## Configuração e Execução

### 1. Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/sincronizacao-tempo.git
cd sincronizacao-tempo
```

### 2. Construir e Executar os Contêineres
```sh
docker-compose up --build
```
Isso iniciará o servidor Flask e os clientes configurados no `docker-compose.yml`.

### 3. Verificar a Sincronização
Os logs do terminal mostrarão o processo de sincronização, incluindo:
- Tempo inicial de cada cliente
- Tempo recebido do servidor
- Ajuste progressivo até o alinhamento com o horário correto

## Configuração do `docker-compose.yml`
- O servidor é construído a partir do `Dockerfile.server` e expõe a porta 5000.
- Os clientes são construídos a partir do `Dockerfile.client` e iniciam com diferentes offsets:
  - `cliente1`: -5 segundos
  - `cliente2`: 0 segundos
  - `cliente3`: +10 segundos
  - `cliente4`: +15 segundos
- Todos os contêineres fazem parte da rede `sync-net`, garantindo comunicação isolada.

### Parar a Execução
Para interromper os contêineres, use:
```sh
docker-compose down
```

## Contribuição
Sinta-se à vontade para contribuir com melhorias!
- Abra uma issue para relatar problemas ou sugerir melhorias.
- Envie um pull request com suas modificações.

---


