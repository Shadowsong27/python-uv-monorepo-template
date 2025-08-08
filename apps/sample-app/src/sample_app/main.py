"""Main module for sample application."""

from loguru import logger


def main() -> None:
    """Main entry point for the application."""
    logger.info("Sample application started")
    print("Hello from sample app!")


if __name__ == "__main__":
    main()
