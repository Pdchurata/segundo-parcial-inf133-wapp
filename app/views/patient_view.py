from flask import render_template

def patients(patients):
    return render_template("patients.html", title="Lista de Pacientes", patients=patients)

def create_patient():
    return render_template("create_patients.html", title="Registrar Paciente")

def update_patient(patient):
    return render_template("update_patient.html", title="Actualizar Paciente", patient=patient)

def delete_patient(patient):
    return render_template("delete_patient.html", title="Eliminar Paciente", patient=patient)
