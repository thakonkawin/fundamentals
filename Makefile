clean:
	@echo "Removing __pycache__ and media folders..."
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name 'media' -exec rm -rf {} +
	@echo "Removing .DS_Store files..."
	@find . -type f -name '.DS_Store' -delete