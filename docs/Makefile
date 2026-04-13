SPHINXBUILD = .venv/bin/sphinx-build
DOCS_DIR    = .
BUILDDIR    = _build

.venv:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install -e ..

html: .venv
	$(SPHINXBUILD) -W $(DOCS_DIR) $(BUILDDIR)/html

clean:
	rm -rf $(BUILDDIR) .venv
