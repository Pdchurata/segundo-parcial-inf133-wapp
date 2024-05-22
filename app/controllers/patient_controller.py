from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from models.patient_model import Patient
from views import patient_view

patient_bp = Blueprint("patient", __name__)

@patient_bp.route("/patients")
@login_required
def list_patients():
    patients = Patient.get_all()
    return patient_view.patients(patients)

@patient_bp.route("/patients/create", methods=["GET", "POST"])
@login_required
def create_patient():
    if current_user.role != 'admin':
        flash("No tienes permiso para realizar esta acción")
        return redirect(url_for("patient.list_patients"))

    if request.method == "POST":
        name = request.form["name"]
        lastname = request.form["lastname"]
        ci = request.form["ci"]
        birth_date = request.form["birth_date"]
        patient = Patient(name, lastname, ci, birth_date)
        patient.save()
        return redirect(url_for("patient.list_patients"))
    return patient_view.create_patient()

@patient_bp.route("/patients/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_patient(id):
    if current_user.role != 'admin':
        flash("No tienes permiso para realizar esta acción")
        return redirect(url_for("patient.list_patients"))

    patient = Patient.get_by_id(id)
    if not patient:
        return "Paciente no encontrado", 404

    if request.method == "POST":
        patient.name = request.form["name"]
        patient.lastname = request.form["lastname"]
        patient.ci = request.form["ci"]
        patient.birth_date = request.form["birth_date"]
        patient.update()
        return redirect(url_for("patient.list_patients"))
    return patient_view.update_patient(patient)

@patient_bp.route("/patients/<int:id>/delete", methods=["GET", "POST"])
@login_required
def delete_patient(id):
    if current_user.role != 'admin':
        flash("No tienes permiso para realizar esta acción")
        return redirect(url_for("patient.list_patients"))

    patient = Patient.get_by_id(id)
    if not patient:
        return "Paciente no encontrado", 404

    if request.method == "POST":
        patient.delete()
        return redirect(url_for("patient.list_patients"))
    return patient_view.delete_patient(patient)
