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
PACKAGE_NAME    := jarbin_toolkit_error_template

# Colors (safe for most terminals)
GREEN           := \033[0;32m
YELLOW          := \033[0;33m
RED             := \033[0;31m
NC              := \033[0m

# ------------------------------------------------------------
# DEFAULT TARGET
# ------------------------------------------------------------

.DEFAULT_GOAL := help

# ------------------------------------------------------------
# HELP
# ------------------------------------------------------------

help:
	@echo -e "$(GREEN)Available commands:$(NC)"
	@echo ""
	@echo -e "\tmake/make help\t\tShow this help message"
	@echo ""
	@echo -e "\tmake install\t\tInstall the package"
	@echo -e "\tmake uninstall\t\tUninstall the package"
	@echo -e "\tmake reinstall\t\tReinstall the package"
	@echo ""
	@echo -e "\tmake test\t\Test the package (pytest)"
	@echo -e "\tmake check\t\tShow package info (PyPI)"
	@echo ""
	@echo -e "\tmake clean\t\tClean cache and build files"
	@echo -e "\tmake info\t\tShow package info"
	@echo ""

# ------------------------------------------------------------
# PACKAGE MANAGEMENT
# ------------------------------------------------------------

install:
	@echo -e "$(YELLOW) [INSTALL] ($(PACKAGE_NAME)) Installing package$(NC)"
	@pip install -e .
	@echo -e "$(GREEN) [INSTALL] ($(PACKAGE_NAME)) Package installed$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] ($(PACKAGE_NAME)) Uninstalling package$(NC)"
	@echo "y" | pip uninstall jarbin_toolkit_error
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
	@pytest --debug=trace --cov=$(PACKAGE_NAME) --cov-report=html
	@xdg-open htmlcov/index.html
	@rm -f .coverage
	@echo -e "$(GREEN) [TEST] ($(PACKAGE_NAME)) Tests ran$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] ($(PACKAGE_NAME)) Checking package$(NC)"
	@pip show jarbin_toolkit_error
	@echo -e "$(GREEN) [CHECK] ($(PACKAGE_NAME)) Package checked$(NC)"

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
	test check \
	info \
	clean
