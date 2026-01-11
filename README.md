# Mechyx

Mechyx is a concept project for the automotive industry: an AI-powered, closed-loop knowledge platform that connects design, manufacturing, supply chain, and service data into one shared system of truth. The goal is to solve a common but overlooked issue in automotive programs: **cross-lifecycle knowledge loss**—where each department captures insights, but the organization never learns fast enough across the full lifecycle.

## Problem Statement

Automotive teams collect rich data at every stage, but that knowledge is fragmented:

- Designers don't see real-world mechanic pain points in time.
- Manufacturing defects are hard to trace back to design decisions.
- Service notes are unstructured and rarely feed back into engineering.
- Supplier quality data is siloed across tiers.

Mechyx focuses on making those insights searchable, connected, and actionable.

## Vision

Build a multi-page, highly usable web platform with AI-driven intelligence that:

- Unifies defect, service, and supplier signals.
- Extracts meaning from unstructured mechanic notes.
- Surfaces likely root causes and design impacts.
- Tracks how changes reduce defect rates over time.

## Core Modules

- **Issue Atlas**: Unified map of defects from manufacturing, service, and suppliers.
- **Mechanic Signal Hub**: AI summarization and trend detection from service notes.
- **Design Impact Simulator**: Links recurring issues to components and design decisions.
- **Supplier Integrity Dashboard**: Risk scoring and anomaly detection.
- **Assembly Guidance Generator**: Turns design intent into clear shop-floor steps.
- **Change Feedback Loop**: Measures improvement after fixes.

## AI Capabilities

- NLP on service notes (symptom, condition, part extraction).
- Similarity search across historical issues.
- Automated triage and tagging of new field reports.
- Design-change suggestions driven by defect patterns.

## Proposed Tech Stack (Free-Tier Friendly)

**Frontend**
- Angular

**Backend**
- Django + Django REST Framework (main API)
- Go microservices for high-throughput ingestion and processing

**Database**
- NoSQL: MongoDB or AWS DocumentDB

**AI + Search**
- LLM API (OpenAI or local LLM)
- Vector search: Qdrant
- Text search: OpenSearch / Elasticsearch

**Cloud + DevOps**
- AWS Free Tier or Azure Student
- Docker + Docker Compose
- GitHub Actions CI/CD
- Terraform (infra as code)
- S3-compatible object storage (e.g., MinIO)

## Roadmap

**Phase 1 (MVP)**
- Ingest service notes + defect logs
- AI summarization + tagging
- Searchable issue dashboard

**Phase 2**
- Supplier scoring and quality insights
- Design-change impact analysis
- Role-based dashboards

**Phase 3**
- Predictive defect risk and AI suggestions
- Workflow automation and alerts

## CV-Ready Project Summary

**Mechyx — Closed-Loop Automotive Quality Intelligence Platform**  
Built an AI-powered system that connects design, manufacturing, suppliers, and field service data to eliminate recurring defects and accelerate design improvements. Features multi-source ingestion, AI-based root-cause discovery, and supplier risk dashboards.

## Project Structure

```
backend/          Django + DRF API
frontend/         Angular UI (MVP scaffold)
services/ingest/  Go ingestion microservice
docker-compose.yml
```

## Getting Started (Local)

### Backend API

#### Windows (PowerShell)

```powershell
cd backend
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If you see an execution policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Windows (Command Prompt)

```bat
cd backend
python -m venv .venv
.\\.venv\\Scripts\\activate.bat
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### macOS/Linux

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/` with a health check at `/api/health/`.

#### Create sample data (optional)

```bash
python manage.py createsuperuser
python manage.py runserver
```

Use the admin at `http://localhost:8000/admin/` to create `Suppliers`, `Components`, `Issues`, and `ServiceNotes`.

### Ingest Service

```bash
cd services/ingest
go run .
```

The ingest service listens on `http://localhost:8081/health`.

#### Sample ingest payloads

```bash
curl -X POST http://localhost:8081/ingest/service-notes \
  -H "Content-Type: application/json" \
  -d '{
    "vin": "1M8GDM9AXKP042788",
    "issue_title": "ABS warning after highway drive",
    "symptom_summary": "ABS light after 20 minutes driving",
    "raw_note": "Customer reports intermittent ABS warning, cleared after restart.",
    "technician": "Jordan Reyes",
    "mileage": 48210,
    "source": "dealer"
  }'

curl -X POST http://localhost:8081/ingest/defects \
  -H "Content-Type: application/json" \
  -d '{
    "line": "Line 3",
    "station": "Torque Bay",
    "component": "Front subframe",
    "severity": "high",
    "description": "Torque variance beyond spec",
    "detected_at": "2024-05-18"
  }'

curl -X POST http://localhost:8081/ingest/supplier-reports \
  -H "Content-Type: application/json" \
  -d '{
    "supplier_name": "Nova Mobility",
    "tier": "Tier 1",
    "region": "NA",
    "risk_score": 4.2,
    "summary": "Battery module defect rate rising above 3%"
  }'
```

### Frontend

```bash
cd frontend
npm install
npm start
```

The Angular app runs at `http://localhost:4200/`.

### Docker Compose

```bash
docker compose up --build
```
