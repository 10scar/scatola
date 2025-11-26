GRUPOS_DATA = [
    {
        "codigo": "LECT_AGUA",
        "titulo": "Consumo de agua en la ciudad",
        "descripcion": (
            "En la ciudad de Aguas Claras, el consumo promedio de agua por persona ha "
            "aumentado en los últimos diez años. Las autoridades locales han implementado "
            "campañas educativas para promover el uso responsable del recurso e instalaron "
            "medidores inteligentes en los hogares. A pesar de estas medidas, algunos barrios "
            "siguen presentando niveles de consumo muy por encima del promedio."
        ),
    },
    {
        "codigo": "LECT_REDESSOC",
        "titulo": "Uso de redes sociales en jóvenes",
        "descripcion": (
            "Durante la última década, el tiempo que los jóvenes pasan en redes sociales ha "
            "crecido considerablemente. Aunque estas plataformas permiten mantener el contacto "
            "con amigos y acceder a información de forma rápida, también pueden generar "
            "ansiedad y distracciones constantes. Por ello, es importante establecer límites "
            "de uso y promover actividades fuera de las pantallas."
        ),
    },
    {
        "codigo": "EN_DIALOGO_CAFE",
        "titulo": "Diálogo en una cafetería",
        "descripcion": (
            "A: Excuse me, is this seat taken?\n"
            "B: No, go ahead. Are you waiting for someone?\n"
            "A: Yes, I'm meeting a friend, but she's a little late.\n"
            "B: I see. Do you come here often?\n"
            "A: Not really, but I love the coffee in this place."
        ),
    },
    {
        "codigo": "FILOS_PLATON",
        "titulo": "Fragmento filosófico",
        "descripcion": (
            "Para algunos filósofos, conocer la verdad implica cuestionar lo que vemos todos "
            "los días. Lo que aparece ante nuestros sentidos puede ser solo una sombra de una "
            "realidad más profunda y permanente. Por eso, el ejercicio filosófico exige dudar, "
            "preguntar y buscar razones más allá de las apariencias."
        ),
    },
]

