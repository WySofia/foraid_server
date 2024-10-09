-- Tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasenia_hash TEXT NOT NULL,
    cargo VARCHAR(50),
    rango VARCHAR(50)
);

-- Tabla TipoCaso
CREATE TABLE TipoCaso (
    id_tipo_caso SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla MetodoCreacion
CREATE TABLE MetodoCreacion (
    id_metodo_creacion SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla Casos
CREATE TABLE Casos (
    id_caso SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    fecha DATE NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT,
    id_tipo_caso INT NOT NULL,
    calle_principal VARCHAR(100),
    calle_secundaria VARCHAR(100),
    provincia VARCHAR(50),
    canton VARCHAR(50),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_tipo_caso) REFERENCES TipoCaso(id_tipo_caso)
);

-- Tabla Identikits
CREATE TABLE Identikits (
    id_identikit SERIAL PRIMARY KEY,
    id_caso INT NOT NULL,
    fecha_creacion DATE NOT NULL,
    id_metodo_creacion INT NOT NULL,
    imagen VARCHAR(255),
    FOREIGN KEY (id_caso) REFERENCES Casos(id_caso),
    FOREIGN KEY (id_metodo_creacion) REFERENCES MetodoCreacion(id_metodo_creacion)
);

-- Tabla Caracteristicas
CREATE TABLE Caracteristicas (
    id_caracteristica SERIAL PRIMARY KEY,
    id_identikit INT NOT NULL,
    nombre_caracteristica VARCHAR(50) NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (id_identikit) REFERENCES Identikits(id_identikit)
);
