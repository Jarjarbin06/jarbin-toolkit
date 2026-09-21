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
	@echo -e "$(YELLOW) [INSTALL] Installing package ($(PACKAGE_NAME))$(NC)"
	@pip install -e .
	@echo -e "$(GREEN) [INSTALL] Package installed ($(PACKAGE_NAME))$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] Uninstalling package ($(PACKAGE_NAME))$(NC)"
	@echo "y" | pip uninstall jarbin_toolkit_error
	@echo -e "$(GREEN) [UNINSTALL] Package uninstalled ($(PACKAGE_NAME))$(NC)"

reinstall:
	@echo -e "$(YELLOW) [REINSTALL] Reinstalling package ($(PACKAGE_NAME))$(NC)"
	@make --no-print-directory uninstall install
	@echo -e "$(GREEN) [REINSTALL] Package reinstalled ($(PACKAGE_NAME))$(NC)"

# ------------------------------------------------------------
# TESTS & CHECKS
# ------------------------------------------------------------

test:
	@echo -e "$(YELLOW) [TEST] Running tests ($(PACKAGE_NAME))$(NC)"
	@pytest --debug=trace --cov=jarbin_toolkit_error_python --cov-report=html
	@xdg-open htmlcov/index.html
	@rm -f .coverage
	@echo -e "$(GREEN) [TEST] Tests ran$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] Checking package ($(PACKAGE_NAME))$(NC)"
	@pip show jarbin_toolkit_error
	@echo -e "$(GREEN) [CHECK] Package checked ($(PACKAGE_NAME))$(NC)"

# ------------------------------------------------------------
# INFORMATION
# ------------------------------------------------------------

info:
	@echo -e "$(YELLOW) [INFO] Getting package informations ($(PACKAGE_NAME))$(NC)"
	@$(PIP) show $(PACKAGE_NAME) >/dev/null 2>&1 && $(PIP) show $(PACKAGE_NAME) && echo -e "$(GREEN) [INFO] Package informations shown$(NC)" || echo -e "$(RED) [INFO] Package not installed$(NC)"

# ------------------------------------------------------------
# CLEANUP
# ------------------------------------------------------------

clean:
	@echo -e "$(YELLOW) [CLEAN] Removing cache, test, log and build files ($(PACKAGE_NAME))$(NC)"
	@find . -type d -name "__pycache__" -exec rm -frd {} +
	@rm -frd *.egg-info *.xml trace htmlcov .pytest_cache .coverage
	@echo -e "$(GREEN) [CLEAN] Cleaning done ($(PACKAGE_NAME))$(NC)"

# ------------------------------------------------------------
# SAFETY
# ------------------------------------------------------------

.PHONY: \
	help \
	install uninstall reinstall \
	test check \
	info \
	clean
