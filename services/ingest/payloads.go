package main

type ServiceNotePayload struct {
    VIN            string `json:"vin"`
    IssueTitle     string `json:"issue_title"`
    SymptomSummary string `json:"symptom_summary"`
    RawNote        string `json:"raw_note"`
    Technician     string `json:"technician"`
    Mileage        int    `json:"mileage"`
    Source         string `json:"source"`
}

type DefectPayload struct {
    Line           string `json:"line"`
    Station        string `json:"station"`
    Component      string `json:"component"`
    Severity       string `json:"severity"`
    Description    string `json:"description"`
    DetectedAt     string `json:"detected_at"`
}

type SupplierReportPayload struct {
    SupplierName string `json:"supplier_name"`
    Tier         string `json:"tier"`
    Region       string `json:"region"`
    RiskScore    float64 `json:"risk_score"`
    Summary      string `json:"summary"`
}
