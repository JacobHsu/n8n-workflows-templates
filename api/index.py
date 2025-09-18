#!/usr/bin/env python3
"""
Simple FastAPI Server for N8N Workflow Documentation (Vercel Compatible)
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
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

# Mount static files
project_root = os.path.dirname(os.path.dirname(__file__))
static_path = os.path.join(project_root, "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

# Serve additional static files with correct routes
@app.get("/src/{file_path:path}")
async def serve_src_files(file_path: str):
    """Serve files from the src directory."""
    try:
        full_path = os.path.join(project_root, "static", "src", file_path)
        if os.path.exists(full_path):
            return FileResponse(full_path)
        else:
            return JSONResponse(status_code=404, content={"error": "File not found"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML interface."""
    try:
        project_root = os.path.dirname(os.path.dirname(__file__))
        html_path = os.path.join(project_root, "static", "index.html")

        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            return HTMLResponse(content=html_content)
        else:
            return HTMLResponse(content="""
            <html>
                <head><title>N8N Workflow Documentation</title></head>
                <body>
                    <h1>N8N Workflow Documentation API</h1>
                    <p>Version: 2.0.0</p>
                    <p>Status: Running</p>
                    <p><a href="/api/workflows">View Workflows API</a></p>
                </body>
            </html>
            """)
    except Exception as e:
        return HTMLResponse(content=f"<html><body><h1>Error</h1><p>{str(e)}</p></body></html>")

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

        # Recursively search for JSON files in all subdirectories
        for root, dirs, files in os.walk(workflows_dir):
            for file in files:
                if file.endswith('.json'):
                    try:
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            workflow_data = json.load(f)

                        # Get relative path from workflows directory
                        relative_path = os.path.relpath(file_path, workflows_dir)
                        category = os.path.dirname(relative_path) if os.path.dirname(relative_path) else "Uncategorized"

                        workflow_files.append({
                            "filename": relative_path.replace("\\", "/"),  # Use forward slashes for web
                            "name": workflow_data.get("name", file),
                            "category": category,
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

@app.get("/api/workflows/{filename:path}")
async def get_workflow(filename: str):
    """Get a specific workflow by filename (supports subdirectories)."""
    try:
        project_root = os.path.dirname(os.path.dirname(__file__))
        workflows_dir = os.path.join(project_root, "workflows")
        # Convert web path separators back to OS path separators
        file_path = os.path.join(workflows_dir, filename.replace("/", os.sep))

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

@app.get("/api/workflows/{filename:path}/download")
async def download_workflow(filename: str):
    """Download a specific workflow file (supports subdirectories)."""
    try:
        project_root = os.path.dirname(os.path.dirname(__file__))
        workflows_dir = os.path.join(project_root, "workflows")
        # Convert web path separators back to OS path separators
        file_path = os.path.join(workflows_dir, filename.replace("/", os.sep))

        if not os.path.exists(file_path):
            return JSONResponse(
                status_code=404,
                content={"error": "Workflow not found"}
            )

        # Get just the filename for download
        download_filename = os.path.basename(filename)

        return FileResponse(
            path=file_path,
            filename=download_filename,
            media_type="application/json"
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to download workflow: {str(e)}"}
        )

# Export app for Vercel
# Vercel will automatically handle ASGI apps