PREGUNTAS_DATA = [
    {
        "contenido_titulo": "Conjuntos Numéricos y Operaciones Fundamentales",
        "grupo_codigo": None,
        "titulo": "Suma de fracciones en una receta",
        "descripcion": (
            "En una receta se usan 3/4 de taza de azúcar en la mañana y 2/3 de taza en la tarde. "
            "¿Cuánta azúcar se utiliza en total?"
        ),
        "opciones": [
            {"texto": "17/12 de taza", "puntaje": 1},
            {"texto": "5/7 de taza", "puntaje": 0},
            {"texto": "13/12 de taza", "puntaje": 0},
            {"texto": "1 taza exacta", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Conjuntos Numéricos y Operaciones Fundamentales",
        "grupo_codigo": None,
        "titulo": "Clasificación de números",
        "descripcion": "Todo número entero es también un número racional.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 2. Proporcionalidad y Porcentajes
    {
        "contenido_titulo": "Proporcionalidad y Porcentajes",
        "grupo_codigo": None,
        "titulo": "Receta proporcional",
        "descripcion": (
            "Una receta requiere 3 tazas de harina para servir a 4 personas. "
            "Si se quiere preparar la receta para 10 personas, ¿cuántas tazas de harina se necesitan "
            "manteniendo la misma proporción?"
        ),
        "opciones": [
            {"texto": "7,5 tazas", "puntaje": 1},
            {"texto": "6 tazas", "puntaje": 0},
            {"texto": "8 tazas", "puntaje": 0},
            {"texto": "10 tazas", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Proporcionalidad y Porcentajes",
        "grupo_codigo": None,
        "titulo": "Aumentar y disminuir un porcentaje",
        "descripcion": (
            "Si el precio de un producto aumenta un 20% y luego disminuye un 20%, "
            "el precio final queda exactamente igual al precio inicial."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 0},
            {"texto": "Falso", "puntaje": 1},
        ],
    },
    # 3. Expresiones Algebraicas y Factorización
    {
        "contenido_titulo": "Expresiones Algebraicas y Factorización",
        "grupo_codigo": None,
        "titulo": "Factorización de diferencia de cuadrados",
        "descripcion": "¿Cuál es la factorización correcta de la expresión x^2 - 9?",
        "opciones": [
            {"texto": "(x - 3)(x + 3)", "puntaje": 1},
            {"texto": "(x - 9)(x + 1)", "puntaje": 0},
            {"texto": "(x - 3)^2", "puntaje": 0},
            {"texto": "x(x - 9)", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Expresiones Algebraicas y Factorización",
        "grupo_codigo": None,
        "titulo": "Producto notable",
        "descripcion": "La expresión (x + 2)(x + 3) es equivalente a x^2 + 5x + 6.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 4. Ecuaciones y Sistemas de Ecuaciones
    {
        "contenido_titulo": "Ecuaciones y Sistemas de Ecuaciones",
        "grupo_codigo": None,
        "titulo": "Resolución de ecuación lineal",
        "descripcion": "Resuelva la ecuación 2x - 5 = 9.",
        "opciones": [
            {"texto": "x = 2", "puntaje": 0},
            {"texto": "x = 7", "puntaje": 1},
            {"texto": "x = -2", "puntaje": 0},
            {"texto": "x = 14", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Ecuaciones y Sistemas de Ecuaciones",
        "grupo_codigo": None,
        "titulo": "Número de soluciones de un sistema",
        "descripcion": (
            "El sistema de ecuaciones x + y = 10 y x - y = 4 tiene una única solución."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 5. Concepto y Gráfica de Funciones
    {
        "contenido_titulo": "Concepto y Gráfica de Funciones",
        "grupo_codigo": None,
        "titulo": "Definición de función",
        "descripcion": (
            "¿Cuál de las siguientes opciones describe mejor una función real de variable real?"
        ),
        "opciones": [
            {
                "texto": (
                    "Una relación que asigna a cada elemento del dominio exactamente "
                    "un elemento del codominio."
                ),
                "puntaje": 1,
            },
            {
                "texto": "Cualquier relación entre dos conjuntos de números reales.",
                "puntaje": 0,
            },
            {"texto": "Una operación que siempre suma dos números.", "puntaje": 0},
            {
                "texto": "Una tabla donde aparecen varios valores de x y un solo y.",
                "puntaje": 0,
            },
        ],
    },
    {
        "contenido_titulo": "Concepto y Gráfica de Funciones",
        "grupo_codigo": None,
        "titulo": "Prueba de la recta vertical",
        "descripcion": (
            "Si la gráfica de una relación en el plano corta a una misma recta vertical en "
            "más de un punto, entonces la relación representa una función."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 0},
            {"texto": "Falso", "puntaje": 1},
        ],
    },
    # 6. Funciones Trigonométricas y Logarítmicas
    {
        "contenido_titulo": "Funciones Trigonométricas y Logarítmicas",
        "grupo_codigo": None,
        "titulo": "Valor trigonométrico básico",
        "descripcion": "¿Cuál es el valor de sin(30°)?",
        "opciones": [
            {"texto": "1/2", "puntaje": 1},
            {"texto": "√3/2", "puntaje": 0},
            {"texto": "0", "puntaje": 0},
            {"texto": "1", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Funciones Trigonométricas y Logarítmicas",
        "grupo_codigo": None,
        "titulo": "Relación logaritmo-exponencial",
        "descripcion": (
            "La función logarítmica (en base positiva distinta de 1) es la función inversa "
            "de la correspondiente función exponencial."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 7. Figuras Geométricas y Medición
    {
        "contenido_titulo": "Figuras Geométricas y Medición",
        "grupo_codigo": None,
        "titulo": "Área de un rectángulo",
        "descripcion": "Un rectángulo tiene base de 5 cm y altura de 3 cm. ¿Cuál es su área?",
        "opciones": [
            {"texto": "8 cm²", "puntaje": 0},
            {"texto": "15 cm²", "puntaje": 1},
            {"texto": "10 cm²", "puntaje": 0},
            {"texto": "30 cm²", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Figuras Geométricas y Medición",
        "grupo_codigo": None,
        "titulo": "Suma de ángulos de un triángulo",
        "descripcion": "La suma de los ángulos internos de cualquier triángulo es 180°.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 8. Teoremas Clásicos (Pitágoras y Tales)
    {
        "contenido_titulo": "Teoremas Clásicos (Pitágoras y Tales)",
        "grupo_codigo": None,
        "titulo": "Aplicación del Teorema de Pitágoras",
        "descripcion": (
            "En un triángulo rectángulo, los catetos miden 6 cm y 8 cm. "
            "¿Cuál es la longitud de la hipotenusa?"
        ),
        "opciones": [
            {"texto": "10 cm", "puntaje": 1},
            {"texto": "12 cm", "puntaje": 0},
            {"texto": "7 cm", "puntaje": 0},
            {"texto": "14 cm", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Teoremas Clásicos (Pitágoras y Tales)",
        "grupo_codigo": None,
        "titulo": "Teorema de Tales y triángulos semejantes",
        "descripcion": "El Teorema de Tales se utiliza para establecer relaciones de semejanza entre triángulos.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 9. Sistemas de Coordenadas y Transformaciones
    {
        "contenido_titulo": "Sistemas de Coordenadas y Transformaciones",
        "grupo_codigo": None,
        "titulo": "Ubicación en el plano cartesiano",
        "descripcion": "El punto (-3, 4) se encuentra en cuál cuadrante del plano cartesiano?",
        "opciones": [
            {"texto": "Primer cuadrante", "puntaje": 0},
            {"texto": "Segundo cuadrante", "puntaje": 1},
            {"texto": "Tercer cuadrante", "puntaje": 0},
            {"texto": "Cuarto cuadrante", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Sistemas de Coordenadas y Transformaciones",
        "grupo_codigo": None,
        "titulo": "Efecto de una traslación",
        "descripcion": "Una traslación en el plano cambia la forma y el tamaño de una figura geométrica.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 0},
            {"texto": "Falso", "puntaje": 1},
        ],
    },
    # 10. Análisis de Datos (Gráficos y Tablas)
    {
        "contenido_titulo": "Análisis de Datos (Gráficos y Tablas)",
        "grupo_codigo": None,
        "titulo": "Lectura de frecuencias",
        "descripcion": (
            "En una encuesta sobre frutas favoritas, los resultados fueron: manzana 10 estudiantes, "
            "mango 15 estudiantes y uva 5 estudiantes. ¿Cuál fruta fue la más elegida?"
        ),
        "opciones": [
            {"texto": "Manzana", "puntaje": 0},
            {"texto": "Mango", "puntaje": 1},
            {"texto": "Uva", "puntaje": 0},
            {"texto": "Todas por igual", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Análisis de Datos (Gráficos y Tablas)",
        "grupo_codigo": None,
        "titulo": "Interpretación de histogramas",
        "descripcion": (
            "En un histograma, el área de cada barra está relacionada con la frecuencia de los datos "
            "en ese intervalo."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 11. Medidas de Tendencia Central y Dispersión
    {
        "contenido_titulo": "Medidas de Tendencia Central y Dispersión",
        "grupo_codigo": None,
        "titulo": "Cálculo de la media aritmética",
        "descripcion": "Halle la media de los datos: 2, 4, 4, 8.",
        "opciones": [
            {"texto": "4,5", "puntaje": 0},
            {"texto": "4", "puntaje": 1},
            {"texto": "5", "puntaje": 0},
            {"texto": "3,5", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Medidas de Tendencia Central y Dispersión",
        "grupo_codigo": None,
        "titulo": "Definición de mediana",
        "descripcion": (
            "La mediana es el valor que divide un conjunto de datos ordenados en dos partes con "
            "igual número de observaciones."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 12. Probabilidad Simple y Técnicas de Conteo
    {
        "contenido_titulo": "Probabilidad Simple y Técnicas de Conteo",
        "grupo_codigo": None,
        "titulo": "Probabilidad en un dado",
        "descripcion": "Al lanzar un dado justo, ¿cuál es la probabilidad de obtener un número par?",
        "opciones": [
            {"texto": "1/6", "puntaje": 0},
            {"texto": "1/2", "puntaje": 1},
            {"texto": "2/3", "puntaje": 0},
            {"texto": "3/4", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Probabilidad Simple y Técnicas de Conteo",
        "grupo_codigo": None,
        "titulo": "Conteo de combinaciones simples",
        "descripcion": (
            "Una tienda tiene camisetas en 3 colores (rojo, azul y negro) y 2 tallas (M y L). "
            "¿Cuántas combinaciones diferentes de color y talla se pueden formar?"
        ),
        "opciones": [
            {"texto": "3", "puntaje": 0},
            {"texto": "5", "puntaje": 0},
            {"texto": "6", "puntaje": 1},
            {"texto": "9", "puntaje": 0},
        ],
    },
    # 13. Identificación de Ideas Principales y Secundarias
    {
        "contenido_titulo": "Identificación de Ideas Principales y Secundarias",
        "grupo_codigo": "LECT_AGUA",
        "titulo": "Idea principal sobre el consumo de agua",
        "descripcion": "Según el texto sobre el consumo de agua en Aguas Claras, ¿cuál es la idea principal?",
        "opciones": [
            {
                "texto": (
                    "El consumo de agua ha aumentado y las autoridades implementan medidas "
                    "para promover un uso más responsable."
                ),
                "puntaje": 1,
            },
            {
                "texto": "Los medidores inteligentes son muy costosos de instalar.",
                "puntaje": 0,
            },
            {
                "texto": "En todos los barrios el consumo de agua es igual.",
                "puntaje": 0,
            },
            {
                "texto": "La ciudad de Aguas Claras es la más grande del país.",
                "puntaje": 0,
            },
        ],
    },
    {
        "contenido_titulo": "Identificación de Ideas Principales y Secundarias",
        "grupo_codigo": "LECT_AGUA",
        "titulo": "Idea secundaria del texto",
        "descripcion": (
            "En el texto, se menciona que algunos barrios presentan niveles de consumo "
            "muy por encima del promedio. Esta información es:"
        ),
        "opciones": [
            {"texto": "Una idea principal", "puntaje": 0},
            {"texto": "Una idea secundaria que amplía la idea principal", "puntaje": 1},
            {"texto": "Un dato irrelevante para el tema del texto", "puntaje": 0},
            {"texto": "Una conclusión final del texto", "puntaje": 0},
        ],
    },
    # 14. Comprensión de Vocabulario en Contexto
    {
        "contenido_titulo": "Comprensión de Vocabulario en Contexto",
        "grupo_codigo": "LECT_AGUA",
        "titulo": "Significado de 'promover'",
        "descripcion": (
            "En el texto se dice que las autoridades implementan campañas educativas para "
            "\"promover el uso responsable\" del agua. En ese contexto, 'promover' significa:"
        ),
        "opciones": [
            {"texto": "Obligar a las personas a usar menos agua.", "puntaje": 0},
            {"texto": "Vigilar constantemente a los ciudadanos.", "puntaje": 0},
            {"texto": "Fomentar y estimular un comportamiento deseado.", "puntaje": 1},
            {"texto": "Prohibir el uso de agua en ciertos barrios.", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Comprensión de Vocabulario en Contexto",
        "grupo_codigo": "LECT_AGUA",
        "titulo": "Significado de 'promedio'",
        "descripcion": (
            "Cuando el texto menciona que algunos barrios están por encima del 'promedio' de consumo, "
            "la palabra 'promedio' hace referencia a:"
        ),
        "opciones": [
            {"texto": "El valor más alto observado.", "puntaje": 0},
            {"texto": "La suma de los consumos sin dividir.", "puntaje": 0},
            {
                "texto": "Un valor representativo calculado a partir de varios datos.",
                "puntaje": 1,
            },
            {"texto": "El valor más bajo observado.", "puntaje": 0},
        ],
    },
    # 15. Inferencia de Intención del Autor y Tono
    {
        "contenido_titulo": "Inferencia de Intención del Autor y Tono",
        "grupo_codigo": "LECT_REDESSOC",
        "titulo": "Intención del autor sobre redes sociales",
        "descripcion": (
            "Según el texto sobre redes sociales, la intención principal del autor es:"
        ),
        "opciones": [
            {
                "texto": "Convencer de que las redes sociales deben prohibirse.",
                "puntaje": 0,
            },
            {
                "texto": "Informar de forma neutral sobre las redes sociales.",
                "puntaje": 0,
            },
            {
                "texto": (
                    "Advertir sobre los riesgos del uso excesivo de redes sociales "
                    "y recomendar establecer límites."
                ),
                "puntaje": 1,
            },
            {
                "texto": "Hacer un relato humorístico sobre la vida en internet.",
                "puntaje": 0,
            },
        ],
    },
    {
        "contenido_titulo": "Inferencia de Intención del Autor y Tono",
        "grupo_codigo": "LECT_REDESSOC",
        "titulo": "Tono del texto sobre redes sociales",
        "descripcion": "El tono del texto sobre redes sociales es principalmente humorístico.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 0},
            {"texto": "Falso", "puntaje": 1},
        ],
    },
    # 16. Diferenciación entre Hechos (Datos) y Opiniones
    {
        "contenido_titulo": "Diferenciación entre Hechos (Datos) y Opiniones",
        "grupo_codigo": "LECT_REDESSOC",
        "titulo": "Identificación de opinión",
        "descripcion": "¿Cuál de las siguientes afirmaciones del tema redes sociales es una opinión?",
        "opciones": [
            {
                "texto": "El tiempo de uso de redes sociales ha aumentado en la última década.",
                "puntaje": 0,
            },
            {
                "texto": "Algunas personas sienten ansiedad por el uso de redes sociales.",
                "puntaje": 0,
            },
            {
                "texto": "Las redes sociales son la peor creación tecnológica de la historia.",
                "puntaje": 1,
            },
            {
                "texto": "Existen plataformas que permiten comunicarse en tiempo real.",
                "puntaje": 0,
            },
        ],
    },
    {
        "contenido_titulo": "Diferenciación entre Hechos (Datos) y Opiniones",
        "grupo_codigo": "LECT_REDESSOC",
        "titulo": "Clasificación de enunciado",
        "descripcion": (
            'La frase "las redes sociales siempre son dañinas para los jóvenes" corresponde a:'
        ),
        "opciones": [
            {"texto": "Un hecho verificable.", "puntaje": 0},
            {"texto": "Una opinión o juicio de valor.", "puntaje": 1},
            {"texto": "Una definición científica.", "puntaje": 0},
            {"texto": "Una estadística oficial.", "puntaje": 0},
        ],
    },
    # 17. Análisis de Tipos de Texto (Continuos y Discontinuos)
    {
        "contenido_titulo": "Análisis de Tipos de Texto (Continuos y Discontinuos)",
        "grupo_codigo": None,
        "titulo": "Texto continuo vs discontinuo",
        "descripcion": "¿Cuál de los siguientes es un ejemplo de texto discontinuo?",
        "opciones": [
            {"texto": "Un cuento de varias páginas.", "puntaje": 0},
            {"texto": "Una carta personal.", "puntaje": 0},
            {"texto": "Un mapa conceptual con palabras clave y flechas.", "puntaje": 1},
            {"texto": "Un ensayo argumentativo.", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Análisis de Tipos de Texto (Continuos y Discontinuos)",
        "grupo_codigo": None,
        "titulo": "Clasificación de tablas",
        "descripcion": "Una tabla de frecuencias se considera un texto discontinuo.",
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 18. Evaluación de Argumentos y Posturas
    {
        "contenido_titulo": "Evaluación de Argumentos y Posturas",
        "grupo_codigo": "LECT_REDESSOC",
        "titulo": "Identificación de argumento",
        "descripcion": (
            "Si alguien afirma que se debe limitar el uso de redes sociales en adolescentes, "
            "¿cuál de las siguientes frases es un argumento que apoya esa postura?"
        ),
        "opciones": [
            {
                "texto": "Muchos adolescentes usan redes sociales todos los días.",
                "puntaje": 0,
            },
            {
                "texto": "Las redes sociales son muy conocidas en todo el mundo.",
                "puntaje": 0,
            },
            {
                "texto": (
                    "El uso excesivo de redes sociales se ha asociado con mayores niveles "
                    "de ansiedad y problemas de concentración."
                ),
                "puntaje": 1,
            },
            {"texto": "Algunos adultos también usan redes sociales.", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Evaluación de Argumentos y Posturas",
        "grupo_codigo": "LECT_REDESSOC",
        "titulo": "Fuerza de un argumento",
        "descripcion": (
            "Un buen argumento se caracteriza por estar apoyado en razones y evidencias "
            "relevantes para la postura que se defiende."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 19. Identificación de Tipos de Narrador
    {
        "contenido_titulo": "Identificación de Tipos de Narrador",
        "grupo_codigo": None,
        "titulo": "Narrador en primera persona",
        "descripcion": (
            'Lee el siguiente fragmento: "Yo caminaba por la calle cuando vi un perro que '
            'parecía seguirme". ¿Qué tipo de narrador se usa?'
        ),
        "opciones": [
            {"texto": "Narrador en primera persona", "puntaje": 1},
            {"texto": "Narrador en tercera persona omnisciente", "puntaje": 0},
            {"texto": "Narrador en segunda persona", "puntaje": 0},
            {"texto": "Narrador testigo en tercera persona", "puntaje": 0},
        ],
    },
    {
        "contenido_titulo": "Identificación de Tipos de Narrador",
        "grupo_codigo": None,
        "titulo": "Narrador omnisciente",
        "descripcion": (
            "Un narrador que conoce los pensamientos y sentimientos de todos los personajes "
            "se denomina narrador omnisciente."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    # 20. Comprensión de Textos Filosóficos
    {
        "contenido_titulo": "Comprensión de Textos Filosóficos",
        "grupo_codigo": "FILOS_PLATON",
        "titulo": "Tema central del texto filosófico",
        "descripcion": (
            "Según el fragmento filosófico, ¿qué se plantea sobre la realidad que percibimos "
            "con los sentidos?"
        ),
        "opciones": [
            {"texto": "Que siempre es totalmente confiable.", "puntaje": 0},
            {
                "texto": (
                    "Que puede ser solo una sombra de una realidad más profunda "
                    "y permanente."
                ),
                "puntaje": 1,
            },
            {
                "texto": "Que no existe ninguna realidad más allá de las apariencias.",
                "puntaje": 0,
            },
            {
                "texto": "Que la filosofía solo describe lo que vemos diariamente.",
                "puntaje": 0,
            },
        ],
    },
    {
        "contenido_titulo": "Comprensión de Textos Filosóficos",
        "grupo_codigo": "FILOS_PLATON",
        "titulo": "Actitud filosófica",
        "descripcion": (
            "El texto sugiere que el ejercicio filosófico exige dudar, preguntar y buscar "
            "razones más allá de las apariencias."
        ),
        "opciones": [
            {"texto": "Verdadero", "puntaje": 1},
            {"texto": "Falso", "puntaje": 0},
        ],
    },
    [
        # 21. Biología Celular (La Célula, Mitosis y Meiosis)
        {
            "contenido_titulo": "Biología Celular (La Célula, Mitosis y Meiosis)",
            "grupo_codigo": None,
            "titulo": "Función de las mitocondrias",
            "descripcion": (
                "En una célula eucariota, ¿cuál es la función principal de las mitocondrias?"
            ),
            "opciones": [
                {"texto": "Realizar la fotosíntesis.", "puntaje": 0},
                {"texto": "Almacenar la información genética.", "puntaje": 0},
                {
                    "texto": "Producir energía en forma de ATP mediante la respiración celular.",
                    "puntaje": 1,
                },
                {
                    "texto": "Controlar el paso de sustancias hacia el núcleo.",
                    "puntaje": 0,
                },
            ],
        },
        {
            "contenido_titulo": "Biología Celular (La Célula, Mitosis y Meiosis)",
            "grupo_codigo": None,
            "titulo": "Número de células hijas en la mitosis",
            "descripcion": (
                "En la mitosis, a partir de una célula madre se originan dos células hijas "
                "con la misma cantidad de cromosomas que la célula original."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 22. Genética y Herencia (Leyes de Mendel)
        {
            "contenido_titulo": "Genética y Herencia (Leyes de Mendel)",
            "grupo_codigo": None,
            "titulo": "Cruce de híbridos mendelianos",
            "descripcion": (
                "En plantas de arveja, el alelo para tallo alto (T) es dominante sobre el "
                "alelo para tallo bajo (t). Si se cruzan dos plantas Tt, ¿cuál es la "
                "probabilidad de obtener una planta de tallo bajo?"
            ),
            "opciones": [
                {"texto": "1/4", "puntaje": 1},
                {"texto": "1/2", "puntaje": 0},
                {"texto": "3/4", "puntaje": 0},
                {"texto": "0", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Genética y Herencia (Leyes de Mendel)",
            "grupo_codigo": None,
            "titulo": "Frecuencia de caracteres dominantes",
            "descripcion": (
                "La afirmación 'un carácter dominante siempre es más frecuente en la población "
                "que el carácter recesivo correspondiente' es correcta."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 0},
                {"texto": "Falso", "puntaje": 1},
            ],
        },
        # 23. Ecología y Ecosistemas (Cadenas Tróficas)
        {
            "contenido_titulo": "Ecología y Ecosistemas (Cadenas Tróficas)",
            "grupo_codigo": None,
            "titulo": "Base de la cadena trófica",
            "descripcion": (
                "En una cadena trófica típica de un ecosistema terrestre, ¿qué organismos se "
                "encuentran en la base de la cadena?"
            ),
            "opciones": [
                {"texto": "Plantas y algas que realizan fotosíntesis.", "puntaje": 1},
                {"texto": "Herbívoros.", "puntaje": 0},
                {"texto": "Carnívoros.", "puntaje": 0},
                {"texto": "Descomponedores.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Ecología y Ecosistemas (Cadenas Tróficas)",
            "grupo_codigo": None,
            "titulo": "Flujo de energía en la cadena trófica",
            "descripcion": (
                "La energía disponible disminuye a medida que se avanza hacia los niveles "
                "tróficos superiores de una cadena alimentaria."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 24. Reinos de la Naturaleza y Homeostasis
        {
            "contenido_titulo": "Reinos de la Naturaleza y Homeostasis",
            "grupo_codigo": None,
            "titulo": "Clasificación de los animales",
            "descripcion": (
                "¿A qué reino pertenecen los seres vivos multicelulares, heterótrofos y sin "
                "pared celular que generalmente tienen capacidad de movimiento?"
            ),
            "opciones": [
                {"texto": "Reino Plantae.", "puntaje": 0},
                {"texto": "Reino Fungi.", "puntaje": 0},
                {"texto": "Reino Animalia.", "puntaje": 1},
                {"texto": "Reino Protista.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Reinos de la Naturaleza y Homeostasis",
            "grupo_codigo": None,
            "titulo": "Definición de homeostasis",
            "descripcion": (
                "La homeostasis es la capacidad de un organismo para mantener relativamente "
                "constantes sus condiciones internas frente a cambios del ambiente."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 25. Estructura Atómica (Tabla Periódica y Configuración)
        {
            "contenido_titulo": "Estructura Atómica (Tabla Periódica y Configuración)",
            "grupo_codigo": None,
            "titulo": "Número atómico",
            "descripcion": "El número atómico de un elemento químico corresponde a:",
            "opciones": [
                {"texto": "La cantidad de protones en el núcleo.", "puntaje": 1},
                {"texto": "La cantidad de neutrones en el núcleo.", "puntaje": 0},
                {"texto": "La suma de protones y neutrones.", "puntaje": 0},
                {"texto": "La cantidad de electrones de valencia.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Estructura Atómica (Tabla Periódica y Configuración)",
            "grupo_codigo": None,
            "titulo": "Elementos de un mismo grupo",
            "descripcion": (
                "Los elementos que pertenecen al mismo grupo (columna) de la tabla periódica "
                "tienden a tener propiedades químicas similares porque comparten el mismo "
                "número de electrones de valencia."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 26. Reacciones y Estequiometría (Balanceo de Ecuaciones)
        {
            "contenido_titulo": "Reacciones y Estequiometría (Balanceo de Ecuaciones)",
            "grupo_codigo": None,
            "titulo": "Balanceo de agua",
            "descripcion": (
                "Considere la reacción de formación de agua: H2 + O2 → H2O. "
                "¿Cuál es el conjunto de coeficientes que la balancea correctamente?"
            ),
            "opciones": [
                {"texto": "1, 1, 1", "puntaje": 0},
                {"texto": "2, 1, 2", "puntaje": 1},
                {"texto": "1, 2, 1", "puntaje": 0},
                {"texto": "2, 2, 1", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Reacciones y Estequiometría (Balanceo de Ecuaciones)",
            "grupo_codigo": None,
            "titulo": "Conservación de la masa",
            "descripcion": (
                "En una reacción química correctamente balanceada, la masa total de los "
                "reactivos es igual a la masa total de los productos."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 27. Enlace Químico (Estructuras de Lewis)
        {
            "contenido_titulo": "Enlace Químico (Estructuras de Lewis)",
            "grupo_codigo": None,
            "titulo": "Enlace entre metal y no metal",
            "descripcion": (
                "¿Qué tipo de enlace se forma generalmente entre un metal y un no metal?"
            ),
            "opciones": [
                {"texto": "Enlace iónico.", "puntaje": 1},
                {"texto": "Enlace covalente no polar.", "puntaje": 0},
                {"texto": "Enlace metálico.", "puntaje": 0},
                {"texto": "Enlace de hidrógeno.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Enlace Químico (Estructuras de Lewis)",
            "grupo_codigo": None,
            "titulo": "Estructura de Lewis del agua",
            "descripcion": (
                "En la estructura de Lewis de la molécula de agua (H2O), el átomo de oxígeno "
                "se representa con dos pares de electrones no compartidos y dos enlaces "
                "sencillos con los átomos de hidrógeno."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 28. Química Orgánica (Hidrocarburos y Grupos Funcionales)
        {
            "contenido_titulo": "Química Orgánica (Hidrocarburos y Grupos Funcionales)",
            "grupo_codigo": None,
            "titulo": "Identificación de un grupo funcional",
            "descripcion": (
                "En la fórmula estructural de un compuesto orgánico aparece el grupo -OH "
                "unido a un carbono saturado. ¿Qué tipo de compuesto es?"
            ),
            "opciones": [
                {"texto": "Un alcohol.", "puntaje": 1},
                {"texto": "Un aldehído.", "puntaje": 0},
                {"texto": "Un ácido carboxílico.", "puntaje": 0},
                {"texto": "Un éster.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Química Orgánica (Hidrocarburos y Grupos Funcionales)",
            "grupo_codigo": None,
            "titulo": "Definición de alcano",
            "descripcion": (
                "Los alcanos son hidrocarburos que solo presentan enlaces covalentes "
                "sencillos entre sus átomos de carbono."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 29. Mecánica Clásica (Cinemática y Dinámica)
        {
            "contenido_titulo": "Mecánica Clásica (Cinemática y Dinámica)",
            "grupo_codigo": None,
            "titulo": "Cálculo de rapidez media",
            "descripcion": (
                "Un automóvil recorre 120 km en 2 horas a velocidad constante. "
                "¿Cuál es su rapidez media?"
            ),
            "opciones": [
                {"texto": "40 km/h", "puntaje": 0},
                {"texto": "60 km/h", "puntaje": 1},
                {"texto": "80 km/h", "puntaje": 0},
                {"texto": "120 km/h", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Mecánica Clásica (Cinemática y Dinámica)",
            "grupo_codigo": None,
            "titulo": "Primera ley de Newton",
            "descripcion": (
                "Según la primera ley de Newton, un cuerpo en reposo o en movimiento rectilíneo "
                "uniforme tiende a mantener su estado si no actúa una fuerza neta sobre él."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 30. Electricidad y Magnetismo
        {
            "contenido_titulo": "Electricidad y Magnetismo",
            "grupo_codigo": None,
            "titulo": "Ley de Ohm",
            "descripcion": "Según la ley de Ohm, la relación entre voltaje (V), corriente (I) y resistencia (R) es:",
            "opciones": [
                {"texto": "V = I / R", "puntaje": 0},
                {"texto": "V = I · R", "puntaje": 1},
                {"texto": "I = V · R", "puntaje": 0},
                {"texto": "R = V + I", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Electricidad y Magnetismo",
            "grupo_codigo": None,
            "titulo": "Interacción entre cargas",
            "descripcion": "Dos cargas eléctricas de igual signo se repelen entre sí.",
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 31. Ondas y Óptica
        {
            "contenido_titulo": "Ondas y Óptica",
            "grupo_codigo": None,
            "titulo": "Propiedades de una onda",
            "descripcion": (
                "¿Cuál de las siguientes magnitudes NO es una característica propia de una onda?"
            ),
            "opciones": [
                {"texto": "Amplitud.", "puntaje": 0},
                {"texto": "Frecuencia.", "puntaje": 0},
                {"texto": "Longitud de onda.", "puntaje": 0},
                {"texto": "Masa.", "puntaje": 1},
            ],
        },
        {
            "contenido_titulo": "Ondas y Óptica",
            "grupo_codigo": None,
            "titulo": "Definición de refracción",
            "descripcion": (
                "El cambio de dirección que experimenta un rayo de luz al pasar de un medio "
                "a otro con diferente índice de refracción se conoce como refracción."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 32. Análisis de Impacto Tecnológico y Ambiental
        {
            "contenido_titulo": "Análisis de Impacto Tecnológico y Ambiental",
            "grupo_codigo": None,
            "titulo": "Impacto ambiental negativo de la tecnología",
            "descripcion": (
                "¿Cuál de los siguientes ejemplos representa un impacto ambiental negativo "
                "asociado al uso de tecnología?"
            ),
            "opciones": [
                {
                    "texto": "Uso de paneles solares para producir energía.",
                    "puntaje": 0,
                },
                {
                    "texto": "Deforestación por expansión de la agricultura mecanizada.",
                    "puntaje": 1,
                },
                {"texto": "Reciclaje de residuos electrónicos.", "puntaje": 0},
                {"texto": "Uso de bicicletas compartidas en la ciudad.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Análisis de Impacto Tecnológico y Ambiental",
            "grupo_codigo": None,
            "titulo": "Efectos de la tecnología",
            "descripcion": (
                "Una misma tecnología puede tener efectos positivos y negativos al mismo "
                "tiempo, dependiendo del contexto en que se utilice."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 33. Geografía Global y de Colombia
        {
            "contenido_titulo": "Geografía Global y de Colombia",
            "grupo_codigo": None,
            "titulo": "Cordillera de los Andes en Colombia",
            "descripcion": (
                "¿Cuál sistema montañoso atraviesa el territorio colombiano de sur a norte y "
                "se divide en tres ramales principales?"
            ),
            "opciones": [
                {"texto": "La cordillera de los Andes.", "puntaje": 1},
                {"texto": "La sierra Madre.", "puntaje": 0},
                {"texto": "Los Alpes.", "puntaje": 0},
                {"texto": "El Himalaya.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Geografía Global y de Colombia",
            "grupo_codigo": None,
            "titulo": "Costas de Colombia",
            "descripcion": (
                "Colombia tiene costas tanto sobre el océano Pacífico como sobre el mar Caribe."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 34. Historia Universal (Sistemas Económicos y Revoluciones)
        {
            "contenido_titulo": "Historia Universal (Sistemas Económicos y Revoluciones)",
            "grupo_codigo": None,
            "titulo": "Característica de la Revolución Industrial",
            "descripcion": (
                "¿Cuál de las siguientes opciones describe mejor una característica de la "
                "Primera Revolución Industrial?"
            ),
            "opciones": [
                {
                    "texto": "Predominio del trabajo artesanal en pequeños talleres.",
                    "puntaje": 0,
                },
                {
                    "texto": "Uso generalizado de máquinas accionadas por energía de vapor.",
                    "puntaje": 1,
                },
                {"texto": "Desaparición total de la agricultura.", "puntaje": 0},
                {
                    "texto": "Sustitución del comercio internacional por mercados locales.",
                    "puntaje": 0,
                },
            ],
        },
        {
            "contenido_titulo": "Historia Universal (Sistemas Económicos y Revoluciones)",
            "grupo_codigo": None,
            "titulo": "Relación feudalismo-campesinado",
            "descripcion": (
                "En el sistema feudal, la mayoría de los campesinos estaba ligada a la tierra "
                "y debía prestar servicios al señor feudal."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 35. Historia de Colombia (Siglo XX)
        {
            "contenido_titulo": "Historia de Colombia (Siglo XX)",
            "grupo_codigo": None,
            "titulo": "La Violencia en Colombia",
            "descripcion": (
                "El periodo conocido como 'La Violencia' en Colombia se asocia principalmente con:"
            ),
            "opciones": [
                {
                    "texto": "Conflictos entre partidos Liberal y Conservador en el campo.",
                    "puntaje": 1,
                },
                {"texto": "La Guerra de los Mil Días.", "puntaje": 0},
                {"texto": "La independencia de España.", "puntaje": 0},
                {"texto": "La disolución de la Gran Colombia.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Historia de Colombia (Siglo XX)",
            "grupo_codigo": None,
            "titulo": "Frente Nacional",
            "descripcion": (
                "El Frente Nacional fue un acuerdo político entre los partidos Liberal y "
                "Conservador para alternar la presidencia de la República."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 36. Fundamentos de la Constitución de 1991
        {
            "contenido_titulo": "Fundamentos de la Constitución de 1991",
            "grupo_codigo": None,
            "titulo": "Colombia como Estado social de derecho",
            "descripcion": (
                "Según la Constitución Política de 1991, Colombia se define como:"
            ),
            "opciones": [
                {"texto": "Un Estado absolutista.", "puntaje": 0},
                {"texto": "Un Estado teocrático.", "puntaje": 0},
                {"texto": "Un Estado social de derecho.", "puntaje": 1},
                {"texto": "Una monarquía parlamentaria.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Fundamentos de la Constitución de 1991",
            "grupo_codigo": None,
            "titulo": "Derechos y tutela",
            "descripcion": (
                "La Constitución de 1991 reconoce derechos fundamentales, colectivos y "
                "mecanismos de protección como la acción de tutela."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 37. Mecanismos de Participación Ciudadana
        {
            "contenido_titulo": "Mecanismos de Participación Ciudadana",
            "grupo_codigo": None,
            "titulo": "Ejemplo de mecanismo de participación",
            "descripcion": (
                "¿Cuál de los siguientes es un mecanismo de participación ciudadana previsto "
                "en la Constitución colombiana?"
            ),
            "opciones": [
                {"texto": "Plebiscito o referendo.", "puntaje": 1},
                {
                    "texto": "Nombramiento directo de ministros por los ciudadanos.",
                    "puntaje": 0,
                },
                {"texto": "Elección vitalicia de congresistas.", "puntaje": 0},
                {"texto": "Nombramiento hereditario de alcaldes.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Mecanismos de Participación Ciudadana",
            "grupo_codigo": None,
            "titulo": "Revocatoria del mandato",
            "descripcion": (
                "La revocatoria del mandato permite a los ciudadanos terminar anticipadamente "
                "el periodo de un gobernante elegido popularmente."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 38. Fundamentos de Filosofía
        {
            "contenido_titulo": "Fundamentos de Filosofía",
            "grupo_codigo": None,
            "titulo": "Pregunta filosófica",
            "descripcion": "¿Cuál de las siguientes preguntas corresponde típicamente a una reflexión filosófica?",
            "opciones": [
                {"texto": "¿Cuánto cuesta este producto en la tienda?", "puntaje": 0},
                {"texto": "¿Qué es la justicia?", "puntaje": 1},
                {"texto": "¿A qué hora pasa el bus?", "puntaje": 0},
                {"texto": "¿Cuántos goles lleva mi equipo?", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Fundamentos de Filosofía",
            "grupo_codigo": None,
            "titulo": "Objeto de la filosofía",
            "descripcion": (
                "La filosofía solo se ocupa de problemas religiosos y no de cuestiones "
                "cotidianas de la vida humana."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 0},
                {"texto": "Falso", "puntaje": 1},
            ],
        },
        # 39. Lógica Proposicional
        {
            "contenido_titulo": "Lógica Proposicional",
            "grupo_codigo": None,
            "titulo": "Traducción de un condicional",
            "descripcion": (
                "Sea p: 'llueve' y q: 'llevo paraguas'. ¿Cuál de las siguientes expresiones "
                "representa 'si llueve, entonces llevo paraguas'?"
            ),
            "opciones": [
                {"texto": "p ∧ q", "puntaje": 0},
                {"texto": "p ∨ q", "puntaje": 0},
                {"texto": "¬p ∨ q", "puntaje": 0},
                {"texto": "p → q", "puntaje": 1},
            ],
        },
        {
            "contenido_titulo": "Lógica Proposicional",
            "grupo_codigo": None,
            "titulo": "Definición de proposición",
            "descripcion": (
                "En lógica proposicional, una proposición es un enunciado que puede ser "
                "verdadero o falso, pero no ambas cosas a la vez."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 40. Identificación de Avisos y Contexto
        {
            "contenido_titulo": "Identificación de Avisos y Contexto",
            "grupo_codigo": None,
            "titulo": "Interpretación de un aviso",
            "descripcion": (
                "En la entrada de un edificio se lee el aviso: 'PROHIBIDO FUMAR. "
                "Espacio libre de humo'. ¿Cuál es el mensaje principal del aviso?"
            ),
            "opciones": [
                {"texto": "Se permite fumar solo en horas de la noche.", "puntaje": 0},
                {"texto": "Está prohibido fumar en ese lugar.", "puntaje": 1},
                {"texto": "Solo se puede fumar en la entrada.", "puntaje": 0},
                {"texto": "El edificio vende cigarrillos.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Identificación de Avisos y Contexto",
            "grupo_codigo": None,
            "titulo": "Importancia del contexto en un aviso",
            "descripcion": (
                "El lugar donde se ubica un aviso (por ejemplo, un hospital o un centro "
                "comercial) puede influir en la interpretación de su mensaje."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 41. Asociación de Vocabulario y Definiciones
        {
            "contenido_titulo": "Asociación de Vocabulario y Definiciones",
            "grupo_codigo": None,
            "titulo": "Significado de 'sostenible'",
            "descripcion": (
                "En el contexto ambiental, ¿qué significa que una actividad sea 'sostenible'?"
            ),
            "opciones": [
                {"texto": "Que se realiza sin ningún tipo de recurso.", "puntaje": 0},
                {
                    "texto": "Que se puede mantener en el tiempo sin agotar los recursos.",
                    "puntaje": 1,
                },
                {"texto": "Que siempre es barata.", "puntaje": 0},
                {"texto": "Que solo beneficia a una empresa.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Asociación de Vocabulario y Definiciones",
            "grupo_codigo": None,
            "titulo": "Sinónimos",
            "descripcion": (
                "Dos palabras sinónimas comparten un significado similar en la mayoría de "
                "los contextos."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 42. Interacción Social Básica
        {
            "contenido_titulo": "Interacción Social Básica",
            "grupo_codigo": "EN_DIALOGO_CAFE",
            "titulo": "Intención de la persona A",
            "descripcion": (
                "En el diálogo de la cafetería, cuando A dice 'Excuse me, is this seat taken?', "
                "¿qué está haciendo?"
            ),
            "opciones": [
                {"texto": "Pidiendo la cuenta.", "puntaje": 0},
                {
                    "texto": "Pidiendo permiso de forma cortés para sentarse.",
                    "puntaje": 1,
                },
                {"texto": "Reservando una mesa para un grupo grande.", "puntaje": 0},
                {"texto": "Preguntando por el menú del día.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Interacción Social Básica",
            "grupo_codigo": "EN_DIALOGO_CAFE",
            "titulo": "Uso de una expresión cortés",
            "descripcion": (
                "La expresión 'Is this seat taken?' se utiliza para preguntar de forma "
                "respetuosa si se puede ocupar un asiento."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 43. Uso del Lenguaje (Gramática y Léxico)
        {
            "contenido_titulo": "Uso del Lenguaje (Gramática y Léxico)",
            "grupo_codigo": None,
            "titulo": "Concordancia verbal",
            "descripcion": "¿Cuál de las siguientes oraciones está escrita de forma gramaticalmente correcta?",
            "opciones": [
                {"texto": "Hubieron muchos problemas en el examen.", "puntaje": 0},
                {"texto": "Hubo muchos problemas en el examen.", "puntaje": 1},
                {"texto": "Habo muchos problemas en el examen.", "puntaje": 0},
                {"texto": "Hubo muchos problema en el examen.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Uso del Lenguaje (Gramática y Léxico)",
            "grupo_codigo": None,
            "titulo": "Uso de 'hubieron'",
            "descripcion": "En español estándar, es correcto decir 'Hubieron muchos problemas'.",
            "opciones": [
                {"texto": "Verdadero", "puntaje": 0},
                {"texto": "Falso", "puntaje": 1},
            ],
        },
        # 44. Lectura Literal y Parafraseo
        {
            "contenido_titulo": "Lectura Literal y Parafraseo",
            "grupo_codigo": None,
            "titulo": "Comprensión literal de un enunciado",
            "descripcion": (
                "Lee el siguiente enunciado: 'El parque fue renovado el año pasado y ahora "
                "cuenta con más zonas verdes y juegos infantiles'. ¿Qué ocurrió el año pasado?"
            ),
            "opciones": [
                {
                    "texto": "Se construyó un centro comercial junto al parque.",
                    "puntaje": 0,
                },
                {"texto": "El parque fue renovado.", "puntaje": 1},
                {"texto": "Se cerraron las zonas verdes.", "puntaje": 0},
                {"texto": "Se eliminaron los juegos infantiles.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Lectura Literal y Parafraseo",
            "grupo_codigo": None,
            "titulo": "Definición de parafrasear",
            "descripcion": (
                "Parafrasear un texto significa expresar su contenido con otras palabras, "
                "manteniendo la misma idea principal."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 45. Lectura Inferencial y Propósito del Autor
        {
            "contenido_titulo": "Lectura Inferencial y Propósito del Autor",
            "grupo_codigo": None,
            "titulo": "Inferencia sobre el propósito de un texto",
            "descripcion": (
                "Un vecino escribe una carta al periódico diciendo que el ruido nocturno de "
                "los bares no le permite dormir y pide controles más estrictos. "
                "¿Cuál es el propósito principal del texto?"
            ),
            "opciones": [
                {"texto": "Invitar a los vecinos a una fiesta.", "puntaje": 0},
                {
                    "texto": "Expresar inconformidad y pedir regulación del ruido.",
                    "puntaje": 1,
                },
                {"texto": "Vender un apartamento cerca de los bares.", "puntaje": 0},
                {"texto": "Hacer publicidad a los bares de la zona.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Lectura Inferencial y Propósito del Autor",
            "grupo_codigo": None,
            "titulo": "Lectura inferencial",
            "descripcion": (
                "La lectura inferencial implica ir más allá de lo explícito en el texto y "
                "deducir información que no está directamente dicha."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 46. Interpretación de Vistas de Sólidos (Proyección Isométrica)
        {
            "contenido_titulo": "Interpretación de Vistas de Sólidos (Proyección Isométrica)",
            "grupo_codigo": None,
            "titulo": "Ejes en una proyección isométrica",
            "descripcion": (
                "En una proyección isométrica típica, las tres aristas principales de un "
                "cubo se representan formando entre sí ángulos de aproximadamente:"
            ),
            "opciones": [
                {"texto": "90°.", "puntaje": 0},
                {"texto": "60°.", "puntaje": 0},
                {"texto": "120°.", "puntaje": 1},
                {"texto": "45°.", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Interpretación de Vistas de Sólidos (Proyección Isométrica)",
            "grupo_codigo": None,
            "titulo": "Paralelismo en proyección isométrica",
            "descripcion": (
                "En una proyección isométrica, las aristas paralelas de un sólido se "
                "representan como segmentos también paralelos en el dibujo."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 47. Conteo de Partes de Sólidos
        {
            "contenido_titulo": "Conteo de Partes de Sólidos",
            "grupo_codigo": None,
            "titulo": "Aristas de un cubo",
            "descripcion": "¿Cuántas aristas tiene un cubo?",
            "opciones": [
                {"texto": "6", "puntaje": 0},
                {"texto": "8", "puntaje": 0},
                {"texto": "12", "puntaje": 1},
                {"texto": "16", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Conteo de Partes de Sólidos",
            "grupo_codigo": None,
            "titulo": "Caras de un prisma rectangular",
            "descripcion": "Un prisma rectangular (paralelepípedo) tiene exactamente 6 caras.",
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 48. Simetría y Efecto Espejo (Rotación Especular)
        {
            "contenido_titulo": "Simetría y Efecto Espejo (Rotación Especular)",
            "grupo_codigo": None,
            "titulo": "Eje de simetría",
            "descripcion": (
                "Una figura plana tiene simetría respecto a una recta si al reflejarla en "
                "esa recta ambas mitades coinciden exactamente."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Simetría y Efecto Espejo (Rotación Especular)",
            "grupo_codigo": None,
            "titulo": "Imagen en un espejo plano",
            "descripcion": (
                "En una imagen reflejada en un espejo plano, las posiciones izquierda y "
                "derecha se intercambian con respecto al objeto real."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 49. Secuencias y Patrones Gráficos
        {
            "contenido_titulo": "Secuencias y Patrones Gráficos",
            "grupo_codigo": None,
            "titulo": "Identificación de un patrón creciente",
            "descripcion": (
                "En una secuencia de figuras, cada término añade un triángulo más que el "
                "anterior (1 triángulo, luego 2, luego 3...). Si la secuencia continúa con "
                "la misma regla, ¿cuántos triángulos tendrá la quinta figura?"
            ),
            "opciones": [
                {"texto": "3", "puntaje": 0},
                {"texto": "4", "puntaje": 0},
                {"texto": "5", "puntaje": 1},
                {"texto": "6", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Secuencias y Patrones Gráficos",
            "grupo_codigo": None,
            "titulo": "Definición de patrón",
            "descripcion": (
                "Reconocer un patrón implica identificar la regla que genera una "
                "secuencia de elementos."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        # 50. Pliegues, Cortes y Armado de Figuras
        {
            "contenido_titulo": "Pliegues, Cortes y Armado de Figuras",
            "grupo_codigo": None,
            "titulo": "Red de un cubo",
            "descripcion": (
                "Una red (desarrollo plano) adecuada de un cubo está formada por seis "
                "cuadrados congruentes dispuestos de manera que puedan plegarse para "
                "formar las seis caras del sólido."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
        {
            "contenido_titulo": "Pliegues, Cortes y Armado de Figuras",
            "grupo_codigo": None,
            "titulo": "Construcción de un cubo a partir de una figura plana",
            "descripcion": (
                "Si se recorta y pliega correctamente una figura plana formada por seis "
                "cuadrados iguales conectados, es posible construir un cubo."
            ),
            "opciones": [
                {"texto": "Verdadero", "puntaje": 1},
                {"texto": "Falso", "puntaje": 0},
            ],
        },
    ],
]
