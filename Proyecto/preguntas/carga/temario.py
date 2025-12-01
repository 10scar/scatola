from preguntas.models import TipoExamen, Componente, Tema, Temario, Contenido

def poblar_datos():
    """
    Función principal que ejecuta la creación de todas
    las entidades del temario.
    """
    print("Iniciando población de la base de datos (V2)...")

    # --- 1. CREACIÓN DE TIPOEXAMEN ---
    icfes_exam, _ = TipoExamen.objects.get_or_create(nombre="ICFES Saber 11")
    unal_exam, _ = TipoExamen.objects.get_or_create(nombre="Admisión UNAL")
    print("Tipos de Examen creados.")

    # --- 2. CREACIÓN DE COMPONENTES ---
    print("Creando Componentes únicos por examen...")
    
    # Nota: El modelo Componente tiene un FK a TipoExamen.
    comp_math_icfes, _ = Componente.objects.get_or_create(
        nombre="Matemáticas - ICFES Saber 11", 
        tipo_examen=icfes_exam,
        defaults={'imagen': 'componentes_img/matematicas.png'}
    )
    comp_math_unal, _ = Componente.objects.get_or_create(
        nombre="Matemáticas - Admisión UNAL", 
        tipo_examen=unal_exam,
        defaults={'imagen': 'componentes_img/matematicas.png'}
    )
    comp_nat_icfes, _ = Componente.objects.get_or_create(
        nombre="Ciencias Naturales - ICFES Saber 11", 
        tipo_examen=icfes_exam,
        defaults={'imagen': 'componentes_img/ciencias.png'}
    )
    comp_nat_unal, _ = Componente.objects.get_or_create(
        nombre="Ciencias Naturales - Admisión UNAL", 
        tipo_examen=unal_exam,
        defaults={'imagen': 'componentes_img/ciencias.png'}
    )
    comp_lect_crit_icfes, _ = Componente.objects.get_or_create(
        nombre="Lectura Crítica - ICFES Saber 11", 
        tipo_examen=icfes_exam,
        defaults={'imagen': 'componentes_img/lectura.png'}
    )
    comp_an_text_unal, _ = Componente.objects.get_or_create(
        nombre="Análisis Textual - Admisión UNAL", 
        tipo_examen=unal_exam,
        defaults={'imagen': 'componentes_img/lectura.png'}
    )
    comp_soc_icfes, _ = Componente.objects.get_or_create(
        nombre="Sociales y Ciudadanas - ICFES Saber 11", 
        tipo_examen=icfes_exam,
        defaults={'imagen': 'componentes_img/sociales.png'}
    )
    comp_soc_unal, _ = Componente.objects.get_or_create(
        nombre="Ciencias Sociales - Admisión UNAL", 
        tipo_examen=unal_exam,
        defaults={'imagen': 'componentes_img/sociales.png'}
    )
    comp_ingles_icfes, _ = Componente.objects.get_or_create(
        nombre="Inglés - ICFES Saber 11", 
        tipo_examen=icfes_exam,
        defaults={'imagen': 'componentes_img/ingles.png'}
    )
    comp_an_img_unal, _ = Componente.objects.get_or_create(
        nombre="Análisis de Imagen - Admisión UNAL", 
        tipo_examen=unal_exam,
        defaults={'imagen': 'componentes_img/imagenes.png'}
    )
    print("Componentes creados.")

    # --- 3. CREACIÓN DE TEMAS, TEMARIOS Y CONTENIDOS ---

    # --- DOMINIO 1: MATEMÁTICAS (Compartido) ---
    print("\nPoblando Dominio: Matemáticas (Compartido)...")

    # Tema 1.1: Pensamiento Numérico y Aritmética
    tema_num, _ = Tema.objects.get_or_create(
        nombre="Pensamiento Numérico y Aritmética",
        defaults={
            'prioridad': 1,
            'descripcion': "Habilidad para comprender y manipular números, sus relaciones y sus operaciones en diferentes contextos."
        }
    )

    Temario.objects.get_or_create(tema=tema_num, componente=comp_math_icfes)
    Temario.objects.get_or_create(tema=tema_num, componente=comp_math_unal)

    Contenido.objects.get_or_create(
        tema=tema_num,
        titulo="Conjuntos Numéricos y Operaciones Fundamentales",
        defaults={'descripcion': "Dominio de los números racionales y sus representaciones (fracciones, razones, decimales, porcentajes). Incluye la comprensión y aplicación de las propiedades básicas de las operaciones aritméticas: suma, resta, multiplicación, división, potenciación y radicación en los números reales."}
    )
    Contenido.objects.get_or_create(
        tema=tema_num,
        titulo="Proporcionalidad y Porcentajes",
        defaults={'descripcion': "Aplicación de la proporcionalidad (directa e inversa) en la resolución de problemas. Esto abarca el manejo fluido de reglas de tres, el cálculo e interpretación de porcentajes, y la comprensión de razones de cambio, tales como tasas de interés, velocidades o tasas cambiarias."}
    )

    # Tema 1.2: Pensamiento Variacional (Álgebra y Funciones)
    tema_alg, _ = Tema.objects.get_or_create(
        nombre="Pensamiento Variacional (Álgebra y Funciones)",
        defaults={
            'prioridad': 2,
            'descripcion': "Reconocimiento de patrones, variables y la comprensión del concepto de función para modelar situaciones de cambio."
        }
    )
    Temario.objects.get_or_create(tema=tema_alg, componente=comp_math_icfes)
    Temario.objects.get_or_create(tema=tema_alg, componente=comp_math_unal)

    Contenido.objects.get_or_create(
        tema=tema_alg,
        titulo="Expresiones Algebraicas y Factorización",
        defaults={'descripcion': "Capacidad para operar con expresiones algebraicas (monomios, polinomios). En la UNAL, esto se profundiza para incluir un dominio de productos notables y los diferentes casos de factorización."}
    )
    Contenido.objects.get_or_create(
        tema=tema_alg,
        titulo="Ecuaciones y Sistemas de Ecuaciones",
        defaults={'descripcion': "Planteamiento y resolución de ecuaciones de primer y segundo grado (lineales y cuadráticas) e inecuaciones. Incluye la habilidad de resolver sistemas de ecuaciones lineales (ej. 2x2 o 3x3) como herramienta para solucionar problemas contextualizados."}
    )
    Contenido.objects.get_or_create(
        tema=tema_alg,
        titulo="Concepto y Gráfica de Funciones",
        defaults={'descripcion': "Interpretación de la noción de función, incluyendo su dominio, rango y representación gráfica en el plano cartesiano. Se enfoca en las funciones básicas: lineal, cuadrática y exponencial."}
    )
    Contenido.objects.get_or_create(
        tema=tema_alg,
        titulo="Funciones Trigonométricas y Logarítmicas",
        defaults={'descripcion': "Este contenido es 'No Genérico' en el ICFES pero es fundamental en la UNAL. Requiere la comprensión de las funciones trigonométricas (seno, coseno, tangente), sus propiedades, periodicidad y gráficas. Asimismo, incluye la función logarítmica, entendida como la inversa de la función exponencial, y sus propiedades."}
    )

    # Tema 1.3: Pensamiento Espacial y Métrico (Geometría)
    tema_geo, _ = Tema.objects.get_or_create(
        nombre="Pensamiento Espacial y Métrico (Geometría)",
        defaults={
            'prioridad': 3,
            'descripcion': "Comprensión de las propiedades de figuras bidimensionales y tridimensionales, y la habilidad de medir y realizar transformaciones en el espacio."
        }
    )
    Temario.objects.get_or_create(tema=tema_geo, componente=comp_math_icfes)
    Temario.objects.get_or_create(tema=tema_geo, componente=comp_math_unal)

    Contenido.objects.get_or_create(
        tema=tema_geo,
        titulo="Figuras Geométricas y Medición",
        defaults={'descripcion': "Dominio de las propiedades y mediciones de figuras planas (triángulos, círculos, paralelogramos) y sólidos (esferas, cilindros, paralelepipedos rectos). Incluye el cálculo de perímetros, áreas y volúmenes, así como la conversión de unidades."}
    )
    Contenido.objects.get_or_create(
        tema=tema_geo,
        titulo="Teoremas Clásicos (Pitágoras y Tales)",
        defaults={'descripcion': "Contenido 'No Genérico' del ICFES. Implica la aplicación del Teorema de Pitágoras $(a^2+b^2=c^2)$ para la resolución de problemas en triángulos rectángulos y el Teorema de Tales para determinar la proporcionalidad de segmentos creados por rectas paralelas."}
    )
    Contenido.objects.get_or_create(
        tema=tema_geo,
        titulo="Sistemas de Coordenadas y Transformaciones",
        defaults={'descripcion': "Uso de sistemas de coordenadas cartesianas para ubicar y describir figuras. Incluye la comprensión de transformaciones en el plano (translaciones, rotaciones, reflexiones o simetrías, y homotecias)."}
    )

    # Tema 1.4: Pensamiento Aleatorio (Estadística y Probabilidad)
    tema_est, _ = Tema.objects.get_or_create(
        nombre="Pensamiento Aleatorio (Estadística y Probabilidad)",
        defaults={
            'prioridad': 4,
            'descripcion': "Habilidad para interpretar, analizar, representar y hacer inferencias a partir de conjuntos de datos."
        }
    )
    Temario.objects.get_or_create(tema=tema_est, componente=comp_math_icfes)
    Temario.objects.get_or_create(tema=tema_est, componente=comp_math_unal)

    Contenido.objects.get_or_create(
        tema=tema_est,
        titulo="Análisis de Datos (Gráficos y Tablas)",
        defaults={'descripcion': "Competencia fundamental para interpretar información presentada en diversos formatos, incluyendo tablas de frecuencia y gráficos (barras, circulares, pictogramas, histogramas)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_est,
        titulo="Medidas de Tendencia Central y Dispersión",
        defaults={'descripcion': "Cálculo e interpretación de las medidas de tendencia central (promedio, mediana, moda) y conceptos básicos de dispersión como el rango."}
    )
    Contenido.objects.get_or_create(
        tema=tema_est,
        titulo="Probabilidad Simple y Técnicas de Conteo",
        defaults={'descripcion': "Cálculo de la probabilidad de eventos simples. Incluye el uso de técnicas de conteo (combinaciones y permutaciones) para determinar el número de casos posibles y favorables en un experimento aleatorio."}
    )

    # --- DOMINIO 2: LECTURA, LENGUAJE Y FILOSOFÍA ---
    print("\nPoblando Dominio: Lectura y Lenguaje...")

    # Tema 2.1: Comprensión Literal (Compartido)
    tema_lect_lit, _ = Tema.objects.get_or_create(
        nombre="Comprensión Literal e Identificación de Información",
        defaults={
            'prioridad': 1,
            'descripcion': "Habilidad para identificar y comprender la información explícita y las partes que conforman un texto."
        }
    )
    Temario.objects.get_or_create(tema=tema_lect_lit, componente=comp_lect_crit_icfes)
    Temario.objects.get_or_create(tema=tema_lect_lit, componente=comp_an_text_unal)

    Contenido.objects.get_or_create(
        tema=tema_lect_lit,
        titulo="Identificación de Ideas Principales y Secundarias",
        defaults={'descripcion': "Capacidad de rastrear información explícita dentro del texto para identificar el tema central (idea principal) y las ideas que lo desarrollan, soportan o ejemplifican (ideas secundarias)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_lect_lit,
        titulo="Comprensión de Vocabulario en Contexto",
        defaults={'descripcion': "Habilidad para determinar el significado de palabras, frases y expresiones clave basándose en el contexto en el que son utilizadas, en lugar de su definición aislada."}
    )

    # Tema 2.2: Análisis Inferencial (Compartido)
    tema_lect_inf, _ = Tema.objects.get_or_create(
        nombre="Análisis Inferencial y Sentido Global",
        defaults={
            'prioridad': 2,
            'descripcion': "Habilidad para comprender cómo se enlazan las partes de un texto para darle un sentido global e inferir información no explícita."
        }
    )
    Temario.objects.get_or_create(tema=tema_lect_inf, componente=comp_lect_crit_icfes)
    Temario.objects.get_or_create(tema=tema_lect_inf, componente=comp_an_text_unal)

    Contenido.objects.get_or_create(
        tema=tema_lect_inf,
        titulo="Inferencia de Intención del Autor y Tono",
        defaults={'descripcion': "Capacidad de inferir el propósito comunicativo del autor (informar, persuadir, criticar, describir) e identificar el tono del texto (ej. crítico, descriptivo, argumentativo, irónico, analítico)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_lect_inf,
        titulo="Diferenciación entre Hechos (Datos) y Opiniones",
        defaults={'descripcion': "Habilidad clave, especialmente evaluada en la prueba UNAL. Requiere que el lector distinga entre afirmaciones objetivas y verificables (datos o hechos) y juicios de valor subjetivos (opiniones)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_lect_inf,
        titulo="Análisis de Tipos de Texto (Continuos y Discontinuos)",
        defaults={'descripcion': "Capacidad para interpretar textos continuos (organizados en párrafos, como ensayos, novelas, crónicas) y textos discontinuos (que requieren una lectura no secuencial, como infografías, cómics, caricaturas y tablas)."}
    )

    # Tema 2.3: Reflexión Crítica (Compartido)
    tema_lect_crit, _ = Tema.objects.get_or_create(
        nombre="Reflexión Crítica e Intertextualidad",
        defaults={
            'prioridad': 3,
            'descripcion': "Capacidad de evaluar la validez de los argumentos, la estructura del texto y la postura del autor frente al contenido."
        }
    )
    Temario.objects.get_or_create(tema=tema_lect_crit, componente=comp_lect_crit_icfes)
    Temario.objects.get_or_create(tema=tema_lect_crit, componente=comp_an_text_unal)

    Contenido.objects.get_or_create(
        tema=tema_lect_crit,
        titulo="Evaluación de Argumentos y Posturas",
        defaults={'descripcion': "Habilidad para identificar la tesis de un texto argumentativo y valorar la solidez, validez y coherencia de los argumentos (razones, premisas) que la sustentan."}
    )
    Contenido.objects.get_or_create(
        tema=tema_lect_crit,
        titulo="Identificación de Tipos de Narrador",
        defaults={'descripcion': "Habilidad clave en el Análisis Textual de la UNAL. Requiere diferenciar entre un narrador en primera persona (personaje que cuenta su historia), un narrador observador (externo, que solo cuenta lo que ve) y un narrador omnisciente (que conoce los pensamientos y sentimientos de los personajes)."}
    )

    # Tema 2.4: Fundamentos Filosóficos (Específico ICFES)
    tema_filo_icfes, _ = Tema.objects.get_or_create(
        nombre="Fundamentos Filosóficos",
        defaults={
            'prioridad': 4,
            'descripcion': "Comprensión de conceptos y textos provenientes de la tradición filosófica."
        }
    )
    Temario.objects.get_or_create(tema=tema_filo_icfes, componente=comp_lect_crit_icfes)

    Contenido.objects.get_or_create(
        tema=tema_filo_icfes,
        titulo="Comprensión de Textos Filosóficos",
        defaults={'descripcion': "Este es un diferenciador clave del ICFES. La prueba dedica un 30% de sus textos continuos a fragmentos 'informativo-filosóficos'. Esto exige al estudiante la habilidad de comprender extractos de autores clásicos o contemporáneos sobre temas como epistemología (el conocimiento), metafísica (el ser), ética (el bien y el mal) y filosofía política."}
    )

    # --- DOMINIO 3: CIENCIAS NATURALES ---
    print("\nPoblando Dominio: Ciencias Naturales (Compartido)...")

    # Tema 3.1: Biología
    tema_bio, _ = Tema.objects.get_or_create(
        nombre="Biología",
        defaults={
            'prioridad': 1,
            'descripcion': "Estudio de los seres vivos, su origen, evolución, funciones vitales y su interacción con el entorno."
        }
    )
    Temario.objects.get_or_create(tema=tema_bio, componente=comp_nat_icfes)
    Temario.objects.get_or_create(tema=tema_bio, componente=comp_nat_unal)

    Contenido.objects.get_or_create(
        tema=tema_bio,
        titulo="Biología Celular (La Célula, Mitosis y Meiosis)",
        defaults={'descripcion': "Comprensión fundamental de la célula como unidad de la vida, identificando sus partes y funciones. Incluye la diferenciación de los procesos de división celular: Mitosis (replicación de células somáticas para crecimiento y reparación) y Meiosis (formación de gametos o células sexuales con variabilidad genética)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_bio,
        titulo="Genética y Herencia (Leyes de Mendel)",
        defaults={'descripcion': "Comprensión de los principios de la herencia genética, un tema clave en la UNAL. Esto incluye las tres Leyes de Mendel, y la aplicación de conceptos como alelos dominantes y recesivos, genotipo (la constitución genética) y fenotipo (la expresión física) en cuadros de Punnett."}
    )
    Contenido.objects.get_or_create(
        tema=tema_bio,
        titulo="Ecología y Ecosistemas (Cadenas Tróficas)",
        defaults={'descripcion': "Análisis del flujo de energía dentro de un ecosistema. Requiere la comprensión de las cadenas tróficas (o alimentarias), identificando el rol de cada eslabón: productores (autótrofos, ej. plantas), consumidores (primarios, secundarios, terciarios) y descomponedores."}
    )
    Contenido.objects.get_or_create(
        tema=tema_bio,
        titulo="Reinos de la Naturaleza y Homeostasis",
        defaults={'descripcion': "Conocimiento de la clasificación de los seres vivos en los principales reinos y los mecanismos biológicos de autorregulación (homeostasis) que permiten a los organismos mantener condiciones internas estables (ej. regulación de temperatura o glucosa)."}
    )

    # Tema 3.2: Química
    tema_qui, _ = Tema.objects.get_or_create(
        nombre="Química",
        defaults={
            'prioridad': 2,
            'descripcion': "Estudio de la composición, estructura, propiedades y transformaciones de la materia."
        }
    )
    Temario.objects.get_or_create(tema=tema_qui, componente=comp_nat_icfes)
    Temario.objects.get_or_create(tema=tema_qui, componente=comp_nat_unal)

    Contenido.objects.get_or_create(
        tema=tema_qui,
        titulo="Estructura Atómica (Tabla Periódica y Configuración)",
        defaults={'descripcion': "Comprensión de la organización de la tabla periódica (grupos, periodos) y la información que provee (número atómico, peso molecular). Incluye la habilidad de determinar la configuración electrónica de los elementos."}
    )
    Contenido.objects.get_or_create(
        tema=tema_qui,
        titulo="Reacciones y Estequiometría (Balanceo de Ecuaciones)",
        defaults={'descripcion': "Tema fundamental en la UNAL. Implica la aplicación de la Ley de Conservación de la Materia, que requiere que el número de átomos de cada elemento sea igual en reactivos y productos. Esto se logra ajustando los coeficientes estequiométricos (balanceo por tanteo o redox). Requiere habilidades matemáticas para cálculos (ej. regla de tres)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_qui,
        titulo="Enlace Químico (Estructuras de Lewis)",
        defaults={'descripcion': "Tema clave en la UNAL. Las estructuras de Lewis son representaciones bidimensionales que muestran los electrones de valencia y cómo forman enlaces (iónicos o covalentes) para cumplir la regla del octeto."}
    )
    Contenido.objects.get_or_create(
        tema=tema_qui,
        titulo="Química Orgánica (Hidrocarburos y Grupos Funcionales)",
        defaults={'descripcion': "Fundamentos de la química del carbono. Se enfoca en la identificación de hidrocarburos (alcanos, alquenos, alquinos) y los principales grupos funcionales (ej. alcoholes, cetonas, ácidos carboxílicos). Aunque la frecuencia de estas preguntas en la UNAL es baja, son decisivas cuando aparecen."}
    )

    # Tema 3.3: Física
    tema_fis, _ = Tema.objects.get_or_create(
        nombre="Física",
        defaults={
            'prioridad': 3,
            'descripcion': "Estudio de la energía, la materia, el movimiento y las fuerzas fundamentales que gobiernan el universo."
        }
    )
    Temario.objects.get_or_create(tema=tema_fis, componente=comp_nat_icfes)
    Temario.objects.get_or_create(tema=tema_fis, componente=comp_nat_unal)

    Contenido.objects.get_or_create(
        tema=tema_fis,
        titulo="Mecánica Clásica (Cinemática y Dinámica)",
        defaults={'descripcion': "Es el área más preguntada de la física en ambas pruebas. Incluye Cinemática: análisis del movimiento (MRU, MUA, velocidad, aceleración), caída libre y movimiento parabólico. Y Dinámica: comprensión de las fuerzas (Leyes de Newton), diagramas de cuerpo libre, peso, fricción y energía (cinética y potencial)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_fis,
        titulo="Electricidad y Magnetismo",
        defaults={'descripcion': "Evaluado principalmente en el ICFES. Requiere el reconocimiento de circuitos eléctricos (componentes en serie y paralelo) y la comprensión de conceptos fundamentales como corriente, voltaje y resistencia (Ley de Ohm)."}
    )
    Contenido.objects.get_or_create(
        tema=tema_fis,
        titulo="Ondas y Óptica",
        defaults={'descripcion': "Evaluado principalmente en el ICFES. Incluye los conceptos básicos de las ondas (frecuencia, amplitud, longitud de onda) y los fenómenos ópticos como la reflexión (espejos), refracción (lentes) y difracción."}
    )

    # Tema 3.4: Ciencia, Tecnología y Sociedad (CTS) (Específico ICFES)
    tema_cts, _ = Tema.objects.get_or_create(
        nombre="Ciencia, Tecnología y Sociedad (CTS)",
        defaults={
            'prioridad': 4,
            'descripcion': "Análisis del impacto de la ciencia y la tecnología en la sociedad, el medio ambiente y la ética."
        }
    )
    Temario.objects.get_or_create(tema=tema_cts, componente=comp_nat_icfes) # Solo ICFES

    Contenido.objects.get_or_create(
        tema=tema_cts,
        titulo="Análisis de Impacto Tecnológico y Ambiental",
        defaults={'descripcion': "Este componente es exclusivo del ICFES. Evalúa la capacidad del estudiante para usar su conocimiento científico (biológico, químico o físico) para analizar situaciones, tomar posturas críticas y evaluar las implicaciones éticas o ambientales del uso de tecnologías (ej. transgénicos, fuentes de energía, deforestación)."}
    )

    # --- DOMINIO 4: CIENCIAS SOCIALES Y CIUDADANAS ---
    print("\nPoblando Dominio: Ciencias Sociales...")

    # Tema 4.1: Historia y Geografía (Compartido)
    tema_hist_geo, _ = Tema.objects.get_or_create(
        nombre="Historia y Geografía",
        defaults={
            'prioridad': 1,
            'descripcion': "Comprensión de eventos históricos clave y la relación del ser humano con el espacio geográfico."
        }
    )
    Temario.objects.get_or_create(tema=tema_hist_geo, componente=comp_soc_icfes)
    Temario.objects.get_or_create(tema=tema_hist_geo, componente=comp_soc_unal)

    Contenido.objects.get_or_create(
        tema=tema_hist_geo,
        titulo="Geografía Global y de Colombia",
        defaults={'descripcion': "Un tema clave en la UNAL. Requiere la ubicación espacial de continentes, países y océanos. Comprensión de coordenadas geográficas (latitud, longitud). A nivel de Colombia, se enfoca en la identificación de relieves (cordilleras), ríos principales y límites departamentales."}
    )
    Contenido.objects.get_or_create(
        tema=tema_hist_geo,
        titulo="Historia Universal (Sistemas Económicos y Revoluciones)",
        defaults={'descripcion': "Fundamental en la UNAL. Exige la comprensión de grandes procesos y conceptos históricos, como la Edad Media, y los sistemas económicos como el Feudalismo y el Capitalismo. Incluye eventos transformadores como la Revolución Industrial y la Revolución Francesa."}
    )
    Contenido.objects.get_or_create(
        tema=tema_hist_geo,
        titulo="Historia de Colombia (Siglo XX)",
        defaults={'descripcion': "Fundamental en la UNAL. Se centra en sucesos clave de la historia moderna colombiana, como el proceso de Independencia, y eventos del siglo XX que definieron al país, como el Bogotazo y la Masacre de las Bananeras."}
    )

    # Tema 4.2: Competencias Ciudadanas y Constitución (Específico ICFES)
    tema_ciu, _ = Tema.objects.get_or_create(
        nombre="Competencias Ciudadanas y Constitución",
        defaults={
            'prioridad': 2,
            'descripcion': "Conocimiento de la estructura del Estado colombiano y los derechos y deberes ciudadanos."
        }
    )
    Temario.objects.get_or_create(tema=tema_ciu, componente=comp_soc_icfes)

    Contenido.objects.get_or_create(
        tema=tema_ciu,
        titulo="Fundamentos de la Constitución de 1991",
        defaults={'descripcion': "Este contenido es el núcleo del componente ciudadano del ICFES. Evalúa el conocimiento de la estructura del Estado (las tres ramas del poder público: Ejecutiva, Legislativa, Judicial) y los organismos de control. Se enfoca en la comprensión de los derechos fundamentales."}
    )
    Contenido.objects.get_or_create(
        tema=tema_ciu,
        titulo="Mecanismos de Participación Ciudadana",
        defaults={'descripcion': "Específico del ICFES. Evalúa el conocimiento de las herramientas democráticas que tienen los ciudadanos para defender sus derechos e intervenir en decisiones públicas, tales como la Acción de Tutela, el referendo, la consulta popular y el voto."}
    )

    # Tema 4.3: Filosofía y Lógica (Específico UNAL)
    tema_filo_logica_unal, _ = Tema.objects.get_or_create(
        nombre="Filosofía y Lógica",
        defaults={
            'prioridad': 3,
            'descripcion': "Aplicación de la lógica formal y el pensamiento filosófico para analizar problemas."
        }
    )
    Temario.objects.get_or_create(tema=tema_filo_logica_unal, componente=comp_soc_unal)

    Contenido.objects.get_or_create(
        tema=tema_filo_logica_unal,
        titulo="Fundamentos de Filosofía",
        defaults={'descripcion': "Específico de la prueba de Sociales de la UNAL. A diferencia del ICFES (que la usa en Lectura Crítica), la UNAL evalúa el conocimiento de conceptos filosóficos y escuelas de pensamiento directamente dentro del componente de Ciencias Sociales."}
    )
    Contenido.objects.get_or_create(
        tema=tema_filo_logica_unal,
        titulo="Lógica Proposicional",
        defaults={'descripcion': "Un diferenciador clave de la UNAL. Evalúa la capacidad de formalizar el lenguaje en argumentos lógicos. Requiere la comprensión de proposiciones simples y compuestas, y el uso de conectivas lógicas (negación 'no', conjunción 'y', disyunción 'o', condicional 'si... entonces', y bicondicional 'si y solo si') para determinar la validez de un argumento, a menudo mediante tablas de verdad."}
    )

    # --- DOMINIO 5: HABILIDADES ESPECÍFICAS ---
    print("\nPoblando Dominio: Habilidades Específicas...")

    # --- Componente: Inglés (Específico ICFES) ---
    # Los temas de inglés son únicos para este componente

    tema_ing_1, _ = Tema.objects.get_or_create(
        nombre="Comprensión de Avisos (Nivel A1 - Parte 1)",
        defaults={'prioridad': 1}
    )
    Temario.objects.get_or_create(tema=tema_ing_1, componente=comp_ingles_icfes)
    Contenido.objects.get_or_create(
        tema=tema_ing_1,
        titulo="Identificación de Avisos y Contexto",
        defaults={'descripcion': "Habilidad para comprender avisos y anuncios cortos del mundo real (ej. señales de tráfico, etiquetas, menús) e identificar el lugar donde se podrían encontrar."}
    )

    tema_ing_2, _ = Tema.objects.get_or_create(
        nombre="Relación de Léxico (Nivel A1 - Parte 2)",
        defaults={'prioridad': 2}
    )
    Temario.objects.get_or_create(tema=tema_ing_2, componente=comp_ingles_icfes)
    Contenido.objects.get_or_create(
        tema=tema_ing_2,
        titulo="Asociación de Vocabulario y Definiciones",
        defaults={'descripcion': "Habilidad para demostrar vocabulario básico. El estudiante debe relacionar un conjunto de descripciones cortas con una lista de palabras de una categoría específica (ej. animales, profesiones, lugares)."}
    )

    tema_ing_3, _ = Tema.objects.get_or_create(
        nombre="Conversaciones (Nivel A1 - Parte 3)",
        defaults={'prioridad': 3}
    )
    Temario.objects.get_or_create(tema=tema_ing_3, componente=comp_ingles_icfes)
    Contenido.objects.get_or_create(
        tema=tema_ing_3,
        titulo="Interacción Social Básica",
        defaults={'descripcion': "Comprensión pragmática básica. El estudiante debe leer un diálogo corto (una intervención) y seleccionar la respuesta o continuación más lógica y coherente."}
    )

    tema_ing_4, _ = Tema.objects.get_or_create(
        nombre="Textos con Espacios (Nivel A1-B1 - Partes 4 y 7)",
        defaults={'prioridad': 4}
    )
    Temario.objects.get_or_create(tema=tema_ing_4, componente=comp_ingles_icfes)
    Contenido.objects.get_or_create(
        tema=tema_ing_4,
        titulo="Uso del Lenguaje (Gramática y Léxico)",
        defaults={'descripcion': "Estas partes evalúan el uso del lenguaje. El estudiante debe leer un texto con espacios en blanco y seleccionar la palabra correcta (ej. preposición, verbo, conector) para completar la idea de manera gramatical y semánticamente correcta. La Parte 4 es de nivel A1 y la Parte 7 de nivel B1."}
    )

    tema_ing_5, _ = Tema.objects.get_or_create(
        nombre="Comprensión Lectora Literal (Nivel A2-B1 - Parte 5)",
        defaults={'prioridad': 5}
    )
    Temario.objects.get_or_create(tema=tema_ing_5, componente=comp_ingles_icfes)
    Contenido.objects.get_or_create(
        tema=tema_ing_5,
        titulo="Lectura Literal y Parafraseo",
        defaults={'descripcion': "Habilidad para leer un texto de longitud media y responder preguntas que indagan sobre información explícita, parafraseo y la idea principal del texto."}
    )

    tema_ing_6, _ = Tema.objects.get_or_create(
        nombre="Comprensión Lectora Inferencial (Nivel B1 - Parte 6)",
        defaults={'prioridad': 6}
    )
    Temario.objects.get_or_create(tema=tema_ing_6, componente=comp_ingles_icfes)
    Contenido.objects.get_or_create(
        tema=tema_ing_6,
        titulo="Lectura Inferencial y Propósito del Autor",
        defaults={'descripcion': "Habilidad de lectura de nivel intermedio (B1). El estudiante debe leer un texto más complejo y responder preguntas que requieren inferir información no explícita, como el propósito del autor, el tono o las conclusiones."}
    )

    # --- Componente: Análisis de Imagen (Específico UNAL) ---
    
    tema_img_esp, _ = Tema.objects.get_or_create(
        nombre="Razonamiento Espacial (Sólidos y Vistas)",
        defaults={
            'prioridad': 1,
            'descripcion': "Habilidad para interpretar, visualizar y manipular mentalmente objetos en tres dimensiones."
        }
    )
    Temario.objects.get_or_create(tema=tema_img_esp, componente=comp_an_img_unal)

    Contenido.objects.get_or_create(
        tema=tema_img_esp,
        titulo="Interpretación de Vistas de Sólidos (Proyección Isométrica)",
        defaults={'descripcion': "Es la habilidad de relacionar un sólido 3D con sus vistas 2D. Se presenta el sólido (en proyección isométrica) y el estudiante debe identificar la vista correcta (frontal/vertical, superior/horizontal o de perfil), o viceversa."}
    )
    Contenido.objects.get_or_create(
        tema=tema_img_esp,
        titulo="Conteo de Partes de Sólidos",
        defaults={'descripcion': "Habilidad para visualizar un sólido (a menudo compuesto por cubos) y contar el número de caras (visibles y ocultas), aristas o vértices que lo componen, o determinar cuántos cubos faltan para completar una estructura mayor."}
    )

    tema_img_abs, _ = Tema.objects.get_or_create(
        nombre="Razonamiento Abstracto (Patrones y Simetría)",
        defaults={
            'prioridad': 2,
            'descripcion': "Habilidad para identificar patrones, secuencias y transformaciones lógicas en figuras abstractas."
        }
    )
    Temario.objects.get_or_create(tema=tema_img_abs, componente=comp_an_img_unal)

    Contenido.objects.get_or_create(
        tema=tema_img_abs,
        titulo="Simetría y Efecto Espejo (Rotación Especular)",
        defaults={'descripcion': "Habilidad para diferenciar una rotación simple de una reflexión. El 'efecto espejo' o rotación especular requiere que el estudiante identifique la figura que es la imagen reflejada de un modelo, como si se viera en un espejo, y no una versión que simplemente ha sido girada en el plano."}
    )
    Contenido.objects.get_or_create(
        tema=tema_img_abs,
        titulo="Secuencias y Patrones Gráficos",
        defaults={'descripcion': "Similar a las pruebas de IQ. El estudiante debe analizar una serie de figuras que siguen una regla lógica (ej. rotación, adición/supresión de elementos, cambio de forma) e identificar la figura que completa correctamente la secuencia."}
    )
    Contenido.objects.get_or_create(
        tema=tema_img_abs,
        titulo="Pliegues, Cortes y Armado de Figuras",
        defaults={'descripcion': "Evalúa la capacidad de visualización espacial. El estudiante debe determinar la figura 2D resultante de desdoblar un papel que ha sido plegado y cortado en un patrón específico, o, inversamente, identificar el sólido 3D que se puede (o no se puede) armar a partir de un molde 2D."}
    )

    print("\n--- Población de la base de datos completada exitosamente (V2). ---")

 
