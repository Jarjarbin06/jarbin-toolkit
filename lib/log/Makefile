# ============================================================
# Jarbin_ToolKit – Makefile
# ============================================================
# Usage:
#   make help
#   make install
#   make test
# ============================================================

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

PYTHON          ?= python3
PIP             ?= pip3
SHELL           := /bin/bash
SCRIPT_DIR      := script
PACKAGE_NAME    := jarbin_toolkit_log

# Colors (safe for most terminals)
GREEN           := \033[0;32m
YELLOW          := \033[0;33m
RED             := \033[0;31m
NC              := \033[0m

# ------------------------------------------------------------
# DEFAULT TARGET
# ------------------------------------------------------------

.DEFAULT_GOAL := install

# ------------------------------------------------------------
# PACKAGE MANAGEMENT
# ------------------------------------------------------------

install:
	@echo -e "$(YELLOW) [INSTALL] Installing package$(NC)"
	@pip install -e .
	@echo -e "$(GREEN) [INSTALL] Installing package$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] Uninstalling package$(NC)"
	@echo "y" | pip uninstall $(PACKAGE_NAME) || true
	@echo -e "$(GREEN) [UNINSTALL] Package uninstalled$(NC)"

reinstall:
	@echo -e "$(YELLOW) [REINSTALL] Reinstalling package$(NC)"
	@make --no-print-directory uninstall install
	@echo -e "$(GREEN) [REINSTALL] Package reinstalled$(NC)"

# ------------------------------------------------------------
# TESTS & CHECKS
# ------------------------------------------------------------

test:
	@echo -e "$(YELLOW) [TEST] Running tests$(NC)"
	@pytest --debug=trace --cov=jarbin_toolkit --cov-report=html
	@xdg-open htmlcov/index.html
	@rm -f .coverage
	@echo -e "$(GREEN) [TEST] Tests ran$(NC)"

test-jartest:
	@echo -e "$(YELLOW) [TEST] Running JarTest tests$(NC)"
	@python -m tests
	@echo -e "$(GREEN) [TEST]  JarTest tests ran$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] Checking package$(NC)"
	@pip show $(PACKAGE_NAME) || true
	@echo -e "$(GREEN) [CHECK] Package checked$(NC)"

check-style:
	@echo -e "$(YELLOW) [CHECK] Checking coding style$(NC)"
	@flake8 . --count --exit-zero --max-line-length=100 --statistic
	@echo -e "$(GREEN) [CHECK] Coding style checked$(NC)"

# ------------------------------------------------------------
# INFORMATION
# ------------------------------------------------------------

info:
	@echo -e "$(YELLOW) [INFO] Getting package informations$(NC)"
	@$(PIP) show $(PACKAGE_NAME) >/dev/null 2>&1 && $(PIP) show $(PACKAGE_NAME) && echo -e "$(GREEN) [INFO] Package informations shown$(NC)" || echo -e "$(RED) [INFO] Package not installed$(NC)"

# ------------------------------------------------------------
# CLEANUP
# ------------------------------------------------------------

clean:
	@echo -e "$(YELLOW) [CLEAN] Removing cache, test, log and build files$(NC)"
	@find . -type d -name "__pycache__" -exec rm -frd {} +
	@rm -frd *.egg-info *.xml trace htmlcov .pytest_cache .coverage
	@echo -e "$(GREEN) [CLEAN] Done$(NC)"

# ------------------------------------------------------------
# SAFETY
# ------------------------------------------------------------

.PHONY: \
	help \
	install uninstall reinstall \
	test check-style \
	info \
	clean
