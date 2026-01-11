package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type HealthResponse struct {
    Status  string `json:"status"`
    Service string `json:"service"`
}

type IngestResponse struct {
    Status   string   `json:"status"`
    Pipeline []string `json:"pipeline"`
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
    response := HealthResponse{Status: "ok", Service: "mechyx-ingest"}
    writeJSON(w, response)
}

func ingestHandler(w http.ResponseWriter, r *http.Request) {
    response := IngestResponse{
        Status:   "ready",
        Pipeline: []string{"service-notes", "defect-logs", "supplier-reports"},
    }
    writeJSON(w, response)
}

func writeJSON(w http.ResponseWriter, payload any) {
    w.Header().Set("Content-Type", "application/json")
    encoder := json.NewEncoder(w)
    if err := encoder.Encode(payload); err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
    }
}

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/health", healthHandler)
    mux.HandleFunc("/ingest", ingestHandler)

    server := &http.Server{
        Addr:    ":8081",
        Handler: mux,
    }

    log.Println("Mechyx ingest service listening on :8081")
    if err := server.ListenAndServe(); err != nil {
        log.Fatal(err)
    }
}
