"""
Australian Department of Home Affairs public-page collector.

This module is responsible only for downloading public web pages.
It does not perform rule interpretation or legal analysis.
"""

from __future__ import annotations

from dataclasses import dataclass

import httpx


@dataclass
class CollectedPage:
    """Represents a downloaded public webpage."""

    url: str
    status_code: int
    content: str


class HomeAffairsCollector:
    """Collect public pages from the Australian Home Affairs website."""

    DEFAULT_TIMEOUT = 30.0

    def __init__(self, timeout: float = DEFAULT_TIMEOUT) -> None:
        self.timeout = timeout

    def fetch(self, url: str) -> CollectedPage:
        """Download a public webpage."""

        headers = {
            "User-Agent": (
                "AUS-Visa-Rule-Watcher/0.1 "
                "(public-information-monitoring-project)"
            )
        }

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            headers=headers,
        ) as client:
            response = client.get(url)
            response.raise_for_status()

        return CollectedPage(
            url=str(response.url),
            status_code=response.status_code,
            content=response.text,
        )