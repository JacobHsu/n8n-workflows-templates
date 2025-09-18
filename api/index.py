#!/usr/bin/env python3
"""
Simple FastAPI Server for N8N Workflow Documentation (Vercel Compatible)
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from pathlib import Path

# Initialize FastAPI app
app = FastAPI(
    title="N8N Workflow Documentation API",
    description="API for browsing workflow documentation",
    version="2.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "N8N Workflow Documentation API",
        "version": "2.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "timestamp": "2024-01-01T00:00:00Z"
    }

@app.get("/api/workflows")
async def list_workflows():
    """List all workflows."""
    try:
        # Get the project root directory
        project_root = os.path.dirname(os.path.dirname(__file__))
        workflows_dir = os.path.join(project_root, "workflows")

        if not os.path.exists(workflows_dir):
            return {"workflows": [], "total": 0, "message": "Workflows directory not found"}

        workflow_files = []
        for file in os.listdir(workflows_dir):
            if file.endswith('.json'):
                try:
                    file_path = os.path.join(workflows_dir, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        workflow_data = json.load(f)

                    workflow_files.append({
                        "filename": file,
                        "name": workflow_data.get("name", file),
                        "tags": workflow_data.get("tags", []),
                        "nodes": len(workflow_data.get("nodes", [])),
                        "createdAt": workflow_data.get("createdAt", ""),
                        "updatedAt": workflow_data.get("updatedAt", "")
                    })
                except Exception as e:
                    # Skip problematic files
                    continue

        return {
            "workflows": workflow_files,
            "total": len(workflow_files)
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to list workflows: {str(e)}"}
        )

@app.get("/api/workflows/{filename}")
async def get_workflow(filename: str):
    """Get a specific workflow by filename."""
    try:
        project_root = os.path.dirname(os.path.dirname(__file__))
        workflows_dir = os.path.join(project_root, "workflows")
        file_path = os.path.join(workflows_dir, filename)

        if not os.path.exists(file_path):
            return JSONResponse(
                status_code=404,
                content={"error": "Workflow not found"}
            )

        with open(file_path, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)

        return workflow_data

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to get workflow: {str(e)}"}
        )

# Export app for Vercel
# Vercel will automatically handle ASGI apps