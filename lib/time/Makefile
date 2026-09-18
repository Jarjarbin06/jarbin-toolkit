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
PACKAGE_NAME    := jarbin_toolkit_time

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
	@echo -e "$(YELLOW) [INSTALL] Installing package ($(PACKAGE_NAME))$(NC)"
	@pip install -e .
	@echo -e "$(GREEN) [INSTALL] Package installed ($(PACKAGE_NAME))$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] Uninstalling package ($(PACKAGE_NAME))$(NC)"
	@echo "y" | pip uninstall $(PACKAGE_NAME) || true
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
	@pytest --debug=trace --cov=jarbin_toolkit --cov-report=html
	@xdg-open htmlcov/index.html
	@rm -f .coverage
	@echo -e "$(GREEN) [TEST] Tests ran$(NC)"

test-jartest:
	@echo -e "$(YELLOW) [TEST] Running JarTest tests ($(PACKAGE_NAME))$(NC)"
	@python -m tests
	@echo -e "$(GREEN) [TEST] JarTest tests ran ($(PACKAGE_NAME))$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] Checking package ($(PACKAGE_NAME))$(NC)"
	@pip show $(PACKAGE_NAME) || true
	@echo -e "$(GREEN) [CHECK] Package checked ($(PACKAGE_NAME))$(NC)"

check-style:
	@echo -e "$(YELLOW) [CHECK] Checking coding style ($(PACKAGE_NAME))$(NC)"
	@flake8 . --count --exit-zero --max-line-length=100 --statistic
	@echo -e "$(GREEN) [CHECK] Coding style checked ($(PACKAGE_NAME))$(NC)"

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
	test check-style \
	info \
	clean
