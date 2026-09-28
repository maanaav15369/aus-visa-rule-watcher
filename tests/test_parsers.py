from app.collectors.home_affairs import HomeAffairsCollector


def test_home_affairs_collector_exists():
    collector = HomeAffairsCollector()

    assert collector is not None
    assert collector.timeout > 0