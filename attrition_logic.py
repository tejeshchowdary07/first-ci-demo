def predict_attrition_risk(overtime, job_satisfaction):
    if overtime == "Yes" and job_satisfaction <= 2:
        return "HIGH"
    else:
        return "LOW"


if __name__ == "__main__":
    result = predict_attrition_risk("Yes", 1)
    print("Predicted Attrition Risk:", result)
