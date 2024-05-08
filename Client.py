import tkinter as tk
from tkinter import ttk
from joblib import load
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model = load('model.pkl')


# Function to predict the obesity level
def predict_obesity():
    gender = gender_encoder.transform([gender_var.get()])[0]
    age = float(age_var.get())
    height = float(height_var.get())
    weight = float(weight_var.get())
    family_history = family_history_encoder.transform([family_history_var.get()])[0]
    favc = favc_encoder.transform([favc_var.get()])[0]
    # Validate FCVC
    fcvc_input = fcvc_var.get()
    if fcvc_input.strip() == "":
        prediction_label.config(text="Please enter a value for FCVC.")
        return
    fcvc = float(fcvc_input)

    ncp_input = ncp_var.get()
    if ncp_input.strip() == "":
        prediction_label.config(text="Please enter a value for NCP.")
        return
    fcvc = float(fcvc_input)
    ncp = float(ncp_var.get())
    caec = caec_encoder.transform([caec_var.get()])[0]
    smoke = smoke_encoder.transform([smoke_var.get()])[0]
    ch2o = float(ch2o_var.get())
    scc = scc_encoder.transform([scc_var.get()])[0]
    faf = float(faf_var.get())
    tue = float(tue_var.get())
    calc = calc_encoder.transform([calc_var.get()])[0]
    mtrans = mtrans_encoder.transform([mtrans_var.get()])[0]

    # Predict the obesity level
    prediction = model.predict([[gender, age, height, weight, family_history, favc, fcvc, ncp, caec, smoke, ch2o, scc,
                                 faf, tue, calc, mtrans]])

    # Display the predicted obesity level
    prediction_label.config(text=f'Predicted obesity level: {prediction[0]}')


# Create the main window
root = tk.Tk()
root.title("Obesity Level Prediction")

# Gender
gender_label = ttk.Label(root, text="Gender:")
gender_label.grid(row=0, column=0, sticky="w")
gender_var = tk.StringVar()
gender_options = ['Male', 'Female']
gender_encoder = LabelEncoder()
gender_encoder.fit(gender_options)
gender_entry = ttk.Combobox(root, textvariable=gender_var, values=gender_options)
gender_entry.grid(row=0, column=1, sticky="w")

# Age
age_label = ttk.Label(root, text="Age:")
age_label.grid(row=1, column=0, sticky="w")
age_var = tk.StringVar()
age_entry = ttk.Entry(root, textvariable=age_var)
age_entry.grid(row=1, column=1)

# Height
height_label = ttk.Label(root, text="Height:")
height_label.grid(row=2, column=0, sticky="w")
height_var = tk.StringVar()
height_entry = ttk.Entry(root, textvariable=height_var)
height_entry.grid(row=2, column=1)

# Weight
weight_label = ttk.Label(root, text="Weight:")
weight_label.grid(row=3, column=0, sticky="w")
weight_var = tk.StringVar()
weight_entry = ttk.Entry(root, textvariable=weight_var)
weight_entry.grid(row=3, column=1)

# Family History
family_history_label = ttk.Label(root, text="Has a family member suffered or suffers from overweight?:")
family_history_label.grid(row=4, column=0, sticky="w")
family_history_var = tk.StringVar()
family_history_options = ['Yes', 'No']
family_history_encoder = LabelEncoder()
family_history_encoder.fit(family_history_options)
family_history_entry = ttk.Combobox(root, textvariable=family_history_var, values=family_history_options)
family_history_entry.grid(row=4, column=1, sticky="w")

# FAVC
favc_label = ttk.Label(root, text="Do you eat high caloric food frequently?:")
favc_label.grid(row=5, column=0, sticky="w")
favc_var = tk.StringVar()
favc_options = ['Yes', 'No']
favc_encoder = LabelEncoder()
favc_encoder.fit(favc_options)
favc_entry = ttk.Combobox(root, textvariable=favc_var, values=favc_options)
favc_entry.grid(row=5, column=1, sticky="w")

# FCVC
fcvc_label = ttk.Label(root, text="Do you usually eat vegetables in your meals?:")
fcvc_label.grid(row=6, column=0, sticky="w")
fcvc_var = tk.StringVar()
fcvc_entry = ttk.Entry(root, textvariable=fcvc_var)
fcvc_entry.grid(row=6, column=1)

