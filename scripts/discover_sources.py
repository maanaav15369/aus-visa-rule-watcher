from app.collectors.home_affairs import HomeAffairsCollector


HOME_AFFAIRS_VISA_LIST_URL = (
    "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing"
)


def main() -> None:
    collector = HomeAffairsCollector()

    page = collector.fetch(HOME_AFFAIRS_VISA_LIST_URL)

    print(f"URL: {page.url}")
    print(f"HTTP status: {page.status_code}")
    print(f"Downloaded characters: {len(page.content)}")


if __name__ == "__main__":
    main()