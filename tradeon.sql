CREATE DATABASE IF NOT EXISTS tradeon;

USE tradeon;

-- Table categoria
CREATE TABLE categoria (
  id_categoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome_categoria VARCHAR(255) NOT NULL,
  desc_categoria VARCHAR(500) NOT NULL,
  active TINYINT(1) NULL DEFAULT NULL
);

-- Table pais
CREATE TABLE pais (
  pais_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome_pais VARCHAR(255) NOT NULL
);

-- Table estado
CREATE TABLE estado (
  estado_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome_estado VARCHAR(255) NOT NULL,
  sigla CHAR(2) NOT NULL,
  pais_id INT NULL DEFAULT NULL,
  CONSTRAINT fk_pais_estado FOREIGN KEY (pais_id) REFERENCES pais (pais_id)
);

-- Table cidade
CREATE TABLE cidade (
  cidade_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome_cidade VARCHAR(255) NOT NULL,
  estado_id INT NULL DEFAULT NULL,
  CONSTRAINT fk_estado_cidade FOREIGN KEY (estado_id) REFERENCES estado (estado_id)
);
    
-- Table endereco
CREATE TABLE endereco (
  id_endereco INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  rua VARCHAR(255) NULL DEFAULT NULL,
  numero INT NULL DEFAULT NULL,
  bairro VARCHAR(255) NULL DEFAULT NULL,
  cidade_id INT NULL DEFAULT NULL,
  estado_id INT NULL DEFAULT NULL,
  pais_id INT NULL DEFAULT NULL,
  active TINYINT(1) NULL DEFAULT NULL,
  CONSTRAINT fk_cidade_endereco FOREIGN KEY (cidade_id) REFERENCES cidade (cidade_id),
  CONSTRAINT fk_estado_endereco FOREIGN KEY (estado_id) REFERENCES estado (estado_id),
  CONSTRAINT fk_pais_endereco FOREIGN KEY (pais_id) REFERENCES pais (pais_id)
);

-- Table fornecedor
CREATE TABLE fornecedor (
  id_fornecedor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome_fornecedor VARCHAR(255) NOT NULL,
  cnpj_fornecedor VARCHAR(500) NOT NULL,
  email_fornecedor VARCHAR(100) NOT NULL,
  active TINYINT(1) NULL DEFAULT NULL,
  id_endereco INT NULL DEFAULT NULL,
  CONSTRAINT fk_endereco_fornecedor FOREIGN KEY (id_endereco) REFERENCES endereco (id_endereco)
);

-- Table telefone
CREATE TABLE telefone (
  id_telefone INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  telefone VARCHAR(20) NOT NULL,
  id_fornecedor INT NOT NULL,
  CONSTRAINT fk_fornecedor_telefone FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id_fornecedor)
);

-- Table produto
CREATE TABLE produto (
  id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome_produto VARCHAR(255) NOT NULL,
  desc_produto VARCHAR(500) NOT NULL,
  quant_min INT NOT NULL,
  peso_prod DOUBLE NULL DEFAULT NULL,
  perecivel TINYINT(1) NULL DEFAULT NULL,
  data_validade DATE NULL DEFAULT NULL,
  valor_unitario DOUBLE NOT NULL,
  valor_venda DOUBLE NOT NULL,
  id_categoria INT NULL DEFAULT NULL,
  quantidade INT NOT NULL,
  active TINYINT(1) NULL DEFAULT NULL,
  CONSTRAINT fk_categoria_produto FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
);

-- Table produto_fornecedor
CREATE TABLE produto_fornecedor (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_produto INT NULL DEFAULT NULL,
  id_fornecedor INT NULL DEFAULT NULL,
  CONSTRAINT fk_produto_fornecedor_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto),
  CONSTRAINT fk_produto_fornecedor_fornecedor FOREIGN KEY (id_fornecedor) REFERENCES fornecedor (id_fornecedor)
);

-- Table entrada_produto
CREATE TABLE entrada_produto (
  id_entrada INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_produto INT NOT NULL,
  data_entrada DATE NOT NULL,
  CONSTRAINT fk_entrada_produto_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

-- Table saida_produto
CREATE TABLE saida_produto (
  id_saida INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_produto INT NOT NULL,
  quantidade INT NOT NULL,
  data_saida DATE NOT NULL,
  CONSTRAINT fk_saida_produto_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);