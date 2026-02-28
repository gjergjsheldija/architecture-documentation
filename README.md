# Architecture Documentation

This repository contains the architecture documentation, managed with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and synchronized from Confluence using [Confluence Markdown Exporter](https://github.com/Sven-H/confluence-markdown-exporter).

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management.

1.  **Install dependencies**:
    This project uses both Python (Poetry) and Node.js (npm).
    ```bash
    make setup
    ```

2.  **Configure Tools**:
    *   **Importer**: Run `poetry run cf-export config` to set up Confluence import credentials.
    *   **Publisher**: Create a `.markdown-confluence.json` file in the root directory:
        ```json
        {
          "confluenceBaseUrl": "https://your-domain.atlassian.net/wiki",
          "confluenceParentId": "123456789",
          "confluenceSpaceKey": "SPACE",
          "folderToPublish": "docs"
        }
        ```
        (See [Configuration](https://markdown-confluence.com/docs/configuration) for details).

## Usage

A `Makefile` is provided for common tasks.

### Import from Confluence
To import the documentation pages from Confluence:
```bash
make import
```

### Preview Documentation
To start the MkDocs development server and preview the documentation:
```bash
make serve
```

### Publish to Confluence
To publish the local Markdown files back to Confluence:
```bash
# Ensure credentials are set in environment variables if not in config
make publish
```

### Export to PDF
To export the documentation to PDF:
```bash
make pdf
```