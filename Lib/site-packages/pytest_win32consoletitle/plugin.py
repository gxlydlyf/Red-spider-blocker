from typing import Optional

import pytest
import win32console
from _pytest.nodes import Item
from _pytest.reports import TestReport
from _pytest.runner import CallInfo

REPORTED_NODE_IDS = 0


def pytest_runtest_logfinish(nodeid: str) -> None:
    global REPORTED_NODE_IDS
    REPORTED_NODE_IDS += 1


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo) -> Optional[TestReport]:
    yield
    if call.when != 'call':
        return

    collected = item.session.testscollected
    percent = (REPORTED_NODE_IDS / collected) * 100
    win32console.SetConsoleTitle(f'{percent:.0f}% - {item.nodeid}')
