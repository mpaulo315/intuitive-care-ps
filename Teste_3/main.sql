DROP DATABASE IF EXISTS TESTE_3;
CREATE DATABASE IF NOT EXISTS TESTE_3
    DEFAULT CHARACTER SET = 'utf8mb4';
USE TESTE_3;
CREATE TABLE IF NOT EXISTS OPERADORAS (
    REG_ANS INT NOT NULL PRIMARY KEY,
    CNPJ VARCHAR(15) NOT NULL,
    RAZAO_SOCIAL VARCHAR(255) NOT NULL,
    NOME_FANTASIA VARCHAR(255),
    MODALIDADE VARCHAR(100) NOT NULL,
    LOGRADOURO VARCHAR(255) NOT NULL,
    NUMERO VARCHAR(20) NOT NULL,
    COMPLEMENTO VARCHAR(255),
    BAIRRO VARCHAR(255) NOT NULL,
    CIDADE VARCHAR(255) NOT NULL,
    UF CHAR(3) NOT NULL,
    CEP VARCHAR(10) NOT NULL,
    DDD VARCHAR(3),
    TELEFONE VARCHAR(20),
    FAX VARCHAR(15),
    EMAIL VARCHAR(255),
    REPRESENTANTE VARCHAR(255) NOT NULL,
    CARGO_REPRESENTANTE VARCHAR(255) NOT NULL,
    REGIAO_COMERCIAL INT,
    DATA_REGISTRO_ANS DATE NOT NULL,

    CONSTRAINT UQ_OPERADORAS_RAZAO_SOCIAL_NOME_FANTASIA UNIQUE (RAZAO_SOCIAL, NOME_FANTASIA)
)

START TRANSACTION;
USE TESTE_3;
LOAD DATA INFILE "/var/lib/mysql-files/Relatorio_cadop.csv"
INTO TABLE OPERADORAS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@registro_ans, @cnpj, @razao_social, @nome_fantasia, @modalidade, @logradouro, @numero, @complemento, @bairro, @cidade, @uf, @cep, @ddd, @telefone, @fax, @email, @representante, @cargo_representante, @regiao_comercial, @data_registro_ans)
SET
    REG_ANS = @registro_ans,
    CNPJ = @cnpj,
    RAZAO_SOCIAL = @razao_social,
    NOME_FANTASIA = @nome_fantasia,
    MODALIDADE = @modalidade,
    LOGRADOURO = @logradouro,
    NUMERO = @numero,
    COMPLEMENTO = @complemento,
    BAIRRO = @bairro,
    CIDADE = @cidade,
    UF = @uf,
    CEP = @cep,
    DDD = @ddd,
    TELEFONE = @telefone,
    FAX = @fax,
    EMAIL = @email,
    REPRESENTANTE = @representante,
    CARGO_REPRESENTANTE = @cargo_representante,
    REGIAO_COMERCIAL = NULLIF(@regiao_comercial, ''),
    DATA_REGISTRO_ANS = @data_registro_ans;
COMMIT;

CREATE TABLE IF NOT EXISTS DEMONSTRATIVOS (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DATA_DEMONSTRATIVO DATE NOT NULL,
    REG_ANS INT,
    CD_CONTA_CONTABIL INT NOT NULL,
    DESCRICAO VARCHAR(255) NOT NULL,
    VL_SALDO_INICIAL DOUBLE(20, 2) NOT NULL,
    VL_SALDO_FINAL DOUBLE(20, 2) NOT NULL
)

START TRANSACTION;
USE TESTE_3;
-- Load 2023 data
LOAD DATA INFILE "/var/lib/mysql-files/2023/1T2023.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE);

LOAD DATA INFILE "/var/lib/mysql-files/2023/2t2023.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE)

LOAD DATA INFILE "/var/lib/mysql-files/2023/3T2023.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE)

LOAD DATA INFILE "/var/lib/mysql-files/2023/4T2023.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = DATE_FORMAT(STR_TO_DATE(@data_demonstrativo, '%d/%m/%Y'), '%Y-%m-%d'),
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE)

-- Load 2024 data
LOAD DATA INFILE "/var/lib/mysql-files/2024/1T2024.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE);

LOAD DATA INFILE "/var/lib/mysql-files/2024/2T2024.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE)

LOAD DATA INFILE "/var/lib/mysql-files/2024/3T2024.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE)

LOAD DATA INFILE "/var/lib/mysql-files/2024/4T2024.csv"
INTO TABLE DEMONSTRATIVOS
FIELDS TERMINATED BY ";"
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@data_demonstrativo, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA_DEMONSTRATIVO = @data_demonstrativo,
    REG_ANS = @reg_ans,
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = NULLIF(@descricao, ""),
    VL_SALDO_INICIAL = CAST(REPLACE(@vl_saldo_inicial, ",", ".") AS DOUBLE),
    VL_SALDO_FINAL = CAST(REPLACE(@vl_saldo_final, ",", ".") AS DOUBLE);
COMMIT;

