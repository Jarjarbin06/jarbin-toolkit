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
PACKAGE_NAME    := jarbin_toolkit_action

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
	@echo -e "$(YELLOW) [INSTALL] ($(PACKAGE_NAME)) Installing package$(NC)"
	@pip install -e .
	@echo -e "$(GREEN) [INSTALL] ($(PACKAGE_NAME)) Package installed$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] ($(PACKAGE_NAME)) Uninstalling package$(NC)"
	@echo "y" | pip uninstall $(PACKAGE_NAME) || true
	@echo -e "$(GREEN) [UNINSTALL] ($(PACKAGE_NAME)) Package uninstalled$(NC)"

reinstall:
	@echo -e "$(YELLOW) [REINSTALL] ($(PACKAGE_NAME)) Reinstalling package$(NC)"
	@make --no-print-directory uninstall install
	@echo -e "$(GREEN) [REINSTALL] ($(PACKAGE_NAME)) Package reinstalled$(NC)"

# ------------------------------------------------------------
# TESTS & CHECKS
# ------------------------------------------------------------

test:
	@echo -e "$(YELLOW) [TEST] ($(PACKAGE_NAME)) Running tests$(NC)"
	@pytest --debug=trace --cov=jarbin_toolkit --cov-report=html
	@xdg-open htmlcov/index.html
	@rm -f .coverage
	@echo -e "$(GREEN) [TEST] ($(PACKAGE_NAME)) Tests ran$(NC)"

test-jartest:
	@echo -e "$(YELLOW) [TEST] ($(PACKAGE_NAME)) Running JarTest tests$(NC)"
	@python -m tests
	@echo -e "$(GREEN) [TEST] ($(PACKAGE_NAME)) JarTest tests ran$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] ($(PACKAGE_NAME)) Checking package$(NC)"
	@pip show $(PACKAGE_NAME) || true
	@echo -e "$(GREEN) [CHECK] ($(PACKAGE_NAME)) Package checked$(NC)"

check-style:
	@echo -e "$(YELLOW) [CHECK] ($(PACKAGE_NAME)) Checking coding style$(NC)"
	@flake8 . --count --exit-zero --max-line-length=100 --statistic
	@echo -e "$(GREEN) [CHECK] ($(PACKAGE_NAME)) Coding style checked$(NC)"

# ------------------------------------------------------------
# INFORMATION
# ------------------------------------------------------------

info:
	@echo -e "$(YELLOW) [INFO] ($(PACKAGE_NAME)) Getting package informations$(NC)"
	@$(PIP) show $(PACKAGE_NAME) >/dev/null 2>&1 && $(PIP) show $(PACKAGE_NAME) && echo -e "$(GREEN) [INFO] Package informations shown$(NC)" || echo -e "$(RED) [INFO] Package not installed$(NC)"

# ------------------------------------------------------------
# CLEANUP
# ------------------------------------------------------------

clean:
	@echo -e "$(YELLOW) [CLEAN] ($(PACKAGE_NAME)) Removing cache, test, log and build files$(NC)"
	@find . -type d -name "__pycache__" -exec rm -frd {} +
	@rm -frd *.egg-info *.xml trace htmlcov .pytest_cache .coverage
	@echo -e "$(GREEN) [CLEAN] ($(PACKAGE_NAME)) Cleaning done$(NC)"

# ------------------------------------------------------------
# SAFETY
# ------------------------------------------------------------

.PHONY: \
	help \
	install uninstall reinstall \
	test check-style \
	info \
	clean
