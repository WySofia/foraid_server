-- Tabla de 'usuarios'
CREATE TABLE usuarios (
    usuario_id SERIAL PRIMARY KEY,
    cargo VARCHAR(128),
    nivel VARCHAR(64),
    nombre VARCHAR(64),
    apellido VARCHAR(64),
    email VARCHAR(128) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de 'casos'
CREATE TABLE casos (
    caso_id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    provincia VARCHAR(64),
    ciudad VARCHAR(64),
    direccion VARCHAR(256),
    descripcion TEXT,
    usuario_id INT,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- Tabla de 'involucrados'
CREATE TABLE involucrados (
    involucrado_id SERIAL PRIMARY KEY,
    caso_id INT NOT NULL,
    nombre_alias VARCHAR(100),
    descripcion TEXT,
    FOREIGN KEY (caso_id) REFERENCES casos(caso_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Tabla de 'imagenes'
CREATE TABLE imagenes (
    imagen_id SERIAL PRIMARY KEY,
    caso_id INT NOT NULL,
    usuario_id INT,
    tipo_generacion VARCHAR(20) NOT NULL CHECK (tipo_generacion IN ('texto_a_imagen', 'imagen_a_imagen')),
    ruta VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (caso_id) REFERENCES casos(caso_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- Tabla de 'detalles_persona'
CREATE TABLE detalles_persona (
    detalle_id SERIAL PRIMARY KEY,
    imagen_id INT NOT NULL,
    edad INT,
    sexo VARCHAR(1) CHECK (sexo IN ('M', 'F')),
    etnia VARCHAR(64) CHECK (etnia IN ('afro', 'blanco', 'indigena', 'mestizo')),
    FOREIGN KEY (imagen_id) REFERENCES imagenes(imagen_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Tabla 'facciones'
CREATE TABLE facciones (
    faccion_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Insertar registros iniciales en 'facciones'
INSERT INTO facciones (nombre) VALUES ('Ojos'), ('Nariz'), ('Boca'), ('Orejas'), ('Cejas'), ('Cabello'), ('Barba'), ('Piel'), ('Frente'), ('Mentón'), ('Mejillas');

-- Tabla de 'metadatos_imagen'
CREATE TABLE metadatos_imagen (
    metadato_id SERIAL PRIMARY KEY,
    imagen_id INT NOT NULL,
    faccion_id INT NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (imagen_id) REFERENCES imagenes(imagen_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (faccion_id) REFERENCES facciones(faccion_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
