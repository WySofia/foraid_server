-- Tabla de 'usuarios'
CREATE TABLE usuarios (
    usuario_id SERIAL PRIMARY KEY,
    cargo VARCHAR(100),
    nivel VARCHAR(50),
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de 'casos'
CREATE TABLE casos (
    caso_id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    direccion VARCHAR(200),
    descripcion TEXT,
    usuario_id INT NOT NULL,
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

-- Tabla de 'lugares'
CREATE TABLE lugares (
    lugar_id SERIAL PRIMARY KEY,
    provincia VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL
);

-- Tabla de 'imagenes'
CREATE TABLE imagenes (
    imagen_id SERIAL PRIMARY KEY,
    caso_id INT NOT NULL,
    usuario_id INT NOT NULL,
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
    lugar_nacimiento INT,
    FOREIGN KEY (imagen_id) REFERENCES imagenes(imagen_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (lugar_nacimiento) REFERENCES lugares(lugar_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

-- Tabla de 'tercios'
CREATE TABLE tercios (
    tercio_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Tabla 'facciones'
CREATE TABLE facciones (
    faccion_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Tabla de 'metadatos_imagen'
CREATE TABLE metadatos_imagen (
    metadato_id SERIAL PRIMARY KEY,
    imagen_id INT NOT NULL,
    tercio_id INT NOT NULL,
    faccion_id INT NOT NULL,
    descripcion TEXT,
    color VARCHAR(50),
    FOREIGN KEY (imagen_id) REFERENCES imagenes(imagen_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (tercio_id) REFERENCES tercios(tercio_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (faccion_id) REFERENCES facciones(faccion_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);