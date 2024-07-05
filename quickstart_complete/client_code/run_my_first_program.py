from nada_dsl import *

# Enable telemetry with a unique identifier
telemetry_id = enable_telemetry("0x3199B1459117Dd7ceeE0b3dA0CE8e98Da30451b2")

def nada_main():
    # Define parties
    employer = Party(name="Employer")
    employee = Party(name="Employee")

    # Define salary components as inputs from the employer
    base_salary = SecretInteger(Input(name="base_salary", party=employer))
    bonus = SecretInteger(Input(name="bonus", party=employer))
    deductions = SecretInteger(Input(name="deductions", party=employer))

    # Calculate the total salary
    total_salary = base_salary + bonus - deductions

    # Output the total salary to the employee
    return [Output(total_salary, "total_salary", employee)]