# NCP
ncp_label = ttk.Label(root, text="How many main meals do you have daily?")
ncp_label.grid(row=7, column=0, sticky="w")
ncp_var = tk.StringVar()
ncp_entry = ttk.Entry(root, textvariable=ncp_var)
ncp_entry.grid(row=7, column=1)

# CAEC
caec_label = ttk.Label(root, text="Do you eat any food between meals?")
caec_label.grid(row=8, column=0, sticky="w")
caec_var = tk.StringVar()
caec_options = ['Yes', 'No']
caec_encoder = LabelEncoder()
caec_encoder.fit(caec_options)
caec_entry = ttk.Combobox(root, textvariable=caec_var, values=caec_options)
caec_entry.grid(row=8, column=1, sticky="w")

# SMOKE
smoke_label = ttk.Label(root, text="SMOKE:")
smoke_label.grid(row=9, column=0, sticky="w")
smoke_var = tk.StringVar()
smoke_options = ['Yes', 'No']
smoke_encoder = LabelEncoder()
smoke_encoder.fit(smoke_options)
smoke_entry = ttk.Combobox(root, textvariable=smoke_var, values=smoke_options)
smoke_entry.grid(row=9, column=1, sticky="w")

# CH2O
ch2o_label = ttk.Label(root, text="How much water do you drink daily?")
ch2o_label.grid(row=10, column=0, sticky="w")
ch2o_var = tk.StringVar()
ch2o_options = ['1', '2', '3']
ch2o_entry = ttk.Combobox(root, textvariable=ch2o_var, values=ch2o_options)
ch2o_entry.grid(row=10, column=1, sticky="w")

# SCC
scc_label = ttk.Label(root, text="Do you monitor the calories you eat daily?")
scc_label.grid(row=11, column=0, sticky="w")
scc_var = tk.StringVar()
scc_options = ['Yes', 'No']
scc_encoder = LabelEncoder()
scc_encoder.fit(scc_options)
scc_entry = ttk.Combobox(root, textvariable=scc_var, values=scc_options)
scc_entry.grid(row=11, column=1, sticky="w")

# FAF
faf_label = ttk.Label(root, text="How often do you have physical activity?")
faf_label.grid(row=12, column=0, sticky="w")
faf_var = tk.StringVar()
faf_options = ['0', '1', '2', '3']
faf_entry = ttk.Combobox(root, textvariable=faf_var, values=faf_options)
faf_entry.grid(row=12, column=1, sticky="w")

# TUE
tue_label = ttk.Label(root, text="How much time do you use technological devices ?")
tue_label.grid(row=13, column=0, sticky="w")
tue_var = tk.StringVar()
tue_options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
tue_entry = ttk.Combobox(root, textvariable=tue_var, values=tue_options)
tue_entry.grid(row=13, column=1, sticky="w")

# CALC
calc_label = ttk.Label(root, text="How often do you drink alcohol?")
calc_label.grid(row=14, column=0, sticky="w")
calc_var = tk.StringVar()
calc_options = ['No', 'Sometimes', 'Frequently']
calc_encoder = LabelEncoder()
calc_encoder.fit(calc_options)
calc_entry = ttk.Combobox(root, textvariable=calc_var, values=calc_options)
calc_entry.grid(row=14, column=1, sticky="w")

# MTRANS
mtrans_label = ttk.Label(root, text="Which transportation do you usually use?")
mtrans_label.grid(row=15, column=0, sticky="w")
mtrans_var = tk.StringVar()
mtrans_options = ['Automobile', 'Motorbike', 'Public Transportation', 'Walking']
mtrans_encoder = LabelEncoder()
mtrans_encoder.fit(mtrans_options)
mtrans_entry = ttk.Combobox(root, textvariable=mtrans_var, values=mtrans_options)
mtrans_entry.grid(row=15, column=1, sticky="w")

# Button to predict
predict_button = ttk.Button(root, text="Predict", command=predict_obesity)
predict_button.grid(row=16, column=1, columnspan=2)

# Label to display the prediction
prediction_label = ttk.Label(root, text="")
prediction_label.grid(row=17, column=0, columnspan=3)

root.mainloop()
