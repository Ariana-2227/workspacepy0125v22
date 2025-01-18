# educacion, realice un programa que administre los alumnos

Alumnos=[
    {
        "nombre":"Gain",
        "dni":"9797799",
        "cursos":["Python","Sql","Java"]
    },
    {
        "nombre":"GIAN",
        "dni":"1496749",
        "cursos":["Python"]
    },
    {
        "nombre":"Juan",
        "dni":"164646",
        "cursos":["Python","PowerBi","Java"]
    },
    {
        "nombre":"carlos",
        "dni":"16464764",
        "cursos":["Python"]
    },
]
# Agregar alumno
nombre=input("Ingrese su nombre:")
dni=input("ingrese su dni:")
curso=input("Ingrese el curso a matricularse")

Alumnos.append(
    {
        "nombre":nombre,
        "dni":dni,
        "curso":[curso]
    }
)
Alumnos=Alumnos
print(Alumnos)


