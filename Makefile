include .env
export

RUN = poetry run

.PHONY: serve

setup:
	poetry install
	npm install

import:
	$(RUN) cf-export pages-with-descendants $(CONFLUENCE_PARENT_ID) ./docs

publish:
	npx @markdown-confluence/cli

serve:
	$(RUN) mkdocs serve

pdf:
	ENABLE_PDF_EXPORT=1 $(RUN) mkdocs build
