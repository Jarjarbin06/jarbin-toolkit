# ============================================================
# Jarbin_ToolKit – Makefile
# ============================================================
# Usage:
#   make help
#   make install
#   make test
#   make demo
# ============================================================

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

PYTHON          ?= python3
PIP             ?= pip3
SHELL           := /bin/bash
SCRIPT_DIR      := script
PACKAGE_NAME    := jarbin_toolkit_action
VENV_DIR        := .venv

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
	@echo -e "\tmake demo\t\tRun the demo"
	@echo ""
	@echo -e "\tmake clean\t\tClean cache and build files"
	@echo -e "\tmake info\t\tShow package info"
	@echo ""

# ------------------------------------------------------------
# PACKAGE MANAGEMENT
# ------------------------------------------------------------

install:
	@echo -e "$(YELLOW) [INSTALL] Installing package$(NC)"
	@./$(SCRIPT_DIR)/install-package
	@echo -e "$(GREEN) [INSTALL] Installing package$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] Uninstalling package$(NC)"
	@./$(SCRIPT_DIR)/uninstall-package
	@echo -e "$(GREEN) [UNINSTALL] Package uninstalled$(NC)"

reinstall:
	@echo -e "$(YELLOW) [REINSTALL] Reinstalling package$(NC)"
	@make -s uninstall install
	@echo -e "$(GREEN) [REINSTALL] Package reinstalled$(NC)"

# ------------------------------------------------------------
# TESTS & CHECKS
# ------------------------------------------------------------

test:
	@echo -e "$(YELLOW) [TEST] Running tests$(NC)"
	@./$(SCRIPT_DIR)/test-package
	@echo -e "$(GREEN) [TEST] Tests ran$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] Checking package$(NC)"
	@./$(SCRIPT_DIR)/check-package
	@echo -e "$(GREEN) [CHECK] Package checked$(NC)"

# ------------------------------------------------------------
# DEMOS
# ------------------------------------------------------------

demo:
	@echo -e "$(YELLOW) [DEMO] Running full demo$(NC)"
	@./$(SCRIPT_DIR)/full_demo && echo -e "$(GREEN) [DEMO] Full demo ran$(NC)" || echo -e "$(RED) [DEMO] Full demo ran with error$(NC)"

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
	@rm -frd *.egg-info *.xml trace htmlcov .pytest_cache
	@echo -e "$(GREEN) [CLEAN] Done$(NC)"

# ------------------------------------------------------------
# SAFETY
# ------------------------------------------------------------

.PHONY: \
	help \
	install uninstall reinstall \
	test check \
	demo \
	info \
	clean