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
PACKAGE_NAME    := jarbin_toolkit

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
	@# independent #
	@make --no-print-directory -C lib/action install || true
	@make --no-print-directory -C lib/config install || true
	@make --no-print-directory -C lib/error install || true
	@make --no-print-directory -C lib/log install || true
	@make --no-print-directory -C lib/time install || true
	@# dependent #
	@make --no-print-directory -C lib/console install || true
	@make --no-print-directory -C lib/jartest install || true
	@# parent #
	@pip install -e .
	@echo -e "$(GREEN) [INSTALL] Installing package$(NC)"

uninstall:
	@echo -e "$(YELLOW) [UNINSTALL] Uninstalling package$(NC)"
	@# parent #
	@echo "y" | pip uninstall $(PACKAGE_NAME) || true
	@# dependent #
	@make --no-print-directory -C lib/jartest uninstall || true
	@make --no-print-directory -C lib/console uninstall || true
	@# independent #
	@make --no-print-directory -C lib/action uninstall || true
	@make --no-print-directory -C lib/config uninstall || true
	@make --no-print-directory -C lib/error uninstall || true
	@make --no-print-directory -C lib/log uninstall || true
	@make --no-print-directory -C lib/time uninstall || true
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
	@# independent #
	@make --no-print-directory -C lib/action test || true
	@make --no-print-directory -C lib/config test || true
	@make --no-print-directory -C lib/error test || true
	@make --no-print-directory -C lib/log test || true
	@make --no-print-directory -C lib/time test || true
	@# dependent #
	@make --no-print-directory -C lib/console test || true
	@make --no-print-directory -C lib/jartest install || true
	@# parent #
	@pytest --debug=trace --cov=$(PACKAGE_NAME) --cov-report=html
	@xdg-open htmlcov/index.html
	@rm -f .coverage
	@echo -e "$(GREEN) [TEST] Tests ran$(NC)"

test-jartest:
	@echo -e "$(YELLOW) [TEST] Running JarTest tests$(NC)"
	@python -m tests
	@echo -e "$(GREEN) [TEST]  JarTest tests ran$(NC)"

check:
	@echo -e "$(YELLOW) [CHECK] Checking package$(NC)"
	@# parent #
	@pip show $(PACKAGE_NAME) || true
	@# dependent #
	@make --no-print-directory -C lib/jartest check || true
	@make --no-print-directory -C lib/console check || true
	@# independent #
	@make --no-print-directory -C lib/action check || true
	@make --no-print-directory -C lib/config check || true
	@make --no-print-directory -C lib/error check || true
	@make --no-print-directory -C lib/log check || true
	@make --no-print-directory -C lib/time check || true
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
	@# independent #
	@make --no-print-directory -C lib/action clean || true
	@make --no-print-directory -C lib/config clean || true
	@make --no-print-directory -C lib/error clean || true
	@make --no-print-directory -C lib/log clean || true
	@make --no-print-directory -C lib/time clean || true
	@# dependent #
	@make --no-print-directory -C lib/console clean || true
	@make --no-print-directory -C lib/jartest clean || true
	@# parent #
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
